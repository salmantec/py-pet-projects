with open("story.txt", "r") as f:
    story = f.read()

old_story = story
words = set()
start_of_char = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_char = i

    if char == target_end and start_of_char != -1:
        word = story[start_of_char: i+1]
        words.add(word)

answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(old_story)
print("\n")
print(story)
