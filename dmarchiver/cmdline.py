# -*- coding: utf-8 -*-

"""
    Direct Messages Archiver - Command Line

    Usage:
    # dmarchiver [-h] [-id CONVERSATION_ID] [-di] [-dg]

    optional arguments:
      -h, --help            show this help message and exit
      -id CONVERSATION_ID, --conversation_id CONVERSATION_ID
                            Conversation ID
      -di, --download-images
                            Download images
      -dg, --download-gifs  Download GIFs (as MP4)
"""

import argparse
import getpass
import sys
from dmarchiver.core import Crawler


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-id", "--conversation_id", help="Conversation ID")
    parser.add_argument(
        "-di",
        "--download-images",
        help="Download images",
        action="store_true")
    parser.add_argument(
        "-dg",
        "--download-gifs",
        help="Download GIFs (as MP4)",
        action="store_true")

    args = parser.parse_args()

    username = input('Enter your username or email: ')
    password = getpass.getpass(
        'Enter your password (characters will not be displayed): ')

    crawler = Crawler()
    try:
        crawler.authenticate(username, password)
    except PermissionError as err:
        print('Error: {0}'.format(err.args[0]))
        print('Exiting.')
        sys.exit()

    if args.conversation_id is not None:
        # Prevent error when using '' instead of ""
        conversation_id = args.conversation_id.strip('\'')
        print(
            'Conversation ID specified ({0}). Retrieving only one thread.'.format(
                args.conversation_id))
        crawler.crawl(
            conversation_id,
            args.download_images,
            args.download_gifs)
    else:
        print('Conversation ID not specified. Retrieving all the threads.')
        threads = crawler.get_threads()
        for thread_id in threads:
            crawler.crawl(thread_id, args.download_images, args.download_gifs)

if __name__ == "__main__":
    main()
