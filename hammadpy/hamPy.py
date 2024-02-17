
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HammadPy ==###################################== Hammad's Python Tools ==## 
##== @/hampy ==#################################################################

from .core import MessageStyles, Message
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

    def text(self):
        """
        Returns an instance of the MessageStyles class.

        Returns:
        -   MessageStyles: An object for creating styled terminal output.
        """
        return self.text
    
    def say(self, message : str, color : str, bg : str = None, style : str = None):
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
            
            bg (str, optional): The background color. Options are as follows:
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
        Message(message, color, bg, style)

    def ask(self):
        """
        Returns the StaticInputInteractions object for static terminal input.

        The StaticInputInteractions object includes the following methods:
        - pause: Pauses the program until the user presses Enter.
        - confirm: Prompts the user for a yes/no confirmation.
        - ask: Prompt for user input in the terminal.
        - choice: Prompts the user to select from a list of choices.

        Returns:
        -   StaticInputInteractions: An instance of StaticInputInteractions.
        """
        return self.ask
    
    def dialog(self):
        """
        Returns the DynamicInputInteractions object for dynamic terminal input.

        The DynamicInputInteractions object includes the following methods:
        - ask: Prompt for user input in the terminal.
        - confirm: Prompt for user confirmation in the terminal.
        - asklist: Prompt for user input from a list of choices in the terminal.
        - radio: Display a dialog with choices offered as a radio list.
        - checkbox: Display a dialog with choices offered as a checkbox list.
        - button: Display a dialog with choices offered as buttons.

        Returns:
        -   DynamicInputInteractions: An instance of DynamicInputInteractions.
        """
        return self.dialog
    
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
    
    def timer(self):
        """
        Returns an instance of the Timer class.

        The Timer class measures and prints the execution time of a task. It includes the following methods:
        - __enter__: Starts the timer.
        - __exit__: Ends the timer and prints the execution time.

        Returns:
        -   Timer: An instance of Timer.
        """
        return self.timer

#=============================================================================#

class LLM:
    """
    This class represents Language Learning Models.

    Attributes:
        key (str): The API key for OpenAI.
        ai (OpenAIQuery): An instance of OpenAIQuery initialized with the provided API key.

    Methods:
        ai(): Returns the OpenAIQuery instance.
    """
    def __init__(self, key : str):
        if not key:
            raise HPYError("OpenAI API Key is required.")
        self.key = key
        self.ai = OpenAIQuery(key)
    
    def ai(self):
        """
        Queries OpenAI Completions.

        Returns:
        -   OpenAIQuery: An instance of OpenAIQuery.
        """
        return self.ai

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



