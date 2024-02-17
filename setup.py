import setuptools

setuptools.setup(
    name="hammadpy",
    version="0.1.41.11",
    author="Hammad Saeed",
    author_email="hammad@supportvectors.com",
    description="Hammad's Python Tools",
    long_description="""
Hammad's Python Tools

Simple Python Utility and LLM Tools.
Documentation available at: https://github.com/hsaeed3/hammad-python
    """,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        "aiohttp==3.9.3",
"aiosignal==1.3.1",
"annotated-types==0.6.0",
"anyio==4.2.0",
"async-timeout==4.0.3",
"attrs==23.2.0",
"build==1.0.3",
"certifi==2024.2.2",
"charset-normalizer==3.3.2",
"click==8.1.7",
"colorama==0.4.6",
"distro==1.9.0",
"docstring-parser==0.15",
"docutils==0.20.1",
"exceptiongroup==1.2.0",
"fastapi==0.109.2",
"frozenlist==1.4.1",
"h11==0.14.0",
"httpcore==1.0.3",
"httpx==0.26.0",
"idna==3.6",
"importlib-metadata==7.0.1",
"instructor==0.5.2",
"jaraco.classes==3.3.1",
"keyring==24.3.0",
"markdown-it-py==3.0.0",
"mdurl==0.1.2",
"more-itertools==10.2.0",
"multidict==6.0.5",
"nh3==0.2.15",
"numpy==1.26.4",
"openai==1.12.0",
"packaging==23.2",
"pandas==2.2.0",
"pillow==10.2.0",
"pkginfo==1.9.6",
"prompt-toolkit==3.0.43",
"pydantic==2.6.1",
"pydantic_core==2.16.2",
"Pygments==2.17.2",
"pyproject_hooks==1.0.0",
"python-dateutil==2.8.2",
"pytz==2024.1",
"readme-renderer==42.0",
"requests==2.31.0",
"requests-toolbelt==1.0.0",
"rfc3986==2.0.0",
"rich==13.7.0",
"six==1.16.0",
"sniffio==1.3.0",
"starlette==0.36.3",
"tenacity==8.2.3",
"tomli==2.0.1",
"tqdm==4.66.2",
"twine==5.0.0",
"typer==0.9.0",
"typing_extensions==4.9.0",
"tzdata==2024.1",
"urllib3==2.2.0",
"uvicorn==0.27.1",
"wcwidth==0.2.13",
"yarl==1.9.4",
"zipp==3.17.0",
],
)