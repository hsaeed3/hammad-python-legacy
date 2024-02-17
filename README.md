# hammad-py
## Hammad's Python Tools - a versatile collection of utilities and LLM integration to streamline your development.

> A curated collection of Python functions and modules crafted to simplify common development tasks and effortlessly > integrate the power of LLMs (Large Language Models). This toolkit enhances efficiency and fosters creative > > > > experimentation across various Python applications. I made it because im lazy.

**Installation**
Install hammad-py directly via pip:

"""
Bash
pip install hammad-py
"""

## Key Features

**Core Utilities**: Cool tools

### Getting Started

## 1. Import the necessary modules:

"""
{
Python
from hammadpy import HammadPyTools
}
"""

## 2. Instantiate the HammadPyTools class:

"""
{
Python
tools = HammadPyTools()
}
"""

## 3. Explore and use the tools:

### Simple Styled Interaction

"""
{
Python
tools.say("Greetings from hammad-py!", "blue")
}
"""

### Query OpenAI for a completion 

"""
{
key = "YOUR_OPENAI_API_KEY" 
result = tools.ai(key).instruct(query="Write a haiku about Python")
print(result)
}
"""

### Create a basic DataFrame

"""
{
tools.frame().create(data={'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
}
"""

### Text Styling:

"""
{
Python
tools.say.green("Success!")
tools.say.emphasis("This is important!")
tools.say.blue_on_yellow("Colorful output!")
}
"""

## Input Handling

Python
{
answer = tools.ask.confirm("Do you want to proceed?")
name = tools.askbox.prompt("Enter your name:", default="World")
}
"""

## LLMs with Pydantic

"""
{
Python
tools.ai(key).chat("Tell me a funny joke.")  # Chat-style interaction
tools.ai(key).instruct(system="Act as a helpful code assistant.",
                          query="Refactor this function to be more concise.")
}
"""

Fork this repository.
Create a new branch for your feature or fix.
Submit a pull request with detailed changes and explanations.
