import json
import os
from typing import Dict, Any
from config import Config

class CostManager:
    def __init__(self):
        self.config = Config()
        self.cost_config = self.config.get_cost_config()
        self.enabled = self.cost_config.get('enabled', False)
        self.max_cost = self.cost_config.get('max_cost', 100.0)
        self.cost_per_1k_tokens = self.cost_config.get('cost_per_1k_tokens', 0.001)
        
        self.total_tokens = 0
        self.current_cost = 0.0
        self._load_state()
    
    def add_tokens(self, tokens: int):
        self.total_tokens += tokens
        self.current_cost = (self.total_tokens / 1000) * self.cost_per_1k_tokens
        self._save_state()
    
    def get_current_cost(self) -> float:
        return self.current_cost
    
    def get_total_tokens(self) -> int:
        return self.total_tokens
    
    def is_over_budget(self) -> bool:
        if not self.enabled:
            return False
        return self.current_cost >= self.max_cost
    
    def get_remaining_budget(self) -> float:
        if not self.enabled:
            return float('inf')
        return max(0.0, self.max_cost - self.current_cost)
    
    def reset(self):
        self.total_tokens = 0
        self.current_cost = 0.0
        self._save_state()
    
    def _save_state(self):
        state = {
            'total_tokens': self.total_tokens,
            'current_cost': self.current_cost
        }
        
        state_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cost_state.json')
        os.makedirs(os.path.dirname(state_path), exist_ok=True)
        
        with open(state_path, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)
    
    def _load_state(self):
        state_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'cost_state.json')
        
        if os.path.exists(state_path):
            with open(state_path, 'r', encoding='utf-8') as f:
                state = json.load(f)
                self.total_tokens = state.get('total_tokens', 0)
                self.current_cost = state.get('current_cost', 0.0)