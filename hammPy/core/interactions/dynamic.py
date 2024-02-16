
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==#
##== @/core/interactions/input ==##############################################
##== Styled CLI Inputs ==######################################################

#==============================================================================#

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import input_dialog, yes_no_dialog, button_dialog, radiolist_dialog, checkboxlist_dialog

#==============================================================================#

class StaticInputInteractions:
    def __init__(self):
        pass

    def confirm(self, message: str = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   message (str): Message to be displayed in the terminal.
        """
        if message:
            self.value = yes_no_dialog(title="Confirmation", text=message).run()
            return self.value
        else:
            print("'message' is required for prompt_confirmation()")

    def asklist(self, message: str = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   message (str): Message to be displayed in the terminal.
        """
        if message:
            self.value = prompt(message)
            return self.value
        else:
            print("'message' is required for prompt_input()")

    def choice(self, message: str = None, choices: list = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   message (str): Message to be displayed in the terminal.
        -   choices (list): List of choices to be displayed in the terminal.
        """
        if message and choices:
            self.value = input_dialog(title=message, text=message, completer=WordCompleter(choices)).run()
            return self.value
        else:
            print("'message' and 'choices' are required for prompt_choice()")

class DynamicInputInteractions:
    def __init__(self):
        pass

    def ask(self, message: str = None, title: str = None):
        """
        Prompt for user input in the terminal. Messages are displayed as popups.

        Args:
        -   message (str): Message to be displayed in the terminal.
        """
        if message and title:
            self.value = input_dialog(title=title, text=message).run()
            return self.value
        else:
            print("'title' and 'message' are required for prompt_input()")

    def confirm(self, message: str = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   message (str): Message to be displayed in the terminal.
        """
        if message:
            self.value = yes_no_dialog(title="Confirmation", text=message).run()
            return self.value
        else:
            print("'message' is required for prompt_confirmation()")

    def asklist(self, message: str = None, choices: str = None):
        """
        Prompt for user input in the terminal.

        Args:
        -   message (str): Message to be displayed in the terminal.
        """
        if message and choices:
            self.message = message
            self.completer = WordCompleter(choices)
            self.value = prompt(message, completer=self.completer)
            return self.value
        else:
            print("'message' and 'choices' are required for prompt_list_choice()")

    def radio(self, message: str = None, choices: list = None):
        """
        Display a dialog with choices offered as a radio list.

        Args:
        -   message (str): Message to be displayed in the terminal.
        -   choices (list): A list of tuples for the radio options.
        """
        if message and choices:
            self.value = radiolist_dialog(title="RadioList dialog", text=message, values=choices).run()
            return self.value
        else:
            print("'message' and 'choices' are required for radiolist()")

    def checkbox(self, message: str = None, choices: list = None):
        """
        Display a dialog with choices offered as a checkbox list.

        Args:
        -   message (str): Message to be displayed in the terminal.
        -   choices (list): A list of tuples for the checkbox options.
        """
        if message and choices:
            self.value = checkboxlist_dialog(title="CheckboxList dialog", text=message, values=choices).run()
            return self.value
        else:
            print("'message' and 'choices' are required for checkboxlist()")

    def button(self, message: str = None, choices: list = None):
        """
        Display a dialog with choices offered as buttons.

        Args:
        -   message (str): Message to be displayed in the terminal.
        -   choices (list): A list of tuples for the button options.
        """
        if message and choices:
            self.value = button_dialog(title="Button dialog", text=message, buttons=choices).run()
            return self.value
        else:
            print("'message' and 'choices' are required for button()")

#==============================================================================#
