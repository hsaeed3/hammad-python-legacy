
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


class ContentModel_STR(BaseModel):
    content: str = Field(..., description="STR")

class ContentModel_INT(BaseModel):
    content: int = Field(..., description="INT")

class ListModel_STR(BaseModel):
    list: List[str] = Field(..., description="STR")

class ListModel_INT(BaseModel):
    list: List[int] = Field(..., description="INT")

class NestedListModel_STR(BaseModel):
    list: List[List[str]] = Field(..., description="NESTED STR")
    list: List[List[str]] = Field(..., description="NESTED STR")

class NestedListModel_INT(BaseModel):
    list: List[List[int]] = Field(..., description="NESTED INT")
    list: List[List[int]] = Field(..., description="NESTED INT")

class NestedListModel_INTSTR(BaseModel):
    list: List[List[int]] = Field(..., description="NESTED INT")
    list: List[List[str]] = Field(..., description="NESTED STR")

class DoubleNestedListModel_STRSTR(BaseModel):
    list: List[str] = Field(..., description="STR")
    list: List[str] = Field(..., description="STR")
    list: List[List[str]] = Field(..., description="NESTED STR")
    list: List[List[str]] = Field(..., description="NESTED STR")

class DoubleNestedListModel_INTSTR(BaseModel):
    list: List(int) = Field(..., description="INT")
    list: List(str) = Field(..., description="STR")
    list: List[List[int]] = Field(..., description="NESTED INTR")
    list: List[List[str]] = Field(..., description="NESTED STR")



