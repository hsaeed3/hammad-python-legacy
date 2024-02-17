
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

import itertools
import time

#==============================================================================#

class Status:
    """Displays a simple animated loading placeholder."""

    def __init__(self, message: str = "Loading...", animation: str = "|/-\\"):
        """
        Initializes the loading placeholder.

        Args:
            message (str, optional): The message to display alongside the animation.
            animation (str, optional):  A sequence of characters for the animation.
        """
        self.message = message
        self.animation = itertools.cycle(animation)

    def __enter__(self):
        """Starts the loading animation."""
        self.is_running = True
        self.start_time = time.time() 
        while self.is_running:
            print(f"\r{self.message} {next(self.animation)}", end="", flush=True)
            time.sleep(0.1)
        return self

    def __exit__(self, *args):
        """Stops the loading animation, clears the line, and displays execution time."""
        self.is_running = False
        print("\r", end='')  # Clear the line
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"{self.message} completed in {elapsed_time:.2f} seconds.") 

#==============================================================================#

class Timer:
    """Measures and prints the execution time of a task."""

    def __init__(self, message: str = "Task"):
        """
        Initializes the TaskTimer object.

        Args:
            message (str, optional): A descriptive message to display (default: "Task").
        """
        self.message = message

    def __enter__(self):
        """Starts the timer."""
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        """Ends the timer and prints the execution time."""
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"{self.message} completed in {elapsed_time:.2f} seconds.")

