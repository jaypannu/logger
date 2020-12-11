import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logger", 
    version="0.0.1",
    author="JayP",
    author_email="jp.pannu@gmail.com",
    description="A small logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaypannu/logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)