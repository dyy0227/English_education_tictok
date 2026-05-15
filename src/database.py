import os
import sqlite3
from typing import List, Dict, Any, Optional
from config import Config

class Database:
    def __init__(self):
        self.config = Config()
        self.db_config = self.config.get_database_config()
        self.conn = None
        self.cursor = None
    
    def connect(self):
        db_type = self.db_config.get('type', 'sqlite')
        
        if db_type == 'sqlite':
            db_path = self.db_config.get('path', './data/proverbs.db')
            os.makedirs(os.path.dirname(db_path), exist_ok=True)
            self.conn = sqlite3.connect(db_path)
        elif db_type == 'mysql':
            import mysql.connector
            self.conn = mysql.connector.connect(
                host=self.db_config.get('host', 'localhost'),
                port=self.db_config.get('port', 3306),
                user=self.db_config.get('username', ''),
                password=self.db_config.get('password', ''),
                database=self.db_config.get('database_name', 'proverbs')
            )
        else:
            raise ValueError(f"不支持的数据库类型: {db_type}")
        
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS proverbs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proverb TEXT NOT NULL,
            type TEXT NOT NULL,
            translation TEXT,
            explanation TEXT,
            context_before TEXT,
            context_after TEXT,
            source_video TEXT NOT NULL,
            output_path TEXT NOT NULL,
            start_time REAL NOT NULL,
            end_time REAL NOT NULL,
            duration REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        self.cursor.execute(create_table_sql)
        self.conn.commit()
    
    def insert_proverb(self, data: Dict[str, Any]) -> int:
        sql = """
        INSERT INTO proverbs (proverb, type, translation, explanation, 
                              context_before, context_after, source_video, 
                              output_path, start_time, end_time, duration)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        params = (
            data.get('proverb', ''),
            data.get('type', ''),
            data.get('translation', ''),
            data.get('explanation', ''),
            data.get('context_before', ''),
            data.get('context_after', ''),
            data.get('source_video', ''),
            data.get('output_path', ''),
            data.get('start_time', 0),
            data.get('end_time', 0),
            data.get('duration', 0)
        )
        
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def insert_proverbs(self, proverbs: List[Dict[str, Any]]):
        for proverb in proverbs:
            self.insert_proverb(proverb)
    
    def get_proverb_by_id(self, proverb_id: int) -> Optional[Dict[str, Any]]:
        sql = "SELECT * FROM proverbs WHERE id = ?"
        self.cursor.execute(sql, (proverb_id,))
        row = self.cursor.fetchone()
        
        if row:
            return self._row_to_dict(row)
        return None
    
    def get_all_proverbs(self) -> List[Dict[str, Any]]:
        sql = "SELECT * FROM proverbs ORDER BY created_at DESC"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows]
    
    def get_proverbs_by_type(self, proverb_type: str) -> List[Dict[str, Any]]:
        sql = "SELECT * FROM proverbs WHERE type = ? ORDER BY created_at DESC"
        self.cursor.execute(sql, (proverb_type,))
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows]
    
    def search_proverbs(self, keyword: str) -> List[Dict[str, Any]]:
        sql = """
        SELECT * FROM proverbs 
        WHERE proverb LIKE ? OR translation LIKE ? OR explanation LIKE ?
        ORDER BY created_at DESC
        """
        pattern = f"%{keyword}%"
        self.cursor.execute(sql, (pattern, pattern, pattern))
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows]
    
    def update_proverb(self, proverb_id: int, data: Dict[str, Any]):
        fields = []
        params = []
        
        if 'proverb' in data:
            fields.append('proverb = ?')
            params.append(data['proverb'])
        if 'type' in data:
            fields.append('type = ?')
            params.append(data['type'])
        if 'translation' in data:
            fields.append('translation = ?')
            params.append(data['translation'])
        if 'explanation' in data:
            fields.append('explanation = ?')
            params.append(data['explanation'])
        if 'output_path' in data:
            fields.append('output_path = ?')
            params.append(data['output_path'])
        
        if not fields:
            return
        
        params.append(proverb_id)
        sql = f"UPDATE proverbs SET {', '.join(fields)} WHERE id = ?"
        self.cursor.execute(sql, params)
        self.conn.commit()
    
    def delete_proverb(self, proverb_id: int):
        sql = "DELETE FROM proverbs WHERE id = ?"
        self.cursor.execute(sql, (proverb_id,))
        self.conn.commit()
    
    def get_proverb_count(self) -> int:
        sql = "SELECT COUNT(*) FROM proverbs"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row[0] if row else 0
    
    def get_proverb_count_by_type(self) -> Dict[str, int]:
        sql = "SELECT type, COUNT(*) FROM proverbs GROUP BY type"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return {row[0]: row[1] for row in rows}
    
    def _row_to_dict(self, row) -> Dict[str, Any]:
        return {
            'id': row[0],
            'proverb': row[1],
            'type': row[2],
            'translation': row[3],
            'explanation': row[4],
            'context_before': row[5],
            'context_after': row[6],
            'source_video': row[7],
            'output_path': row[8],
            'start_time': row[9],
            'end_time': row[10],
            'duration': row[11],
            'created_at': row[12]
        }
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()