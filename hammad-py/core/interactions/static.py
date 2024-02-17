
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==##
##== @/core/interactions/message ==############################################
##== Base styled CLI text, used in all tools. ==###############################

#==============================================================================#

from colorama import Fore, Style, Back
from prompt_toolkit.shortcuts import message_dialog

#==============================================================================#

class MessageStyles:
    """
    Simple text styles for terminal output.

    Args:
    -   message (str): Message to be displayed in the terminal.
    """

    def __init__ (self):
        self.text_black = Fore.BLACK
        self.text_lightblack = Fore.LIGHTBLACK_EX
        self.text_blue = Fore.BLUE
        self.text_lightblue = Fore.LIGHTBLUE_EX
        self.text_cyan = Fore.CYAN
        self.text_lightcyan = Fore.LIGHTCYAN_EX
        self.text_green = Fore.GREEN
        self.text_lightgreen = Fore.LIGHTGREEN_EX
        self.text_magenta = Fore.MAGENTA
        self.text_lightmagenta = Fore.LIGHTMAGENTA_EX
        self.text_red = Fore.RED
        self.text_lightred = Fore.LIGHTRED_EX
        self.text_white = Fore.WHITE
        self.text_lightwhite = Fore.LIGHTWHITE_EX
        self.text_yellow = Fore.YELLOW
        self.text_lightyellow = Fore.LIGHTYELLOW_EX
        self.text_reset = Style.RESET_ALL
        self.bg_black = Back.BLACK
        self.bg_lightblack = Back.LIGHTBLACK_EX
        self.bg_blue = Back.BLUE
        self.bg_lightblue = Back.LIGHTBLUE_EX
        self.bg_cyan = Back.CYAN
        self.bg_lightcyan = Back.LIGHTCYAN_EX
        self.bg_green = Back.GREEN
        self.bg_lightgreen = Back.LIGHTGREEN_EX
        self.bg_magenta = Back.MAGENTA
        self.bg_lightmagenta = Back.LIGHTMAGENTA_EX
        self.bg_red = Back.RED
        self.bg_lightred = Back.LIGHTRED_EX
        self.bg_white = Back.WHITE
        self.bg_lightwhite = Back.LIGHTWHITE_EX
        self.bg_yellow = Back.YELLOW
        self.bg_lightyellow = Back.LIGHTYELLOW_EX
        self.bg_reset = Back.RESET

    def box(self, message, title=None):
        """
        Creates a message box with the provided message.

        Args:
            message (str): The message to display in the box.
            title (str, optional): The title of the box.
        """
        if title:
            message_dialog(title=title, text=message).run()
        else:
            message_dialog(title="Message", text=message).run()

    def say(self, message, color, bg=None, style=None):
        """
        Prints a styled message to the terminal.

        Args:
            message (str): The message to print.
            color (str): Text color (e.g., 'red', 'blue').
            bg (str, optional): Background color.
            style (str, optional): Text style (e.g., 'bold', 'underline').
        """
        color_map = {
            "black": self.text_black, "lightblack": self.text_lightblack,
            "blue": self.text_blue, "lightblue": self.text_lightblue,
            "cyan": self.text_cyan, "lightcyan": self.text_lightcyan,
            "green": self.text_green, "lightgreen": self.text_lightgreen,
            "magenta": self.text_magenta, "lightmagenta": self.text_lightmagenta,
            "red": self.text_red, "lightred": self.text_lightred,
            "white": self.text_white, "lightwhite": self.text_lightwhite,
            "yellow": self.text_yellow, "lightyellow": self.text_lightyellow
        }

        bg_map = {
            "black": self.bg_black, "lightblack": self.bg_lightblack,
            "blue": self.bg_blue, "lightblue": self.bg_lightblue,
            "cyan": self.bg_cyan, "lightcyan": self.bg_lightcyan,
            "green": self.bg_green, "lightgreen": self.bg_lightgreen,
            "magenta": self.bg_magenta, "lightmagenta": self.bg_lightmagenta,
            "red": self.bg_red, "lightred": self.bg_lightred,
            "white": self.bg_white, "lightwhite": self.bg_lightwhite,
            "yellow": self.bg_yellow, "lightyellow": self.bg_lightyellow
        }

        style_map = {
            "reset": self.text_reset,
            "bold": Style.BRIGHT,
            "dim": Style.DIM,
        }

        text_color = color_map.get(color, "")
        background_color = bg_map.get(bg, "") if bg else ""
        additional_style = style_map.get(style, "") if style else ""

        print(f"{additional_style}{text_color}{background_color}{message}{self.text_reset}{self.bg_reset if bg else ''}")


class Message(MessageStyles):
    def __init__(self, message, color, bg=None, style=None):
        super().__init__()
        self.say(message, color, bg, style)