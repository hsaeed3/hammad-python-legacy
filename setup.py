import setuptools

setuptools.setup(
    name="hammadpy",
    version="2.6.0",
    author="Hammad Saeed",
    author_email="hammad@supportvectors.com",
    description="Hammad's Accelarated Micro Modules for Application Development (Hammad's Python Library)",
    long_description="""
Hammad's Accelarated Micro Modules for Application Development (Hammad's Python Library)

Documentation available at: https://github.com/hsaeed3/hammad-python
    """,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.9',
    install_requires=[
"art",
"aiohttp",
"aiosignal",
"annotated-types",
"annoy",
"anyio",
"attrs",
"certifi",
"charset-normalizer",
"click",
"colorama",
"dash-table",
"dash-html-components",
"dash-core-components",
"dash",
"Flask",
"Werkzeug",
"distro",
"docstring-parser",
"filelock",
"frozenlist",
"fsspec",
"h11",
"httpcore",
"httpx",
"huggingface-hub",
"hpyrust_text",
"idna",
"instructor",
"itsdangerous",
"Jinja2",
"joblib",
"markdown-it-py",
"MarkupSafe",
"mdurl",
"mpmath",
"multidict",
"nest-asyncio",
"networkx",
"numpy",
"openai",
"packaging",
"pandas",
"pillow",
"plotly",
"prompt-toolkit",
"pydantic",
"pydantic_core",
"Pygments",
"python-dateutil",
"pytz",
"PyYAML",
"regex",
"retrying",
"requests",
"rich",
"safetensors",
"scikit-learn",
"scipy",
"sentence-transformers",
"setuptools",
"six",
"sniffio",
"sympy",
"tenacity",
"threadpoolctl",
"tokenizers",
"torch",
"tqdm",
"transformers",
"typer",
'tinydb',
"typing_extensions",
"tzdata",
"urllib3",
"wcwidth",
"wheel",
"Whoosh",
"yarl"
    ]
)