import csv
from collections import Counter
import spacy

nlp = spacy.load("fr_core_news_sm")


def count_words(input_file, word_freq_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
        doc = nlp(text)

    word_freq = Counter()
    effective_words = []

    included_type = ["NOUN", "VERB", "ADJ", "ADV"]
    for token in doc:
        if nlp(token.lemma_)[0].pos_ in included_type:
            word = token.lemma_
            word_freq[word] += 1
            if word.lower().strip() not in effective_words:
                effective_words.append(word)

    with open(word_freq_file, "w", newline="", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)

        for word in effective_words:
            csvwriter.writerow([word_freq[word], word, nlp(word)[0].pos_])

    print(f"Word Frequency saved to {word_freq_file}")


def split_sentences(input_file, sent_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
        doc = nlp(text)

    txt_file_path = sent_file.rsplit('.', 1)[0] + '(copy).txt'  # Generate txt file path

    with open(txt_file_path, 'a', encoding='utf-8') as txt_file:
        for sent in doc.sents:
            cleaned_sent = sent.text.strip()
            if len(cleaned_sent) >= 30 and "\n" not in cleaned_sent:
                txt_file.write(cleaned_sent + '\n')

    print(f"Split Sentences saved to {sent_file}")


def recognize_entities(input_file, entities_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
        doc = nlp(text)

    entity_set = set()

    with open(entities_file, "a", encoding="utf-8") as ne_file:
        for entity in doc.ents:
            if entity.text not in entity_set and "\n" not in entity.text:
                entity_set.add(entity.text.strip())
                ne_file.write(f"Entity: {entity.text} Type: {entity.label_}\n")

    print(f"Entity Name saved to {entities_file}")
