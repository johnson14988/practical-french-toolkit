from lemmatizer import annotate_lemma
from query_lemma1 import search_from_lemma_list
from query_lemma2 import search_lemma
from text_process import count_words, recognize_entities, split_sentences


def text_lemmatizer():
    original_file = input("Input absolute path of your target file:\n>>>")
    output_file = f"{original_file}_lemmatized.txt"
    annotate_lemma(original_file, output_file)


def process_text():
    input_file = input("Enter absolute input_file path(.txt)\n>>>")
    stem_name = input_file.rsplit(".")[0]

    word_freq_file = f"{stem_name}_freq.csv"
    entities_file = f"{stem_name}_entity.txt"
    sent_file = f"{stem_name}_sent.txt"

    count_words(input_file, word_freq_file)
    recognize_entities(input_file, entities_file)
    split_sentences(input_file, sent_file)

while True:
    print("Please select a function:")
    print(">1.annotate all verbs' lemma in a text")
    print(">2.count word frequency and so on (text process)")
    print(">3.query single lemma (using spaCy model)")
    print(">4.query single lemma (using corpora data)")
    print("---------------------------------------------")
    order = input("Enter index number (type "q" to exit)\n>>>")

    if order == "1":
        text_lemmatizer()
    elif order == "2":
        process_text()
    elif order == "3":
        search_lemma()
    elif order == "4":
        search_from_lemma_list()
    elif order == "q"
        exit()
    else:
        print("Invalid input")
