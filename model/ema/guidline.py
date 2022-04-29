"""
download the guidelines from EMS
"""
import os
import time
import chromedriver_autoinstaller
from selenium import webdriver
from tqdm import tqdm


class EMSscraper:
    """
    download the ems's clinical trial guidelines
    """

    def __init__(self, utils):
        self.utils = utils


    def run(self) -> None:
        """
        run the functions
        """
        self.utils.check_dir()
        self.utils.config_selenium()
