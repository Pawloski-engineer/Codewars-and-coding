text = "If enabled (On) and the user hovers/ clicks/ taps over the information icon (i) next to the field name, displays the help text you enter in the provided text box. Maximum length: 140 characters"

# text = "If enabled (On) and the user hovers/ clicks/ taps over the information icon (i) next to the field name, displays the help text you enter in the provided text box. Maximum length: 140"

def divide_to_words(text):
    words = []
    i = 0
    j = 0
    while i < len(text):
        if text[i] != ' ':
            sth = text[0:i+1]
            i += 1
            if i == len(text):
                word = text[j:i]
                words.append(word)
        else:
            word = text[j:i]
            words.append(word)
            j = i + 1
            i += 1
    return words

def show_lengths(data):
    lengths = []
    for word in data:
        lengths.append(len(word))
    return lengths

words = divide_to_words(text)

print(words)


# def justify(text, width):
#     words = divide_to_words(text)
#     lengths = show_lengths(words)
#     lines = []
#     i = 0
#     while i+1 < len(lengths):
#         sum = lengths[i]
#         while sum <= width:
#             sum = sum + 1 + lengths[i+1]
#             i += 1
#         sum = sum - 1 - lengths[i]
#         lines.append(sum)
#     lines.append(lengths[i])
#     return lines


def justify(text, width):
    words = divide_to_words(text)
    lengths = show_lengths(words)
    lines_lengths = []
    first_last_word_in_line = []
    i = 0
    while i+1 < len(words):
        sum = lengths[i]
        a = i
        while sum <= width and i+1<len(words):
            sum = sum + 1 + lengths[i+1]
            i += 1
        sum = sum - 1 - lengths[i]
        z = i
        az = [a,z]
        lines_lengths.append(sum)
        first_last_word_in_line.append(az)
    lines_lengths.append(lengths[i])
    first_last_word_in_line.append(z)
    return lines_lengths, first_last_word_in_line




solution = justify(text, 12)

print(solution[0])
print(solution[1])

# def justify(text, width):
#     words = divide_to_words(text)
#     lines = []
#     line = ''
#     i = 0
#     while i < len(words):
#         line = line + words[i]
#         if len(line) <= width:
#             line2 = line + " " + words[i+1]
#             if len(line2) <= width:
#                 line = line2
#             i += 1
#         else:
#             lines.append(line)
#             line = ''
#             i += 1
#     return line


# sth = justify(text, 10)





#
# words = divide_to_words(text)
#
# print(words)

