import time
from collections import deque

# Inserting spaces

def insert_spaces(sentence, dictionary):
    """Given a `sentence` string not containing any spaces, return the same string but
    with spaces inserted between the words. All words must exist in the provided
    `dictionary` set.

    The function behaves 'greedy', meaning that it will try to match longer words
    before it matches shorter words. For instance: `insert_spaces("todolist")` should
    return `"todo list"` instead of `"to do list"`.

    In case no solution is found, `None` is returned. (This shouldn't happen for the
    sentences provided in `data.txt` though.)
    """
    if len(sentence) == 0:
        return ""

    word = sentence

    while word:
        if word in dictionary:
            remaining = sentence.removeprefix(word)

            result = insert_spaces(remaining, dictionary)

            if result is not None:
                if result == "":
                    return word

                return word + " " + result

        word = word[:-1]

    return None


# Top words

def get_common_words(sentences, count):
    """Given a `list` of `sentences` (strings), this function returns a `set` of the
    `count` most frequently occurring words. When words have the same number of
    occurrences, priority is given to words that come earlier in the alphabet.
    """
    found = {}

    for sentence in sentences:
        for word in sentence.split():
            if word not in found:
                found[word] = 1
            else:
                found[word] += 1

    sorted_words = sorted(
        found.items(),
        key=lambda item: (-item[1], item[0])
    )

    return {
        word
        for word, _ in sorted_words[:count]
    }


# Word graph

def create_word_graph(sentences):
    """Given a `list` of `sentences` (strings), this function creates a data structure
    representing a bidirectional graph, where each word in the text is a vertex (point),
    and each edge (line) indicates that words occur together in at least one sentence.
    """
    result: dict[str, set[str]] = {}

    for sentence in sentences:
        words = sentence.split()

        for word in words:
            if word not in result:
                result[word] = set()

            for other_word in words:
                if other_word != word:
                    result[word].add(other_word)

    return result


# Word connections

def get_distance(word_graph, word1, word2, blacklist = set()):  # noqa: B006
    """Return the minimum distance between two given words in a word graph. In case no path
    can be found, the string `"infinite"` is returned. The `blacklist` argument is an optional
    set of words that may not be used for constructing the shortest path.
    """
    if word1 in blacklist or word2 in blacklist:
        return "infinite"

    if word1 == word2:
        return 0
    
    queue = deque()
    visited = set()

    queue.append((0, word1))
    visited.add(word1)

    while queue:
        distance, word = queue.popleft()

        for neighbor in word_graph.get(word, set()):

            if neighbor in blacklist or neighbor in visited:
                continue

            if neighbor == word2:
                return distance + 1
            
            visited.add(neighbor)
            queue.append((distance + 1, neighbor))

    return "infinite"


# Demo

# You should not need to edit anything below this. (Except of course for
# experimenting.)

if __name__ == "__main__":
    with open('data.txt') as file:
        lines = [line.rstrip("\n") for line in file]

    with open('english.txt') as file:
        english = {line.rstrip("\n") for line in file} # a set generator

    start_time = time.perf_counter()


    # Inserting spaces

    sentences = [insert_spaces(line, english) for line in lines]
    sentences = [s for s in sentences if s is not None]
    
    with open('output-data.txt', "w") as file:
        file.write("\n".join(sentences))

    word_count = " ".join(sentences).count(" ") + 1
    print(f"The {len(sentences)} sentences have been split into {word_count} words and written to 'output-data.txt'.")


    # Top words

    top50 = get_common_words(sentences, 50)
    top1000 = get_common_words(sentences, 1000)

    print()
    print(f"The top 50 most common words are: {', '.join(sorted(top50))}.")


    # Word graph

    word_graph = create_word_graph(sentences)


    # Word connections

    for blacklist in [set(), top50, top1000]:
        print()
        if blacklist:
            print(f"Using the top {len(blacklist)} common words as blacklist...")
        else:
            print("Without a blacklist...")
        for word1, word2 in [("score", "score"), ("atoms", "ghosts"), ("textbook", "falling"), ("broom", "textbook")]:
            dist = get_distance(word_graph, word1, word2, blacklist)
            print(f"  the distance between '{word1}' and '{word2}' is {dist}.")


    print()
    print(f"Execution took {round(time.perf_counter()-start_time, 3)}s\n")
