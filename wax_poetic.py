from random import choice

nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert', 'gorilla' ]
verbs = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 'curdles' ]
adjectives = ['furry', 'balding', 'incrediulous', 'fragrant', 'exuberant', 'glistening' ]
propositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within' ]
adverbs = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously' ]

def uniq_string_in_list( src_list, dst_list ):
    while True:
        string = choice( src_list)
        if string not in dst_list:
            return string

noun1 = choice( nouns )
noun2 = uniq_string_in_list( nouns, [ noun1 ] )
noun3 = uniq_string_in_list( nouns, [ noun1, noun2 ] )

starting_word = 'A'
if noun1[0] == 'a' or noun1[0] == 'e':
    starting_word = "An"

print("""{} {} Poem

        {} is too lazy to pick more choices
        so the {} kills him
        The end.""".format(starting_word, noun1, noun2, noun3)
)
