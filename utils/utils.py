"""
scraper's global Utils for beauty of code
"""
import os
import chromedriver_autoinstaller
from selenium import webdriver


class Utils:
    """
    utils of scraper
    """
    def __init__(self, info):
        self.dirs = info.base_info['dirs']
        self.url = info.base_info['url']
        self.selenium_exper_pps = info.base_info['selenium']['prefs']
        self.selenium_ops = info.base_info['selenium']['ops']

    def check_dir(self) -> None:
        """
        check the directories
        """
        for directory in self.dirs:
            if not os.path.exists(directory):
                os.mkdir(directory)

    def config_selenium(self):
        """
        config the selenium options and download folder
        """
        chromedriver_autoinstaller.install(path='Data/chrome_driver')
        options = webdriver.ChromeOptions()
        for option in self.selenium_ops:
            options.add_argument(option)

        return options
