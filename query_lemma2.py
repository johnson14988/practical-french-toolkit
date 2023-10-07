import spacy


def search_lemma():
    nlp = spacy.load('fr_core_news_lg')
    while True:
        word = input("Enter word to get it lemma (enter 'exit' to break):\n>>>").lower()
        if word != "exit":
            processed_word = nlp(word)[0]
            lemma = processed_word.lemma_
            print(f"Lemma of {word}: {lemma}")
        else:
            break
