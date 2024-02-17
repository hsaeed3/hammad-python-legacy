
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

from pydantic import BaseModel, Field

#==============================================================================#


class ContentModel_STR(BaseModel):
    content: str = Field

class ContentModel_INT(BaseModel):
    content: int = Field

class ListModel_STR(BaseModel):
    list: list[str] = Field

class ListModel_INT(BaseModel):
    list: list[int] = Field

class DoubleListModel_STR(BaseModel):
    list: list[str] = Field
    list: list[str] = Field

class DoubleListModel_INT(BaseModel):
    list: list[int] = Field
    list: list[int] = Field

class TripleListModel_STR(BaseModel):
    list: list[str] = Field
    list: list[str] = Field
    list: list[str] = Field

class TripleListModel_INT(BaseModel):
    list: list[int] = Field
    list: list[int] = Field
    list: list[int] = Field

class NestedListModel_STR(BaseModel):
    list: list[list[str]] = Field
    list: list[list[str]] = Field

class NestedListModel_INT(BaseModel):
    list: list[list[int]] = Field
    list: list[list[int]] = Field

class NestedListModel_INTSTR(BaseModel):
    list: list[list[int]] = Field
    list: list[list[str]] = Field

class DoubleNestedListModel_STRSTR(BaseModel):
    list: list[str] = Field
    list: list[str] = Field
    list: list[list[str]] = Field
    list: list[list[str]] = Field

class DoubleNestedListModel_INTSTR(BaseModel):
    list: list(int) = Field
    list: list(str) = Field
    list: list[list[int]] = Field
    list: list[list[str]] = Field



