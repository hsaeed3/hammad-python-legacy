
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== hammadpy ==##################################== Hammad's Python Library ==#
##== @/analyze/cluster ==#######################################################

#==============================================================================#

from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN

#==============================================================================#

class Clustering:
    """Provides clustering functionality using scikit-learn models"""

    def __init__(self, model_type='kmeans', **kwargs):
        """
        Args:
            model_type (str): Type of clustering algorithm ('kmeans', 'agglomerative', 'dbscan', etc.). Defaults to 'kmeans'.
            **kwargs: Keyword arguments for specific clustering models.
        """
        self.model_type = model_type
        self.model_kwargs = kwargs
        self.model = None

    def fit(self, X):
        """Trains the clustering model.

        Args:
            X: Feature data.
        """
        if self.model_type == 'kmeans':
            self.model = KMeans(**self.model_kwargs)
        elif self.model_type == 'agglomerative':
            self.model = AgglomerativeClustering(**self.model_kwargs)
        elif self.model_type == 'dbscan':
            self.model = DBSCAN(**self.model_kwargs)
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")

        self.model.fit(X)

    def predict(self, X):
        """Assigns data points to clusters.

        Args:
            X: Feature data.

        Returns:
            Cluster labels.
        """
        if self.model is None:
            raise RuntimeError("Model is not trained. Call fit() first.")
        return self.model.predict(X)