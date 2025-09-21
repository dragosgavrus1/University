import sqlite3
from datetime import datetime

class ChatHistoryManager:
    def __init__(self, db_path="chat_history.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
            """)

    def save_message(self, question, answer):
        with self.conn:
            self.conn.execute("""
            INSERT INTO chat_history (question, answer, timestamp)
            VALUES (?, ?, ?)
            """, (question, answer, datetime.utcnow().isoformat()))

    def get_recent_history(self, limit=50):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT question, answer FROM chat_history
        ORDER BY id DESC
        LIMIT ?
        """, (limit,))
        return cursor.fetchall()

    def search_history(self, query, limit=5):
        cursor = self.conn.cursor()
        # Simple LIKE search (for now), can upgrade to embeddings if needed
        wildcard_query = f"%{query}%"
        cursor.execute("""
        SELECT question, answer FROM chat_history
        WHERE question LIKE ? OR answer LIKE ?
        ORDER BY id DESC
        LIMIT ?
        """, (wildcard_query, wildcard_query, limit))
        return cursor.fetchall()