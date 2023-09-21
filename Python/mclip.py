#! python3
# mclip.py - A multi-clipboard program.
#
# this program will accept a keyword when is called by windows execute on a bat file located on C:\windows
# mclip.bat has the following:
#
#@py.exe D:\file_path\mclip.py %*
#@pause
#
# the program should be called as:
#
# mclip.bat keyword


TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)