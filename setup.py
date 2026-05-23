from setuptools import setup, find_packages

setup(
    name="amnlp",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "regex",
        "datasets",
        "transformers"
    ],
    author="Eyosyas Yoseph",
    description="Amharic NLP Library",
    python_requires=">=3.8",
)