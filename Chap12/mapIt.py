#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import logging
logging.disable(logging.CRITICAL)  # comment to enable debug logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')
import webbrowser, sys, pyperclip
logging.debug('sys.argv variable is (%s)' %sys.argv)
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
    logging.debug('Address entered is (%s)' %address)
else:
    # Get address from clipboard
    address = pyperclip.paste()
    logging.debug('Address copied from clipboard is (%s)' %address)

webbrowser.open('https://www.google.com/maps/place/' + address)
