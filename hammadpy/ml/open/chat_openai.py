import os
from openai import OpenAI
import instructor
from hammadpy.interactions.messages import TextStyles
from hammadpy.interactions.status import Status
from typing import List, Optional
from pydantic import BaseModel, Field

"""
hammadpy/ml/open/chat_openai.py
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the ChatOpenAI class which uses OpenAI's Chat Completions
to generate responses to user queries.

Classes:
    ChatOpenAI: This class uses OpenAI's Chat Completions to generate responses to user queries.

Methods:
    chat(self, query: str = None, model : str = 'gpt-3.5-turbo-1106', ): Creates a simple, base query to OpenAI Chat Completions.
    ask(self, query: str = None, model : str = 'gpt-3.5-turbo-1106'): Asks a question, using OpenAI Chat Completions.
    code(self, query: str = None, model: str = 'gpt-3.5-turbo'): Generates 1 finished line of code, depending on the query.
    command(self, query: str = None, model : str = 'gpt-3.5-turbo-1106'): Generates a terminal command, depending on the query.
    vocabulary(self, query: str = None, model : str = 'gpt-3.5-turbo-1106', ): Upscales the vocabulary of a query, using OpenAI Chat Completions.
    plan(self, query: str = None, model : str = 'gpt-3.5-turbo-1106'): Creates a plan, using OpenAI Chat Completions.
"""

#==============================================================================#

