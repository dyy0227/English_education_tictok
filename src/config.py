import yaml
import os
from typing import Dict, Any

class Config:
    _instance = None
    
    def __new__(cls, config_path: str = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config(config_path)
        return cls._instance
    
    def _load_config(self, config_path: str = None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件不存在: {config_path}")
        
        with open(config_path, 'r', encoding='utf-8') as f:
            self._config = yaml.safe_load(f)
    
    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def get_video_config(self) -> Dict:
        return self._config.get('video', {})
    
    def get_proverb_config(self) -> Dict:
        return self._config.get('proverb', {})
    
    def get_llm_config(self) -> Dict:
        return self._config.get('llm', {})
    
    def get_gpu_config(self) -> Dict:
        return self._config.get('gpu', {})
    
    def get_database_config(self) -> Dict:
        return self._config.get('database', {})
    
    def get_cost_config(self) -> Dict:
        return self._config.get('cost', {})
    
    def get_whisper_config(self) -> Dict:
        return self._config.get('whisper', {})
    
    def get_subtitle_config(self) -> Dict:
        return self._config.get('subtitle', {})
    
    def get_logging_config(self) -> Dict:
        return self._config.get('logging', {})
    
    def get_processing_config(self) -> Dict:
        return self._config.get('processing', {})
    
    def reload(self, config_path: str = None):
        self._load_config(config_path)