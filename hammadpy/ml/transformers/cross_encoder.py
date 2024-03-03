
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadML ==================================================================#

from typing import List, Dict, Tuple, Optional, Union
from sentence_transformers import CrossEncoder

#==============================================================================#

class XEncoder:
    def __init__(self, model_name: Optional[str] = None, max_length: Optional[int] = None):
        """
        Initializes a new CrossEncoder model for scoring sentence pairs.
        Defaults to using the MS MARCO model if none is specified.

        Args:
            model_name (Optional[str]): The pre-trained SentenceTransformers CrossEncoder model name.
            max_length (Optional[int]): Maximum sequence length for the model inputs.
        """
        default_model = "cross-encoder/ms-marco-MiniLM-L-12-v2"  # Default to MS MARCO model
        self.model = CrossEncoder(model_name or default_model, max_length=max_length)

    def re_rank(self, query: str, x: List[str], y: List[str]) -> List[Tuple[int, float]]:
        """
        Re-ranks pairs formed by two lists of chunks based on their relevance to a single query using the CrossEncoder model.
        If the two lists of chunks have different lengths, the longer one is truncated to match the shorter one.

        Args:
            query (str): The query sentence.
            x (List[str]): The first list of text chunks.
            y (List[str]): The second list of text chunks.

        Returns:
            List[Tuple[int, float]]: A list of tuples where each tuple contains the index of the chunk pair and its corresponding score, 
                                     sorted in descending order of scores. The index corresponds to the position in the original lists.
        """
        min_length = min(len(x), len(y))
        x = x[:min_length]
        y = y[:min_length]
        pairs = [(query, chunk1 + " " + chunk2) for chunk1, chunk2 in zip(x, y)]
        scores = self.model.predict(pairs)
        index_with_score = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

        return index_with_score
    
#==============================================================================#
