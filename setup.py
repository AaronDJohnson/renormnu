import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="renormnu",
    version="0.0.1",
    author="Aaron Johnson",
    author_email="johnsoad@uwm.edu",
    description="Functions used in computing nu in black hole perturbation theory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AaronDJohnson/renormnu",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'mpmath>=1.1.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)