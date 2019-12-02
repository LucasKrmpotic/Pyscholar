import os.path
import sys
from configparser import ConfigParser, RawConfigParser

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait

from pyscholar.model.meta import Singleton


def _get_class_name(name):
    parts = name.split('_')
    class_name = ''
    for part in parts:
        class_name += part.capitalize()
    return class_name


class Config(metaclass=Singleton):

    def __init__(self, config_file=None):
        if config_file is None:
            config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
        self.config_file = config_file

        self.parser = ConfigParser()
        self.parser.read(self.config_file)
        self.errors = []

    def get(self, section, attribute):
        try:
            return self.parser[section][attribute]
        except KeyError as e:
            self.errors.append(str(e))
            return False

    def set(self, section, attribute, value):
        self.parser.set(section, attribute, value)
        self._save()

    def get_driver(self):
        # cap = DesiredCapabilities().FIREFOX
        # cap["marionette"] = False

        binary = FirefoxBinary(self._get_firefox_binary_path())
        driver = webdriver.Firefox(firefox_binary=binary)
        driver.wait = WebDriverWait(driver, 5)
        driver.get(self._get_start_url())
        driver.implicitly_wait(5)

        return driver

    def get_storage_module(self):
        return self.parser['storage']['strategy']

    def get_storage_class_name(self):
        return _get_class_name(self.parser['storage']['strategy'])

    def get_storage_full_name(self):
        return self.get_storage_module() + '.' + self.get_storage_class_name()

    def get_storage_file_name(self):
        return self.parser['storage']['file_name']

    def _save(self):
        with open(self.config_file, 'w') as configfile:
            self.parser.write(configfile)

    def add_section(self, section_name):
        raw_parser = RawConfigParser()
        raw_parser.add_section(section_name)
        self._save()

    @property
    def sections(self):
        return self.parser.sections()

    def _get_firefox_binary_path(self):
        return self.parser['driver']['firefox_binary']

    def _get_start_url(self):
        return 'https://scholar.google.com.ar/scholar?hl=es&as_sdt=0%2C5&q=smart+cities&btnG='
