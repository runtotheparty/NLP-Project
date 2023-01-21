import spacy  # importing spacy

nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# I found it interesting that apple and monkey were so dissimilar despite a monkey would easily eat both fruit given
# the chance

# here is my own example
tokens = nlp('bread man wheat field ')
# I'm surprised that wheat and field are not very similar, I would have expected them to be 0.5 or 0.6 at least

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
