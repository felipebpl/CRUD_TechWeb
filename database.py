import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:

    def __init__(self, DB_NAME):

        if not DB_NAME.endswith('.db'):
            DB_NAME = DB_NAME + '.db'
            self.conn = sqlite3.connect(DB_NAME)
        else:
            self.conn = sqlite3.connect(DB_NAME)

        self.TABLE_NAME = "note"
        self.CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL);'
        self.conn.execute(self.CREATE_TABLE)
        self.conn.commit()

    def add(self, note):
        self.ADD_DATA = f'INSERT INTO {self.TABLE_NAME} (title, content) VALUES ("{note.title}", "{note.content}");'
        self.conn.execute(self.ADD_DATA)
        self.conn.commit()

    def get_all(self):
        self.SELECT = "SELECT id, title, content FROM note"
        self.Cursor = self.conn.execute(self.SELECT)
        self.LIST_DATA = []
        for linha in self.Cursor:
            self.LIST_DATA.append(Note(linha[0],linha[1],linha[2]))
        return self.LIST_DATA

    def update(self, entry):
        self.DATA_UPDATE = f"UPDATE {self.TABLE_NAME} SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id}"
        self.conn.execute(self.DATA_UPDATE)
        self.conn.commit()

    def delete(self, note_id):
        self.DELETE_DATA = f"DELETE FROM {self.TABLE_NAME} WHERE id = {note_id};"
        self.conn.execute(self.DELETE_DATA)
        self.conn.commit()


        