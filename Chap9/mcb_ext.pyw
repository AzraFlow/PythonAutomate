#! python3
# mcb_ext.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb_ext.pyw save <keyword> - Saves clipboard to keyword.
#   py.exe mcb_ext.pyw <keyword> - Loads keyword to clipboard.
#   py.exe mcb_ext.pyw list - Loads all keywords to clipboard.
#   py.exe mcb_ext.pyw delete <keyword> - Delete keyword from clipboard.
#   py.exe mcb_ext.pyw clear - Delete all keywords from clipboard.

import shelve, pyperclip, sys

mcbShelfExt = shelve.open('mcb_ext')

# Save clipboard content or delete keyword.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelfExt[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelfExt:
            del mcbShelfExt[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelfExt.keys())))
    elif sys.argv[1].lower() == 'clear':
        for shelfKey in mcbShelfExt.keys():
            del mcbShelfExt[shelfKey]
    elif sys.argv[1] in mcbShelfExt:
        pyperclip.copy(mcbShelfExt[sys.argv[1]])
mcbShelfExt.close()
