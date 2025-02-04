text = "Hello , world!\nThis is a test."

word_to_remove = "Hello"

# Check if the text starts with the word followed by space or punctuation
if text.startswith(word_to_remove):
    new_text = text[len(word_to_remove):].lstrip()  # Remove the word and strip leading spaces
else:
    new_text = text  # Keep the original text if the word isn't at the start

print(new_text)