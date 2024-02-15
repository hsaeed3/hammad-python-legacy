
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==## 
##== @/llms/completions/openai/query ==#########################################
##== Queries OpenAI Chat Completions ==#########################################

#==============================================================================#

from ....llms.lib.models import QueryContentModel, QueryListModel, QueryNestedListModel

import re
import os
import json
import getpass
import asyncio
import instructor
from openai import OpenAI

#==============================================================================#
class OpenAIKey:
    def __init__(self):
        print("Testing OpenAI API Key.")

    def key(self):
        if os.getenv("OPENAI_API_KEY") == None:
            print("No OpenAI API Key found in environment variables.")
            self.key = getpass.getpass("OpenAI API Key: ")
            os.environ["OPENAI_API_KEY"] = self.key
            self.apikey = os.getenv("OPENAI_API_KEY")
            return self.apikey
        else:
            os.environ["OPENAI_API_KEY"] = self.key
            self.key = os.getenv("OPENAI_API_KEY")
            return self.apikey          
            
#==============================================================================#

class OpenAIQuery:
    def __init__(self, key: str = None):
        self.key = key
        self.ai = instructor.patch(OpenAI(api_key=self.key))


    def chat_content(self, model: str = None, system: str = None, query: str = None):
        """"
        Sends a query to OpenAI Chat Completions.
        
        
        Args:
        -   model (str): Model to be used for the query.
        -   pymodel (str): Pydantic Model to be used for the query.
        -   system (str): System message to be used for the query.
        -   query (str): Query to be sent to OpenAI.
        """
        if model == "3":
            self.model = "gpt-3.5-turbo"
        if model == "4":
            self.model = "gpt-4-preview-1106"
        self.pymodel = QueryContentModel
        self.system = system
        self.query = query
        if self.model == None:
            print("Model is required for invoke()")
            return
        elif self.pymodel == None:
            print("Pydantic Model is required for invoke()")
            return
        elif self.system == None:
            print("System message is required for invoke()")
            return
        elif self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.completion = self.ai.chat.completions.create(
                model=self.model,
                response_model=self.pymodel,
                messages=[{"role": "system", "content": self.system}, {"role": "user", "content": self.query}]
            )
            assert isinstance(self.completion, QueryContentModel)
            print(self.completion.model_dump_json(indent=2))
            self.completion = self.completion.model_dump_json(indent=2)
            self.completion = json.loads(self.completion)
            self.completion = self.completion["content"]
            return self.completion
        
    def chat_list(self, model: str = None, system: str = None, query: str = None):
        """"
        Sends a query to OpenAI Chat Completions.
        Returns a list of completions.
        
        
        Args:
        -   model (str): Model to be used for the query.
        -   pymodel (str): Pydantic Model to be used for the query.
        -   system (str): System message to be used for the query.
        -   query (str): Query to be sent to OpenAI.
        """
        if model == "3":
            self.model = "gpt-3.5-turbo"
        if model == "4":
            self.model = "gpt-4-preview-1106"
        self.pymodel = QueryListModel
        self.system = system
        self.query = query
        if self.model == None:
            print("Model is required for invoke()")
            return
        elif self.pymodel == None:
            print("Pydantic Model is required for invoke()")
            return
        elif self.system == None:
            print("System message is required for invoke()")
            return
        elif self.query == None:
            print("Query is required for invoke()")
            return
        elif self.query == tuple:
            for i in self.query:
                self.completion = self.ai.chat.completions.create(
                    model=self.model,
                    response_model=self.pymodel,
                    messages=[{"role": "system", "content": self.system}, {"role": "user", "content": i}]
                )
                assert isinstance(self.completion, QueryListModel)
                return self.completion
        else:
            self.completion = self.ai.chat.completions.create(
                model=self.model,
                response_model=self.pymodel,
                messages=[{"role": "system", "content": self.system}, {"role": "user", "content": self.query}]
            )
            assert isinstance(self.completion, QueryListModel)
            self.completion = self.completion.model_dump_json(indent=2)
            self.completions = json.loads(self.completion)
            self.completions = self.completions["items"]
            return self.completions
        
    def chat_nestedlist(self, model: str = None, system: str = None, query: str = None):
        """
        Sends a query to OpenAI Chat Completions.
        

        Args:
        -   model (str): Model to be used for the query.
        -   pymodel (str): Pydantic Model to be used for the query.
        -   system (str): System message to be used for the query.
        -   query (str): Query to be sent to OpenAI.
        """
        if model == "3":
            self.model = "gpt-3.5-turbo"
        if model == "4":
            self.model = "gpt-4-preview-1106"
        self.pymodel = QueryNestedListModel
        self.system = system
        self.query = query
        if self.model == None:
            print("Model is required for invoke()")
            return
        elif self.pymodel == None:
            print("Pydantic Model is required for invoke()")
            return
        elif self.system == None:
            print("System message is required for invoke()")
            return
        elif self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.completions = self.ai.chat.completions.create(
                model=self.model,
                response_model=self.pymodel,
                messages=[{"role": "system", "content": self.system}, {"role": "user", "content": self.query}]
            )
            assert isinstance(self.completion, QueryNestedListModel)
            self.completions = self.completion.model_dump_json(indent=2)
            self.completions = json.loads(self.completion)
            self.completions = self.completions["nested_items"]
            return self.completions

    def invoke(self, query: str = None):
        """"
        Creates a simple, base query to OpenAI Chat Completions.
        
        
        Args:
        -   query (str): Query to be sent to OpenAI.
        """
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.completion = self.ai.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": self.query}]
            )
            return self.completion