from sentence_transformers import SentenceTransformer, util
import torch
from typing import List, Tuple

"""
hammadpy.ml.transformers.semantic_search
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the SemanticSearch class which uses sentence transformers
to perform semantic search on a list of sentences.

Classes:
    SemanticSearch: This class uses a SentenceTransformer model to perform semantic search on a list of sentences.

Methods:
    encode_corpus(self, corpus: List[str]) -> torch.Tensor: Encodes a list of sentences into embeddings.
    search(self, query: str, corpus_embeddings: torch.Tensor, corpus: List[str], top_k: int = 5) -> List[Tuple[str, float]]: Performs semantic search on a list of sentences.
"""
#==============================================================================#

class SemanticSearch:
    """
    A class used to perform semantic search on a list of sentences using a SentenceTransformer model.

    Attributes
    ----------
    model : SentenceTransformer
        a SentenceTransformer model used to compute sentence embeddings

    Methods
    -------
    encode_corpus(corpus: List[str]) -> torch.Tensor:
        Encodes a list of sentences into embeddings.
    search(query: str, corpus_embeddings: torch.Tensor, corpus: List[str], top_k: int = 5) -> List[Tuple[str, float]]:
        Performs semantic search on a list of sentences.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Constructs all the necessary attributes for the SemanticSearch object.

        Parameters
        ----------
            model_name : str, optional
                the name of the SentenceTransformer model to use (default is "all-MiniLM-L6-v2")
        """
        self.model = SentenceTransformer(model_name)

    def encode_corpus(self, corpus: List[str]) -> torch.Tensor:
        """
        Encodes a list of sentences into embeddings.

        Parameters
        ----------
            corpus : List[str]
                the list of sentences to encode

        Returns
        -------
        torch.Tensor
            a tensor containing the embeddings of the sentences
        """
        return self.model.encode(corpus, convert_to_tensor=True)

    def search(self, query: str, corpus_embeddings: torch.Tensor, corpus: List[str], top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Performs semantic search on a list of sentences.

        Parameters
        ----------
            query : str
                the query sentence
            corpus_embeddings : torch.Tensor
                the embeddings of the corpus sentences
            corpus : List[str]
                the list of sentences to search
            top_k : int, optional
                the number of results to return (default is 5)

        Returns
        -------
            List[Tuple[str, float]]
                a list of tuples, each containing a sentence from the corpus and its similarity score to the query
        """
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
        top_results = torch.topk(cos_scores, k=top_k)

        return [(corpus[idx], score.item()) for score, idx in zip(top_results[0], top_results[1])]

#==============================================================================#