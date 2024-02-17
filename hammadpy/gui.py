
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==##
##== @/extensions/tkinter ==################################################

#==============================================================================#

import tkinter as tk

#==============================================================================#

class GuiBuilder:
    """
    Provides a simplified interface for creating common Tkinter GUI elements.
    """

    def __init__(self, master):
        """
        Initializes the GuiBuilder with a master window or frame.

        Args:
            master (tk.Tk or tk.Frame): The parent container.
        """
        self.master = master

    def label(self, text, row, column, **kwargs):
        """
        Creates a label and places it on a grid.

        Args:
            text (str): The label text.
            row (int): The grid row to place the label.
            column (int): The grid column to place the label.
            **kwargs: Additional options for the label (e.g., font, padx, pady).
        """
        label = tk.Label(self.master, text=text, **kwargs)
        label.grid(row=row, column=column)

    def entry(self, row, column, initial_value="", **kwargs):
        """
        Creates an entry widget and places it on a grid.

        Args:
            initial_value (str, optional): The initial value of the entry field.
            row (int): The grid row to place the entry.
            column (int): The grid column to place the entry.
            **kwargs: Additional options for the entry (e.g., width).

        Returns:
            tk.Entry: The created entry widget.
        """
        entry = tk.Entry(self.master, **kwargs)
        entry.insert(0, initial_value)
        entry.grid(row=row, column=column)
        return entry

    def button(self, text, command, row, column, **kwargs):
        """
        Creates a button and places it on a grid.

        Args:
            text (str): The button text.
            command (function): The function to execute when the button is clicked.
            row (int): The grid row to place the button.
            column (int): The grid column to place the button.
            **kwargs: Additional options for the button.
        """
        button = tk.Button(self.master, text=text, command=command, **kwargs)
        button.grid(row=row, column=column)

    def checkbox(self, text, row, column, variable=None, **kwargs):
        """
        Creates a checkbox and places it on a grid.

        Args:
            text (str):  The label text for the checkbox.
            row (int): The grid row to place the checkbox.
            column (int): The grid column to place the checkbox.
            variable (tk.IntVar, optional):  A variable to associate with the checkbox.
            **kwargs: Additional options for the checkbox.
        """
        if variable is None:
            variable = tk.IntVar()

        checkbox = tk.Checkbutton(self.master, text=text, variable=variable, **kwargs)
        checkbox.grid(row=row, column=column)
        return variable

    def radio_buttons(self, text, options, row, column, initial_value="", **kwargs):
        """
        Creates a group of radio buttons and places them on a grid.

        Args:
            text (str): Label text for the radio button group.
            options (dict):  Dictionary where keys are radio button labels and values are associated values.
            initial_value (str, optional): The initial selected option's value.
            row (int): The grid row to place the label.
            column (int): The grid column to place the label.
            **kwargs: Additional keyword arguments (e.g., command).

        Returns:
            tk.StringVar: A StringVar associated with the selected radio button value.
        """
        variable = tk.StringVar(self.master)
        variable.set(initial_value)

        if text:
            label = tk.Label(self.master, text=text)
            label.grid(row=row, column=column)
            row += 1 

        for (label, value) in options.items():
            radio = tk.Radiobutton(self.master, text=label, value=value, variable=variable, **kwargs)
            radio.grid(row=row, column=column)
            row += 1 

        return variable

    def textarea(self, row, column, initial_text="", **kwargs):
        """
        Creates a multi-line text area widget and places it on a grid.

        Args:
            initial_text (str, optional): The initial text to display.
            row (int): The grid row to place the text area in.
            column (int): The grid column to place the text area in.
            **kwargs: Additional keyword arguments for the text area (e.g., height, width).

        Returns:
            tk.Text: The created Text widget.
        """
        text_area = tk.Text(self.master, **kwargs)
        text_area.insert(tk.END, initial_text)
        text_area.grid(row=row, column=column)
        return text_area
    
    def listbox(self, options, row, column, initial_selection=(), **kwargs):
        """
        Creates a listbox widget and places it on a grid.

        Args: 
            options (list): A list of items for the listbox.
            initial_selection (tuple, optional): Indices of initially selected items.
            row (int): The grid row to place the listbox in.
            column (int): The grid column to place the listbox in.
            **kwargs: Additional keyword arguments (e.g., height, selectmode).

        Returns:
            tk.Listbox: The created Listbox widget.
        """
        listbox = tk.Listbox(self.master, **kwargs)
        for item in options:
            listbox.insert(tk.END, item)
        listbox.grid(row=row, column=column)

        for index in initial_selection:
            listbox.selection_set(index)

        return listbox
    
#==============================================================================#
