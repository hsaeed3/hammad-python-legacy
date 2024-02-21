
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

from hammadpy.core.interactions import TextStyles
from hammadpy.core.interactions import Status

from typing import List, Optional
from pydantic import BaseModel, Field

#==============================================================================#

class ChatOpenAI:
    def __init__(self, key: str = None):
        self.pymodel = None
        self.status = Status()
        self.text = TextStyles()
        self.text.say("Testing OpenAI API Key...", color="blue", style="bold")
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("OpenAI API key is required.")
        else:
            self.llm = OpenAI(api_key=api_key)
            self.text.say("Verified", color="green", style="bold")
        pass

    def chat(self, query: str = None, model : str = 'gpt-3.5-turbo-1106', ):
        """"
        Creates a simple, base query to OpenAI Chat Completions.
        
        Args:
        -   query (str): Query to be sent to OpenAI.
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
            self.text.say(f"Completion: {completion}")
            return completion
        
    def ask(self, query: str = None, model : str = 'gpt-3.5-turbo-1106'):
        """"
        Asks a question, using OpenAI Chat Completions.
        
        Args:
        -   query (str): Query to be sent to OpenAI.
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
            self.text.say(message=f"Answer: {self.text.text_black}{completion}", color="green", style="bold")
            return completion
        
    def vocabulary(self, query: str = None, model : str = 'gpt-3.5-turbo-1106', ):
        """"
        Upscales the vocabulary of a query, using OpenAI Chat Completions.
        
        Args:
        -   query (str): Query to be sent to OpenAI.
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
            self.text.say(message=f"Enriched Query: {self.text.text_black}{completion}", color="green", style="bold")
            return completion
        
    def plan(self, query: str = None, model : str = 'gpt-3.5-turbo-1106'):
        """"
        Creates a plan, using OpenAI Chat Completions.
        
        Args:
        -   query (str): Query to be sent to OpenAI.
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
            self.text.say("Tasks:", color="green", style="bold")
            for task in completion.tasks:
                self.text.say(task, color="black", style="bold")
            return completion