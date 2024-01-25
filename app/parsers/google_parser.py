
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from app.common.json_logging import logger


class GoogleSearch:
    """
    Обьект для парсинга поисковой системы с использованием Selenium
    """
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--headless')
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def search(self, query: str):
        """
        Эмулирует запрос браузера в гугл и собирает необходимые данные
        :param query: текст запроса в виде строки
        :return: результат сбора данных в виде строки
        """
        try:
            self.driver.get(f"https://www.google.com/search?q={query}&num=10&hl=ru")
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            result = soup.find('div', id='result-stats').text
            logger.info('result-stats %s' % result)
            return result
        except Exception as error:
            logger.info(error)
        finally:
            self.driver.close()
            self.driver.quit()


if __name__ == "__main__":
    Google = GoogleSearch()
    Google.search("погода")
