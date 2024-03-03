
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

####### CORE CORE CORE CORE CORE CORE CORE CORE CORE CORE CORE CORE CORE #######
#== HammadPyCore ==#############################################################

from hammadpy.interactions import TextStyles, Input, Dialog, Status, Timer, Verifier

################################################################################

class HammadPy:
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
