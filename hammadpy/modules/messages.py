from colorama import Fore, Style, Back
from prompt_toolkit.shortcuts import message_dialog
from typing import List
from art import text2art

"""
hammadpy.modules.messages
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the TextStyles class which provides simple text styles for terminal output.
It is capable of printing styled messages and lists to the terminal.

Classes:
    TextStyles: This class provides simple text styles for terminal output.

Methods:
    box(self, message: str, title: str) -> None: Creates a message box with the provided message.
    say(self, message: str, color: str, bg: str, style: str) -> None: Prints a styled message to the terminal.
    list(self, items: list, title: str, color: str, bg: str, style: str) -> None: Prints each item in the list as a separate line.
"""

#==============================================================================#

class TextStyles:
    """
    A class for providing simple text styles for terminal output.

    Attributes
    ----------
    black : Fore
        black text color
    lightblack : Fore
        light black text color
    blue : Fore
        blue text color
    lightblue : Fore
        light blue text color
    cyan : Fore
        cyan text color
    lightcyan : Fore
        light cyan text color
    green : Fore
        green text color
    lightgreen : Fore
        light green text color
    magenta : Fore
        magenta text color
    lightmagenta : Fore
        light magenta text color
    red : Fore
        red text color
    lightred : Fore
        light red text color
    white : Fore
        white text color
    lightwhite : Fore
        light white text color
    yellow : Fore
        yellow text color
    lightyellow : Fore
        light yellow text color
    reset : Style
        reset all text styles and colors
    bg_black : Back
        black background color
    bg_lightblack : Back
        light black background color
    bg_blue : Back
        blue background color
    bg_lightblue : Back
        light blue background color
    bg_cyan : Back
        cyan background color
    bg_lightcyan : Back
        light cyan background color
    bg_green : Back
        green background color
    bg_lightgreen : Back
        light green background color
    bg_magenta : Back
        magenta background color
    bg_lightmagenta : Back
        light magenta background color
    bg_red : Back
        red background color
    bg_lightred : Back
        light red background color
    bg_white : Back
        white background color
    bg_lightwhite : Back
        light white background color
    bg_yellow : Back
        yellow background color
    bg_lightyellow : Back
        light yellow background color
    bg_reset : Back
        reset background color
    bold : Style
        bright/bold text style
    dim : Style
        dim text style

    Methods
    -------
    box(message, title=None)
        Creates a message box with the provided message.
    say(message, color, bg=None, style=None)
        Prints a styled message to the terminal.
    list(items, title=None, color="white", bg=None, style=None)
        Prints each item in the list as a separate line.
    """

    def __init__ (self):
        self.black = Fore.BLACK
        self.lightblack = Fore.LIGHTBLACK_EX
        self.blue = Fore.BLUE
        self.lightblue = Fore.LIGHTBLUE_EX
        self.cyan = Fore.CYAN
        self.lightcyan = Fore.LIGHTCYAN_EX
        self.green = Fore.GREEN
        self.lightgreen = Fore.LIGHTGREEN_EX
        self.magenta = Fore.MAGENTA
        self.lightmagenta = Fore.LIGHTMAGENTA_EX
        self.red = Fore.RED
        self.lightred = Fore.LIGHTRED_EX
        self.white = Fore.WHITE
        self.lightwhite = Fore.LIGHTWHITE_EX
        self.yellow = Fore.YELLOW
        self.lightyellow = Fore.LIGHTYELLOW_EX
        self.reset = Style.RESET_ALL
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
        self.bold = Style.BRIGHT
        self.dim = Style.DIM
        pass

    def box(self, message, title=None):
        """
        Creates a message box with the provided message.

        Args:
            message (str): The message to display in the box.
            title (str, optional): The title of the box.

        Returns:
            None
        """
        if title:
            message_dialog(title=title, text=message).run()
        else:
            message_dialog(title="Message", text=message).run()

    def say(self, message : str, color : str, bg=None, style=None):
        """
        Prints a styled message to the terminal.

        Args:
            message (str): The message to print.
            color (str): Text color (e.g., 'red', 'blue').
            bg (str, optional): Background color.
            style (str, optional): Text style (e.g., 'bold', 'underline').

        Returns:
            None
        """
        if not color:
            color = "white"
        
        color_map = {
            "black": self.black, "lightblack": self.lightblack,
            "blue": self.blue, "lightblue": self.lightblue,
            "cyan": self.cyan, "lightcyan": self.lightcyan,
            "green": self.green, "lightgreen": self.lightgreen,
            "magenta": self.magenta, "lightmagenta": self.lightmagenta,
            "red": self.red, "lightred": self.lightred,
            "white": self.white, "lightwhite": self.lightwhite,
            "yellow": self.yellow, "lightyellow": self.lightyellow
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
            "reset": self.reset,
            "bold": self.bold,
            "dim": self.dim
        }

        color = color_map.get(color, "")
        background_color = bg_map.get(bg, "") if bg else ""
        additional_style = style_map.get(style, "") if style else ""

        print(f"{additional_style}{color}{background_color}{message}{self.reset}{self.bg_reset if bg else ''}")

    def list(self, items: List, title=None, color="white", bg=None, style=None):
        """
        Prints each item in the list as a separate line.

        Args:
            items (list): The list of items to print.
            title (str, optional): The title of the list.
            color (str, optional): Text color (e.g., 'red', 'blue').
            bg (str, optional): Background color.
            style (str, optional): Text style (e.g., 'bold', 'underline').

        Returns:
            None
        """
        if title:
            self.say(title, color, bg, style)
        for item in items:
            self.say(item, color, bg, style)

    def splash(self, message: str = None, art: str = None, color: str = None, bg: str = None, style: str = None):
        """
        Creates an ASCII art styled Splash 'Logo' in the terminal.

        Args:
            message (str): The message to display in the splash.
            art (str): The ASCII art style to use.
            color (str): Text color (e.g., 'red', 'blue').
            style (str): Text style (e.g., 'bold', 'underline').

        Returns:
            None
        """
        if not message:
            message = "hammadpy"
        if not art:
            art = "random"
        if not color:
            color = "white"
        if not bg:
            bg = ""
        if not style:
            style = "bold"

        color_map = {
            "black": self.black, "lightblack": self.lightblack,
            "blue": self.blue, "lightblue": self.lightblue,
            "cyan": self.cyan, "lightcyan": self.lightcyan,
            "green": self.green, "lightgreen": self.lightgreen,
            "magenta": self.magenta, "lightmagenta": self.lightmagenta,
            "red": self.red, "lightred": self.lightred,
            "white": self.white, "lightwhite": self.lightwhite,
            "yellow": self.yellow, "lightyellow": self.lightyellow
        }

        style_map = {
            "reset": self.reset,
            "bold": self.bold,
            "dim": self.dim
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

        color = color_map.get(color, "")
        background_color = bg_map.get(bg, "") if bg else ""
        additional_style = style_map.get(style, "") if style else ""

        if art == "random":
            fonts = ["block", "caligraphy", "doh", "dohc", "doom", "epic", "fender", "graffiti", "isometric1", "isometric2", "isometric3", "isometric4", "letters", "alligator", "dotmatrix", "bubble", "bulbhead", "digital", "ivrit", "lean", "mini", "script", "shadow", "slant", "speed", "starwars", "stop", "thin", "3-d", "3x5", "5lineoblique", "acrobatic", "alligator2", "alligator3", "alphabet", "banner", "banner3-D", "banner3", "banner4", "barbwire", "basic", "bell", "big", "bigchief", "binary", "block", "broadway", "bubble", "caligraphy", "doh", "dohc", "doom", "dotmatrix", "drpepper", "epic", "fender", "graffiti", "isometric1", "isometric2", "isometric3", "isometric4", "letters", "alligator", "dotmatrix", "bubble", "bulbhead", "digital", "ivrit", "lean", "mini", "script", "shadow", "slant", "speed", "starwars", "stop", "thin", "3-d", "3x5", "5lineoblique", "acrobatic", "alligator2", "alligator3", "alphabet", "banner", "banner3-D", "banner3", "banner4", "barbwire", "basic", "bell", "big", "bigchief", "binary", "block", "broadway", "bubble", "caligraphy", "doh", "dohc", "doom", "dotmatrix", "drpepper", "epic", "fender", "graffiti", "isometric1", "isometric2", "isometric3", "isometric4", "letters", "alligator", "dotmatrix", "bubble", "bulbhead", "digital", "ivrit", "lean", "mini", "script", "shadow", "slant", "speed", "starwars", "stop", "thin"]
            import random
            art = random.choice(fonts)
            art = text2art(message, font=art)
            print(f"{additional_style}{color}{background_color}{art}{self.reset}{self.bg_reset if bg else ''}")
        else:
            art = text2art(message, font=art)
            print(f"{additional_style}{color}{background_color}{art}{self.reset}{self.bg_reset if bg else ''}")

#==============================================================================#
        
if __name__ == "__main__":
    styles = TextStyles()
    styles.say("Hello, World!", "blue", "lightyellow", "bold")
    styles.say("Hello, World!", "red", "lightgreen", "dim")
    list = ["Item 1", "Item 2", "Item 3"]
    styles.list(list, "List Title", "white", "lightblue", "bold")
    styles.splash()


