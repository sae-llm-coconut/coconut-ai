import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="coconut-ai",
    version="0.1.0",
    author="Coconut AI",
    description="Coconut AI",
    url="https://github.com/sae-llm-coconut/coconut-ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.10, <3.11',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'requests==2.31.0',
        'pillow==10.2.0'
    ],
    extra_requires={
        'dev': [
            'autopep8==2.0.4',
            'editorconfig-checker==2.7.3',
            'mypy==1.8.0',
            'setuptools',
            'types-pillow==10.2.0.20240111',
            'types-requests==2.31.0.20240106'
        ]
    }
)
