
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==## 
##== @/llms/huggingface/models ==###############################################
##== Creates Langchain Pydantic Models ==#######################################

#==============================================================================#

from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field

#==============================================================================#

class QueryLangchainContentModel(BaseModel):
    """
    Model for Completion Content.
    """
    content: str = Field(description="Generated content, from request.")

class QueryLangchainListModel(BaseModel):
    """
    Model for Completion List.
    """
    items: list[str] = Field(description="List of items, from request.")

#==============================================================================#

class QueryContentModel(BaseModel):
    """
    Model for Langchain Query.
    """
    content: str = Field(..., description="Content Model.")

class QueryListModel(BaseModel):
    """
    Model for Langchain List.
    """
    items: list[str] = Field(..., description="List Model.")

class QueryNestedListModel(BaseModel):
    """
    Model for Langchain Nested List.
    """
    nested_items: list[list[str]] = Field(..., description="Nested list of items, from request.")

