
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==## 
##== @/api/fastapi ==###########################################################

#==============================================================================#

import uvicorn
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Body, Request

#==============================================================================#

class API(FastAPI):
    """
    Provides a simple wrapper for FastAPI, facilitating common API operations.
    """

    def route(self, path: str, endpoint, methods: list = ["GET"]):
        """
        Adds a new route to the API.

        Args:
            path (str): The URL path for the route.
            endpoint: The function that will handle requests to the route.
            methods (list, optional): A list of supported HTTP methods. Defaults to ["GET"].
        """
        self.app.add_api_route(path, endpoint, methods=methods)


    def start(self, host: str = "0.0.0.0", port: int = 8000):
        """
        Starts the API server.

        Args:
            host (str, optional): The host address to listen on. Defaults to "0.0.0.0".
            port (int, optional): The port to listen on. Defaults to 8000.
        """
        uvicorn.run(self, host=host, port=port)

    async def get_data(self, request: Request):
        """
        Extracts data sent by the client in various possible formats. 

        Extracts JSON from the request body, form data, or query parameters.

        Args:
            request (Request): The incoming FastAPI request object.

        Returns:
            dict: The parsed data from the client.
        """
        try:
            json_data = await request.json()
            return json_data
        except ValueError:  # Not JSON
            form_data = await request.form()
            query_params = request.query_params
            return {**form_data, **query_params}  # Combine form data and query params

    def send_data(self, data: dict, status_code: int = 200):
        """
        Sends data to the client as a JSON response with a specified status code.

        Args:
            data (dict): The data to send to the client.
            status_code (int, optional):  The HTTP status code. Defaults to 200.

        Returns:
            fastapi.responses.JSONResponse: The JSON response object.
        """
        return JSONResponse(content=data, status_code=status_code)

#==============================================================================#