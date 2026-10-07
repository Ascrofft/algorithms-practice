def get_words_recursive(count, letters):
    """Returns a list of all random 'words' consisting of `count` `letters` using recursion.

    Arguments:
        letters {string} -- A string of letters (characters) to be used in the words.
        count {number} -- The number of letters that should be in each word.

    Example:
        get_words_recursive(3, 'ab') == ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']

    The order of the strings in your output list doesn't matter.
    """

    # Base case: count == 1
    #  - return all possible single letter words
    # Recursive case: count > 1
    #  - use recursion to get all words of length count-1
    #  - create our result by adding each possible letter to each of these word

    return [] # TODO!


# Code below is a example of the iterative implementation, debug and implement a recursion version above in get_words_recursive
def get_words_iterative(count, letters):
    """Returns a list of all random 'words' consisting of `count` `letters` using loops and *without* recursion.

    Arguments:
        letters {string} -- A string of letters (characters) to be used in the words.
        count {number} -- The number of letters that should be in each word.

    Example:
        get_words_iterative(3, 'ab') == ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']

    The order of the strings in your output list doesn't matter.
    """
    words = []
    if count <= 0:
        return words
    
    letter_indices = [0] * count

    while True:
        # Make sure all each letter index < len(letters)
        for pos, index in enumerate(letter_indices):
            if index < len(letters):
                break # All indexes are valid
            if pos + 1 >= count:
                return words # We've seen al combinations
            letter_indices[pos] = 0
            letter_indices[pos+1] += 1

        # Add the word indicated by the `letter_indices` to `words`.
        word = ''.join([letters[index] for index in letter_indices])
        words.append(word)

        # Change the leftmost letter to the next one. This may go past the length
        # of `letters`, but if that's the case, it will be fixed at the top of
        # the loop.
        letter_indices[0] += 1
