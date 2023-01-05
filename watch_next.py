#Documentation, Task, Personal tought
#
#
#_____________________________________________________________________________

#=========Import=========
import spacy

#Load nlp
nlp = spacy.load('en_core_web_md')

#Function to compare a description of a movie with other from other movies and find the most similar
def method_lookForMovies(local_string_description : str) -> str:

    #Load the file and split each line (movies) in a list
    file_film = open("movies.txt", "r", encoding="utf-8")
    local_list_string_film = file_film.read().split("\n")

    #Prepare variable
    local_float_similarity = 0
    local_nlp_toWatch = nlp("")
    local_string_return = ""
    local_list_string_split : list[str] = []

    #Compare the given description with the one of each movie in list
    for i in range(len(local_list_string_film)): 
        #Split to get only description
        local_list_string_split = local_list_string_film[i].split(":")

        if len(local_list_string_split) > 1:

            local_nlp_toWatch = nlp(local_list_string_split[1])
            #Check if this description is more similar than all the precedent and eventually mark as most similar
            if local_string_description.similarity(local_nlp_toWatch) > local_float_similarity:
                local_float_similarity = local_string_description.similarity(local_nlp_toWatch)
                local_string_return = local_list_string_split[0]

    file_film.close()

    #Print similarity and return the movie title
    print(f"Similarity: {local_float_similarity}")
    return local_string_return


#START
#Movie description to compare
nlp_description = nlp("""Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator""")
 
print(f"The suggested movie is: {method_lookForMovies(nlp_description)}")

