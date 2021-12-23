import json
from pathlib import Path
from typing import Set, Tuple, Union

from logger import SUFFIX_TIMESTAMP, get_logger
from test_links_registry import known_invalid_urls, selenium_links_registry
from test_links_requests import RequestsLinkVerifier
from test_links_selenium import SeleniumChecker

logger = get_logger("test_links")

URL = "https://tobked.github.io/blog/"

JSON_OUTPUT = f"invalid_links{SUFFIX_TIMESTAMP}.json"


def dump_dict_to_json(file: str, data: Set) -> None:
    source_dir = Path(__file__).parent.resolve()
    filepath = source_dir / file
    with open(filepath, "w") as fp:
        try:
            json.dump(data, fp, indent=4)
        except TypeError:
            json.dump(list(data), fp, indent=4)


def log_summary(
    logger,
    total_urls_visited=None,
    internal_urls=None,
    external_urls=None,
    invalid_links=None,
) -> None:
    logger.info("-------------------------------------------------")
    if total_urls_visited:
        logger.info(f"{total_urls_visited=}")
    if internal_urls:
        logger.info(f"internal_urls: {len(internal_urls)}")
    if external_urls:
        logger.info(f"external_urls: {len(external_urls)}")
    if invalid_links:
        logger.info(f"invalid_links: {len(invalid_links)}")
    logger.info("")
    if invalid_links:
        logger.info("invalid_links details:")
    for url, href in invalid_links or []:
        logger.info(f"{url}: {href}")
    logger.info("-------------------------------------------------")


if __name__ == "__main__":
    logger.info("-------------------------------------------------")
    logger.info("---------------- START REQUESTS -----------------")
    r_verifier = RequestsLinkVerifier(URL, urls_to_ignore=known_invalid_urls)
    r_verifier.get_all_website_links()

    internal_urls: Set[str] = r_verifier.internal_urls
    external_urls: Set[str] = r_verifier.external_urls
    invalid_links: Set[Tuple[str, Union[str, None]]] = r_verifier.invalid_links
    total_urls_visited: int = r_verifier.total_urls_visited

    log_summary(
        logger=logger,
        total_urls_visited=total_urls_visited,
    )

    logger.info("---------------- START SELENIUM -----------------")
    s_verifier = SeleniumChecker(
        invalid_links=invalid_links, links_registry=selenium_links_registry
    )
    s_verifier.check_urls()
    invalid_links: Set[Tuple[str, Union[str, None]]] = s_verifier.invalid_links
    total_urls_visited: int = s_verifier.total_urls_visited

    log_summary(
        logger=logger,
        total_urls_visited=total_urls_visited,
        internal_urls=internal_urls,
        external_urls=external_urls,
        invalid_links=invalid_links,
    )

    dump_dict_to_json(JSON_OUTPUT, invalid_links)

    logger.info("-------------------------------------------------")
    logger.info("----------------- END SELENIUM ------------------")
