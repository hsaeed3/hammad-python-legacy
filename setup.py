import setuptools

setuptools.setup(
    name="hammadpy",
    version="1.1.1",
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
'aiohttp==3.9.3',
'aiosignal==1.3.1',
'annotated-types==0.6.0',
'anyio==4.2.0',
'async-timeout==4.0.3',
'attrs==23.2.0',
'blis==0.7.11',
'bottleneck==1.3.6',
'catalogue==2.0.10',
'certifi==2024.2.2',
'charset-normalizer==3.3.2',
'click==8.1.7',
'cloudpathlib==0.16.0',
'colorama==0.4.6',
'confection==0.1.4',
'cymem==2.0.8',
'dataclasses-json==0.6.4',
'distro==1.9.0',
'docstring-parser==0.15',
'exceptiongroup==1.2.0',
'fastapi==0.109.2',
'filelock==3.13.1',
'frozenlist==1.4.1',
'fsspec==2024.2.0',
'greenlet==3.0.3',
'h11==0.14.0',
'httpcore==1.0.3',
'httpx==0.26.0',
'huggingface-hub==0.20.3',
'idna==3.6',
'instructor==0.6.0',
'Jinja2==3.1.3',
'joblib==1.3.2',
'jsonpatch==1.33',
'jsonpointer==2.4',
'langchain==0.1.7',
'langchain-community==0.0.20',
'langchain-core==0.1.23',
'langcodes==3.3.0',
'langsmith==0.0.87',
'markdown-it-py==3.0.0',
'MarkupSafe==2.1.5',
'marshmallow==3.20.2',
'mdurl==0.1.2',
'multidict==6.0.5',
'murmurhash==1.0.10',
'mypy-extensions==1.0.0',
'nltk==3.8.1',
'numpy==1.26.4',
'openai==1.12.0',
'packaging==23.2',
'pandas==2.2.0',
'preshed==3.0.9',
'prompt-toolkit==3.0.43',
'pydantic==2.6.1',
'pydantic_core==2.16.2',
'Pygments==2.17.2',
'python-dateutil==2.8.2',
'pytz==2024.1',
'PyYAML==6.0.1',
'regex==2023.12.25',
'requests==2.31.0',
'rich==13.7.0',
'scikit-learn==1.4.1.post1',
'scipy==1.12.0',
'six==1.16.0',
'smart-open==6.4.0',
'sniffio==1.3.0',
'spacy==3.7.4',
'spacy-legacy==3.0.12',
'spacy-loggers==1.0.5',
'SQLAlchemy==2.0.27',
'srsly==2.4.8',
'starlette==0.36.3',
'tenacity==8.2.3',
'thinc==8.2.3',
'threadpoolctl==3.3.0',
'tqdm==4.66.2',
'typer==0.9.0',
'typing-inspect==0.9.0',
'typing_extensions==4.9.0',
'tzdata==2024.1',
'urllib3==2.2.1',
'uvicorn==0.27.1',
'wasabi==1.1.2',
'wcwidth==0.2.13',
'weasel==0.3.4',
'yarl==1.9.4'
    ]
)