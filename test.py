from opml import parse
from requests import get

def main():
    urls = [opml._root.get('xmlUrl') for opml in parse('backup.opml')]
    noDuplicates(urls)
    [
        checkUrlExists(url) 
        for url in urls 
        if 'reddit' not in url and 'edri' not in url
    ]

def noDuplicates(urls):
    assert len(urls) == len(set(urls))

def checkUrlExists(url):
    status = get(url).status_code
    print(url)
    assert 200 == status

if __name__ == '__main__':
    main()
