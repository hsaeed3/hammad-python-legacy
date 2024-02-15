
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==## 
##== @/hampy ==#################################################################

from .core import MessageStyles
from .core import DynamicInputInteractions, StaticInputInteractions
from .core import Validator

from .llms import OpenAIQuery, GoogleQuery, HuggingfaceQuery

#==============================================================================#

def ai(key : str): 
    openai = OpenAIQuery(key=key)
    return openai

#==============================================================================#

class HammadPyTools:
    """
    All Tools are accessible from this class.
    """
    def __init__(self):
        self.say = MessageStyles()
        self.ask = StaticInputInteractions()
        self.askbox = DynamicInputInteractions()

    def say(self):
        return self.say
    
    def ask(self):
        return self.ask
    
    def askbox(self):
        return self.askbox
    
    def validator(self, input : str, val : str):
        self.validator = Validator(input=input, val=val)
        return self.validator
    
    def google(self):
        self.google = GoogleQuery()
        return self.google
    
    def huggingface(self):
        self.huggingface = HuggingfaceQuery()
        return self.huggingface
    
#==============================================================================#

if __name__ == "__main__":
    tools = HammadPyTools()
    input = tools.ask.prompt_input("Test", "This is a test message.")
    tools.say.emphasis(input)
    completion = tools.openai.invoke("Hello!")
    tools.say.blue(completion)


