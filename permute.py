#CMPS5P
#return a list of all permutations of a word

def permutation(word):
    #base case
    if word == "":
        return([word])
    else:
        first_letter = word[0]
        short_word = word[1:]
        new_list = []
        for permute_sh_wrd in permutation(short_word):
            for i in range(len(permute_sh_wrd) + 1):
                new_list = new_list + [permute_sh_wrd[0:i] + first_letter + permute_sh_wrd[i:]]
        return(new_list)
