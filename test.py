import opml

def main():
    noDuplicates(opml.parse('backup.opml'))

def noDuplicates(opmls):
    urls = [x._root.get('xmlUrl') for x in opmls]
    assert len(urls) == len(set(urls))

if __name__ == '__main__':
    main()
