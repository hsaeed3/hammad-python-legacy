
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HammadPy ==###################################== Hammad's Python Tools ==## 
##== @/hampy ==#################################################################

from .core import MessageStyles
from .core import DynamicInputInteractions, StaticInputInteractions
from .core import Validation
from .core import Status, Timer
from .core import Frame

from .llms import OpenAIQuery

#=============================================================================#

class HPYError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#=============================================================================#

class HammadPy:
    """
    Base Python Tools
    """
    def __init__(self):
        self.text = MessageStyles()
        self.ask = StaticInputInteractions()
        self.verify = Validation()
        self.dialog = DynamicInputInteractions()
        self.timer = Timer()
    
    def say(self, message : str, color : str = None, style : str = None):
        """
        Prints a styled message to the terminal using the Message class.

        Args:
            message (str): The message to be printed.
            color (str): The text color. Options are as follows:
                - 'black'
                - 'lightblack'
                - 'blue'
                - 'lightblue'
                - 'cyan'
                - 'lightcyan'
                - 'green'
                - 'lightgreen'
                - 'magenta'
                - 'lightmagenta'
                - 'red'
                - 'lightred'
                - 'white'
                - 'lightwhite'
                - 'yellow'
                - 'lightyellow'
            
            style (str, optional): Text style. Options are as follows:
                - 'reset'
                - 'bold'
                - 'dim'
        """
        self.text.say(message, color, style=style)
    
    def status(self):
        """
        Returns an instance of the Status class.

        The Status class displays a simple animated loading placeholder. It includes the following methods:
        - __enter__: Starts the loading animation.
        - __exit__: Stops the loading animation, clears the line, and displays execution time.

        Returns:
        -   Status: An instance of Status.
        """
        return Status()
    
#=============================================================================#

class LLM(OpenAIQuery):
    """
    This class represents Language Learning Models.

    Attributes:
        key (str): The API key for OpenAI.
        ai (OpenAIQuery): An instance of OpenAIQuery initialized with the provided API key.

    Methods:
        ai(): Returns the OpenAIQuery instance.
    """
    def __init__(self, key : str):
        return super().__init__(key)

#=============================================================================#

class Data:
    """
    Data Manipulation Tools
    """
    def __init__(self):
        pass
    
    def frame(self):
        """
        Creates a new pandas DataFrame.

        Returns:
        -   Frame: An instance of Frame.
        """
        self.frame = Frame()
        return self.frame
    
#=============================================================================#

if __name__ == "__main__":
    tools = HammadPy()



