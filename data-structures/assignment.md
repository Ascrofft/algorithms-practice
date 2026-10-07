# Would MyDataStructure be helpful in Objective 2?

MyDataStructure has useful functionality for this objective because it behaves
similarly to a set and implements `difference()`. It could therefore be used
to find the American words that are not present in the British dictionary.

However, it is not as efficient as Python's built-in set for large amounts of
data. MyDataStructure has a fixed capacity of 1024 buckets and does not resize.
As more values are added, the buckets become larger and searching inside a
bucket takes longer. Therefore a built-in set is a better fit when considering
Big O time complexity.

# Would MyDataStructure be helpful in Objective 3?

MyDataStructure implements `intersection()`, so functionally it can find the
words that occur in both dictionaries. The result could then be converted to
a list using `to_list()` and sorted using `list.sort()`.

However, because MyDataStructure has a fixed number of buckets, membership
checks become slower as more data is stored. A built-in set therefore provides
better scaling and is a better fit for this objective.

# Would MyDataStructure be helpful in Objective 4?

No. Objective 4 requires storing a prefix together with the number of times it
occurs. MyDataStructure only stores unique values and cannot associate a key
with a count. A dict or defaultdict is a better fit because the prefix can be
used as the key and the occurrence count as its value.
