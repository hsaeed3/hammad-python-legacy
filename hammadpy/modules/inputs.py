from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import input_dialog, yes_no_dialog, button_dialog, radiolist_dialog, checkboxlist_dialog

"""
hammadpy.modules.inputs
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the Input and Dialog classes which provide a simple interface for user input and dialog boxes.

Classes:
    Input: This class provides a simple interface for user input.
    Dialog: This class provides a simple interface for dialog boxes.
"""

#==============================================================================#

class Input:
    def __init__(self):
        """
        Initializes the Input class.

        Args:
            None

        Methods:
            pause(self, message: str = None): Pauses the program and waits for user input.
            confirm(self, message: str = None): Prompts the user for a yes/no confirmation.
            ask(self, message: str = None): Prompt for user input in the terminal.
            choice(self, message: str = None, choices: list = None): Prompts the user to select from a list of choices.
        """
        pass

    @staticmethod
    def pause(message: str = None):
        if not message:
            message = """
Press Enter to continue...

"""

    @staticmethod
    def confirm(message: str = None):
        """
        Prompts the user for a yes/no confirmation.

        Args:
            message (str): The message to display to the user.

        Returns:
            bool: True if the user confirms, False otherwise.
        """
        if not message:
            message = ""
        if message:
            value = yes_no_dialog(title="Confirmation", text=message).run()
            return value
        else:
            print("'message' is required for prompt_confirmation()")

    @staticmethod
    def ask(message: str = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   message (str): Message to be displayed in the terminal.
        """
        if not message:
            message = """
"""     
        if message:
            message = f"""
{message}

"""
        if message:
            value = prompt(message)
            return value
        else:
            print("'message' is required for prompt_input()")

    @staticmethod
    def choice(message: str = None, choices: list = None):
        """
        Prompts the user to select from a list of choices.

        Args:
            message (str): The message to display to the user.
            choices (list): A list of options for the user to choose from.

        Returns:
            str: The user's selected choice.
        """
        if not message:
            message = """
"""
        if message:
            message = f"""
{message}

"""
        if message and choices:
            value = input_dialog(title=message, text=message, completer=WordCompleter(choices)).run()
            return value
        else:
            print("'message' and 'choices' are required for prompt_choice()")

class Dialog:
    def __init__(self):
        pass

    @staticmethod
    def ask(message: str = None, title: str = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   message (str): Message to be displayed in the terminal.
        """
        if not title:
            title = "Input"
        if message and title:
            value = input_dialog(title=title, text=message).run()
            return value
        else:
            print("'title' and 'message' are required for prompt_input()")

    @staticmethod
    def confirm(message: str = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   message (str): Message to be displayed in the terminal.
        """
        if not message:
            message = ""
        if message:
            value = yes_no_dialog(title="Confirmation", text=message).run()
            return value
        else:
            print("'message' is required for prompt_confirmation()")

    @staticmethod
    def asklist(choices: list = None, message: str = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   choices (list): A list of options for the user to choose from.
        -   message (str): Message to be displayed in the terminal.
        """
        if not message:
            message = ""
        if message and choices:
            value = input_dialog(title=message, text=message, completer=WordCompleter(choices)).run()
            return value
        else:
            print("'message' and 'choices' are required for asklist()")

    @staticmethod
    def radio(choices: str = None, message: str = None):
        """
        Display a dialog with choices offered as a radio list.

        Args:
        -   message (str): Message to be displayed in the terminal.
        -   choices (list): A list of tuples for the radio options.
        """
        if not message:
            message = ""
        if message and choices:
            value = radiolist_dialog(title="RadioList dialog", text=message, values=choices).run()
            return value
        else:
            print("'message' and 'choices' are required for radiolist()")

    @staticmethod
    def checkbox(choices: str = None, message: str = None):
        """
        Display a dialog with choices offered as a checkbox list.

        Args:
        -   message (str): Message to be displayed in the terminal.
        -   choices (list): A list of tuples for the checkbox options.
        """
        if not message:
            message = ""
        if message and choices:
            value = checkboxlist_dialog(title="CheckboxList dialog", text=message, values=choices).run()
            return value
        else:
            print("'message' and 'choices' are required for checkboxlist()")

    @staticmethod
    def button(choices: str = None, message: str = None):
        """
        Display a dialog with choices offered as buttons.

        Args:
        -   message (str): Message to be displayed in the terminal.
        -   choices (list): A list of tuples for the button options.
        """
        if not message:
            message = ""
        if message and choices:
            value = button_dialog(title="Button dialog", text=message, buttons=choices).run()
            return value
        else:
            print("'message' and 'choices' are required for button()")

#==============================================================================#

if __name__ == "__main__":
    list = ["Red", "Green", "Blue"]
    Input.pause()
    Input.ask("What is your name?")
    Input.confirm("Are you sure?")
    Input.choice("Choose a color:", list)
    Dialog.ask("What is your name?")
    Dialog.confirm("Are you sure?")
    Dialog.asklist("Choose a color:", list)
    Dialog.radio("Choose a color:", list)
    Dialog.checkbox("Choose a color:", list)
    Dialog.button("Choose a color:", list)