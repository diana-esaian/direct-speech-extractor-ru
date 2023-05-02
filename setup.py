from setuptools import setup

def long_desc():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="dialogue-extractor-ru",
    version="0.1.0",
    author="Diana Esaian",
    author_email="diana.esaian@gmail.com",
    description="Direct speech extractor for texts in Russian",
    long_description=long_desc(),
    long_description_content_type="text/markdown",
    packages=['dialogue-extractor-ru'],
    url="https://github.com/diana-esaian/dialogue-extractor-ru",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Natural Language :: Russian",
        "Topic :: Text Processing"
    ],
    python_requires='>=3.6',
    license="MIT",
    install_requires=[
        'pandas'
    ],
    include_package_data=True
)
