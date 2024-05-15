from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):  # this will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")


# Pytest- HTML report


# # This hook is for adding environment details in the HTML report
# def pytest_configure(config):
#     config._metadata['Project_Name'] = 'nop Commerce'
#     config._metadata['Module_Name'] = 'customers'
#     config._metadata['Tester'] = 'Bhushan'


# This hook is for delete/ modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)
