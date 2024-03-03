import os
from typing import Optional, Union, List, Dict, BinaryIO, Path
from huggingface_hub import InferenceClient

#==============================================================================#

class HfHub:
    """
    This class extends the Hugging Face InferenceClient to make it more flexible for usage within
    different projects. It automatically checks for an environment token if not provided.
    """

    def __init__(self, model: Optional[str] = None, token: Optional[str] = None, 
                 timeout: Optional[float] = None, headers: Optional[dict] = None, 
                 cookies: Optional[dict] = None):
        """
        Initializes the ExtendedInferenceClient with the given parameters. If the token is not provided,
        it attempts to retrieve it from the OS environment variable.

        Args:
            model (Optional[str]): The model ID or URL for inference.
            token (Optional[str]): Hugging Face token for authentication. Defaults to None.
            timeout (Optional[float]): Max seconds to wait for a response. Defaults to None.
            headers (Optional[dict]): Additional headers for requests. Defaults to None.
            cookies (Optional[dict]): Additional cookies for requests. Defaults to None.
        """
        self.token = token if token is not None else os.getenv("HUGGINGFACE_HUB_TOKEN")
        self.client = InferenceClient(model=model, token=self.token, timeout=timeout, 
                                      headers=headers, cookies=cookies)