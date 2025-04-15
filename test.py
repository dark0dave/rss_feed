#!/usr/bin/env python

import asyncio
import opml
import requests
import sys


def no_duplicates(urls: list) -> None:
    if len(urls) != len(set(urls)):
        seen = set()
        duplicates = []

        for feed in urls:
            if feed in seen:
                duplicates.append(feed)
            else:
                seen.add(feed)
        sys.exit(f"Duplicates detected {duplicates}")


async def check_url_exists(url: str) -> None:
    try:
        status = requests.get(url).status_code
    except:
        print(f"Fail to get {url}")
        return
    if 200 != status:
        print(f"Fail to find {url}")


async def main() -> None:
    feeds = [
        feed._root.get("xmlUrl")
        for feed in opml.parse("backup.opml")
        if feed._root.get("xmlUrl") is not None
    ]
    no_duplicates(feeds)
    await asyncio.gather(
        *[check_url_exists(feed) for feed in feeds]
    )


if __name__ == "__main__":
    asyncio.run(main())
