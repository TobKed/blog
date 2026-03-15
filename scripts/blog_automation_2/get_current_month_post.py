import calendar
from datetime import date


def get_filename_for_date(dt: date) -> str:
    # Get last day of the month
    _, last_day = calendar.monthrange(dt.year, dt.month)

    # Get lowercase full month name
    month_name = dt.strftime("%B").lower()

    # Format: content/posts/YYYY_MM_DD_monthname_links.md
    return (
        f"content/posts/{dt.year}_{dt.month:02d}_{last_day:02d}_{month_name}_links.md"
    )


if __name__ == "__main__":
    import sys

    dt = date.today()
    if len(sys.argv) > 1:
        dt = date.fromisoformat(sys.argv[1])
    # IMPORTANT: Do not print newlines or spaces around this string to stdout without stripping
    print(get_filename_for_date(dt))
