# Step 1
# def print_upper_words(words):
#     for word in words:
#         print (word.upper())

# Step 2 - Only words Starting With E
# def print_upper_words(words):
#     for word in words:
#         if word.lower().startswith('e'):
#             print (word.upper())


def print_upper_words(words, must_start_with):
    for word in words:
        for item in must_start_with:
            if word.lower().startswith(item):
                print(word.upper())