from setuptools import setup

with open("REAME.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="RRB",
    description="A small package for dvc dl pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RenukaRajendra/DVC_DL_OPS",
    author_email="techrrb@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requi1res=[
        "dvc",
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3" ,
    ]
)