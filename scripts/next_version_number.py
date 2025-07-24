from datetime import UTC, datetime

from orma import __version__

MAJOR_VERSION = 0


def next_version_number():
    """Returns the next version number based on the current version."""
    _, current_minor, current_patch = __version__.split(".")

    now = datetime.now(UTC)
    year = str(now.year % 100)
    month = str(now.month).zfill(2)

    new_minor = f"{year}{month}"
    new_patch = int(current_patch) + 1
    if current_minor != new_minor:
        new_patch = 0

    next_version = f"{MAJOR_VERSION}.{new_minor}.{new_patch}"

    return next_version


if __name__ == "__main__":
    print(next_version_number())
