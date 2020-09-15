# RSS Feed

## Contains

* My rss in an [opml](https://en.wikipedia.org/wiki/OPML) format: [backup.opml](https://gitlab.com/dark0dave/rss_feed/blob/master/backup.opml)
* Raw format backup.opml from exports [Sparss](https://f-droid.org/packages/net.etuldan.sparss.floss/) (fdroid app)
* Test to prevent duplicates

## Notes

* I suggest you ensure your rss client works over a vpn and tor for maximium privacy.
* PRs welcome :)


## Running

Ensure you have [python3.8](https://www.python.org/downloads/release/python-381/) and [pip](https://pip.pypa.io/en/stable/installing/) installed
 ```bash
 pip install poetry
 poetry install
 poetry run python test.py
 ```
