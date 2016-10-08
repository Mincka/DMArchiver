# DMArchiver
A tool to archive **all** the direct messages from your private conversations on Twitter.

## Introduction
Have you ever need to retrieve old information from a chat with your friends on Tweeter? Or maybe you would just like to backup all these cheerful moments and keep them safe.

I have made this tool to retrieve all the tweets from my private conversations and transform them in an _IRC-like_ log for archiving. Emoji are currently kept with their description to prevent encoding issues.

**Output sample:**
```
[2016-09-07 10:35:55] <Michael> [Media-image] https://ton.twitter.com/1.1/ton/data/dm/773125478562429059/773401254876366208/mfeDmXXj.jpg I am so a Dexter fan...
[2016-09-07 10:37:12] <Kathy> He is so sexy. [Flushed face] I love him. [Heavy red heart]
[2016-09-07 10:38:10] <Steve> You guys are ridiculous! [Face with tears of joy]
```

This tool is also able to **download all the uploaded images** in their original resolution and, as a bonus, also retrieve the **GIFs** you used in your conversation as MP4 files (the format used by Tweeter to optimized them and save space).

This tool does not leverage the Twitter API because of its very restrictive limitations in regard of the handling of the Direct Messages. Actually, it is currently possible to retrieve only the latest 200 messages of a private conversation.

Because it is still possible to retrieve the older messages from a Direct Conversation by scrolling up, this script only simulates this behavior to retrieve automatically the messages.

## Prerequisites
You need two things to retrieve your tweets:
- Your `auth-token` value, which is present in your `auth-token` cookie when you are connected on Twitter. This is a 40 characters string like `9e6ecbd088g0baaf2fa9cf2c690aca8ff8027b9f`. Do not share your `auth-token` with anyone, it is like a password to authenticate on the Tweeter site or API.
- The `conversation-id` which is the identifier of the conversation you want to backup. This one is just a little bit harder to find:
	- Open the _Network_ panel in the _Development Tools_ of your favorite browser.
	- Open a the desired conversation on Tweeter and have a look in the requests.
	- Identify a request with the following arguments:
	`https://twitter.com/messages/with/conversation?id=645754097571131337&max_entry_id=78473919348771337`
	- Use the `id` value as your `conversation-id`. This identifier can contain special characters such as '-'.
	
I will try to ease this setup in a future version. :wink:

## Installation
### Using pip
`$ pip install dmarchiver`

## Usage

### Command line tool
```
$ dmarchiver [-h] [-di] [-dg] conversation-id auth-token
$ dmarchiver-script.py [-h] [-di] [-dg] conversation-id auth-token

$ dmarchiver --help
    positional arguments:
      conversation-id       Conversation ID
      auth-token            Authentication token

    optional arguments:
      -h, --help            show this help message and exit
      -di, --download-images
                            Download images
      -dg, --download-gifs  Download GIFs (as MP4)
```

The script output is a `tweets.txt` file with the conversation formatted in an _IRC-like_ style.

If the switches have been set for the download of images and gifs, the files can be respectively found in the `/images` and `/mp4` folders.

### Module import
```python
>>> from dmarchiver import Crawler
>>> crawler = Crawler('CONVERSATION_ID', 'AUTH_TOKEN')
>>> crawler.crawl()
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