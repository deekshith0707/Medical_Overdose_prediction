import sqlite3
from datetime import datetime

DB_NAME = 'overdose_records.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS overdose_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            dosage REAL,
            duration REAL,
            prior_overdose INTEGER,
            prediction TEXT,
            probability REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_record(age, dosage, duration, prior_overdose, prediction, probability):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO overdose_records (age, dosage, duration, prior_overdose, prediction, probability, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (age, dosage, duration, prior_overdose, prediction, probability, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
