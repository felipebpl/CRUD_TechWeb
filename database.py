import sqlite3

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:

    def __init__(self, database):
        self.db_name = database + '.db'
        self.conn = sqlite3.connect(self.db_name)
        # id (chave primária do tipo inteiro), title (do tipo string), content (do tipo string e não pode ser vazia).
        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS note 
        (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);
        ''')
    
    def add(self, note):
        self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}');")
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        return [Note(id=i,title=t,content=c) for i,t,c in cursor]

    def update(self,entry):
        self.conn.execute(f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id}")
        self.conn.commit()
    
    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()

        

