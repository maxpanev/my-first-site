import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово на русский
        russian_word = translator.translate(english_words, src='en', dest='ru').text
        russian_definition = translator.translate(word_definition, src='en', dest='ru').text

        # Добавим перевод русских слов в словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition,
            "russian_word": russian_word,
            "russian_definition": russian_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()

        # Переводим слово на русский
        russian_word = word_dict.get("russian_word")
        russian_definition = word_dict.get("russian_definition")

        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ")
        if user.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break
            

word_game()