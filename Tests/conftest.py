import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture(params=['firefox'], scope='class')
# @pytest.fixture(params=['chrome'], scope='class')
@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        # options.add_argument('--headless')
        web_driver = webdriver.Chrome(service=service, options=options)

    if request.param == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        # options.add_argument('--headless')
        web_driver = webdriver.Firefox(service=service, options=options)

    request.cls.driver = web_driver
    yield
    web_driver.close()
