#! python3
# mclip.py - A multi-clipboard program
# Project: Multi-Clipboard Automatic Messages

# Step 1: Program Design and Data Structures
TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would your consider making this a monthly donation?""",
}

# Step 2: Handle Command Line Arguments

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: py mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

# Step 3: Copy the Right Phrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print("There is no text for " + keyphrase)
