import os
import sys
from datetime import date

import pytest

# Add parent dir to path so we can import the script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import get_current_month_post


def test_get_filename_for_date():
    # March 15, 2026
    test_date = date(2026, 3, 15)
    result = get_current_month_post.get_filename_for_date(test_date)
    assert result == "content/posts/2026_03_31_march_links.md"

    # February 10, 2026 (leap year check usually for feb, but 2026 is 28 days)
    test_date = date(2026, 2, 10)
    result = get_current_month_post.get_filename_for_date(test_date)
    assert result == "content/posts/2026_02_28_february_links.md"
