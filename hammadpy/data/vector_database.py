
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadML ==================================================================#

from hammadpy import HammadPy

import os
import uuid
from typing import Union, List, Tuple
from annoy import AnnoyIndex
from sentence_transformers import SentenceTransformer
import glob

#==============================================================================#

class VectorDatabase:
    def __init__(self, input_data: Union[str, List[str], AnnoyIndex, List[Tuple[str, list]]], 
                 model_name: str = "all-MiniLM-L6-v2", num_trees: int = 10):
        """
        Initializes a new vector database using Annoy. The input can be a directory containing text files, 
        a pre-built Annoy index, a list/array of sentences, or a list of tuples with sentences and their vectors.
        It also initializes a SentenceTransformer model for converting sentences to vectors unless vectors are provided.

        Args:
            input_data (Union[str, List[str], AnnoyIndex, List[Tuple[str, list]]]): Input to build the index from.
            model_name (str): The pre-trained SentenceTransformers model name (ignored if vectors are provided).
            num_trees (int): The number of trees for the Annoy index.
        """
        self.hpy = HammadPy()
        self.model = SentenceTransformer(model_name) if not isinstance(input_data, list) or isinstance(input_data[0], str) else None
        self.num_trees = num_trees
        self.index = None
        self.dimension = self.model.get_sentence_embedding_dimension() if self.model else len(input_data[0][1])
        self.document_ids = [] 

        if isinstance(input_data, str):
            self.hpy.say("Detected string input for input_data...", "lightblack", "dim")
            self.hpy.say(f"Building vector index using {len(input_data)} entries.", "lightblack", "dim")
            self._handle_string_input(input_data)
            self.hpy.say("Index built successfully.", "lightblue", "dim")
        elif isinstance(input_data, list):
            self.hpy.say("Detected list input for input_data...", "lightblack", "dim")
            self.hpy.say(f"Building vector index using {len(input_data)} entries.", "lightblack", "dim")
            self.hpy.say("Building Vector Index...", "yellow", "dim")
            self._handle_list_input(input_data)
            self.hpy.say("Index built successfully.", "lightblue", "dim")
        elif isinstance(input_data, AnnoyIndex):
            self.hpy.say("Detected an Annoy Index for input_data...", "lightblack", "dim")
            self.index = input_data
        else:
            raise ValueError("Invalid type for input_data.")

        self.hpy.say("Loading Vector Database...", "lightblack", "dim")
        if hasattr(self, 'sentences') and self.sentences:
            self.hpy.say("Detected 'sentences' key..", "lightblack", "dim")
            self.hpy.say(f"Loading {len(self.sentences)} entries.", "lightblack", "dim")
            self._build_index_from_sentences()
            self.hpy.say("Vector Index built successfully.", "lightblue", "dim")
            self.hpy.say("Vector Database loaded.", "blue", "dim")
        elif hasattr(self, 'vectors') and self.vectors:
            self.hpy.say("Detected 'vectors' key..", "lightblack", "dim")
            self.hpy.say(f"Loading {len(self.vectors)} entries.", "lightblack", "dim")
            self._build_index_from_vectors()
            self.hpy.say("Vector Index built successfully.", "lightblue", "dim")
            self.hpy.say("Vector Database loaded.", "blue", "bold")

    def _handle_string_input(self, input_data: str):
        if os.path.isdir(input_data):
            self.sentences, self.document_ids = self._load_sentences_from_directory(input_data)
        elif os.path.isfile(input_data):
            self.index = AnnoyIndex(self.dimension, 'angular')
            self.index.load(input_data)  
        else:
            raise ValueError("Invalid path provided.")

    def _handle_list_input(self, input_data: list):
        if all(isinstance(i, str) for i in input_data): 
            self.sentences = input_data
            self.document_ids = [str(uuid.uuid4()) for _ in input_data]  
        elif all(isinstance(i, tuple) and len(i) == 2 for i in input_data): 
            self.sentences, self.vectors = zip(*input_data)
            self.document_ids = [str(uuid.uuid4()) for _ in input_data]  
        else:
            raise ValueError("Invalid list content for input_data.")

    def _load_sentences_from_directory(self, directory: str) -> Tuple[List[str], List[str]]:
        sentences = []
        document_ids = []
        for file_path in glob.glob(os.path.join(directory, '*.txt')):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_sentences = file.readlines()
                file_id = str(uuid.uuid4())
                sentences.extend(file_sentences)
                document_ids.extend([file_id] * len(file_sentences))  
        return sentences, document_ids

    def _build_index_from_sentences(self):
        self.index = AnnoyIndex(self.dimension, 'angular')
        for i, sentence in enumerate(self.sentences):
            vector = self.model.encode(sentence) if self.model else self.vectors[i]
            self.index.add_item(i, vector)
        self.index.build(self.num_trees)

    def _build_index_from_vectors(self):
        self.index = AnnoyIndex(self.dimension, 'angular')
        for i, vector in enumerate(self.vectors):
            self.index.add_item(i, vector)
        self.index.build(self.num_trees)

    def search(self, query: str, k: int) -> List[Tuple[int, str]]:
        if not self.index:
            raise ValueError("Index has not been built or loaded.")
        query_vector = self.model.encode([query])[0] if self.model else query
        indices = self.index.get_nns_by_vector(query_vector, k, include_distances=False)
        return [(indices[i], self.document_ids[indices[i]]) for i in range(len(indices))]

#==============================================================================#

