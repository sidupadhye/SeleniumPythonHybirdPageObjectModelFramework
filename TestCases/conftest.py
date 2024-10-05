import pytest
from selenium import webdriver

@pytest.fixture()
def setup_and_teardown(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver=webdriver.Edge()
        print("Launching IE Browser")
    return driver

def pytest_addoption(parser):   #this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")

'''##### PYtest HTML Report #######

#It is a hook adding enviroment to html Report

def pytest_configure(config):
    config.metadata['Project Name']='ncommerceApp'
    config.metadata['Module Name']='Customers'
    config.metadata['Tester']='JP Boss'

# it is hook for delete/modifying Enviroment info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
'''