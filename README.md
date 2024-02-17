# hammadpy
## Hammad's Python Tools - a versatile collection of utilities and LLM integration to streamline your development.

> I made this because I'm lazy.

**Installation**
Install hammad-py directly via pip:

```bash

pip install hammadpy

```

## Key Features

**Core Utilities**: Cool tools

### Getting Started

# 1. Import

```python
#
from hammadpy import HammadPy
#
```

# 2. Instantiate the HammadPy class

```python
#
tools = HammadPy()
#
```

# 3. Explore and use the tools

# Styled Interactions

```python
#
tools.say("Greetings from hammad-py!", "blue", "bold", "black")
tools.say("Greetings from hammad-py!",
"color",
"style",
"background color")
#
```

# Query OpenAI for a completion 

```python
#
client = tools.ai(key= " YOUR OPENAI KEY " )
completion = client.chat(model="3", query="hello!")
#
```

### Create a basic DataFrame

```python
#
tools.frame()
#
```

# Text Styling

```python
#
# Colored
tools.say(" YOUR MESSAGE ", " COLOR ")
#
```

# Input Handling

```python
#
answer = tools.ask.confirm("Do you want to proceed?")
name = tools.askbox.prompt("Enter your name:", default="World")
#
```

# LLMs with Pydantic

```python
#
tools.ai(key).chat("Tell me a funny joke.")  # Chat-style interaction
tools.ai(key).instruct(system="Act as a helpful code assistant.",
                          query="Refactor this function to be more concise."
                          pymodel="Content_STR")
#
```

# FastAPI Extension

```python

from hammadpy import API

api = API() 

@api.route("/calculate", methods=["POST"])
async def calculate(request: Request):
    data = await api.get_data(request) 
    result = data["value1"] * data["value2"] 
    return api.send_data({"result": result}) 

api.start() 

```

# Easy GUI with Tkinter

```python

from hammadpy import GuiBuilder

root = tk.Tk()
root.title("My Application")

builder = GuiBuilder(root)

builder.label("Name:", 0, 0) 
builder.entry(row=0, column=1) 

builder.label("Options:", 1, 0) 
size_options = {"Small": "S", "Medium": "M", "Large": "L"}
builder.radio_buttons("", size_options, row=1, column=1) 

builder.button("Submit", command=lambda: print("Submit clicked!"), row=2, column=0) 

root.mainloop() 

```

# Requests

```python

from hammadpy.web import Requests

requests = Requests()

# Sending data in a POST request (using a placeholder API for demonstration)
data = {"field1": "value1", "field2": "value2"}
response = requests.send("POST", "https://jsonplaceholder.typicode.com/posts", json=data) 

# Getting JSON data (using a weather API as an example)
weather_data = requests.get_json("https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY") 

```

## 

Fork this repository.
Create a new branch for your feature or fix.
Submit a pull request with detailed changes and explanations.
