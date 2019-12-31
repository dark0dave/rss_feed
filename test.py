import asyncio
from opml import parse
from requests import get

async def main():
    urls = [opml._root.get('xmlUrl') for opml in parse('backup.opml')]
    noDuplicates(urls)
    [
        await checkUrlExists(url) 
        for url in urls 
        if 'reddit' not in url and 'edri' not in url
    ]

def noDuplicates(urls):
    assert len(urls) == len(set(urls))

async def checkUrlExists(url):
    status = get(url).status_code
    assert 200 == status

if __name__ == '__main__':
    asyncio.run(main())
