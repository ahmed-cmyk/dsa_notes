import sqlite3

class HashDB():
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def initialize_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS file_hashes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE NOT NULL,
                hash TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def save_hashes(self, hashes):
        # fetch existing hashes
        self.cursor.execute("SELECT path, hash FROM file_hashes")
        existing = dict(self.cursor.fetchall())

        to_insert = []
        for path, h in hashes:
            if path not in existing:
                to_insert.append((path, h))
            elif existing[path] != h:
                to_insert.append((path, h))

        if to_insert:
            self.cursor.executemany("""
                INSERT INTO file_hashes (path, hash)
                VALUES (?, ?)
                ON CONFLICT(path) DO UPDATE SET hash=excluded.hash
            """, to_insert)
            self.conn.commit()
        else:
            print("✅ Nothing to insert or update.")

        self.conn.commit()

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
