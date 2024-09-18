from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def search_wikipedia(query):
    search_box = browser.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(query)
    search_box.submit()
    time.sleep(2)

def list_paragraphs():
    paragraphs = browser.find_elements(By.CSS_SELECTOR, "p")
    for i, paragraph in enumerate(paragraphs[:5], 1):
        print(f"{i}. {paragraph.text[:100]}...")

def list_links():
    links = browser.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    return links

def main():
    browser.get("https://ru.wikipedia.org")

    query = input("Введите запрос: ")
    search_wikipedia(query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == "1":
            list_paragraphs()
        elif choice == "2":
            links = list_links()
            for i, link in enumerate(links[:10], 1):  # Ограничимся первыми 10 ссылками для простоты
                print(f"{i}. {link.text} ({link.get_attribute('href')})")

            link_choice = int(input("Введите номер ссылки для перехода: ")) - 1

            if 0 <= link_choice < len(links):
                browser.get(links[link_choice].get_attribute('href'))
                time.sleep(2)
            else:
                print("Некорректный выбор.")
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    browser = webdriver.Chrome()
    try:
        main()
    finally:
        browser.quit()