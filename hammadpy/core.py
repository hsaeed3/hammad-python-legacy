from hammadpy.modules.messages import TextStyles
from hammadpy.modules.inputs import Input, Dialog
from hammadpy.modules.status import Status, Timer
from hammadpy.modules.verifiers import Verifier

"""
hammadpy.module
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module is the entry point for the HammadPy core modules. They can all be
accessed through the Modules class.

Classes:
-   Modules: The main class for accessing the HammadPy core modules.   

Methods:
-   say: Prints a styled message to the terminal using the Message class.
-   input: CLI input methods.
-   dialog: CLI dialog methods.
-   status: Uses the Status class to display a simple animated loading placeholder.
"""

class Core:
    def __init__(self):
        self.text = TextStyles()
        self.input = Input()
        self.verify = Verifier()
        self.dialog = Dialog()
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
            style (str): The text style. Options are as follows:
                - 'bold'
                - 'dim'
                - 'italic'
                - 'underline'
                - 'blink'
                - 'reverse'
                - 'hidden'
        """
        self.text.say(message, color, style)

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
