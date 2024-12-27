from setuptools import setup, find_packages

setup(
    name="webp2gif",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Pillow>=10.0.0",
        "webp>=0.1.0",
    ],
    entry_points={
        "console_scripts": [
            "webp2gif=src.cli:main",
        ],
    },
)
