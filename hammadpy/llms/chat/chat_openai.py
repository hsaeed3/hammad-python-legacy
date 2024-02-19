
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== hammadpy ==##################################== Hammad's Python Library ==##
#== @/llms/chat/chat_openai ==##################################################

#==============================================================================#

import os
from openai import OpenAI
import instructor

from typing import List, Optional
from pydantic import BaseModel, Field

#==============================================================================#

class ChatOpenAI:
    def __init__(self, key: str = None):
        self.key = key
        if self.key == None:
            os.getenv("OPENAI_API_KEY")
        self.ai = OpenAI(api_key=self.key)
        self.pymodel = None
        pass

    def chat(self, model : str = None, query: str = None):
        """"
        Creates a simple, base query to OpenAI Chat Completions.
        
        Args:
        -   query (str): Query to be sent to OpenAI.
        """
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            completion = self.ai.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "system", "content": "You are a helpful assistant. Answer the following Query."}, 
                          {"role": "user", "content": self.query}]
            )
            completion = completion.choices[0].message.content
            return completion
        
    def ask(self, model : str = None, query: str = None):
        """"
        Asks a question, using OpenAI Chat Completions.
        
        Args:
        -   query (str): Query to be sent to OpenAI.
        """
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            completion = self.ai.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "system", "content": "You are a helpful assistant. Explain the following Query. In a detailed, but incredibly simple way that anyone could understand."}, 
                          {"role": "user", "content": self.query}]
            )
            completion = completion.choices[0].message.content
            return completion
        
    def vocabulary(self, model : str = None, query: str = None):
        """"
        Upscales the vocabulary of a query, using OpenAI Chat Completions.
        
        Args:
        -   query (str): Query to be sent to OpenAI.
        """
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            completion = self.ai.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "system", "content": "You are a helpful assistant. Rewrite the following Query with a larger vocabulary, and a more professional tone. Do not answer, respond, or provide any information. Just rewrite the query."}, 
                          {"role": "user", "content": self.query}]
            )
            completion = completion.choices[0].message.content
            return completion
        
    def plan(self, model : str = None, query: str = None):
        """"
        Creates a plan, using OpenAI Chat Completions.
        
        Args:
        -   query (str): Query to be sent to OpenAI.
        """
        self.llm = instructor.patch(self.llm)

        class PlanModel(BaseModel):
            tasks: List[str] = Field(..., title="List of Tasks")
            subtasks: Optional[List[str]] = Field(None, title="List of Subtasks")

        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            completion = self.ai.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "system", "content": """
                        You are a helpful assistant. Create a to-do list from the following Query.
                        Only create a list of tasks; that are included in the task the user needs
                        to complete, do not respond with any other information. The objective could
                        be anything, from planning a trip; or writing an essay, all you will do is
                        create a to-do list from the user's query"""}, 
                          {"role": "user", "content": self.query}],
                response_model=PlanModel
            )
            assert hasattr(completion, 'list') and completion.list, "No completion returned."
            return completion