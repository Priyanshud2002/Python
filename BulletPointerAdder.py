import pyperclip

# Get text from clipboard
text = pyperclip.paste()

# Split text into lines
lines = text.split("\n")

# Add a bullet (*) before each line
for i in range(len(lines)):
    lines[i] = "* " + lines[i]  # Add "* " (with space) to each line

# Join the modified lines into a single string
text = "\n".join(lines)

# Copy the modified text to the clipboard
pyperclip.copy(text)

print("Bullet points added and copied to clipboard!")
