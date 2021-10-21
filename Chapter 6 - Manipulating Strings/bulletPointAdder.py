#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

# Project: Adding Bullets to Wiki Markup

# Step 1: Copy and Paste from the Clipboard
import pyperclip

text = pyperclip.paste()

# TODO: Separate lines and add stars


# Step 2: Separate the Lines of Text and Add the Star
lines = text.split("\n")
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[i] = "* " + lines[i]  # add start to each string in "lines" list


# Step 3: Join the Modified Lines
text = "\n".join(lines)

pyperclip.copy(text)
