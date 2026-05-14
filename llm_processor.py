import json
importimport json
import requests

class LLMProcessor:
    def __import json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.apiimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llmimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    defimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following Englishimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
import json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2import json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocationimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5import json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Exampleimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [import json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",import json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",
                "definition_en": "English definition",
                "definition_zh": "Chinese definitionimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",
                "definition_en": "English definition",
                "definition_zh": "Chinese definition",
                "example_en": "English example",
                "example_zh": "Chineseimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",
                "definition_en": "English definition",
                "definition_zh": "Chinese definition",
                "example_en": "English example",
                "example_zh": "Chinese example"
            }}
        ]
        
        Only return the JSON array, nothing else.
import json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",
                "definition_en": "English definition",
                "definition_zh": "Chinese definition",
                "example_en": "English example",
                "example_zh": "Chinese example"
            }}
        ]
        
        Only return the JSON array, nothing else.
        '''

        if self.provider == 'ollama':
            return self._call_ollimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",
                "definition_en": "English definition",
                "definition_zh": "Chinese definition",
                "example_en": "English example",
                "example_zh": "Chinese example"
            }}
        ]
        
        Only return the JSON array, nothing else.
        '''

        if self.provider == 'ollama':
            return self._call_ollama(prompt)
        else:
            return self._call_openai(prompt)

import json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",
                "definition_en": "English definition",
                "definition_zh": "Chinese definition",
                "example_en": "English example",
                "example_zh": "Chinese example"
            }}
        ]
        
        Only return the JSON array, nothing else.
        '''

        if self.provider == 'ollama':
            return self._call_ollama(prompt)
        else:
            return self._call_openai(prompt)

    def _call_ollama(self, prompt):
        url = f"{self.api_baseimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",
                "definition_en": "English definition",
                "definition_zh": "Chinese definition",
                "example_en": "English example",
                "example_zh": "Chinese example"
            }}
        ]
        
        Only return the JSON array, nothing else.
        '''

        if self.provider == 'ollama':
            return self._call_ollama(prompt)
        else:
            return self._call_openai(prompt)

    def _call_ollama(self, prompt):
        url = f"{self.api_base}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "streamimport json
import requests

class LLMProcessor:
    def __init__(self, config):
        self.config = config
        self.provider = config['llm']['provider']
        self.model = config['llm']['model']
        self.api_base = config['llm']['api_base']
        self.max_tokens = config['llm']['max_tokens']
        self.temperature = config['llm']['temperature']

    def extract_proverbs(self, transcript):
        prompt = f'''
        Analyze the following English transcript and extract all proverbs, sayings, colloquialisms, slang, collocations, phrasal verbs, and set phrases.
        
        Transcript:
        {transcript}
        
        For each extracted item, provide:
        1. The exact phrase
        2. The type (Proverb, Saying, Colloquialism, Slang, Collocation, Phrasal verb, Set phrase)
        3. English definition/meaning
        4. Chinese translation
        5. Example sentence in English
        6. Example sentence in Chinese
        
        Format your response as a JSON array with the following structure:
        [
            {{
                "phrase": "phrase text",
                "type": "type",
                "definition_en": "English definition",
                "definition_zh": "Chinese definition",
                "example_en": "English example",
                "example_zh": "Chinese example"
            }}
        ]
        
        Only return the JSON array, nothing else.
        '''

        if self.provider == 'ollama':
            return self._call_ollama(prompt)
        else:
            return self._call_openai(prompt)

    def _call_ollama(self, prompt):
        url = f"{self.api_base}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "max_tokens": self.max