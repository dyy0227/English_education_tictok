import json
import ollama
from typing import List, Dict, Any
from config import Config

class ProverbDetector:
    def __init__(self):
        self.config = Config()
        self.llm_config = self.config.get_llm_config()
        self.proverb_config = self.config.get_proverb_config()
        self.provider = self.llm_config.get('provider', 'ollama')
    
    def _build_prompt(self, text: str) -> str:
        proverb_types = self.proverb_config.get('types', [])
        min_words = self.proverb_config.get('min_words', 2)
        max_words = self.proverb_config.get('max_words', 10)
        
        prompt = f"""
你是一个英语熟语识别专家。请从以下文本中识别所有英语熟语。

文本:
{text}

需要识别的熟语类型:
{', '.join(proverb_types)}

要求:
1. 熟语长度应在 {min_words} 到 {max_words} 个词之间
2. 请提供每个熟语的上下文（前后各3个词）
3. 请提供每个熟语的中文翻译
4. 请提供每个熟语的解释

请以JSON格式输出，包含以下字段:
- proverb: 熟语原文
- type: 熟语类型（从上面列表中选择）
- context_before: 前面的上下文
- context_after: 后面的上下文
- translation: 中文翻译
- explanation: 解释说明

如果没有找到熟语，请返回空数组。
""".strip()
        
        return prompt
    
    def detect_proverbs(self, text: str) -> List[Dict[str, Any]]:
        if self.provider == 'ollama':
            return self._detect_with_ollama(text)
        else:
            raise NotImplementedError(f"不支持的LLM提供商: {self.provider}")
    
    def _detect_with_ollama(self, text: str) -> List[Dict[str, Any]]:
        model = self.llm_config.get('model', 'llama3.1:8b')
        api_base = self.llm_config.get('api_base', 'http://localhost:11434')
        timeout = self.llm_config.get('timeout', 60)
        
        prompt = self._build_prompt(text)
        
        try:
            response = ollama.chat(
                model=model,
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                options={
                    'timeout': timeout,
                    'num_ctx': self.llm_config.get('max_tokens', 2000)
                }
            )
            
            content = response.get('message', {}).get('content', '[]')
            
            try:
                result = json.loads(content)
                if isinstance(result, list):
                    return result
                else:
                    return []
            except json.JSONDecodeError:
                return []
        
        except Exception as e:
            print(f"LLM调用失败: {e}")
            return []
    
    def detect_from_transcript(self, transcript: Dict[str, Any]) -> List[Dict[str, Any]]:
        full_text = ' '.join(segment['text'] for segment in transcript['segments'])
        return self.detect_proverbs(full_text)