# DMArchiver
A tool to archive **all** the direct messages from your private conversations on Twitter.

## Introduction
Have you ever need to retrieve old information from a chat with your friends on Twitter? Or maybe you would just like to backup all these cheerful moments and keep them safe.

I have made this tool to retrieve all the tweets from my private conversations and transform them in an _IRC-like_ log for archiving. Emoji are currently kept with their description to prevent encoding issues.

**Output sample:**
```
[2016-09-07 10:35:55] <Michael> [Media-image] https://ton.twitter.com/1.1/ton/data/dm/773125478562429059/773401254876366208/mfeDmXXj.jpg I am so a Dexter fan...
[2016-09-07 10:37:12] <Kathy> He is so sexy. [Flushed face] I love him. [Heavy red heart]
[2016-09-07 10:38:10] <Steve> You guys are ridiculous! [Face with tears of joy]
```

This tool is also able to **download all the uploaded images** in their original resolution and, as a bonus, also retrieve the **GIFs** you used in your conversation as MP4 files (the format used by Twitter to optimized them and save space).

This tool does not leverage the Twitter API because of its very restrictive limitations in regard of the handling of the Direct Messages. Actually, it is currently possible to retrieve only the latest 200 messages of a private conversation.

Because it is still possible to retrieve the older messages from a Direct Conversation by scrolling up, this script only simulates this behavior to retrieve automatically the messages.

## Installation & Quick start
### Ubuntu
Python 3 should be already there.

```
$ pip install dmarchiver
$ dmarchiver
```
### Windows
You can build it yourself with `pyinstaller` or just check out the [project releases](https://github.com/Mincka/DMArchiver/releases) for binary builds.

```
> pip install pyinstaller
> pyinstaller --onefile dmarchiver\cmdline.py -n dmarchiver.exe
> cd dist
> dmarchiver.exe
```

### macOS
You may need to install Python 3.

```
$ brew install python3
$ pip3 install dmarchiver
$ dmarchiver
```

## Upgrade
```
$ pip install dmarchiver --upgrade
```

## Usage

### Command line tool
```
$ dmarchiver [-h] [-id CONVERSATION_ID] [-di] [-dg]

$ dmarchiver --help
	usage: cmdline.py [-h] [-id CONVERSATION_ID] [-di] [-dg]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -id CONVERSATION_ID, --conversation_id CONVERSATION_ID
	                        Conversation ID
	  -di, --download-images
	                        Download images
	  -dg, --download-gifs  Download GIFs (as MP4)
```

### Example
To retrieve only a conversation with images and GIFs:

`$ dmarchiver -id "645754097571131337" -di -dg`

The script output will be the `645754097571131337.txt` file with the conversation formatted in an _IRC-like_ style.

If the switches are set for the download of images and gifs, the files can be respectively found in the `/images` and `/mp4` folders.

### Module import
```python
>>> from dmarchiver.core import Crawler
>>> crawler = Crawler()
>>> crawler.authenticate('username', 'password')
>>> crawler.crawl('conversation_id')
```

## Development setup
```shell
$ git clone https://github.com/Mincka/DMArchiver.git
$ cd dmarchiver
$ virtualenv venv
$ source venv/bin/activate # "venv/Scripts/Activate.bat" on Windows
$ pip install -r requirements.txt
$ python setup.py install
```

## Troubleshooting
You may encounter building issues with the `lxml` library on Windows. The most simple and straightforward fix is to download and install a precompiled binary from [this site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) and install the package locally:

`$ pip install lxml-3.6.4-cp35-cp35m-win_amd64.whl`

## License

Copyright (C) 2016 Julien EHRHART

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.