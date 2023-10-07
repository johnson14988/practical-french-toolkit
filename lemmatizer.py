import spacy
nlp = spacy.load("fr_core_news_lg")  # optionally fr_core_news_sm is okay, details on https://spacy.io/usage


def annotate_lemma(file_name, new_file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
    doc = nlp(text)

    annotated_text = []
    for token in doc:
        if token.pos_ == "VERB":  # only process verb
            verb_lemma = token.lemma_
            annotated_text.append(f"{token.text}{{{verb_lemma}}}")
        else:
            annotated_text.append(token.text)

    new_text = " ".join(annotated_text)

    with open(new_file_name, "w", encoding="utf-8") as f:
        f.write(new_text)

    print(f"Result saved to {new_file_name}")


