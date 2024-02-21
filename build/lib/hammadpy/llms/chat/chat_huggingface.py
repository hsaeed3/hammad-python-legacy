
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== hammadpy ==##################################== Hammad's Python Library ==##
#== @/llms/ask/ask_huggingface ==###############################################

from hammadpy.core.interactions import TextStyles
from hammadpy.core.interactions import Status

import os 
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.messages import SystemMessage

#==============================================================================#

class ChatHuggingFace:
    def __init__(self, repo_id: str = None, token : str = None, model_kwargs: dict = {}):
        """
        Initializes a LangChain wrapper for Hugging Face models.

        Args:
            repo_id (str): The Hugging Face repository ID of the model. 
            model_kwargs (dict, optional): Model configuration or settings.
                                           Defaults to {}.
        """
        self.status = Status()
        self.text = TextStyles()
        self.text.say("Testing HF API Token...", color="blue", style="bold")
        if not repo_id:
            repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
        if not token:
            os.getenv("HUGGINGFACE_API_TOKEN")
            if not token:
                raise ValueError("Hugging Face token is required.")
            self.llm = HuggingFaceHub(repo_id=repo_id, model_kwargs=model_kwargs)
        else:
            huggingfacehub_api_token = token
            self.llm = HuggingFaceHub(repo_id=repo_id, huggingfacehub_api_token=huggingfacehub_api_token, model_kwargs=model_kwargs)
        self.text.say("Verified", color="green", style="bold")
        pass

    def chat(self, prompt: str = None):
        """
        Sends simple query to the Hugging Face model.
        
        Args:
        -   prompt (str): Query to be sent to the model.
        """
        self.status.enter()
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=(
                        "You are a helpful assistant."
                    )
                ),
                HumanMessagePromptTemplate.from_template("{text}"),
            ]
        )
        messages = chat_template.format_messages(text=prompt)
        response = self.llm.invoke(messages)
        self.status.exit()
        self.text.say("Response:", color="green", style="bold")
        self.text.say(response)
        return response

    def vocabulary(self, prompt : str = None):
        """
        Sends a query to the Hugging Face model, to upscale the
        user's prompt's vocabulary.
        
        Args:
        -   prompt (str): Query to be sent to the model.
        """
        self.status.enter()
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=(
                        """You are a helpful assistant. Rewrite the following Query with a larger vocabulary, and a more professional tone.
                        Do not answer, respond, or provide any information. Just rewrite the query."""
                    )
                ),
                HumanMessagePromptTemplate.from_template("{text}"),
            ]
        )
        messages = chat_template.format_messages(text=prompt)
        response = self.llm.invoke(messages)
        self.status.exit()
        self.text.say("Response:", color="green", style="bold")
        self.text.say(response)
        return response
    
    def ask(self, prompt : str = None):
        """
        Sends a query to the Hugging Face model, to explain the
        user's prompt.
        
        Args:
        -   prompt (str): Query to be sent to the model.
        """
        self.status.enter()
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=(
                        """You are a helpful assistant. Explain the following Query. In a detailed, but incredibly simple way that anyone could understand."""
                    )
                ),
                HumanMessagePromptTemplate.from_template("{text}"),
            ]
        )
        messages = chat_template.format_messages(text=prompt)
        response = self.llm.invoke(messages)
        self.status.exit()
        self.text.say("Response:", color="green", style="bold")
        self.text.say(response)
        return response
    
    def plan(self, prompt : str = None):
        """
        Sends a query to the Hugging Face model, to create a
        to-do list from the user's prompt.
        
        Args:
        -   prompt (str): Query to be sent to the model.
        """
        self.status.enter()
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content=str(
                        """You are a helpful assistant. Create a to-do list from the following Query.
                        Only create a list of tasks; that are included in the task the user needs
                        to complete, do not respond with any other information. The objective could
                        be anything, from planning a trip; or writing an essay, all you will do is
                        create a to-do list from the user's query."""
                    )
                ),
                HumanMessagePromptTemplate.from_template("{text}"),
            ]
        )
        messages = chat_template.format_messages(text=prompt)
        response = self.llm.invoke(messages)
        self.status.exit()
        self.text.say("Response:", color="green", style="bold")
        self.text.say(response)
        return response
    
if __name__ == "__main__":
    sample_query = "What is the capital of France?"
    sample_plan = "I need to plan a trip to Paris."
    asker = ChatHuggingFace(token="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")
    response = asker.ask(sample_query)
    plan = asker.plan(sample_plan)
    vocabulary_response = asker.vocabulary(sample_query)
    print(response)