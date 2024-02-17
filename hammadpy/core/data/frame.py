
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==##
##== @/core/data/frame ==#######################################################
##== Quick Pandas Toolkit ==####################################################

#==============================================================================#

import pandas as pd
from pandas import DataFrame

#==============================================================================#

class Frame(DataFrame):
    """
    Provides a simple wrapper for pandas DataFrames, facilitating common DataFrame operations.
    """

    def add_column(self, column_name: str, data: list):
        """
        Adds a new column to the DataFrame.

        Args:
            column_name (str): The name of the new column.
            data (list): A list of values to populate the column.
        """
        super().__setitem__(column_name, data)

    def add_row(self, data: dict):
        """
        Adds a new row to the DataFrame.

        Args:
            data (dict): A dictionary where keys represent column names and values represent row data.
        """
        super().append(data, ignore_index=True)

    def concat(self, other: DataFrame, axis: int = 0):
        """
        Concatenates two DataFrames.

        Args:
            other (DataFrame): The DataFrame to concatenate with the current DataFrame.
            axis (int, optional): The axis to concatenate along. Defaults to 0.
        """
        return pd.concat([self, other], axis=axis)

    def shape(self):
        """
        Returns the shape of the DataFrame as a tuple (rows, columns).
        """
        return self.shape

