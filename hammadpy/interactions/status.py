
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

from hammadpy.interactions.messages import TextStyles

import threading
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
        self.say = TextStyles()
        self.timer = Timer()
        self.message = message
        self.animation = animation
        self.is_running = False  
        self.index = 0  

    def enter(self):
        self.timer.enter()
        self.is_running = True
        self.thread = threading.Thread(target=self.__enter__)
        self.thread.start()
        return self

    def __enter__(self):
        self.start_time = time.time()
        while self.is_running:
            print(f"\r{self.say.text_blue}{self.message} {self.say.text_red}{self.animation[self.index]}", end="", flush=True)
            time.sleep(0.1)
            self.index = (self.index + 1) % len(self.animation)

    def __exit__(self):
        self.exit()

    def exit(self):
        self.is_running = False
        self.thread.join() 
        clear = " " * (len(self.message) + len(self.animation) + 1)
        print(f"\r{clear}{self.say.reset}\r", end="", flush=True)
        self.timer.exit()

#==============================================================================#

class Timer:
    """Measures and prints the execution time of a task."""

    def __init__(self, message: str = "Task"):
        """
        Initializes the TaskTimer object.

        Args:
            message (str, optional): A descriptive message to display (default: "Task").
        """
        self.say = TextStyles()
        self.message = message

    def enter(self):
        """Starts the timer."""
        self.start_time = time.time()
        return self

    def exit(self, *args):
        """Ends the timer and prints the execution time."""
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        message = f"{self.message} completed in {elapsed_time:.2f} seconds."
        self.say.say(message=message, color="green", style="bold")
    
    def end(self):
        """Ends the timer."""
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        message = f"{self.message} completed in {elapsed_time:.2f} seconds."
        self.say.say(message=message, color="green", style="bold")

if __name__ == "__main__":
    
    status = Status()
    timer = Timer()

    with status:
        timer.__enter__()
        time.sleep(3)
        status.exit()
        timer.__exit__()
    