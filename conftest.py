import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=r'D:\PycharmProjects\test\venv\Include\chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.save_screenshot("./sourse/result.png")
    driver.quit()
