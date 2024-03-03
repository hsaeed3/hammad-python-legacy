
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadML =================================================---==============#

from sentence_transformers import SentenceTransformer, losses
import torch

#==============================================================================#

class Loss:
    def __init__(self, loss_type: str, data_format: str, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.loss = self.initialize_loss(loss_type, data_format)

    def initialize_loss(self, loss_type: str, data_format: str):
        if data_format == "single_sentences":
            return self._init_single_sentence_loss(loss_type)
        elif data_format == "sentence_pairs":
            return self._init_sentence_pair_loss(loss_type)
        elif data_format == "triplets":
            return self._init_triplet_loss(loss_type)
        else:
            raise ValueError("Unsupported data format")

    def _init_single_sentence_loss(self, loss_type: str):
        if loss_type == "BatchAllTripletLoss":
            return losses.BatchAllTripletLoss(model=self.model)
        elif loss_type == "BatchHardTripletLoss":
            return losses.BatchHardTripletLoss(model=self.model)
        elif loss_type == "BatchSemiHardTripletLoss":
            return losses.BatchSemiHardTripletLoss(model=self.model)
        else:
            raise ValueError("Unsupported loss type for single sentences")

    def _init_sentence_pair_loss(self, loss_type: str):
        if loss_type == "SoftmaxLoss":
            return losses.SoftmaxLoss(model=self.model)
        elif loss_type == "ContrastiveLoss":
            return losses.ContrastiveLoss(model=self.model)
        else:
            raise ValueError("Unsupported loss type for sentence pairs")

    def _init_triplet_loss(self, loss_type: str):
        if loss_type == "TripletLoss":
            return losses.TripletLoss(model=self.model)
        elif loss_type == "MultipleNegativesRankingLoss":
            return losses.MultipleNegativesRankingLoss(model=self.model)
        else:
            raise ValueError("Unsupported loss type for triplets")
        
#==============================================================================#