import os
from typing import Optional
from huggingface_hub import InferenceClient

"""
hammadpy/ml/hf/client.py
Author: Hammad Saeed
Contact: hammad@supportvectors.com
Website: python.hammad.fun

This module contains the HfHub class which extends the Hugging Face InferenceClient
to make it more flexible for usage within different projects.

Classes:
    HfHub: This class extends the Hugging Face InferenceClient to make it more flexible for usage within different projects.

Methods:
    __init__(self, model: Optional[str] = None, token: Optional[str] = None, timeout: Optional[float] = None, headers: Optional[dict] = None, cookies: Optional[dict] = None): Initializes the ExtendedInferenceClient with the given parameters.
"""

#==============================================================================#

class HfHub:
    """
    This class extends the Hugging Face InferenceClient to make it more flexible for usage within different projects.

    Attributes
    ----------
    token : Optional[str]
        Hugging Face token for authentication
    """

    def __init__(self, model: Optional[str] = None, token: Optional[str] = None, 
                 timeout: Optional[float] = None, headers: Optional[dict] = None, 
                 cookies: Optional[dict] = None):
        """
        Initializes the ExtendedInferenceClient with the given parameters. If the token is not provided,
        it attempts to retrieve it from the OS environment variable.

        Parameters
        ----------
            model : Optional[str], optional
                the model name or path to the model
            token : Optional[str], optional
                the Hugging Face token for authentication
            timeout : Optional[float], optional
                the timeout for the request
            headers : Optional[dict], optional
                the headers for the request
            cookies : Optional[dict], optional
                the cookies for the request
        """
        self.token = token if token is not None else os.getenv("HUGGINGFACE_HUB_TOKEN")
        self.client = InferenceClient(model=model, token=self.token, timeout=timeout, 
                                      headers=headers, cookies=cookies)
        pass