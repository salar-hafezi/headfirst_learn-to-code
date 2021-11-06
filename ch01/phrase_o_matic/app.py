import random

# a list of verbs
verbs = ['fuck', 'eat', 'suck']
# a list of adjectives
adjectives = ['hard', 'fast', 'well']
# a list of nouns
nouns = ['Amanda', 'Sharon', 'That dog']

# create a sentence by randomly choosing its parts
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)

sentence = noun + ' ' + verb + ' ' + adjective + '!'

print(sentence)
