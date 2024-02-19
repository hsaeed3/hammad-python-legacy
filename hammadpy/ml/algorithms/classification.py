
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== hammadpy ==##################################== Hammad's Python Library ==#
##== @/analyze/classification  ==###############################################

#==============================================================================#

from sklearn.neighbors import KNeighborsClassifier

#==============================================================================#

class Classification:
    """Provides classification functionality using scikit-learn models"""

    def __init__(self, model_type='knn', **kwargs):
        """
        Args:
            model_type (str): Type of classifier ('knn', 'svm', etc.). Defaults to 'knn'.
            **kwargs:  Keyword arguments for specific classifier models.
        """
        self.model_type = model_type
        self.model_kwargs = kwargs
        self.model = None

    def fit(self, X, y):
        """Trains the classification model.

        Args:
            X: Feature data.
            y: Target labels.
        """
        if self.model_type == 'knn':
            self.model = KNeighborsClassifier(n_neighbors=3, **self.model_kwargs)
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")

        self.model.fit(X, y)

    def predict(self, X):
        """Performs prediction using the trained model.

        Args:
            X: Feature data for prediction.

        Returns:
             Predicted labels.
        """
        if self.model is None:
            raise RuntimeError("Model is not trained. Call fit() first.")
        return self.model.fit(X)