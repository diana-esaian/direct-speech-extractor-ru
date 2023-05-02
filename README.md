# Direct Speech Extractor
> Python package for extracting direct speech from texts in Russian

Returned attributes for the list of extracted quotes:

-   `text_wordcount` - word count of the whole text 
-   `direct_speech_wordcount` - word count of all the extracted quotes 
-   `ratio` - ratio of the extracted quotes to the whole text (_direct_speech_wordcount to text_wordcount_)

## Installation
Install the package using pip:
```sh
pip install direct-speech-extractor-ru
```

## Usage
```python
>>> from direct-speech-extractor-ru import Extractor
>>> text = """Он добр и чувствителен, но вспыльчив. Когда на почте кто-нибудь из посетителей протестует, не соглашается или просто начинает рассуждать, то Михаил Аверьяныч багровеет, трясется всем телом и кричит громовым голосом: «Замолчать!», так что за почтовым отделением давно уже установилась репутация учреждения, в котором страшно бывать. Михаил Аверьяныч уважает и любит Андрея Ефимыча за образованность и благородство души, к прочим же обывателям относится свысока, как к своим подчиненным.
– А вот и я! – говорит он, входя к Андрею Ефимычу. – Здравствуйте, мой дорогой! Небось я уже надоел вам, а?
– Напротив, очень рад, – отвечает ему доктор. – Я всегда рад вам."""
```
In order to extract all the quotes, use _direct_spech()_ method:
```python
>>> extract_direct = Extractor(text)
>>> extracted = extract_direct.direct_speech()
>>> extracted
[' «Замолчать!»',
 '– А вот и я!',
 '– Здравствуйте, мой дорогой! Небось я уже надоел вам, а?',
 '– Напротив, очень рад,',
 '– Я всегда рад вам.']
```
In order to extract information about the word counts and the ratio, use the method _statistics()_:
```python
>>> extract_direct.statistics(extracted)
{'text_wordcount': 97,
 'direct_speech_wordcount': 21,
 'ratio': 0.21649484536082475}
```
