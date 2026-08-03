import sqlite3
import pandas as pd

class DatabaseHandler:
    def __init__(self, db_name="trading_system.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock TEXT,
                action TEXT,
                entry_price REAL,
                stop_loss REAL,
                target REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def log_trade(self, stock, action, entry_price, stop_loss, target):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO trades (stock, action, entry_price, stop_loss, target)
            VALUES (?, ?, ?, ?, ?)
        ''', (stock, action, entry_price, stop_loss, target))
        conn.commit()
        conn.close()