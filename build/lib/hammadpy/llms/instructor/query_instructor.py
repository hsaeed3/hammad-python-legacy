
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== hammadpy ==##################################== Hammad's Python Library ==##
#== @/llms/completions/openai/query ==#########################################

#==============================================================================#

import os
import instructor
from openai import OpenAI

from typing import List
from pydantic import BaseModel, Field

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

#==============================================================================#

class Instructor:
    def __init__(self, key: str = None):
        self.key = key
        if self.key == None:
            os.getenv("OPENAI_API_KEY")
        self.ai = instructor.patch(OpenAI(api_key=self.key))
        self.pymodel = None
        
    def instruct_model(self, 
             model: str = None, 
             system: str = None, 
             query: str = None, 
             pymodel = ['content_str', 'content_int', 'list_str', 'list_int', 
                        'double_list_str', 'double_list_int', 'triple_list_str',
                        'triple_list_int', 'nested_list_str', 'nested_list_int', 
                        'nested_list_intstr']):
        """
        Creates an OpenAI query, with a user provided Pydantic model.

        Args:
        -   model (str): Model to be used for the query.
        -   system (str): System message to be used for the query.
        -   query (str): Query to be sent to OpenAI.
        -   pymodel (str):  **Name** of the Pydantic model to structure the response. 
                          Supported models:

            * **content_str:** Expects a single string response (*ContentModel_STR*)
            * **content_int:** Expects a single integer response (*ContentModel_INT*)
            * **list_str:** Expects a list of strings (*ListModel_STR*)
            * **list_int:** Expects a list of integers (*ListModel_INT*)
            * **double_list_str:** Expects two lists of strings (*DoubleListModel_STR*)
            * **double_list_int:** Expects two lists of integers (*DoubleListModel_INT*)
            * **triple_list_str:** Expects three lists of strings (*TripleListModel_STR*)
            * **triple_list_int:** Expects three lists of integers (*TripleListModel_INT*)
            * **nested_list_str:** Expects a nested list of strings (list of lists of strings) (*NestedListModel_STR*)
            * **nested_list_int:** Expects a nested list of integers (*NestedListModel_INT*)
            * **nested_list_intstr:** Expects a nested list with inner lists containing integers and strings (*NestedListModel_INTSTR*)

        """
        if pymodel == None:
            self.pymodel = ContentModel_STR
        elif pymodel == "content_str":
            self.pymodel = ContentModel_STR
        elif pymodel == "content_int":
            self.pymodel = ContentModel_INT
        elif pymodel == "list":
            self.pymodel = ListModel_STR
        elif pymodel == "list_int":
            self.pymodel = ListModel_INT
        elif pymodel == "double_list_str":
            self.pymodel = DoubleListModel_STR
        elif pymodel == "double_list_int":
            self.pymodel = DoubleListModel_INT
        elif pymodel == "triple_list_str":
            self.pymodel = TripleListModel_STR
        elif pymodel == "triple_list_int":
            self.pymodel = TripleListModel_INT
        elif pymodel == "nested_list_str":
            self.pymodel = NestedListModel_STR
        elif pymodel == "nested_list_int":
            self.pymodel = NestedListModel_INT
        elif pymodel == "nested_list_intstr":
            self.pymodel = NestedListModel_INTSTR
        if model == "3":
            self.model = "gpt-3.5-turbo"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.system = system
        self.query = query
        if self.model == None:
            print("Model is required for invoke()")
            return
        elif self.system == None:
            print("System message is required for invoke()")
            return
        elif self.query == None:
            print("Query is required for invoke()")
            return
        else:
            for _ in range(3): 
                try:
                    completion = self.ai.chat.completions.create(
                        model=self.model,
                        response_model=self.pymodel,
                        messages=[{"role": "system", "content": self.system}, {"role": "user", "content": self.query}]
                    )
                    if self.pymodel in [ContentModel_STR, ContentModel_INT]:
                        assert hasattr(completion, 'content') and completion.content, "No completion returned."
                    else:
                        assert hasattr(completion, 'list') and completion.list, "No completion returned."
                    return completion
                except AssertionError:
                    print("Assertion failed, retrying...")
                    continue
            raise ValueError("Failed to get a valid completion after 3 attempts.")
        
    def instruct(self, model: str = None, query: str = None, system: str = None, pydantic = None):
        """
        User Provided Pydantic Model Query

        Args:
        -   model (str): Model to be used for the query.
        -   query (str): Query to be sent to OpenAI.
        -   system (str): System message to be used for the query.
        -   pydantic (BaseModel) : Pydantic model to structure the response.
        """
        if pydantic == None:
            raise Exception("Pydantic model is required for invoke_model()")
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        self.system = system
        completion = self.ai.chat.completions.create(
            model=self.model,
            response_model=pydantic,
            messages=[{"role": "system", "content": self.system}, {"role": "user", "content": self.query}]
        )
        return completion