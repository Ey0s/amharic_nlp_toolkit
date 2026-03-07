from setuptools import setup, find_packages

setup(
    name="amnlp",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "regex",
        "datasets",
        "transformers"
    ],
    author="Your Name",
    description="Amharic NLP Library",
    python_requires=">=3.8",
)