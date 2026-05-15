import os
import ffmpeg
from typing import List, Dict, Any
from config import Config
from subtitle_generator import SubtitleGenerator

class VideoCutter:
    def __init__(self):
        self.config = Config()
        self.video_config = self.config.get_video_config()
        self.subtitle_generator = SubtitleGenerator()
    
    def cut_video(self, input_path: str, start_time: float, end_time: float, output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        (
            ffmpeg
            .input(input_path, ss=start_time, to=end_time)
            .output(output_path, codec='copy')
            .run(quiet=True, overwrite_output=True)
        )
    
    def cut_with_subtitle(self, input_path: str, start_time: float, end_time: float, 
                          output_path: str, subtitle_text: str, subtitle_translation: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        temp_subtitle_path = output_path + '.ass'
        
        proverbs = [{
            'start_time': 0,
            'end_time': end_time - start_time,
            'proverb': subtitle_text,
            'translation': subtitle_translation
        }]
        
        self.subtitle_generator.generate_ass(proverbs, temp_subtitle_path)
        
        try:
            (
                ffmpeg
                .input(input_path, ss=start_time, to=end_time)
                .output(output_path, vf=f"ass={temp_subtitle_path}", crf=23)
                .run(quiet=True, overwrite_output=True)
            )
        finally:
            if os.path.exists(temp_subtitle_path):
                os.remove(temp_subtitle_path)
    
    def extract_audio(self, input_path: str, output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        (
            ffmpeg
            .input(input_path)
            .output(output_path, acodec='pcm_s16le', ar='16k', ac=1)
            .run(quiet=True, overwrite_output=True)
        )
    
    def get_video_info(self, input_path: str) -> Dict[str, Any]:
        try:
            probe = ffmpeg.probe(input_path)
            video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
            audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
            
            duration = float(probe.get('format', {}).get('duration', 0))
            
            return {
                'duration': duration,
                'video_codec': video_stream.get('codec_name', '') if video_stream else '',
                'audio_codec': audio_stream.get('codec_name', '') if audio_stream else '',
                'width': video_stream.get('width', 0) if video_stream else 0,
                'height': video_stream.get('height', 0) if video_stream else 0
            }
        except Exception as e:
            print(f"获取视频信息失败: {e}")
            return {
                'duration': 0,
                'video_codec': '',
                'audio_codec': '',
                'width': 0,
                'height': 0
            }