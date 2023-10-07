import spacy

# 加载Spacy模型
nlp = spacy.load("fr_core_news_sm")


def is_ordered_sublist(list1, list2, max_gap):
    i = 0  # track list1's order

    for item in list2:
        found = False  # a mark indicate if word is found
        while i < len(list1):
            if list1[i] == item:
                found = True
                i += 1
                break
            i += 1
        if not found:
            return False

    # check if the gap of two items <= max_gap
    for j in range(1, len(list2)):
        if list1.index(list2[j]) - list1.index(list2[j - 1]) > max_gap:
            return False

    return True


def sentence_info(sent):
    doc = nlp(sent)

    words = []
    lemmas = []
    pos_tags = []

    for token in doc:
        words.append(token.text)
        lemmas.append(token.lemma_)
        pos_tags.append(token.pos_)

    return words, lemmas, pos_tags


def search_sentence_by_expr():
    sent_file = input("Enter absolute file_path(.txt) which stores sentences:\n>>>")
    target_sents = []
    expr = input("Enter word combination:\n>>>")
    max_gap = int(input("Enter max_gap: \n>>>"))

    with open(sent_file, "r", encoding="utf-8") as f:
        line_list = f.readlines()
        for sentence in line_list:
            words, lemmas1, _ = sentence_info(sentence.lower())
            _, lemmas2, _ = sentence_info(expr.lower())

            if is_ordered_sublist(words, lemmas2, max_gap) or is_ordered_sublist(lemmas1, lemmas2, max_gap):
                target_sents.append(sentence)

        i = 1
        for sent in target_sents:
            print(i, sent)
            i += 1


search_sentence_by_expr()
input("Press any key to exit...\n>>>")
