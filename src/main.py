import os
import argparse
from tqdm import tqdm
from config import Config
from video_scanner import VideoScanner
from whisper_transcriber import WhisperTranscriber
from proverb_detector import ProverbDetector
from video_cutter import VideoCutter
from classifier import Classifier
from database import Database
from cost_manager import CostManager

def main():
    parser = argparse.ArgumentParser(description='英语熟语视频总结程序')
    parser.add_argument('-c', '--config', help='配置文件路径')
    parser.add_argument('-i', '--input', help='输入视频文件夹路径')
    parser.add_argument('-o', '--output', help='输出文件夹路径')
    parser.add_argument('-v', '--verbose', action='store_true', help='详细输出')
    args = parser.parse_args()
    
    if args.config:
        config = Config(args.config)
    else:
        config = Config()
    
    if args.input:
        config.set('video.input_folder', args.input)
    if args.output:
        config.set('video.output_folder', args.output)
    
    video_scanner = VideoScanner()
    whisper_transcriber = WhisperTranscriber()
    proverb_detector = ProverbDetector()
    video_cutter = VideoCutter()
    classifier = Classifier()
    database = Database()
    cost_manager = CostManager()
    
    try:
        database.connect()
        
        videos = video_scanner.scan_folder()
        print(f"\n[信息] 发现 {len(videos)} 个视频文件")
        
        if not videos:
            print("[警告] 未发现视频文件")
            return
        
        processed_count = 0
        proverb_count = 0
        
        for video in tqdm(videos, desc="处理视频", unit="个"):
            video_path = video['filepath']
            filename = video['filename']
            
            print(f"\n[处理] {filename}")
            
            if cost_manager.is_over_budget():
                print(f"[警告] 费用已超出限制 ({cost_manager.get_current_cost():.2f} / {cost_manager.max_cost})")
                break
            
            try:
                print("[步骤1/5] 提取音频并转写...")
                transcript = whisper_transcriber.transcribe(video_path)
                print(f"  ✓ 转写完成，时长: {transcript['duration']:.2f}秒")
                
                print("[步骤2/5] 识别熟语...")
                proverbs = proverb_detector.detect_from_transcript(transcript)
                print(f"  ✓ 识别到 {len(proverbs)} 个熟语")
                
                if not proverbs:
                    print("  - 未识别到熟语，跳过")
                    continue
                
                print("[步骤3/5] 定位时间戳...")
                proverbs_with_timestamps = []
                for proverb in proverbs:
                    proverb_text = proverb.get('proverb', '')
                    start_time, end_time = find_proverb_timestamps(transcript, proverb_text)
                    
                    proverb['start_time'] = start_time
                    proverb['end_time'] = end_time
                    proverb['duration'] = end_time - start_time
                    proverb['source_video'] = video_path
                    
                    proverbs_with_timestamps.append(proverb)
                
                print("[步骤4/5] 生成视频切片...")
                for proverb in tqdm(proverbs_with_timestamps, desc="生成切片", unit="个", leave=False):
                    output_path = classifier.save_proverb_video(proverb)
                    proverb['output_path'] = output_path
                    
                    video_cutter.cut_with_subtitle(
                        video_path,
                        proverb['start_time'],
                        proverb['end_time'],
                        output_path,
                        proverb['proverb'],
                        proverb['translation']
                    )
                
                print("[步骤5/5] 保存到数据库...")
                database.insert_proverbs(proverbs_with_timestamps)
                classifier.save_index(proverbs_with_timestamps, video_path)
                
                processed_count += 1
                proverb_count += len(proverbs_with_timestamps)
                
            except Exception as e:
                print(f"[错误] 处理 {filename} 时出错: {e}")
                continue
        
        print("\n" + "="*50)
        print("处理完成!")
        print(f"处理视频数: {processed_count}/{len(videos)}")
        print(f"识别熟语数: {proverb_count}")
        print(f"累计费用: {cost_manager.get_current_cost():.4f}元")
        
    finally:
        database.close()

def find_proverb_timestamps(transcript, proverb_text):
    words = proverb_text.lower().split()
    segments = transcript['segments']
    
    all_words = []
    for segment in segments:
        for word in segment.get('words', []):
            all_words.append({
                'word': word['word'].lower().strip('.,!?;:()[]"\''),
                'start': word['start'],
                'end': word['end']
            })
    
    proverb_length = len(words)
    for i in range(len(all_words) - proverb_length + 1):
        match = True
        for j in range(proverb_length):
            if all_words[i + j]['word'] != words[j]:
                match = False
                break
        
        if match:
            start_time = all_words[i]['start'] - 0.5
            end_time = all_words[i + proverb_length - 1]['end'] + 0.5
            return max(0, start_time), end_time
    
    return 0, 1

if __name__ == '__main__':
    main()