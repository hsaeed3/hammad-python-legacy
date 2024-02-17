
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==##
##== @/pydantic/models ==#######################################################
##== Pydantic Models ==#########################################################

#==============================================================================#

from typing import List
from pydantic import BaseModel, Field

#==============================================================================#

class Pydantic:
    def __init__(self):
        pass

    def model(self, model : str = None):
        if model == "":
            raise Exception("Model not provided.")
        elif model == "str":
            return ContentModel_STR
        elif model == "int":
            return ContentModel_INT
        elif model == "list":
            return ListModel_STR
        elif model == "list_int":
            return ListModel_INT
        elif model == "double_list":
            return DoubleListModel_STR
        elif model == "double_list_int":
            return DoubleListModel_INT
        elif model == "triple_list":
            return TripleListModel_STR
        elif model == "triple_list_int":
            return TripleListModel_INT
        elif model == "nested_list":
            return NestedListModel_STR
        elif model == "nested_list_int":
            return NestedListModel_INT
        elif model == "nested_list_intstr":
            return NestedListModel_INTSTR
        elif model == "double_nested_list":
            return DoubleNestedListModel_STRSTR
        elif model == "double_nested_list_intstr":
            return DoubleNestedListModel_INTSTR

#==============================================================================#

class ContentModel_STR(BaseModel):
    """Model for storing a single string value."""
    content: str = Field(...)

class ContentModel_INT(BaseModel):
    """Model for storing a single integer value."""
    content: int = Field(...)

class ListModel_STR(BaseModel):
    """Model for storing a list of strings."""
    list: List[str] = Field(...)

class ListModel_INT(BaseModel):
    """Model for storing a list of integers."""
    list: List[int] = Field(...)

class DoubleListModel_STR(BaseModel):
    """Model for storing two lists of strings."""
    list: List[str] = Field(...)
    list: List[str] = Field(...)

class DoubleListModel_INT(BaseModel):
    """Model for storing two lists of integers."""
    list: List[int] = Field(...)
    list: List[int] = Field(...)

class DoubleListModel_STR(BaseModel):
    """Model for storing two lists of strings."""
    list: List[str] = Field(...)
    list: List[str] = Field(...)

class DoubleListModel_INT(BaseModel):
    """Model for storing two lists of integers."""
    list: List[int] = Field(...)
    list: List[int] = Field(...)

class TripleListModel_STR(BaseModel):
    """Model for storing three lists of strings."""
    list: List[str] = Field(...)
    list: List[str] = Field(...)
    list: List[str] = Field(...)

class TripleListModel_INT(BaseModel):
    """Model for storing three lists of integers."""
    list: List[int] = Field(...)
    list: List[int] = Field(...)
    list: List[int] = Field(...)

class NestedListModel_STR(BaseModel):
    """Model for storing a nested list of strings (list of lists of strings)."""
    list: List[List[str]] = Field(...)

class NestedListModel_INT(BaseModel):
    """Model for storing a nested list of integers (list of lists of integers)."""
    list: List[List[int]] = Field(...)

class NestedListModel_INTSTR(BaseModel):
    """Model for storing a nested list with mixed integers and strings."""
    list: List[List[int]] = Field(...)
    list: List[List[str]] = Field(...)

class DoubleNestedListModel_STRSTR(BaseModel):
    """Model for storing two nested lists of strings."""
    list: List[List[str]] = Field(...)
    list: List[List[str]] = Field(...)

class DoubleNestedListModel_INTSTR(BaseModel):
    """Model for storing two nested lists, one of integers and one of strings."""
    list: List[List[int]] = Field(...)
    list: List[List[str]] = Field(...)


