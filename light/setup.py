import setuptools

setuptools.setup(
    name="hammadpy_sm",
    version="1.0.0",
    author="Hammad Saeed",
    author_email="hammad@supportvectors.com",
    description="Hammad's Python Library",
    long_description="""
Hammad's Python Tools

Documentation available at: https://github.com/hsaeed3/hammad-python
    """,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.10',
    install_requires=[
        'anyio',
        'attrs',
        'certifi',
        'charset-normalizer',
        'click',
        'colorama',
        'distro',
        'docstring-parser',
        'frozenlist',
        'h11',
        'httpcore',
        'httpx',
        'idna',
        'instructor',
        'markdown-it-py',
        'mdurl',
        'multidict',
        'openai',
        'prompt_toolkit',
        'pydantic',
        'pydantic_core',
        "Pygments",
        'rfc3986',
        'rich',
        'sniffio',
        'tenacity',
        'tqdm',
        'typer',
        'typing_extensions',
        'validus',
        'wcwidth',
        'yarl',
    ]
)