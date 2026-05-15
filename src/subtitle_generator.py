import os
from typing import List, Dict, Any
from config import Config

class SubtitleGenerator:
    def __init__(self):
        self.config = Config()
        self.subtitle_config = self.config.get_subtitle_config()
    
    def generate_srt(self, proverbs: List[Dict[str, Any]], output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for i, proverb in enumerate(proverbs, 1):
                start_time = proverb.get('start_time', 0)
                end_time = proverb.get('end_time', 1)
                
                start_str = self._format_time(start_time)
                end_str = self._format_time(end_time)
                
                english_text = proverb.get('proverb', '')
                chinese_text = proverb.get('translation', '')
                
                f.write(f"{i}\n")
                f.write(f"{start_str} --> {end_str}\n")
                f.write(f"{english_text}\n")
                f.write(f"{chinese_text}\n")
                f.write("\n")
    
    def generate_ass(self, proverbs: List[Dict[str, Any]], output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        font_size = self.subtitle_config.get('font_size', 24)
        font_color = self.subtitle_config.get('font_color', 'white')
        font = self.subtitle_config.get('font', 'Arial')
        position = self.subtitle_config.get('position', 'bottom')
        
        ass_content = f"""[Script Info]
Title: Proverb Subtitles
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,{font},{font_size},&H{self._hex_color(font_color)},&H{self._hex_color(font_color)},&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2,2,{self._get_alignment(position)},10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
        
        for i, proverb in enumerate(proverbs, 1):
            start_time = proverb.get('start_time', 0)
            end_time = proverb.get('end_time', 1)
            
            start_str = self._format_time_ass(start_time)
            end_str = self._format_time_ass(end_time)
            
            english_text = proverb.get('proverb', '').replace('\\', '\\\\').replace('{', '\\{').replace('}', '\\}')
            chinese_text = proverb.get('translation', '').replace('\\', '\\\\').replace('{', '\\{').replace('}', '\\}')
            
            text = f"{english_text}\\N{chinese_text}"
            
            ass_content += f"Dialogue: 0,{start_str},{end_str},Default,,0,0,0,,{text}\n"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(ass_content)
    
    def _format_time(self, seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}".replace('.', ',')
    
    def _format_time_ass(self, seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        
        return f"{hours}:{minutes:02d}:{secs:06.2f}"
    
    def _hex_color(self, color_name: str) -> str:
        color_map = {
            'white': 'FFFFFF',
            'black': '000000',
            'red': 'FF0000',
            'green': '00FF00',
            'blue': '0000FF',
            'yellow': 'FFFF00',
            'cyan': '00FFFF',
            'magenta': 'FF00FF'
        }
        return color_map.get(color_name.lower(), 'FFFFFF')
    
    def _get_alignment(self, position: str) -> int:
        position_map = {
            'top': 8,
            'middle': 5,
            'bottom': 2
        }
        return position_map.get(position.lower(), 2)