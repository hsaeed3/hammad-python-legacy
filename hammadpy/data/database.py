
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadML ==================================================================#

from hammadpy import HammadPy

import os
from whoosh import index as whoosh_index
from whoosh.analysis import StandardAnalyzer
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser, MultifieldParser
import pandas as pd
from typing import Optional, List, Dict, Union, Tuple

#==============================================================================#

class Database:
    def __init__(self, index_dir: Optional[str] = None, content: Optional[Union[str, Tuple, List]] = None,
                 schema: Optional[Schema] = None):
        """
        Initializes the search index.

        Args:
            index_dir (Optional[str]): Path to the index directory.
            content (Optional[Union[str, Tuple, List]]): A tuple/array representing the index or a string for the content field.
            schema (Optional[Schema]): A Whoosh Schema to define the index structure.
                                       Defaults to a basic schema with 'id' and 'content'.
        """
        self.hpy = HammadPy()
        self.index_dir = index_dir
        self.content = content
        self.schema = schema if schema is not None else Schema(id=ID(stored=True), content=TEXT(analyzer=StandardAnalyzer(), stored=True))


        self.ix = None
        if self.content is not None:
            self.hpy.say("Creating Database Index from content...", "lightblack", "dim")
            self.hpy.say(f"Detected {len(self.content)} entries.", "lightblack", "dim")
            self._create_index_from_content()
        elif self.index_dir is not None:
            self.hpy.say("Building Index...", "lightblack", "dim")
            self.hpy.say(f"Directory: {self.index_dir}", "lightblack", "dim")
            self._use_existing_index()
        self.hpy.say("Database loaded.", "green", "bold")

    def _create_index_from_content(self):
        if self.index_dir is None:
            self.index_dir = "temp_db"
            if not os.path.exists(self.index_dir):
                os.mkdir(self.index_dir)

        self.ix = whoosh_index.create_in(self.index_dir, self.schema)

        with self.ix.writer() as writer:
            if isinstance(self.content, (tuple, list)):
                for item_id, item_content in enumerate(self.content):
                    writer.add_document(id=str(item_id), content=str(item_content))
            elif isinstance(self.content, str):
                writer.add_document(id="1", content=self.content)

    def _use_existing_index(self):
        if not os.path.exists(self.index_dir):
            os.mkdir(self.index_dir)
            self.ix = whoosh_index.create_in(self.index_dir, self.schema)
        else:
            self.ix = whoosh_index.open_dir(self.index_dir)

    def add_csv(self, csv_path: str, id_column: str, content_column: str):
        """
        Adds documents to the index from a CSV file.
        """
        df = pd.read_csv(csv_path)
        writer = self.ix.writer()
        for _, row in df.iterrows():
            writer.add_document(id=str(row[id_column]), content=str(row[content_column]))
        writer.commit()

    def add(self, documents: List[Dict[str, str]]):
        """
        Adds documents to the index.
        """
        writer = self.ix.writer()
        for document in documents:
            if 'id' in document and 'content' in document: 
                writer.add_document(**document)
            else:
                raise ValueError("Each document must contain 'id' and 'content' fields.")
        writer.commit()

    def search(self, query_str: str, fieldname: str = 'content') -> List[Dict[str, str]]:
        """
        Searches the index.
        """
        results_list = []
        with self.ix.searcher() as searcher:
            query = QueryParser(fieldname, self.ix.schema).parse(query_str)
            results = searcher.search(query, limit=None)  
            for result in results:
                doc_id = result.get('id', 'No ID available')
                content = result.get('content', 'No content available')
                results_list.append({"id": doc_id, "content": content})
        return results_list
    
#==============================================================================#