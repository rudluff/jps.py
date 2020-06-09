# jps.py
I wanted to grab massive amounts of torrents based on vague queries like "MUSIC. TAGS: 70s,80s (ANY)" and feed them into my torrent client's "watched" folder. I didn't like the existing programs to yank from JPS, and because of the (unfortunately irreparable) lack of API, I implemented this by scraping the JPS search, page by page.
How bad is it? Just take a look at it, man... it has only one thing going for it: brevity. Damn thing's barely longer than the short GPL disclaimer:
![yes-i-program-in-mousepad-fight-me](https://github.com/rudluff/jps.py/blob/master/yes-i-program-in-mousepad-fight-me.png)
# Usage
```python3 -m pip install requests bs4```

```./jps.py 'JPS-SEARCH-URL'```

Open up jps.py and put your own PHPSESSID in. Go to jpopsuki's Search/Advanced Search and make a query that you like. Feed the script that search URL.
It doesn't work on the plain torrents.php page, only searches. It also doesn't work on single-page search results. It ALSO won't work if (for some reason) you want to do ```python3 jps.py 'URL'``` (change sys.argv[1] to sys.argv[2]).

# What it will do
It will grab every single torrent file that appeared in that search. It traverses pages. The torrents end up in the same folder jps.py itself is in.
It's not "smart", and always clobbers (so if you don't have it living in your watched directory like me, make sure to clear torrents between runs). It's not "helpful" either: It has no error handling or meaningful error messages.
It *is* "polite", and waits 2.2 seconds between each request.
The torrent files are named pagenumber-torrentnumberwithinpage.torrent e.g. 1-52.torrent, 3-2.torrent.
Use at your own risk.
