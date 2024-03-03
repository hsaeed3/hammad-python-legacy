
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadML ==================================================================#

from sentence_transformers import SentenceTransformer, util
import torch
from typing import List, Tuple

#==============================================================================#

class SemanticSearch:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode_corpus(self, corpus: List[str]) -> torch.Tensor:
        return self.model.encode(corpus, convert_to_tensor=True)

    def search(self, query: str, corpus_embeddings: torch.Tensor, corpus: List[str], top_k: int = 5) -> List[Tuple[str, float]]:
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
        top_results = torch.topk(cos_scores, k=top_k)

        return [(corpus[idx], score.item()) for score, idx in zip(top_results[0], top_results[1])]

#==============================================================================#