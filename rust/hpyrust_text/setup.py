from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="hpyrust_text",
    version="0.1.3",
    rust_extensions=[RustExtension("hpyrust_text", binding=Binding.PyO3, path="Cargo.toml")],
    packages=["hpyrust_text"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    zip_safe=False,
    python_requires=">=3.7",
)