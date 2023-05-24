"""
    Wordle solver.
"""
def wordle_solver(guess, result, init_pool,found_letters):
    """
        Wordle Sovler
    """
    letters = [*guess]
    results = [*result]
    count = 0

    found_letters = [letter for (letter,index) in zip(letters,range(0,5)) if results[index] != "_"]
    print("Found Letters:", found_letters)

    for i,j in zip(results,letters):

        if i == "_":
            if j not in found_letters:
                ending_pool=[word for word in init_pool if j not in word]
                init_pool = ending_pool
        elif i == "*":
            ending_pool=[word for word in init_pool if j in word and word[count]!=j]
            init_pool = ending_pool
        else: 
            ending_pool=[word for word in init_pool if j in word and word[count]==j]
            init_pool = ending_pool

        count+=1

    return ending_pool,found_letters

