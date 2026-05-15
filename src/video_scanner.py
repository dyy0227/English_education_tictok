import os
import glob
from typing import List, Dict, Any
from config import Config

class VideoScanner:
    def __init__(self):
        self.config = Config()
        self.video_config = self.config.get_video_config()
        self.supported_formats = self.video_config.get('supported_formats', ['.mp4', '.avi', '.mkv', '.mov'])
    
    def scan_folder(self, folder_path: str = None) -> List[Dict[str, Any]]:
        if folder_path is None:
            folder_path = self.video_config.get('input_folder', '.')
        
        if not os.path.isdir(folder_path):
            raise ValueError(f"文件夹路径无效: {folder_path}")
        
        video_files = []
        
        for fmt in self.supported_formats:
            pattern = os.path.join(folder_path, f'*{fmt}')
            files = glob.glob(pattern, recursive=True)
            video_files.extend(files)
        
        video_files = sorted(video_files)
        
        result = []
        for filepath in video_files:
            file_info = self._get_file_info(filepath)
            result.append(file_info)
        
        return result
    
    def _get_file_info(self, filepath: str) -> Dict[str, Any]:
        filename = os.path.basename(filepath)
        file_size = os.path.getsize(filepath)
        file_size_mb = file_size / (1024 * 1024)
        
        return {
            'filepath': filepath,
            'filename': filename,
            'size_bytes': file_size,
            'size_mb': round(file_size_mb, 2),
            'folder': os.path.dirname(filepath)
        }
    
    def get_video_count(self, folder_path: str = None) -> int:
        videos = self.scan_folder(folder_path)
        return len(videos)