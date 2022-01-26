# Multilingual Online Translator
This program can translate words into multiple languages. Use cases in sentences are provided as well.

Supported Languages: Arabic, German, English, Spanish, French, Hebrew, Japanese, Dutch, Polish, Portuguese, Romanian, Russian, Turkish

## How to use
Run the [file](https://github.com/qilinz/Multilingual-Online-Translator/blob/main/translator.py) with three arguments:
- Language to translate from
- Language to translate to
- Word to translate

Examples:
- `python translator.py english french hello`: translate "hello" from English to French.
- `python translator.py english all hello`: translate "hello" from English to all supported languages.

## Mechanism
Input arguments are parsed using argparse module. The word to translate is then translated by [Reverso Context](https://context.reverso.net/translation). The results are parsed by BeautifulSoup module.

## Examples
``` 
> python translator.py english german hello
German Translations:
hallo

German Example:
We agreedellen wolf is innocent. hello.:
Wir waren einverstanden damit, dass Wolf unschuldig ist. Hallo.
```
Disclaimer: The original project idea is from [JetBrains Academy](https://hyperskill.org/projects/99). All codes were written by myself.