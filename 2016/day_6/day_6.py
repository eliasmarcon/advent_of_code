from collections import Counter

with open("input") as file:

    signal = file.readlines()

signal = [line.strip() for line in signal]


def most_common_character(arr, most_common_bool):

    char_count = Counter(arr)

    if most_common_bool:
        
        most_common_items = char_count.most_common(1)

    else:

        most_common_items = char_count.most_common()[:-len(char_count)-1:-1]

    most_common_char, most_common_count = most_common_items[0]

    return most_common_char


def create_final_word(final_word, signal, most_common_bool = True):

    for i in range(0, 8):
        
        colum_chars = [col[i] for col in signal]

        most_common = most_common_character(colum_chars, most_common_bool)

        final_word += most_common

    return final_word


## PART 1 ----------------------------------------------------------------------------------------------------------
final_word = ""

final_word = create_final_word(final_word, signal)
print(final_word)


## PART 2 ----------------------------------------------------------------------------------------------------------
final_word_part_2 = ""

final_word_part_2 = create_final_word(final_word_part_2, signal, False)
print(final_word_part_2)