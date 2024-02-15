
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==## 
##== @/llms/google/query ==#####################################################
##== Sends Queries to Google Gemini ==##########################################

#==============================================================================#

from ....llms.lib.models import QueryLangchainContentModel, QueryLangchainListModel

import os
import getpass
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

#==============================================================================#

class GoogleKey:
    def __init__(self):
        print("Testing Google API Key...")

    def key(self):
        if os.getenv("GOOGLE_API_KEY") == None:
            print("No Google API Key found in environment variables.")
            self.key = getpass.getpass("Google API Key: ")
            os.environ["GOOGLE_API_KEY"] = self.key
            self.key = os.getenv("GOOGLE_API_KEY")
            return self.key
        else:
            os.environ["GOOGLE_API_KEY"] = self.key
            self.key = os.getenv("GOOGLE_API_KEY")
            return self.key 

#==============================================================================#

class GoogleQuery:
    def __init__(self):
        self.key = GoogleKey()
        self.key = self.key.key()
        self.ai = ChatGoogleGenerativeAI(model="gemini-pro")
        return None
    
    def invoke(self, message: str = None):
        """
        Sends a query to Google Gemini Generative AI.
        
        
        Args:
        -   message (str): Query to be sent to Google Gemini.
        """
        self.completion = self.ai.invoke(message)
        return self.completion