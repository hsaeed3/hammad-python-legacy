from hammadpy import Core
import os
import uuid
from typing import Union, List, Tuple, Optional
from annoy import AnnoyIndex
from sentence_transformers import SentenceTransformer
import glob

"""
hammadpy.vector_database
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the VectorDatabase class which uses sentence transformers
to build and search a vector database using Annoy.

Classes:
    VectorDatabase: This class uses a SentenceTransformer model to build and search a vector database using Annoy.
    SentenceBERT: This class uses a SentenceTransformer model to generate embeddings for a list of sentences.

Methods:    
    search(self, query: str, k: int) -> List[Tuple[int, str]]: Searches the index for the k most similar vectors to the query.
    embed(self, sentences: List[str]) -> List[Tuple[str, List[float]]]: Encodes a list of sentences into embeddings.
"""

#==============================================================================#

class SentenceBERT:
    """
    A class for generating sentence embeddings using the SentenceTransformers library.
    
    Attributes
    ----------
    model : SentenceTransformer
        a SentenceTransformer model used to generate sentence embeddings

    Methods
    -------
    encode(sentences: List[str]) -> List[Tuple[str, List[float]]]:
        Encodes a list of sentences into embeddings.
    """

    def __init__(self, model_name: Optional[str] = "all-MiniLM-L6-v2"):
        """
        Initializes the SentenceEmbedder with a specified model.

        Parameters
        ----------
            model_name : str, optional
                the name of the SentenceTransformer model to use (default is "all-MiniLM-L6-v2")
        """
        if not model_name:
            raise ValueError("Model name cannot be None")
        self.model = SentenceTransformer(model_name)

    def embed(self, sentences: List[str]) -> List[Tuple[str, List[float]]]:
        """
        Encodes a list of sentences into embeddings.

        Parameters
        ----------
            sentences : List[str]
                the list of sentences to encode

        Returns
        -------
            List[Tuple[str, List[float]]]
                a list of tuples containing the original sentences and their embeddings
        """
        if not sentences:
            raise ValueError("Sentences list cannot be empty")
        embeddings = self.model.encode(sentences)
        return list(zip(sentences, embeddings))
    
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
        self.hpy = Core()
        self.model = SentenceTransformer(model_name) if not isinstance(input_data, list) or isinstance(input_data[0], str) else None
        self.num_trees = num_trees
        self.index = None
        self.dimension = self.model.get_sentence_embedding_dimension() if self.model else len(input_data[0][1])
        self.document_ids = [] 

        if isinstance(input_data, str):
            self._handle_string_input(input_data)
            self.hpy.say("Index built successfully.", "lightblue", style="dim")
        elif isinstance(input_data, list):
            self._handle_list_input(input_data)
            self.hpy.say("Index built successfully.", "lightblue", style="dim")
        elif isinstance(input_data, AnnoyIndex):
            self.index = input_data
        else:
            raise ValueError("Invalid type for input_data.")

        self.hpy.say("Loading Vector Database...", "lightblack", style="dim")
        if hasattr(self, 'sentences') and self.sentences:
            self._build_index_from_sentences()
        elif hasattr(self, 'vectors') and self.vectors:
            self._build_index_from_vectors()
            self.hpy.say("Vector Database loaded.", "blue", style="bold")

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

    def _build_index_from_sentences(self):
        self.index = AnnoyIndex(self.dimension, 'angular')
        for i, sentence in enumerate(self.sentences):
            vector = self.model.encode([sentence])[0] if self.model else self.vectors[i]
            self.index.add_item(i, vector)
        self.index.build(self.num_trees)

    def _build_index_from_vectors(self):
        self.index = AnnoyIndex(self.dimension, 'angular')
        for i, vector in enumerate(self.vectors):
            self.index.add_item(i, vector)
        self.index.build(self.num_trees)

    def search(self, query: str, k: int = 5) -> List[Tuple[int, str]]:
        if not self.index:
            raise ValueError("Index has not been built or loaded.")
        query_vector = self.model.encode([query])[0] if self.model else query
        indices = self.index.get_nns_by_vector(query_vector, k, include_distances=False)
        results = []
        for index in indices:
            sentence = self.sentences[index]
            document_id = self.document_ids[index]
            vector = self.index.get_item_vector(index)
            results.append((index, sentence, document_id, vector))
        return results    

#==============================================================================#

