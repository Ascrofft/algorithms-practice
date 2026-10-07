
def count_unrecognized(american_path, british_path):
    """
    Timecomplexity: O(n + m)

    n = number of British words
    m = number of American words

    We iterate once over the n British words to build a set.
    Then we iterate once over the m American words.
    Membership lookup in a set is O(1) on average.
    """
    british_words = set()

    with open(british_path, "r") as file:
        for line in file:
            word = line.strip()
            british_words.add(word)

    count = 0

    with open(american_path, "r") as file:
        for line in file:
            word = line.strip()

            if word not in british_words:
                count += 1

    return count

# print(count_unrecognized('./american-english', './british-english'), end="\n\n")


def alpha_order_communal_words(american_path, british_path):
    """
    Time complexity: O(n + m + k log k)

    n = number of British words
    m = number of American words
    k = number of words occurring in both dictionaries

    Building the British set takes O(n).
    Checking all American words takes O(m), because set lookup is O(1) on average.
    Sorting the k common words takes O(k log k).
    """
    british_words = set()
    
    with open(british_path, "r") as file:
        for line in file:
            word = line.strip()
            british_words.add(word)

    communal_words = []

    with open(american_path, "r") as file:
        for line in file:
            word = line.strip()

            if word in british_words:
                communal_words.append(word)

    communal_words.sort()
    
    return communal_words

# print(alpha_order_communal_words('./american-english', './british-english'), end="\n\n")


def count_popular_prefixes(path):
    """
    Time complexity: O(m + p log p)

    m = number of words in the American dictionary
    p = number of unique three-letter prefixes

    We iterate over all m words once. Dictionary lookup/update is O(1) on average.
    Afterwards the p unique prefixes are sorted by their count, which takes
    O(p log p).
    """
    prefixes = {}

    with open(path, "r") as file:
        for line in file:
            word = line.strip()

            if len(word) >= 3:
                prefix = word[:3]

                if prefix in prefixes:
                    prefixes[prefix] += 1
                else:
                    prefixes[prefix] = 1

    sorted_prefixes = sorted(
        prefixes.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_prefixes[:20]

# print(count_popular_prefixes('./american-english'), end="\n\n")
# print(count_popular_prefixes('./british-english'), end="\n\n")
