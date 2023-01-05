#Documentation, Task, Personal tought
#
#
#_____________________________________________________________________________

"""
NOTE:
Run the example file with the small database instead of medium give this sort of "error", mostly the complain is about word vector

The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger,
parser and NER, which may not give useful similarity judgements. 
This may happen if you're using one of the small models, e.g. `en_core_web_sm`, 
which don't ship with word vectors and only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the larger models instead if available.

Can be noticed that the result are much less accurate and probabily not given any really usefull information about
"""




#=========Import=========
import spacy

nlp = spacy.load('en_core_web_md')

#================1===================
print("1__________________________________________")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""
NOTE:
Interesting to see how can this system recognise tons of word an some of their connection.
Cat and monkey are both animals so they have an higher similarities, this make sense
Monkey and banana have a good connection to be totaly different "things" but gives a good similarity as monkey are famous to eat banana
Cat and monkey instead have definitely not a good connection and sounds pretty accurate as difference.
"""
print("CUSTOM EXAMPLE")
word1 = nlp("Laptop")
word2 = nlp("Dekstop")
word3 = nlp("Computer monitor")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""
NOTE:
In this custom example seems that the similarities amount are even quite accurate but by using slightly different word
that should refer to the same object in real word can give quite different result.
For example, by writing Monitor instead of computer monitor, there is a noticeably difference in result.
Even the word computer insert instead of desktop give some unexpected result compared to laptop.
"""





#=================2==================
print("2__________________________________________")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))



#=================3==================
print("3__________________________________________")
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

