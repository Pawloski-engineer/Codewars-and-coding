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


# def justify(text, width):
#     words = divide_to_words(text)
#     lengths = show_lengths(words)
#     lines_lengths = []
#     first_last_word_in_line = []
#     sentence = ''
#     i = 0
#     while i+1 < len(words):
#         sum = lengths[i]
#         a = i
#         while sum <= width and i+1<len(words):
#             sum = sum + 1 + lengths[i+1]
#             i += 1
#         sum = sum - 1 - lengths[i]
#         z = i
#         az = [a,z]
#         lines_lengths.append(sum)
#         first_last_word_in_line.append(az)
#     lines_lengths.append(lengths[i])
#     first_last_word_in_line.append(z)
#     word_numbers = []
#     # word_numbers.append(first_last_word_in_line[0][0])
#     i = 0
#     while i < len(first_last_word_in_line):
#
#         word_numbers.append(type(first_last_word_in_line[i]))
#         word_numbers.append('//')
#         i += 1
#
#     return lines_lengths, first_last_word_in_line, word_numbers


def justify(text, width):
    words = divide_to_words(text)
    lengths = show_lengths(words)
    lines_lengths = []
    first_last_word_in_line = []
    sentence = ''
    i = 0
    while i+1 < len(words):
        sum = lengths[i]
        a = i
        while sum <= width and i+1<len(words):
            sum = sum + 1 + lengths[i+1]
            i += 1
        sum = sum - 1 - lengths[i]
        z = i
        az = range(a, z)
        lines_lengths.append(sum)
        first_last_word_in_line.append(az)
    lines_lengths.append(lengths[i])
    first_last_word_in_line.append([z])
    print("type of first last words", type(first_last_word_in_line[0]))
    for n in first_last_word_in_line:
        for m in n:
            sentence = sentence + words[m] + ' '
        sentence = sentence + '\n'
    return lines_lengths, first_last_word_in_line, sentence


solution = justify(text, 12)

print(solution[0])
print(solution[1])
print(solution[2])



#
# a = 0
# b = 5
#
#
# print(range(a, b))