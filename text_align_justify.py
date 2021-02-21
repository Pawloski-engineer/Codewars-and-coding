# text = "If enabled (On) and the user hovers/ clicks/ taps over the information icon (i) next to the field name, displays the help text you enter in the provided text box. Maximum length: 140 characters"

text = "If enabled (On) and the user hovers/ clicks/ taps over the information icon (i) next to the field name, displays the help text you enter in the provided text box. Maximum length: 140"

# text = "If enabled (On) and the"

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
            u = words[i]
            sum = sum + 1 + lengths[i+1]
            i += 1
        if sum > width:
            sum = sum - 1 - lengths[i]
        z = i
        az = range(a, z)
        lines_lengths.append(sum)
        first_last_word_in_line.append(az)
    lines_lengths.append(lengths[i])
    if lines_lengths[-1] + len(words[z]) <= width:
        first_last_word_in_line[-1] = range(a, z+1)
        lines_lengths.pop()
    else:
        first_last_word_in_line.append([z])
    # print("type of first last words", type(first_last_word_in_line[0]))
    i = 0
    for n in first_last_word_in_line:
        speces = width - lines_lengths[i]   # number of all spaces that need to be added to the line
        # num_of_words_in_line = ??                                    # defeine number of words in the line

        for m in n:
            # additional_spaces = spaces/math.ceil(num_of_words_in_line-1)                                    # define number of spaces between the current words
            # spaces = spaces - additional_spaces
            sentence = sentence + words[m] + (1 + additional_spaces) * ' '    #multiply spaces by line (length-width)/(number_of_words - 1)
        sentence = sentence + '\n'
        i += 1
    sentence = sentence[0: -2]
    return lines_lengths, first_last_word_in_line, sentence


solution = justify(text, 12)

print(solution[0])
print(solution[1])
print(solution[2])

