def single_root_words(root_word, *other_words):
    same_words = []
    j = list(other_words)
    for i in range(len(j)):
        if (root_word.lower() in j[i].lower()) or (j[i].lower() in root_word.lower()):
            same_words.append(j[i])
    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)