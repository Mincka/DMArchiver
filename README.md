[![GitHub release](https://img.shields.io/github/release/Mincka/DMArchiver.svg)](https://github.com/Mincka/DMArchiver/releases) [![PyPI](https://img.shields.io/pypi/v/DMArchiver.svg)](https://pypi.python.org/pypi/dmarchiver) [![Github All Releases](https://img.shields.io/github/downloads/Mincka/DMArchiver/total.svg)](https://github.com/Mincka/DMArchiver/releases) 


# DMArchiver
A tool to archive **all** the direct messages from your private conversations on Twitter.

## Introduction
Have you ever need to retrieve old information from a chat with your friends on Twitter? Or maybe you would just like to backup all these cheerful moments and keep them safe.

I have made this tool to retrieve all the tweets from my private conversations and transform them in an _IRC-like_ log for archiving. 

**Output sample:**
```
[2016-09-07 10:35:55] <Michael> [Media-image] https://ton.twitter.com/1.1/ton/data/dm/773125478562429059/773401254876366208/mfeDmXXj.jpg I am so a Dexter fan...
[2016-09-07 10:37:12] <Kathy> He is so sexy. [Flushed face] I love him. [Heavy red heart]
[2016-09-07 10:38:10] <Steve> You guys are ridiculous! [Face with tears of joy]
```

Emoji are currently kept with their description to prevent encoding issues.

This tool is also able to **download all the uploaded images** in their original resolution and, as a bonus, also retrieve the **GIFs** you used in your conversations as MP4 files (the format used by Twitter to optimize them and save space).

You may have found suggestions to use the Twitter's archive feature to do the same but Direct Messages are not included in the generated archive.

The script does not leverage the Twitter API because of its very restrictive limitations in regard of the handling of the Direct Messages. Actually, it is currently possible to retrieve only the latest 200 messages of a private conversation.

Because it is still possible to retrieve older messages from a Conversation by scrolling up, this script only simulates this behavior to automatically get the messages.

**Disclaimer:**
Using this tool will only behave like you using the Twitter web site with your browser, so there is nothing illegal to use it to retrieve your own data. However, depending on your conversations' length, it may trigger a lot of requests to the site that could be suspicious for Twitter. No one has reported issues upon now but use it at your discretion.

## Installation & Quick start

### Windows

Download a Windows build from the [project releases](https://github.com/Mincka/DMArchiver/releases).

Then run the tool in a Command Prompt.
```
> C:\Temp\DMArchiver.exe
```

### Mac OS X / macOS

Download a macOS build from the [project releases](https://github.com/Mincka/DMArchiver/releases).

Then run Terminal and execute the following commands:
```
$ cd Downloads
$ ./dmarchiver
```

Note: If you run the tool by clicking on it, the result files will be available in your `/users/username`folder.

### Ubuntu

```
$ pip3 install dmarchiver
$ dmarchiver
```

### Installation & upgrade with pip (any platform)

```
$ pip3 install dmarchiver
$ dmarchiver
$ pip3 install dmarchiver --upgrade
```

## Advanced usage

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
      -r, --raw-output      Write the raw HTML to a file
```

### Examples

#### Archive all conversations with images:
`$ dmarchiver -di`

The script output will be the `645754097571131337.txt` file with the conversation formatted in an _IRC-like_ style.

The images and GIFs files can be respectively found in the `645754097571131337/images` and `645754097571131337/mp4` folders.

#### Archive a specific conversation:
To retrieve only one conversation with the ID `645754097571131337`:

`$ dmarchiver -id "645754097571131337"`

The script output will be the `645754097571131337.txt` file with the conversation formatted in an _IRC-like_ style.

#### How to get a `conversation_id`?

The `conversation_id` is the identifier of a specific conversation you want to backup.

- Click on the "Messages" button on Twitter.
- Press the F12 key and go to the "Console" tab of your browser.
- Past and execute the following JavaScript code to show the IDs next to the conversation titles:

```javascript
conversations = document.getElementsByClassName('DMInbox-conversationItem')

for (var i = 0; i < conversations.length; i++) {
  threadId = conversations[i].getElementsByClassName('DMInboxItem')[0].getAttribute('data-thread-id');
  fullName = conversations[i].getElementsByClassName('fullname')[0];
  var p = document.createElement("p");
  var t = document.createTextNode("The conversation_id for \"" + fullName.innerHTML + "\" is \"" + threadId + "\""); 
  p.appendChild(t);                                
  conversations[i].parentNode.insertBefore(p, conversations[i]);
}
```

### Module import
```python
>>> from dmarchiver.core import Crawler
>>> crawler = Crawler()
>>> crawler.authenticate('username', 'password')
>>> crawler.crawl('conversation_id')
```

## Development

### Ubuntu / Windows

```shell
$ git clone https://github.com/Mincka/DMArchiver.git
$ cd DMArchiver
$ virtualenv venv
$ source venv/bin/activate # "venv/Scripts/Activate.bat" on Windows
$ pip install -r requirements.txt
```

### Mac OS X / macOS

To build and run the `pip3` package, you need to have **Xcode** (≈ 130 MB), **Homebrew** and **Python 3** (≈ 20 MB):

```
$ xcode-select --install
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python3
```

### Binary build with pyinstaller

#### On Windows

```
> pip3 install pyinstaller
> pyinstaller --onefile dmarchiver\cmdline.py -n dmarchiver.exe
> cd dist
> dmarchiver.exe
```

#### On Mac OS / macOS

```
$ pip3 install pyinstaller
$ pyinstaller --onefile dmarchiver/cmdline.py -n dmarchiver
$ cd dist
$ ./dmarchiver
```

## Known issue

### Missing emoji support in quoted tweets and usernames (Mac OS X / macOS only)
There is an issue with the `lxml` build on macOS which prevent the parsing of four-byte encoded characters. Consequently, as a workaround, the script will replace emojis (and other special characters, like Pi (U+1D70B)) in usernames and tweets. See [issue #1](https://github.com/Mincka/DMArchiver/issues/1) for more information.

## Troubleshooting

### Error building `lxml`
You may encounter building issues with the `lxml` library on Windows (`error: Unable to find vcvarsall.bat`). The most simple and straightforward fix is to download and install a precompiled binary from [this site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) and install the package locally:

`$ pip install lxml-3.6.4-cp35-cp35m-win_amd64.whl`

### `dmarchiver` script not found after `pip3 install`
If Python bin path in not in your environment PATH variable, the program will not be found. Just run it with the complete path (location may vary...):
```
$ /Library/Frameworks/Python.framework/Versions/3.5/bin/dmarchiver
```

## FAQ

### What happens to my password and my messages? Are they sent to a third-party service?
Not at all. Everything happens on your computer. Your username and your password are only sent once to Twitter using a secured connection. Your messages are downloaded from your connection, and are written on your computer at the end of the script execution, so are the images and the GIFs if you chose to download them.

### I received an e-mail from Twitter saying a suspicious connection occured on Twitter, should I be worried about it?
Not at all. The tool simulates a Firefox browser on Windows 10. Consequently, if you do not use usually this configuration, Twitter warns you about this. You can safely ignore this message if you received it at the same time the tool was used.

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
