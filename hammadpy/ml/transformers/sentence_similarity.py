
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

class SentenceSimilarity:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def compute_similarity(self, sentences1: List[str], sentences2: List[str]) -> List[Tuple[str, str, float]]:
        embeddings1 = self.model.encode(sentences1, convert_to_tensor=True)
        embeddings2 = self.model.encode(sentences2, convert_to_tensor=True)
        cosine_scores = util.cos_sim(embeddings1, embeddings2)

        return [(sentences1[i], sentences2[j], cosine_scores[i][j].item()) for i in range(len(sentences1)) for j in range(len(sentences2))]

#==============================================================================#
