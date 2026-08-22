from setuptools import setup, find_packages
import re
import os

# Single source of truth: read version from amnlp/version.py
def read_version():
    path = os.path.join(os.path.dirname(__file__), "amnlp", "version.py")
    with open(path, encoding="utf-8") as f:
        match = re.search(r'__version__\s*=\s*["\'](.+?)["\']', f.read())
    if not match:
        raise RuntimeError("Cannot find __version__ in amnlp/version.py")
    return match.group(1)

setup(
    name="amnlp",
    version=read_version(),
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