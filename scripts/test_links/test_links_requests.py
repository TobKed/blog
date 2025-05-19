from time import sleep
from typing import Iterable, Set, Tuple, Union
from urllib.request import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from logger import get_logger
from yaspin import yaspin
from yaspin.spinners import Spinners

logger = get_logger(__name__)


class RequestsLinkVerifier:
    RETRY_NR: int = 5

    def __init__(self, url: str, urls_to_ignore: Iterable[str]) -> None:
        self.url = url
        self.urls_to_ignore: Set[str] = set(urls_to_ignore)

        self.internal_urls: Set[str] = set()
        self.external_urls: Set[str] = set()
        self.invalid_links: Set[Tuple[str, Union[str, None]]] = set()
        self.total_urls_visited: int = 0

    @staticmethod
    def is_valid(url: str) -> bool:
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def check_url(self, url: str) -> bool:
        self.total_urls_visited += 1
        try:
            return requests.head(url).ok
        except:
            return False

    def check_yt_url(self, url: str) -> bool:
        r = requests.get(url)
        if not r.ok:
            return False
        return (
            "https://www.youtube.com/img/desktop/unavailable/unavailable_video.png"
            not in r.text
        )

    def check_external_url(self, url: str) -> bool:
        logger.debug(f"test (external): {url}")
        if any(yt in url for yt in ("youtube.com", "youtu.be")):
            return self.check_yt_url(url)
        return self.check_url(url)

    def check_internal_url(self, url: str) -> bool:
        logger.debug(f"test (internal): {url}")
        return self.check_url(url)

    @yaspin(Spinners.dots, text="Checking website links (requests).", timer=True)
    def get_all_website_links(self, url: str = None) -> None:
        """
        Returns all URLs that is found on `url` in which it belongs to the same website
        """
        url = url or self.url
        logger.debug(f"get_all_website_links: {url}")
        domain_name = urlparse(url).netloc
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                self.invalid_links.add((url, href))
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = (
                href
                if (
                    parsed_href.netloc.endswith("youtube.com")
                    or parsed_href.netloc.endswith("youtu.be")
                )
                else parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            )

            if not self.is_valid(href):
                if href not in self.urls_to_ignore:
                    self.invalid_links.add((url, href))
                continue
            if (
                # href in self.internal_urls
                # or href in self.external_urls
                href
                in self.urls_to_ignore
            ):
                continue

            if domain_name not in href and self.url not in href:
                if href not in self.external_urls:
                    self.external_urls.add(href)
                    if not self.check_external_url(href):
                        logger.debug(f"INVALID {(url, href)}")
                        logger.debug("\tretrying")
                        for _ in range(self.RETRY_NR):
                            sleep(1)
                            if self.check_external_url(href):
                                logger.debug("\tseems to work !!!")
                                continue
                        self.invalid_links.add((url, href))
            else:
                if href not in self.internal_urls:
                    self.internal_urls.add(href)
                    if not self.check_internal_url(href):
                        self.invalid_links.add((url, href))
                        logger.debug(f"INVALID {(url, href)}")
                    try:
                        self.get_all_website_links(href)
                    except:
                        self.invalid_links.add((url, href))
                        logger.debug(f"INVALID {(url, href)}")
