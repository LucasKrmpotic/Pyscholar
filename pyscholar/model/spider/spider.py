import re
import importlib

from pyscholar.config.config import Config

"""
from pyscholar.config.config import Config
from pyscholar.model.item_factory import ItemFactory
from pyscholar.storage import StorageFactory
"""

# Create options object for the browser
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('no-sandbox')
# Instantiate browser to scrape
# driver = webdriver.Chrome(options=options)

class ScholarSpider:

    def __init__self(self):
        importlib.import_module('pyscholar', 'config')
        self.config = Config()
        self.driver = self.config.get_driver()
        self.storage = StorageFactory.create_storage(self.config.get_storage_full_name())

    def crawl(self):
        count_results = self._get_num_of_results()
        scraped = 0

        while scraped < int(count_results):
            scraped += self.crawl_page()
            self.next_()

        self.storage.save()

    def next_(self):
        btn = self.driver.find_element_by_xpath(self.config.parser['xpath_control']['next'])
        btn.click()

    def crawl_page(self):
        results = self.driver.find_elements_by_xpath(self.config.parser['container_xpath']['item_container'])
        for result in results:
            item = self._parse_item(result)
            self.storage.add(item)
        return len(results)

    def _parse_item(self, container):
        item = ItemFactory.create_item(self.config.parser['item_model']['module_name'])

        title_section = container.find_element_by_xpath(self.config.parser['section_xpaths']['tile_section'])
        file_section = container.find_element_by_xpath(self.config.parser['section_xpaths']['file_section'])
        authors_section = container.find_element_by_xpath(self.config.parser['section_xpaths']['authors_section'])
        abstract_section = container.find_element_by_xpath(self.config.parser['section_xpaths']['abstract_section'])
        footer_section = container.find_element_by_xpath(self.config.parser['section_xpaths']['footer_section'])

        self.parse_title_section(title_section, item)
        self.parse_file_section(file_section, item)
        self.parse_authors_section(authors_section, item)
        self.parse_abstract_section(abstract_section, item)
        self.parse_footer_section(footer_section, item)

        return item

    def parse_title_section(self, container, item):
        item.title = container.find_element_by_css_selector('a').text

    def parse_file_section(self, container, item):
        file_container = container.find_element_by_css_selector('a')
        item.file_type = file_container.find_element_by_css_selector('span')
        item.file_url = file_container.get_attribute('href')
        item.source = self._remove_tags(file_container.text, 'between')

    def parse_authors_section(self, container, item):
        for a in container.find_elements_by_css_selector('a'):
            item.authors.append(a.text)
        item.year = self._get_year(container.text)

    def parse_abstract_section(self, container, item):
        item.abstract = self._remove_tags(container.text)

    def parse_footer_section(self, container, item):
        item.citations = container.find_element_by_xpath('.//a[3]').text
        item.related_articles = container.find_element_by_xpath('.//a[4]').get_attribute('href')

    def _remove_tags(self, str_, mode=None):
        if mode is not None and mode == 'between':
            return re.sub(r"<.*?>*?</.*?>", "", str_)
        return re.sub(r"<.*?></.*?>", "", str_)

    def _get_year(self, str_):
        return re.search(r"(19|20)\d{2}", str_)[0] if re.match(r"(19|20)\d{2}", str_) else None

    def _get_num_of_results(self):
        count_ = self.driver.find_element_by_xpath(self.config.parser['control_xpaths']['count_results']).text
        regex = r"\d+(\.\d+)?"
        return re.search(regex, count_)[0] if re.match(regex, count_) else None


if __name__ == "__main__":
    spider = ScholarSpider()
    spider.crawl();
