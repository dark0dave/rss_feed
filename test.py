#!/usr/bin/python

import asyncio
import opml
import requests


def no_duplicates(urls) -> None:
    assert len(urls) == len(set(urls))


async def check_url_exists(url) -> bool:
    status = requests.get(url).status_code
    print(f"Found: {url} with status: {status}")
    return 200 == status


async def main() -> None:
    feeds = [feed._root.get("xmlUrl") for feed in opml.parse("backup.opml")]
    no_duplicates(feeds)
    [await check_url_exists(feed) for feed in feeds]


if __name__ == "__main__":
    asyncio.run(main())
