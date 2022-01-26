import time
import argparse
import requests
from bs4 import BeautifulSoup
import re

languages = ["Arabic", "German", "English", "Spanish", "French",
             "Hebrew", "Japanese", "Dutch", "Polish", "Portuguese",
             "Romanian", "Russian", "Turkish"]
ENDPOINT = "https://context.reverso.net/translation"


def translate_one(file_to_write, from_language, to_language, word_to_translate):
    url = f"{ENDPOINT}/{from_language}-{to_language}/{word_to_translate}"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

    r = requests.get(url, headers=headers)

    if r:
        soup = BeautifulSoup(r.content, "html.parser")

        # find word translations
        word_block = soup.find(id="translations-content")
        words = word_block.select(".translation")
        print(words)

        word_list = [word.text.strip() for word in words]

        # find example sentences
        sentence_block = soup.find(id="examples-content")
        sentences = sentence_block.select(".text")
        sentence_list = [sentence.text.strip() for sentence in sentences]

        # print the result
        # print words
        word_samples = [word for word in word_list if
                        re.match(r"\w+[\s\"']", word) is None]  # no commas, quotes or phrases
        file_to_write.write(f"{to_language.title()} Translations:\n{word_samples[0]}\n")

        # print sentences
        sentence_output = "\n".join(sentence_list[:2])
        file_to_write.write(f"\n{to_language.title()} Examples:\n{sentence_output}\n\n\n")

    elif r.status_code == 404:
        print(f"Sorry, unable to find {word_to_translate}")
        quit()
    else:
        print("Something wrong with your internet connection")
        quit()


def main():
    parser = argparse.ArgumentParser(description="This program translates word to other languages.")
    parser.add_argument("from_language", help="The language to translate from.")
    parser.add_argument("to_language", help="The language to translate to. all means all the supported languages.")
    parser.add_argument("word", help="The word you would like to translate.")

    args = parser.parse_args()
    from_language = args.from_language.lower()
    to_language = args.to_language.lower()
    word = args.word

    if from_language.title() not in languages or (to_language.title() not in languages and to_language != "all"):
        print("Sorry, the program doesn't support korean")
        quit()

    with open(f"{word}.txt", "w") as file:
        if to_language == "all":
            for language in languages:
                if language.lower() != from_language:
                    translate_one(file, from_language, language.lower(), word)
                    time.sleep(0.1)
        else:
            translate_one(file, from_language, to_language, word)

    with open(f"{word}.txt") as file:
        print(file.read())


if __name__ == "__main__":
    main()