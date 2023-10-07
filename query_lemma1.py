def load_lemma_list(file_path):
    lemma_dict = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(' -> ')
            if len(parts) == 2:
                lemma = parts[0]
                word_forms = parts[1].split(',')
                for form in word_forms:
                    lemma_dict[form] = lemma

    return lemma_dict


def search_from_lemma_list():
    lemma_file_path = "data/lemma_list_fra.txt"
    lemma_dict = load_lemma_list(lemma_file_path)
    while True:
        word = input("Enter word to get it lemma (enter 'exit' to break):\n>>>")
        if word == 'exit':
            break
        lemma = lemma_dict.get(word, "Can't get its lemma")
        print(f"Lemma of {word}: {lemma}")
