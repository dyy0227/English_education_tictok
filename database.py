import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path='./proverbs.db'):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS proverbs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                proverb TEXT UNIQUE,
                type TEXT,
                definition_en TEXT,
                definition_zh TEXT,
                example_en TEXT,
                example_zh TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS video_clips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                proverb_id INTEGER,
                source_video_path TEXT,
                clip_path TEXT,
                start_time REAL,
                end_time REAL,
                duration REAL,
                FOREIGN KEY(proverb_id) REFERENCES proverbs(id)
            )
        ''')
        
        conn.commit()
        conn.close()

    def add_proverb(self, proverb, type_, definition_en, definition_zh, example_en, example_zh):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO proverbs (proverb, type, definition_en, definition_zh, example_en, example_zh)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (proverb, type_, definition_en, definition_zh, example_en, example_zh))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            cursor.execute('SELECT id FROM proverbs WHERE proverb = ?', (proverb,))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            conn.close()

    def add_video_clip(self, proverb_id, source_video_path, clip_path, start_time, end_time):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        duration = end_time - start_time
        cursor.execute('''
            INSERT INTO video_clips (proverb_id, source_video_path, clip_path, start_time, end_time, duration)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (proverb_id, source_video_path, clip_path, start_time, end_time, duration))
        
        conn.commit()
        conn.close()

    def get_all_proverbs(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM proverbs')
        result = cursor.fetchall()
        conn.close()
        return result

    def get_clips_by_proverb(self, proverb_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM video_clips WHERE proverb_id = ?', (proverb_id,))
        result = cursor.fetchall()
        conn.close()
        return result

    def get_proverb_by_id(self, proverb_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM proverbs WHERE id = ?', (proverb_id,))
        result = cursor.fetchone()
        conn.close()
        return result