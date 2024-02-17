#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==##
##== @/image ==#################################################################
##== OpenAI DALL-E Image Generation ==##########################################

#==============================================================================#

from openai import OpenAI
from PIL import Image
from io import BytesIO
import requests

#==============================================================================#

class DALL_E:
    def __init__(self, key : str):
        self.client = OpenAI(api_key=key)

    def png(self, dir: str = None, prompt : str = None, size : str = ['1024x1024', '1792x1024', '1024x1792'], style : str = ['vivid', 'natural']):
        """
        Create a PNG image from OpenAI DALL-E.

        Args:
        -   dir (str): Directory to save the image. (Required)
        -   prompt (str): Prompt to generate the image. (Required)
        -   size (str): Size of the image. (Optional)
        -   style (str): Style of the image. (Optional)
        """
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=style,
            n=1,
        )

        image_url = response.data[0].url
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.save(f"{dir}/image.png")
        return img
    
    def viewable_png(self, prompt : str = None, size : str = ['1024x1024', '1792x1024', '1024x1792'], style : str = ['vivid', 'natural']):
        """
        Create a viewable PNG image from OpenAI DALL-E without saving it.

        Args:
        -   prompt (str): Prompt to generate the image. (Required)
        -   size (str): Size of the image. (Optional)
        -   style (str): Style of the image. (Optional)
        """
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=style,
            n=1,
        )

        image_url = response.data[0].url
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        return img
    
class Resize:
    def __init__(self):
        pass

    def resize(self, image: str = None, height: int = None, width: int = None):
        """
        Resize an image.

        Args:
        -   image (str): Image to be resized. (Required)
        -   height (int): Desired height of the image. (Required)
        -   width (int): Desired width of the image. (Required)
        """
        img = Image.open(image)
        img = img.resize((height, width))
        return img