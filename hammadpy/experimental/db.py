from hammadpy.modules.messages import TextStyles
from tinydb import TinyDB, Query
from typing import Optional, List, Dict, Union

"""
hammadpy.database
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the Database class which provides a simple interface for creating and searching a TinyDB database.

Classes:
    Database: This class provides a simple interface for creating and searching a TinyDB database.

Methods:
    add(self, documents: List[Dict]): Adds documents to the database.
    search(self, query: Query) -> List[Dict]: Searches the database using a TinyDB Query object.

Attributes:
    db_path: str
    db: TinyDB
"""

class Database:
    def __init__(self, db_path: Optional[str] = None):
        """
        Initializes the TinyDB database.

        Args:
            db_path (Optional[str]): Path to the database file. If not provided, an in-memory database will be used.
        """
        self.db_path = db_path
        if self.db_path is None:
            self.db = TinyDB(storage=MemoryStorage)
        else:
            self.db = TinyDB(self.db_path)
        
        self.TextStyles = TextStyles()
        self.TextStyles.say(message="Database loaded.", color="green", style="bold")

    def add(self, documents: List[Dict]):
        """
        Adds documents to the database.
        """
        self.db.insert_multiple(documents)

    def search(self, query: Query) -> List[Dict]:
        """
        Searches the database using a TinyDB Query object.
        """
        return self.db.search(query)

if __name__ == "__main__":
    docs = [
        {"text": "The quick brown fox jumps over the lazy dog."},
        {"text": "The quick brown fox jumps over the lazy dog."},
        {"text": "I am very happy today."},
        {"text": "I am very happy today."},
        {"text": "How are you doing today?"},
        {"text": "How are you doing today?"}
    ]
    
    db = Database()
    db.add(docs)

    query = Query()
    results = db.search(query.text.search("happy"))
    print(results)