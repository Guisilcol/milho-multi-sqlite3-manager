from setuptools import setup, find_packages

setup(
    name="dataenvmanager",
    version="0.3.0",
    packages=find_packages(),
    author="Guilherme dos Santos Magalhães",
    author_email="silcol455@gmail.com",
    description="Manage your data environments with ease.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Guisilcol/milho-multi-sqlite3-manager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)