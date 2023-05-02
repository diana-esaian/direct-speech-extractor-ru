# Dialogue Extractor
> Python package for extracting direct speech from Russian texts 

Returned attributes for extracted list of remarks:

-   `text_wordcount` - word count of the whole text 
-   `dialogues_wordcount` - word count of all the extracted dialogues 
-   `ratio` - ratio of dialogues to the whole text (_dialogues_wordcount to text_wordcount_)

## Installation
1. Install the package using pip:
```sh
pip install moscow-toponyms==0.1.0
```
2. Download _ru_core_news_sm_
```sh
pip install https://github.com/explosion/spacy-models/releases/download/ru_core_news_sm-3.1.0/ru_core_news_sm-3.1.0.tar.gz
```

## Quick start
```python
>>> from moscow_toponyms import QuickExtract
>>> text = "Однажды весною, в час небывало жаркого заката, в Москве, на Патриарших прудах, появились два гражданина."
>>> toponyms = QuickExtract(text)
>>> toponyms.extract()
[{'toponym': 'Патриарших прудах',
  'lemmatized_toponym': 'Патриаршие пруды',
  'start_char': 60,
  'stop_char': 77}]
```

## Usage
```python
>>> from moscow_toponyms import ExtractMosToponyms
>>> text = "Однажды весною, в час небывало жаркого заката, в Москве, на Патриарших прудах, появились два гражданина."
>>> extract_toponyms = ExtractMosToponyms(text)
```
Using SpaCy extract toponyms and their position in a text, lemmatize extracted toponyms using PyMorphy2:
```python
>>> spacy_extracted = extract_toponyms.spacy_extract()
>>> print(spacy_extracted)
({51: 'смоленский площадь'}, {0: 'саша панкратов'})
>>> spacy_dict = spacy_extracted[0]
>>> spacy_names = spacy_extracted[1]
```
Using Natasha extract toponyms and their position in a text:
```python
>>> natasha_extractor = extract_toponyms.natasha_extract()
>>> print(natasha_extractor)
({51: ['Смоленской площади', 'Смоленская площадь', 69]}, {0: 'Саша Панкратов'})
>>> natasha_dict = natasha_extractor[0]
>>> natasha_names = natasha_extractor[1]
``` 
Add the extracted names to the existing black list for cleaner output:
```python
>>> black_list = extract_toponyms.merging_blacklists(spacy_names, natasha_names)
```
Filter all extracted toponyms and return only Moscow toponyms in inflected and base forms, their start and end character indices
``` python
>>> final_results = extract_toponyms.inner_merging_filtering(black_list, spacy_dict, natasha_dict)
>>> print(final_results)
[{'toponym': 'Смоленской площади', 'lemmatized_toponym': 'Смоленская площадь', 'start_char': 51, 'stop_char': 69}]
```
