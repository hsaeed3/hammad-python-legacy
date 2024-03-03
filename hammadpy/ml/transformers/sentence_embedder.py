
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadML ============---===================================================#

from typing import List, Optional, Tuple
from sentence_transformers import SentenceTransformer

#==============================================================================#

class SentenceBERT:
    """
    A class for generating sentence embeddings using the SentenceTransformers library.
    """

    def __init__(self, model_name: Optional[str] = "all-MiniLM-L6-v2"):
        """
        Initializes the SentenceEmbedder with a specified model.

        Args:
            model_name (Optional[str]): The name of the SentenceTransformer model to use.
        """
        if not model_name:
            raise ValueError("Model name cannot be None")
        self.model = SentenceTransformer(model_name)

    def encode(self, sentences: List[str]) -> List[Tuple[str, List[float]]]:
        """
        Encodes a list of sentences into embeddings.

        Args:
            sentences (List[str]): A list of sentences to encode.

        Returns:
            List[Tuple[str, List[float]]]: A list of tuples where each tuple contains the original sentence and its corresponding embedding.
        """
        if not sentences:
            raise ValueError("Sentences list cannot be empty")
        embeddings = self.model.encode(sentences)
        return list(zip(sentences, embeddings))

#==============================================================================#

if __name__ == "__main__":
    embedder = SentenceBERT()
    sentences = [
        "This framework generates embeddings for each input sentence",
        "Sentences are passed as a list of string.",
        "The quick brown fox jumps over the lazy dog."
    ]
    embeddings = embedder.encode_sentences(sentences)
    for sentence, embedding in embeddings:
        print("Sentence:", sentence)
        print("Embedding:", list(embedding))
