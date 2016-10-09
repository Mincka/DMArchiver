# -*- coding: utf-8 -*-

"""
    Direct Messages Archiver - Command Line
    
    Usage:
    # dmarchiver [-h] [-di] [-dg] conversation-id auth-token
    # dmarchiver-script.py [-h] [-di] [-dg] conversation-id auth-token
    
    positional arguments:
      conversation-id       Conversation ID
      auth-token            Authentication token

    optional arguments:
      -h, --help            show this help message and exit
      -di, --download-images
                            Download images
      -dg, --download-gifs  Download GIFs (as MP4)
"""

import argparse
from dmarchiver.core import Crawler

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("conversation_id",  metavar='conversation-id', nargs=1, help="Conversation ID")
    parser.add_argument("auth_token", metavar='auth-token', nargs=1, help="Authentication token")
    parser.add_argument("-di", "--download-images", help="Download images", action="store_true")
    parser.add_argument("-dg", "--download-gifs", help="Download GIFs (as MP4)", action="store_true")

    args = parser.parse_args()
  
    crawler = Crawler(args.conversation_id[0], args.auth_token[0])
    crawler.crawl(args.download_images, args.download_gifs)
    
if __name__ == "__main__":
    main()