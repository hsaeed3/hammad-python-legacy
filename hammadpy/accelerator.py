import concurrent.futures

"""
hammadpy.accelerator
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the Accelerator and SequentialExecutor classes, which provide
simple functions for parallel and sequential execution of tasks.

Classes:
    Accelerator: Executes tasks in parallel using a thread pool executor.
    SequentialExecutor: Executes tasks sequentially.

Methods:
    ParallelExecutor.run_parallel(method, args_list, max_workers): Executes tasks in parallel.
    SequentialExecutor.run_sequential(method, args_list): Executes tasks sequentially.
"""

class Accelerator:
    """
    A class that provides a simple function for executing tasks in parallel.

    Methods:
        run(method, args_list, max_workers): Executes tasks in parallel using a thread pool executor.
    """

    def __init__(self):
        """
        Initializes the Accelerator object.
        """
        pass

    @staticmethod
    def run(method, *args, max_workers):
        """
        Executes tasks in parallel using a thread pool executor.

        Parameters:
            method: The method to be executed in parallel.
            *args: Variable-length arguments to be passed to the method for each task.
            max_workers: The maximum number of worker threads to be used.

        Returns:
            A list of results from the parallel execution.
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(method, arg) for arg in args]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        return results

class SequentialExecutor:
    """
    A class that provides a simple function for executing tasks sequentially.

    Methods:
        run_sequential(method, args_list): Executes tasks sequentially.
    """

    def __init__(self):
        """
        Initializes the SequentialExecutor object.
        """
        pass

    @staticmethod
    def run_sequential(method, *args):
        """
        Executes tasks sequentially.

        Parameters:
            method: The method to be executed sequentially.
            *args: Variable-length arguments to be passed to the method for each task.

        Returns:
            A list of results from the sequential execution.
        """
        results = []
        for arg in args:
            result = method(arg)
            results.append(result)
        return results