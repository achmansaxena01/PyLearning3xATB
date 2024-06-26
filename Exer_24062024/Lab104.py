letters_list = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k']


def vowel_giver(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


result = vowel_giver('f')
print(result)

filtered_words = filter(vowel_giver, letters_list)
print(list(filtered_words))
