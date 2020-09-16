from opml import parse
from requests import get

def main():
    urls = [opml._root.get('xmlUrl') for opml in parse('backup.opml')]
    noDuplicates(urls)
    [
        checkUrlExists(url) 
        for url in urls
    ]

def noDuplicates(urls):
    assert len(urls) == len(set(urls))

def checkUrlExists(url):
    status = get(url).status_code
    print(f'Found: {url} with status: {status}')
    assert 200 == status

if __name__ == '__main__':
    main()
