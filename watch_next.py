# start

import spacy  # importing spacy

nlp = spacy.load('en_core_web_md')


# Create function to read file, create a dictionary and return the key (movie + description) with the highest similarity
def watch_next(mov_deets):
    movie_compare = mov_deets
    mov_text = open("movies.txt", "r")
    movies = mov_text.readlines()
    similar_dict = {}
    movie_compare = nlp(movie_compare)
    for text in movies:
        similarity = nlp(text).similarity(movie_compare)

        similar_dict[text] = similarity

    return max(similar_dict, key=similar_dict.get)


planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

w2w = watch_next(planet_hulk)

print(w2w)

# End
