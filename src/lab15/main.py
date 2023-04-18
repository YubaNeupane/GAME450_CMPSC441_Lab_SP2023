
import spacy

# Metric:
# Jaccard similarity coefficient measures the similarity between two sets of data, such as the sets of words in two sentences,
# by calculating the ratio of the number of common elements to the total number of elements. In the context of sentence similarity,
# the Jaccard coefficient can be used to compare the sets of words in two sentences to determine how similar they are. After we get get the jaccard coefficient similarity
# Calculate the average sentence similarity score between the two texts.

sentences = [
    ["The estimated age of the Earth is approximately 4.54 billion years. This age is determined through a variety of scientific methods, including radiometric dating of rocks and minerals, analysis of the Earth's magnetic field, and examination of the ages of meteorites and other extraterrestrial materials that are believed to have formed around the same time as the Earth.",
     "The Earth is estimated to be around 4.54 billion years old. This age has been determined through a variety of scientific methods, including radiometric dating of rocks and meteorites, studies of the Earth's magnetic field, and analysis of the formation and decay of isotopes in minerals."
     ],
    ["A black hole is a region in space where the gravitational pull is so strong that nothing, including light, can escape from it. This happens when a massive star collapses in on itself, creating a singularity, which is an infinitely dense point of space-time. The gravitational field of a black hole is so intense that it warps space and time, causing everything in its vicinity to be pulled towards it.The boundary around a black hole from which nothing can escape is called the event horizon. Beyond the event horizon, the gravitational force is so strong that even light cannot escape. This makes it impossible to observe a black hole directly, as it does not emit any radiation. Instead, scientists infer the presence of a black hole from its effects on nearby matter, such as stars or gas clouds, that orbit around it.Black holes come in different sizes, with the smallest ones being only a few times the mass of the sun and the largest ones having the mass of billions of suns. They are thought to be present in the centers of most galaxies, including our own Milky Way galaxy.",
     "A black hole is a region of space where the gravitational pull is so strong that nothing, not even light, can escape it. It is formed when a massive star runs out of fuel and collapses under the force of its own gravity, creating a point of infinite density called a singularity. The boundary around a black hole from which nothing can escape is called the event horizon. Beyond the event horizon, the gravitational pull is so strong that even light cannot escape, making it impossible to observe directly. Black holes are classified by their mass, with stellar-mass black holes having a mass between a few to tens of times that of the sun, and supermassive black holes having a mass equivalent to millions or billions of suns. Black holes are important objects in astrophysics and have been the subject of intense study for decades. They are believed to play a significant role in shaping the structure of galaxies and the evolution of the universe."
     ],
    ["The world is made up of various elements, compounds, and particles. At its most fundamental level, the world is composed of atoms, which are the basic building blocks of matter. These atoms are made up of protons, neutrons, and electrons, which are held together by powerful forces.In addition to atoms, the world is also made up of various forms of energy, such as electromagnetic radiation and the various forms of kinetic and potential energy. The world also contains various forms of matter, such as solids, liquids, gases, and plasma, which can exist in a wide range of states and conditions.Overall, the world is a complex and diverse place, made up of countless different elements, compounds, and particles, all interacting with each other in various ways to create the many different forms and phenomena we observe around us.",
        "The world is made up of a variety of components, including matter, energy, and forces. At its most basic level, matter is composed of atoms, which are the building blocks of everything we see and experience. These atoms combine to form molecules, which make up the different types of matter that we encounter in our daily lives, such as water, air, and rocks.Energy is another key component of the world, and it takes many different forms, such as thermal energy, light energy, and kinetic energy. Energy is essential to everything we do, from powering our homes and vehicles to driving biological processes within our bodies.Forces also play a crucial role in shaping the world around us, from the gravitational forces that hold planets in orbit to the electromagnetic forces that govern the behavior of atoms and molecules. Overall, the world is a complex and interconnected system, made up of many different components that work together to create the rich and varied environment we inhabit."]
]


nlp = spacy.load("en_core_web_md")


def jaccard_similarity(sentence1, sentence2):
    """Calculate the Jaccard similarity coefficient between two sentences."""
    doc1 = nlp(sentence1)
    doc2 = nlp(sentence2)
    words1 = set(token.text.lower()
                 for token in doc1 if not token.is_punct and not token.is_space)
    words2 = set(token.text.lower()
                 for token in doc2 if not token.is_punct and not token.is_space)
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    if union > 0:
        return intersection / union
    else:
        return 0.0


def calculate_similarity(text1, text2):
    """Calculate the average sentence similarity score between the two texts."""
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    sentence_scores = []
    sentence_scores.append(jaccard_similarity(text1, text2))
    for sent1, sent2 in zip(doc1.sents, doc2.sents):
        score = sent1.similarity(sent2)
        sentence_scores.append(score)
    if len(sentence_scores) > 0:
        return sum(sentence_scores) / len(sentence_scores)
    else:
        return 0.0


for sen in sentences:
    similarity_score = calculate_similarity(sen[0], sen[1])
    print(sen[0], "\n<->\n", sen[1])

    print(f"Similarity score: {similarity_score:.2f}")

    if (similarity_score > 0.78):
        print("CHATGPT IS TELLING THE TRUST 😁")
    else:
        print("CHATGPT IS THE LYING 😭")

    print("========================================\n")
