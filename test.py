import time
import string
import random
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login():
    login = "OsminogKrevetkin@nasa.gov"
    password = "300888"
    url = "https://adscout.ru"

    browser.get(url)
    # Кликаем по кнопке "войти".
    login_button = wait.until(
        ec.presence_of_element_located((By.CLASS_NAME, "home-header-btn"))
    )
    login_button.click()

    # Вводим регистрационные данные.
    email_area = wait.until(ec.presence_of_element_located((By.ID, "email")))
    password_area = wait.until(
        ec.presence_of_element_located((By.ID, "password"))
    )
    email_area.send_keys(login)
    password_area.send_keys(password)
    # Нажимаем кнопку "войти".
    submit_login_data_button = wait.until(
        ec.presence_of_element_located(
            (By.XPATH, "//*[@id='app']/div/form/div[2]/div/button")
        )
    )
    submit_login_data_button.click()

    return str(datetime.datetime.now()) + "\nLogged in."


def create_project():
    """Создание проекта со случайным названием.
    Функция вовзращает имя созданного проекта."""

    # Генерируем случайное название проекта.
    letters = string.ascii_letters
    digits = string.digits

    project_name = "".join(random.choice(letters + digits) for __ in range(12))

    # Нажимаем на кнопку создания проекта.
    add_project_button = wait.until(
        ec.presence_of_element_located(
            (By.XPATH, "//*[@id='app']/div/main/div/div[3]/div[1]/div[1]")
        )
    )
    add_project_button.click()

    name_project_window = wait.until(
        ec.presence_of_element_located((By.ID, "nameproject"))
    )

    name_project_window.send_keys(f"Test_{project_name}")
    name_project_window.send_keys(Keys.ENTER)

    time.sleep(1)

    for a in browser.find_elements_by_tag_name("a"):
        link_href = a.get_attribute("href")
        if "/project/" in link_href and link_href not in projects_list:
            return link_href


def move_to_project():
    """Перемещаемся в случайный проект."""
    project_url = random.choice(projects_list)
    browser.get(project_url)

    message = str(datetime.datetime.now()) + f"\nMoved to {project_url}"
    return message


def create_subproject(project_url):
    """Создаем подпроект внутри проекта."""
    browser.get(project_url)
    # Генерируем случайное название проекта.
    letters = string.ascii_letters
    digits = string.digits

    subproject_name = "".join(
        random.choice(letters + digits) for __ in range(12)
    )

    # Нажимаем на кнопку создания проекта.
    add_subproject_button = wait.until(
        ec.presence_of_element_located(
            (By.XPATH, "//*[@id='app']/div/main/div/div[3]/div[1]/div[1]")
        )
    )
    add_subproject_button.click()

    name_subproject_window = wait.until(
        ec.presence_of_element_located((By.ID, "namesubproject"))
    )

    name_subproject_window.send_keys(f"Test_{subproject_name}")
    name_subproject_window.send_keys(Keys.ENTER)

    time.sleep(1)

    for a in browser.find_elements_by_tag_name("a"):
        link_href = a.get_attribute("href")
        if "/sub/" in link_href and link_href not in subprojects_list:
            return link_href


def move_to_subproject():
    """Перемещаемся в случайный подпроект."""
    subproject_url = random.choice(subprojects_list)
    browser.get(subproject_url)

    message = str(datetime.datetime.now()) + f"\nMoved to {subproject_url}"
    return message


def start_search(subproject_url, query, location):
    browser.get(subproject_url)
    start_search_button = wait.until(
        ec.presence_of_element_located(
            (
                By.XPATH,
                "//*[@id='app']/div/main/div[2]/div[1]/div/div[1]/div/i",
            )
        )
    )
    start_search_button.click()

    input_location = wait.until(
        ec.presence_of_element_located(
            (By.XPATH, "//*[@id='location-query']/div[1]/div/div/div[2]")
        )
    )
    input_location.click()
    text_area = wait.until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='ajax']"))
    )
    text_area.send_keys(location)
    text_area.send_keys(Keys.ENTER)

    input_query = wait.until(ec.presence_of_element_located((By.ID, "query")))
    input_query.send_keys(query)

    start_button = wait.until(
        ec.presence_of_element_located(
            (By.XPATH, "//*[@id='seach-many']/div/div[2]/div[2]/button")
        )
    )
    start_button.click()
    message = f"Started search {query}/{location}."
    return message


def start_rsy(subproject_url, query):
    subproject_url = subproject_url.replace("search", "rsya")
    browser.get(subproject_url)
    start_search_button = wait.until(
        ec.presence_of_element_located(
            (
                By.XPATH,
                "//*[@id='app']/div/main/div[2]/div[1]/div[1]/div/button/i",
            )
        )
    )
    start_search_button.click()

    input_query = wait.until(ec.presence_of_element_located((By.ID, "query")))
    input_query.send_keys(query)

    start_button = wait.until(
        ec.presence_of_element_located(
            (By.XPATH, "//*[@id='settingsModal']/div/div[2]/div/button")
        )
    )
    start_button.click()
    message = f"Started RSY {query}."
    return message


def start_banner_search(subproject_url, query, location):
    subproject_url = subproject_url.replace("search", "baner")
    browser.get(subproject_url)
    start_search_button = wait.until(
        ec.presence_of_element_located(
            (
                By.XPATH,
                "//*[@id='app']/div/main/div[2]/div[1]/div/div[1]/div/i",
            )
        )
    )
    start_search_button.click()

    input_location = wait.until(
        ec.presence_of_element_located(
            (By.XPATH, "//*[@id='location-query']/div[1]/div/div/div[2]")
        )
    )
    input_location.click()
    text_area = wait.until(
        ec.presence_of_element_located((By.XPATH, "//*[@id='ajax']"))
    )
    text_area.send_keys(location)
    text_area.send_keys(Keys.ENTER)

    input_query = wait.until(ec.presence_of_element_located((By.ID, "query")))
    input_query.send_keys(query)

    start_button = wait.until(
        ec.presence_of_element_located(
            (By.XPATH, "//*[@id='seach-many']/div/div[2]/div[2]/button")
        )
    )
    start_button.click()
    message = f"Started search {query}/{location}."
    return message


options = Options()
options.headless = True
browser = webdriver.Chrome(
    executable_path="./webdriver/chromedriver", options=options
)
wait = WebDriverWait(browser, 10)

queries = [
    "пластиковые окна",
    "ворота",
    "жалюзи",
    "окна",
    "двери",
    "кровля",
    "телевизор",
    "запчасти",
    "стеклотара",
    "евроремонт",
    "кошачий корм",
    "щербет",
    "микроволновка",
    "гамбургер",
    "пицца",
    "реклама",
]
locations = ["москва", "вологда", "калуга", "воркута", "самара"]


if __name__ == "__main__":
    projects_list = []
    subprojects_list = []
    login = login()
    print(login)

    while True:
        for i in range(9):
            projects_list.append(create_project())

        print(move_to_project())

        for i in range(7):
            subprojects_list.append(
                create_subproject(random.choice(projects_list))
            )

        for s in subprojects_list:
            print(
                start_search(
                    s, random.choice(queries), random.choice(locations)
                )
            )
            time.sleep(20)
        time.sleep(25 * 60)

        for s in subprojects_list[1:3]:
            print(start_rsy(s, random.choice(queries)))
            time.sleep(10)
        time.sleep(60 * 60)

        for i in range(30):
            for s in subprojects_list:
                print(
                    start_banner_search(
                        s, random.choice(queries), random.choice(locations)
                    )
                )
                time.sleep(20)

    browser.quit()
