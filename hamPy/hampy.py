
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==## 
##== @/hampy ==#################################################################

from .core import MessageStyles, Message
from .core import DynamicInputInteractions, StaticInputInteractions
from .core import Validation

from .llms import OpenAIQuery

#==============================================================================#

class HPYError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#==============================================================================#

class HammadPyTools:
    """
    All Tools are accessible from this class.
    """
    def __init__(self):
        self.text = MessageStyles()
        self.ask = StaticInputInteractions()
        self.askbox = DynamicInputInteractions()
    
    def ai(self, key : str): 
        self.key = key
        self.ai = OpenAIQuery(key)
        return self.ai
    
    def error(self, message : str):
        self.error = HPYError(message)
        return self.error
    
    def say(self, message, color, bg=None, style=None):
        Message(message, color, bg, style)

    def text(self):
        return self.text
    
    def ask(self):
        return self.ask
    
    def askbox(self):
        return self.askbox
    
    def validate_type(self, value, type):
        self.validator = Validation()
        return self.validator.type(value, type)
    
    def validate_empty(self, value):
        self.validator = Validation()
        return self.validator.empty(value)
    
#==============================================================================#

if __name__ == "__main__":
    tools = HammadPyTools()
    input = tools.ask.prompt_input("Test", "This is a test message.")
    tools.say.emphasis(input)
    completion = tools.openai.invoke("Hello!")
    tools.say.blue(completion)


