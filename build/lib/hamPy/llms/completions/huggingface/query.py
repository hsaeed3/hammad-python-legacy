
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==## 
##== @/llms/huggingface/query ==################################################
##== Sends Huggingface Chat Completion Queries ==###############################

#==============================================================================#

from ...lib import QueryLangchainContentModel, QueryLangchainListModel

import os
import getpass
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub

#==============================================================================#

class HuggingfaceKey:
    def __init__(self):
        print("Testing Huggingface Token...")

    def key(self):
        if os.getenv("HUGGINGFACE_API_TOKEN") == None:
            print("No Huggingface API Token found in environment variables.")
            self.key = getpass.getpass("Huggingface API Token: ")
            os.environ["HUGGINGFACE_API_TOKEN"] = self.key
            self.key = os.getenv("HUGGINGFACE_API_TOKEN")
            return self.key
        else:
            os.environ["HUGGINGFACE_API_TOKEN"] = self.key
            self.key = os.getenv("HUGGINGFACE_API_TOKEN")
            return self.key 

#==============================================================================#

class HuggingfaceQuery:
    def __init__(self):
        self.key = HuggingfaceKey()
        self.key = self.key.key()
        return None
    
    def invoke_mixtral(self, message: str = None):
        """
        Sends a query to Huggingface Chat Completions.
        Model : Mixtral 8x7B Instruct
        
        
        Args:
        -   message (str): Query to be sent to Huggingface.
        """
        self.repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
        self.ai = HuggingFaceHub(repo_id=self.repo_id, model_kwargs={"temperature": 0.5, "max_length": 96})
        self.completion = self.ai.invoke(message)
        return self.completion

