# Open hello.txt and read its contents
with open("hello.txt", "r") as file:
    content = file.read().strip()  # Removes any trailing newline characters

# Write the content to hello2.csv directly
with open("hello2.csv", "w") as csvfile:
    csvfile.write(content)  # Writes the content without adding extra newlines
