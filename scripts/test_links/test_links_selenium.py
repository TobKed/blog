import time
from copy import copy
from typing import Dict, Set, Tuple, Union

from logger import LOGS_DIR, SUFFIX_TIMESTAMP, get_logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from yaspin import yaspin
from yaspin.spinners import Spinners

logger = get_logger(__name__)

SCREENSHOTS_PATH = LOGS_DIR / f"screenshots{SUFFIX_TIMESTAMP}"
SCREENSHOTS_GOOD_PATH = SCREENSHOTS_PATH / "good"
SCREENSHOTS_BAD_PATH = SCREENSHOTS_PATH / "bad"


class SeleniumChecker:
    RETRY_WAIT = 10

    def __init__(
        self,
        invalid_links: Set[Tuple[str, Union[str, None]]],
        links_registry: Dict[str, Tuple[str, str]],
    ):
        self.invalid_links = copy(invalid_links)
        self.selenium_links_registry = copy(links_registry)
        self.total_urls_visited = 0

        SCREENSHOTS_GOOD_PATH.mkdir(parents=True, exist_ok=True)
        SCREENSHOTS_BAD_PATH.mkdir(parents=True, exist_ok=True)

    def remove_url_form_invalid_links(self, url):
        logger.debug(f"remove_url_form_invalid_links({url=})")
        for home, href in {
            (home, href) for home, href in self.invalid_links if href == url
        }:
            self.invalid_links.remove((home, href))

    def check_url(
        self,
        url: str,
        xpath: str,
        assert_text: str,
        driver: ChromiumDriver,
        wait: int = None,
    ) -> bool:
        driver.get(url)
        if wait:
            driver.implicitly_wait(wait)
            time.sleep(wait)
        self.total_urls_visited += 1

        try:
            element = driver.find_element(by=By.XPATH, value=xpath)
        except NoSuchElementException:
            return False

        return assert_text in element.text

    @staticmethod
    def make_screenshot(url: str, is_good: bool, driver: ChromiumDriver) -> None:
        filename = url.replace(":", "").replace("/", "__").replace(".", "_") + ".png"
        filepath = (
            SCREENSHOTS_GOOD_PATH / filename
            if is_good
            else SCREENSHOTS_BAD_PATH / filename
        )
        driver.save_screenshot(str(filepath))

    @yaspin(Spinners.dots, text="Checking website links (selenium).", timer=True)
    def check_urls(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        for url, (xpath, assert_text) in self.selenium_links_registry.items():
            is_good = self.check_url(url, xpath, assert_text, driver=driver)

            if not is_good:
                is_good = self.check_url(
                    url, xpath, assert_text, driver=driver, wait=self.RETRY_WAIT
                )

            self.make_screenshot(url, is_good, driver)
            if is_good:
                logger.debug(f"GOOD: {url}")
                self.remove_url_form_invalid_links(url)

        driver.quit()
