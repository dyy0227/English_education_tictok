import os
import torch
from faster_whisper import WhisperModel
from typing import List, Dict, Any, Optional
from config import Config

class WhisperTranscriber:
    def __init__(self):
        self.config = Config()
        self.whisper_config = self.config.get_whisper_config()
        self.gpu_config = self.config.get_gpu_config()
        self._model = None
        self._device = None
        self._compute_type = None
    
    def _get_device(self) -> str:
        if not self.gpu_config.get('enabled', True):
            return 'cpu'
        
        device = self.gpu_config.get('device', 'auto')
        
        if device == 'auto':
            if torch.cuda.is_available():
                return 'cuda'
            elif torch.backends.mps.is_available():
                return 'mps'
            else:
                return 'cpu'
        elif device == 'rocm':
            if torch.cuda.is_available():
                return 'cuda'
            else:
                return 'cpu'
        elif device == 'cuda':
            if torch.cuda.is_available():
                return 'cuda'
            else:
                return 'cpu'
        else:
            return device
    
    def _get_compute_type(self) -> str:
        if self.gpu_config.get('fp16', True) and self._device != 'cpu':
            return 'float16'
        return 'float32'
    
    def load_model(self):
        model_size = self.whisper_config.get('model', 'base')
        self._device = self._get_device()
        self._compute_type = self._get_compute_type()
        
        self._model = WhisperModel(
            model_size,
            device=self._device,
            compute_type=self._compute_type,
            download_root=os.path.join(os.path.dirname(__file__), '..', 'models')
        )
    
    def transcribe(self, video_path: str) -> Dict[str, Any]:
        if self._model is None:
            self.load_model()
        
        language = self.whisper_config.get('language', 'en')
        beam_size = self.whisper_config.get('beam_size', 5)
        best_of = self.whisper_config.get('best_of', 5)
        
        segments, info = self._model.transcribe(
            video_path,
            language=language,
            beam_size=beam_size,
            best_of=best_of,
            word_timestamps=True
        )
        
        segments_list = []
        for segment in segments:
            words = []
            if segment.words:
                for word in segment.words:
                    words.append({
                        'word': word.word,
                        'start': word.start,
                        'end': word.end,
                        'probability': word.probability
                    })
            
            segments_list.append({
                'id': segment.id,
                'start': segment.start,
                'end': segment.end,
                'text': segment.text,
                'words': words
            })
        
        return {
            'language': info.language,
            'language_probability': info.language_probability,
            'duration': info.duration,
            'segments': segments_list
        }
    
    def get_transcript_text(self, video_path: str) -> str:
        result = self.transcribe(video_path)
        return ' '.join(segment['text'] for segment in result['segments'])