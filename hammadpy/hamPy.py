
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
from .core import Status, Timer
from .core import Frame

from .llms import OpenAIQuery

#==============================================================================#

class HPYError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#==============================================================================#

#==============================================================================#

class HammadPy:
    """
    All Tools are accessible from this class.
    """
    def __init__(self):
        """
        Initializes the HammadPyTools class with required objects.
        """
        self.text = MessageStyles()
        self.ask = StaticInputInteractions()
        self.askbox = DynamicInputInteractions()
    
    def ai(self, key : str): 
        """
        Queries OpenAI Completions.

        Args:
        -   key (str): The API key for OpenAI.
        
        Returns:
        -   OpenAIQuery: An instance of OpenAIQuery.
        """
        self.key = key
        self.ai = OpenAIQuery(key)
        return self.ai
    
    def status(self):
        """
        Returns an instance of the Status class.

        Returns:
        -   Status: An instance of Status.
        """
        self.status = Status()
        return self.status
    
    def timer(self):
        """
        Returns an instance of the Timer class.

        Returns:
        -   Timer: An instance of Timer.
        """
        self.timer = Timer()
        return self.timer
    
    def error(self, message : str):
        """
        Raises a custom error (HPYError) with the provided message.

        Args:
            message (str): The error message to display.

        Returns:
            HPYError: An instance of the HPYError class.
        """
        self.error = HPYError(message)
        return self.error
    
    def frame(self):
        """
        Creates a new pandas DataFrame.

        Returns:
        -   Frame: An instance of Frame.
        """
        self.frame = Frame()
        return self.frame
    
    def say(self, message : str, color : str, bg : str = None, style : str = None):
        """
        Prints a styled message to the terminal using the Message class.

        Args:
            message (str): The message to be printed.
            color (str): The text color.
            bg (str, optional): The background color.
            style (str, optional): Text style (e.g., 'bold', 'underline').
        """
        Message(message, color, bg, style)

    def text(self):
        """
        Returns an instance of the MessageStyles class.

        Returns:
            MessageStyles: An object for creating styled terminal output.
        """
        return self.text
    
    def ask(self):
        """
        Returns the StaticInputInteractions object for static terminal input.

        Returns:
        -   StaticInputInteractions: An instance of StaticInputInteractions.
        """
        return self.ask
    
    def askbox(self):
        """
        Returns the DynamicInputInteractions object for dynamic terminal input.

        Returns:
        -   DynamicInputInteractions: An instance of DynamicInputInteractions.
        """
        return self.askbox
    
    def validate_type(self, value : str, type : str):
        """
        Validates the type of a value.

        Args:
        -   value (str): The value to be validated.
        -   type (str): The expected type of the value.
        
        Returns:
        -   bool: True if the value matches the expected type, False otherwise.
        """
        self.validator = Validation()
        return self.validator.type(value, type)
    
    def validate_empty(self, value : str):
        """
        Validates that a value is not empty.

        Args:
        -   value (str): The value to be validated.
        
        Returns:
        -   bool: True if the value is not empty, False otherwise.
        """
        self.validator = Validation()
        return self.validator.empty(value)
    
#==============================================================================#

if __name__ == "__main__":
    tools = HammadPyTools()
    input = tools.ask.prompt_input("Test", "This is a test message.")
    tools.say.emphasis(input)
    completion = tools.openai.invoke("Hello!")
    tools.say.blue(completion)


