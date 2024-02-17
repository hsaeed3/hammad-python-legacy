# hammad-python
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

## 1. Import

```python
#
from hammadpy import HammadPy
#
```

## 2. Instantiate the HammadPy class

```python
#
tools = HammadPy()
#
```

## 3. Explore and use the tools

### Simple Styled Interaction

```python
#
tools.say("Greetings from hammad-py!", "blue")
#
```

### Query OpenAI for a completion 

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

### Text Styling

```python
#
# Colored
tools.say(" YOUR MESSAGE ", " COLOR ")
#
```

## Input Handling

```python
#
answer = tools.ask.confirm("Do you want to proceed?")
name = tools.askbox.prompt("Enter your name:", default="World")
#
```

## LLMs with Pydantic

```python
#
tools.ai(key).chat("Tell me a funny joke.")  # Chat-style interaction
tools.ai(key).instruct(system="Act as a helpful code assistant.",
                          query="Refactor this function to be more concise."
                          pymodel="Content_STR")
#
```

Fork this repository.
Create a new branch for your feature or fix.
Submit a pull request with detailed changes and explanations.
