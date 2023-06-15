from setuptools import setup, find_packages

setup(
    name="multisqlite3manager",
    version="0.1",
    packages=find_packages(),
    author="Guilherme dos Santos Magalhães",
    author_email="silcol455@gmail.com",
    description="SQLite3 Database Multiple File Manager",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="URL do repositório do seu projeto",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)