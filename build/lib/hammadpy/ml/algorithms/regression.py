
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== hammadpy ==##################################== Hammad's Python Library ==#
##== @/analyze/regression ==####################################################

#==============================================================================#

from sklearn.linear_model import LinearRegression

#==============================================================================#

class Regression:
    """Provides regression functionality using scikit-learn models"""

    def __init__(self, model_type='linear', **kwargs):
        """
        Args:
            model_type (str): Type of regressor ('linear', 'ridge', etc.). Defaults to 'linear'. (Currently only linear is supported.)
            **kwargs:  Keyword arguments for specific regressor models.
        """
        self.model_type = model_type
        self.model_kwargs = kwargs
        self.model = None

    def fit(self, X, y):
        """Trains the regression model.

        Args:
            X: Feature data.
            y: Target values.
        """
        if self.model_type == 'linear':
            self.model = LinearRegression(**self.model_kwargs) 
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")

        self.model.fit(X, y)

    def predict(self, X):
        """Performs prediction using the trained model.

        Args:
            X: Feature data for prediction.

        Returns:
             Predicted values.
        """
        if self.model is None:
            raise RuntimeError("Model is not trained. Call fit() first.")
        return self.model.predict(X)