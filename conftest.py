from pytest import fixture
from selenium import webdriver
from config import Config
import json


@fixture(scope='session')
def session_browser():
    browser = webdriver.Chrome()
    yield browser

@fixture(scope='function')
def function_browser():
    browser = webdriver.Chrome()
    yield browser

def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store",
        default="dev",
        help="Environment Selection for Tests"
    )
    parser.addoption(
        "--browser", 
        action="store",
        default="chrome",
        help="Browser Selection for Tests"
    )

@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg

data_path = 'test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data

@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

