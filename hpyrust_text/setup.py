from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="hpyrust_text",
    version="0.1.1",
    rust_extensions=[RustExtension("hpyrust_text.hpyrust_text", binding=Binding.PyO3)],
    packages=["hpyrust_text"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    zip_safe=False,
)