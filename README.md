[![GitHub release](https://img.shields.io/github/release/Mincka/DMArchiver.svg)](https://github.com/Mincka/DMArchiver/releases) [![PyPI](https://img.shields.io/pypi/v/DMArchiver.svg)](https://pypi.python.org/pypi/dmarchiver) [![Github All Releases](https://img.shields.io/github/downloads/Mincka/DMArchiver/total.svg)](http://www.somsubhra.com/github-release-stats/?username=Mincka&repository=DMArchiver) 

# DMArchiver
A tool to archive **all** the direct messages from your private conversations on Twitter.

## Warning: possible account lockout
Users are starting to report account lockouts because of the use of this tool. Twitter seems to lock accounts more aggressively if a new login context is detected. Even though locking can be reverted, you should be aware of this risk when using this tool. An additional attempt after unlocking can allow the tool to perform better on the second run.

## Introduction
Have you ever need to retrieve old information from a chat with your friends on Twitter? Or maybe you would just like to backup all these cheerful moments and keep them safe.

I have made this tool to retrieve all the tweets from my private conversations and transform them in an _IRC-like_ log for archiving. 

**Output sample:**
```
[2016-09-07 10:35:55] <Michael> [Media-image] https://ton.twitter.com/1.1/ton/data/dm/773125478562429059/773401254876366208/mfeDmXXj.jpg I am so a Dexter fan...
[2016-09-07 10:36:12] <Michael> [Media-sticker] [Grinning face] https://ton.twimg.com/stickers/stickers/10001_raw.png
[2016-09-07 10:37:12] <Kathy> He is so sexy. 😳 I love him. ❤️
[2016-09-07 10:38:10] <Steve> You guys are ridiculous! 😂
```

This tool is also able to **download all the uploaded images and videos** in their original resolution and, as a bonus, also retrieve the **GIFs** you used in your conversations as MP4 files (the format used by Twitter to optimize them and save space).

You may have found suggestions to use the Twitter's archive feature to do the same but Direct Messages are not included in the generated archive.

The script does not leverage the Twitter API because of its very restrictive limitations in regard of the handling of the Direct Messages. Actually, it is currently possible to retrieve only the latest 200 messages of a private conversation.

Because it is still possible to retrieve older messages from a Conversation by scrolling up, this script only simulates this behavior to automatically get the messages.

**Warning:**
Because this script leverages an unsupported method to retrieve the tweets, it may break at any time. Indeed, Twitter may change the output code without warning. If you get errors you did not have previously, please check if new releases of the tool are available.

**Disclaimer:**
Using this tool will only behave like you using the Twitter web site with your browser, so there is nothing illegal to use it to retrieve your own data. However, depending on your conversations' length, it may trigger a lot of requests to the site that could be suspicious for Twitter.  In this case, Twitter could lock preemptively the account.

## Installation & Quick start

By running the tool without any argument, you will be only prompted for your username and your password. The script will retrieve all the messages, from all the conversations without the images or the GIFs.

### Windows

Download a Windows build from the [project releases](https://github.com/Mincka/DMArchiver/releases).

Unzip the archive in a temporary folder and double-click the executable or run it in a Command Prompt (mandatory if you want to use parameters to download images and videos):
```
> C:\Temp\DMArchiver.exe
```

Note: If you run the tool directly from the zip archive window, it may fail when writing the log file. Instead, copy `DMArchiver.exe` to any directory and run it from there.

### Mac OS X / macOS

Download a macOS build from the [project releases](https://github.com/Mincka/DMArchiver/releases).

Then click on the executable, or run Terminal and execute the following commands (mandatory if you want to use parameters to download images and videos):
```
$ cd Downloads
$ ./dmarchiver
```

Note: If you run the tool by clicking on it, the result files will be available in your `/users/username` folder.

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
$ dmarchiver [-h] [-id CONVERSATION_ID] [-u] [-p] [-di] [-dg] [-dv]

$ dmarchiver --help
	usage: cmdline.py [-h] [-id CONVERSATION_ID] [-u] [-p] [-di] [-dg] [-dv]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -id CONVERSATION_ID, --conversation_id CONVERSATION_ID
	                        Conversation ID
	  -u,  --username       Username (e-mail or handle)
	  -p,  --password       Password
	  -d,  --delay          Delay between requests (seconds)
	  -di, --download-images
	                        Download images
	  -dg, --download-gifs  Download GIFs (as MP4)
	  -dg, --download-videos
	                        Download videos (as MP4)
	  -r, --raw-output      Write the raw HTML to a file
```

### Examples

#### Archive all conversations with images and videos:
```
$ dmarchiver -di -dv
```

The script output will be the `645754097571131337.txt` file with the conversation formatted in an _IRC-like_ style.

The images and videos files can be respectively found in the `645754097571131337/images` and `645754097571131337/mp4-*` folders.

#### Archive a specific conversation:
To retrieve only one conversation with the ID `645754097571131337`:

```
$ dmarchiver -id "645754097571131337"
```

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

#### Schedule a task to perform incremental backups of a conversation
You can also specify the username and the password in the options. Because DMArchiver is able to perform incremental updates, you can schedule a task or create a shortcut with the following arguments:

```
$ dmarchiver -id "conversation_id" -di -dg -dv -u your_username -p your_password
```

## Development

### Ubuntu / Windows

```shell
$ git clone https://github.com/Mincka/DMArchiver.git
$ cd DMArchiver
$ virtualenv venv
$ source venv/bin/activate # "venv/Scripts/Activate.bat" on Windows
$ pip install -r requirements.txt
$ python -m dmarchiver.cmdline
```

### Mac OS X / macOS

To build and run the `pip3` package, you need to have **Xcode** (≈ 130 MB), **Homebrew** and **Python 3** (≈ 20 MB):

```
$ xcode-select --install
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install python3
```

### Binary build with pyinstaller

The Python 3.4 (32-bit) branch is recommended to build the binaries. It will allow the best compatibility with all the platforms.

#### On Windows

```
> pip3 install pyinstaller
> pyinstaller --onefile dmarchiver\cmdline.py -n dmarchiver.exe
or alternative in case of import error
pyinstaller --onefile dmarchiver\cmdline.py --paths=dmarchiver -n dmarchiver.exe --hidden-import queue
> cd dist
> dmarchiver.exe
```

#### On Mac OS / macOS

```
$ pip3 install pyinstaller
$ pyinstaller --onefile dmarchiver/cmdline.py -n dmarchiver
or alternative for macOS Sierra with handling of external imports
$ /Library/Frameworks/Python.framework/Versions/3.4/bin/pyinstaller --onefile dmarchiver/cmdline.py -n dmarchiver --hidden-import cssselect --hidden-import lxml --hidden-import urllib3 --hidden-import requests --hidden-import queue 
$ cd dist
$ ./dmarchiver
```

### Package upload to PyPI Live

```
python setup.py sdist upload -r pypi
```

## Known issues

### Missing messages in conversations
Sometimes, generally due to a connection error, the script will write the messages of the conversations before retrieving all the messages. In this case, you should try to run the script again.

### Error message: "Unknown element type" / "Unknown media type" / "Unknown media"
Twitter may introduce new features or change the HTML output at any time. When it happens, DMArchiver may generate empty, broken logs or even crash. This kind of error message means the tool must be updated to handle the new output. Feel free to create a new issue when you encounter one of these messages.

## Troubleshooting

### Error building `lxml`
You may encounter building issues with the `lxml` library on Windows (`error: Unable to find vcvarsall.bat`). The most simple and straightforward fix is to download and install a precompiled binary from [this site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) and install the package locally:

`$ pip install lxml‑3.8.0‑cp34‑cp34m‑win32.whl`

### `dmarchiver` script not found after `pip3 install`
If Python bin path in not in your environment PATH variable, the program will not be found. Just run it with the complete path (location may vary...):
```
$ /Library/Frameworks/Python.framework/Versions/3.4/bin/dmarchiver
```

## FAQ

### What happens to my password and my messages? Are they sent to a third-party service?
Not at all. Unlike other online backup services, everything happens here on your computer. Your username and your password are only sent once to Twitter using a secured connection. Your messages are downloaded from your connection, and are written on your computer at the end of the script execution, so are the images and the GIFs if you chose to download them.

### I received an e-mail from Twitter saying a suspicious connection occured on Twitter, should I be worried about it?
Not at all. The tool simulates a Chrome (Windows or Linux) or Safari (macOS) browser on your current operation system. Because the tool does not keep any cookie locally, Twitter will warn you each time you use it. You can safely ignore this message if you received it at the same time the tool was used.

### macOS says the application is blocked because it is not from an identified developer, what should I do?
I am not able to sign the macOS executable. You will have to unblock the application if you want to use it. Go the "Security & Privacy" settings and click on the "Open Anyway" button.

## License

Copyright (C) 2016-2017 Julien EHRHART

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
