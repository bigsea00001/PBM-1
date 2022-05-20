import os
from typing import List, Dict


class Pre_set:
    def __init__(self, info):
        self.info = info

    def _dir_check(self) -> None:
        directories = self.info.base_info['dirs']

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)

    def _selenium_options_config(self):
        from selenium import webdriver

        pre_options = self.info.selenium_info['options']
        pre_experi_options = self.info.selenium_info['prefs']

        options: webdriver.ChromeOption = webdriver.ChromeOptions()
        for pre_option in pre_options:
            options.add_argument(pre_option)

        options.add_experimental_option('prefs', pre_experi_options)

        return options
