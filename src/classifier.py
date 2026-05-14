import os
import json
from typing import List, Dict, Any
from config import Config

class Classifier:
    def __init__(self):
        self.config = Config()
        self.video_config = self.config.get_video_config()
        self.proverb_config = self.config.get_proverb_config()
        self.output_folder = self.video_config.get('output_folder', './output')
        
        self.proverb_types = self.proverb_config.get('types', [
            'Proverb',
            'Saying',
            'Colloquialism',
            'Slang',
            'Collocation',
            'Phrasal_verb',
            'Set_phrase'
        ])
    
    def _get_type_folder(self, proverb_type: str) -> str:
        type_folder = os.path.join(self.output_folder, proverb_type)
        os.makedirs(type_folder, exist_ok=True)
        return type_folder
    
    def save_proverb_video(self, video_data: Dict[str, Any]) -> str:
        proverb_type = video_data.get('type', 'Other')
        proverb_text = video_data.get('proverb', 'unknown')
        
        type_folder = self._get_type_folder(proverb_type)
        
        safe_filename = self._sanitize_filename(f"{proverb_text}.mp4")
        output_path = os.path.join(type_folder, safe_filename)
        
        counter = 1
        while os.path.exists(output_path):
            safe_filename = self._sanitize_filename(f"{proverb_text}_{counter}.mp4")
            output_path = os.path.join(type_folder, safe_filename)
            counter += 1
        
        return output_path
    
    def save_index(self, proverbs: List[Dict[str, Any]], source_video: str):
        index_path = os.path.join(self.output_folder, 'index.json')
        
        index_data = []
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
        
        for proverb in proverbs:
            entry = {
                'proverb': proverb.get('proverb', ''),
                'type': proverb.get('type', ''),
                'translation': proverb.get('translation', ''),
                'explanation': proverb.get('explanation', ''),
                'source_video': source_video,
                'output_path': proverb.get('output_path', ''),
                'start_time': proverb.get('start_time', 0),
                'end_time': proverb.get('end_time', 0),
                'duration': proverb.get('duration', 0)
            }
            index_data.append(entry)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)
    
    def _sanitize_filename(self, filename: str) -> str:
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename[:200]