class ChatOpenAI:
    """
    A class used to generate responses to user queries using OpenAI's Chat Completions.

    Attributes
    ----------
    llm : OpenAI
        an OpenAI object used to interact with the OpenAI API
    status : Status
        a Status object used to manage the status of the OpenAI API
    text : TextStyles
        a TextStyles object used to format text
    
    Methods
    -------
    chat(query: str = None, model : str = 'gpt-3.5-turbo-1106', ): Creates a simple, base query to OpenAI Chat Completions.
    ask(query: str = None, model : str = 'gpt-3.5-turbo-1106'): Asks a question, using OpenAI Chat Completions.
    code(query: str = None, model: str = 'gpt-3.5-turbo'): Generates 1 finished line of code, depending on the query.
    command(query: str = None, model : str = 'gpt-3.5-turbo-1106'): Generates a terminal command, depending on the query.
    vocabulary(query: str = None, model : str = 'gpt-3.5-turbo-1106', ): Upscales the vocabulary of a query, using OpenAI Chat Completions.
    plan(query: str = None, model : str = 'gpt-3.5-turbo-1106'): Creates a plan, using OpenAI Chat Completions.
    """
    def __init__(self, key: str = None):
        """
        Constructs all the necessary attributes for the ChatOpenAI object.

        Parameters
        ----------
            key : str, optional
                the OpenAI API key to use (default is None)

        Raises
        ------
        ValueError
            If the API key is not available
        """
        self.pymodel = None
        self.status = Status()
        self.text = TextStyles()
        self.text.say("Testing OpenAI API Key...", color="blue", style="bold")
        api_key = key
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")
            try:
                self.llm = OpenAI(api_key=api_key)
                self.text.say("Verified", color="green", style="bold")
            except:
                self.text.say("API Key is not available", color="red", style="bold")
        else:
            self.llm = OpenAI(api_key=api_key)
            self.text.say("Verified", color="green", style="bold")
        pass

    def chat(self, query: str = None, model : str = 'gpt-3.5-turbo-1106', ):
        """"
        Creates a simple, base query to OpenAI Chat Completions.

        Parameters
        ----------
        query : str, optional
            the query to be sent to OpenAI (default is None)

        Returns
        -------
        str
        """
        self.model = model
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.status.enter()
            completion = self.llm.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "system", "content": "You are a helpful assistant. Answer the following Query."}, 
                          {"role": "user", "content": self.query}]
            )
            completion = completion.choices[0].message.content
            self.status.exit()
            self.text.say(f"Query: {self.query}", color="black", style="dim")
            self.text.say(f"Completion: {completion}")
            return completion
        
    def ask(self, query: str = None, model : str = 'gpt-3.5-turbo-1106'):
        """"
        Asks a question, using OpenAI Chat Completions.

        Parameters
        ----------
        query : str, optional
            the query to be sent to OpenAI (default is None)
        model : str, optional
            the model to be used for the completion (default is 'gpt-3.5-turbo-1106')

        Returns
        -------
        str
        """
        self.llm = instructor.patch(self.llm)

        class AnswerModel(BaseModel):
            answer: str = Field(..., title="Answer", description="The answer to the question.")

        self.model = model
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.status.enter()
            completion = self.llm.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are a helpful assistant. Explain the following Query. In a detailed, but incredibly simple way that anyone could understand."}, 
                          {"role": "user", "content": self.query}],
                response_model=AnswerModel
            )
            assert hasattr(completion, 'answer') and completion.answer, "No completion returned."
            completion = completion.answer
            self.status.exit()
            self.text.say(f"Query: {self.query}", color="black", style="dim")
            self.text.say(message=f"Answer: {self.text.text_lightwhite}{completion}", color="green", style="bold")
            return completion
        
    def code(self, query: str = None, model: str = 'gpt-3.5-turbo'):
        """
        Generates 1 finished line of code, depending on the query.

        Parameters
        ----------
        query : str, optional
            the query to be sent to OpenAI (default is None)    

        Returns
        -------
        str
        """
        self.llm = instructor.patch(self.llm)

        class CodeModel(BaseModel):
            code: str = Field(..., title="Code", description="The code generated by the model.")

        self.model = model
        if model == "3":
            self.model = "gpt-3.5-turbo"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.status.enter()
            completion = self.llm.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are a helpful assistant. Write a line of code that does the following."}, 
                          {"role": "user", "content": self.query}],
                response_model=CodeModel
            )
            assert hasattr(completion, 'code') and completion.code, "No completion returned."
            completion = completion.code
            self.status.exit()
            self.text.say(f"Query: {self.query}", color="black", style="dim")
            self.text.say(message=f"Code: {self.text.text_lightwhite}{completion}", color="green", style="bold")
            return completion
        
    def command(self, query: str = None, model : str = 'gpt-3.5-turbo-1106'):
        """
        Generates a terminal command, depending on the query.

        Parameters
        ----------
        query : str, optional
            the query to be sent to OpenAI (default is None)
        model : str, optional
            the model to be used for the completion (default is 'gpt-3.5-turbo-1106')

        Returns
        -------
        str
        """
        self.llm = instructor.patch(self.llm)

        class CommandModel(BaseModel):
            command: str = Field(..., title="Command", description="The command generated by the model.")

        self.model = model
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.status.enter()
            completion = self.llm.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are a helpful assistant. Write a terminal command that does the following."}, 
                          {"role": "user", "content": self.query}],
                response_model=CommandModel
            )
            assert hasattr(completion, 'command') and completion.command, "No completion returned."
            completion = completion.command
            self.status.exit()
            self.text.say(f"Query: {self.query}", color="black", style="dim")
            self.text.say(message=f"Command: {self.text.text_lightwhite}{completion}", color="green", style="bold")
            return completion

    def vocabulary(self, query: str = None, model : str = 'gpt-3.5-turbo-1106', ):
        """"
        Upscales the vocabulary of a query, using OpenAI Chat Completions.

        Parameters
        ----------
        query : str, optional
            the query to be sent to OpenAI (default is None)
        model : str, optional
            the model to be used for the completion (default is 'gpt-3.5-turbo-1106')

        Returns
        -------
        str
        """
        self.llm = instructor.patch(self.llm)

        class VocabModel(BaseModel):
            vocab: str = Field(..., title="Vocabulary", description="The query with an upscaled vocabulary.")

        self.model = model
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.status.enter()
            completion = self.llm.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are a helpful assistant. Rewrite the following Query with a larger vocabulary, and a more professional tone. Do not answer, respond, or provide any information. Just rewrite the query."}, 
                          {"role": "user", "content": self.query}],
                response_model=VocabModel
            )
            completion = completion.vocab
            self.status.exit()
            self.text.say(f"Query: {self.query}", color="black", style="dim")
            self.text.say(message=f"Enriched Query: {self.text.text_lightwhite}{completion}", color="green", style="bold")
            return completion
        
    def plan(self, query: str = None, model : str = 'gpt-3.5-turbo-1106'):
        """"
        Creates a plan, using OpenAI Chat Completions.
        
        Parameters
        ----------
        query : str, optional
            the query to be sent to OpenAI (default is None)

        Returns
        -------
        str
        """
        self.llm = instructor.patch(self.llm)

        class PlanModel(BaseModel):
            tasks: List[str] = Field(..., title="List of Tasks", description="Each item in the list should be prefixed with '1:, 2:, 3: ' to indicate its order.")

        self.model = model
        if model == "3":
            self.model = "gpt-3.5-turbo-1106"
        if model == "4":
            self.model = "gpt-4-turbo-preview"
        self.query = query
        if self.query == None:
            print("Query is required for invoke()")
            return
        else:
            self.status.enter()
            completion = self.llm.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": """
                        You are a helpful assistant. Create a to-do list from the following Query.
                        Only create a list of tasks; that are included in the task the user needs
                        to complete, do not respond with any other information. The objective could
                        be anything, from planning a trip; or writing an essay, all you will do is
                        create a to-do list from the user's query"""}, 
                          {"role": "user", "content": self.query}],
                response_model=PlanModel
            )
            assert hasattr(completion, 'tasks') and completion.tasks, "No completion returned."
            self.status.exit()
            self.text.say(f"Query: {self.query}", color="black", style="dim")
            self.text.say("Tasks:", color="green", style="bold")
            for task in completion.tasks:
                self.text.say(task, color="lightwhite", style="bold")
            return completion