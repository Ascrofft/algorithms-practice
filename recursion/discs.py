stacks = ['A', 'B', 'C']

def solve(source, target, count):
    """Assuming stack `source` contains `count` discs, numbered 1 (the smallest) through `count` (the biggest),
    return a list of instructions for moving the discs to stack `target`, observing the rules:
    - Only a single disc can be moved at a time.
    - A disc can never be on top of a smaller disc.
    - One additional stack may be used.
    
    Each instruction in the list should be a tuple containing the source disc, the target disc and the
    disc number to be moved. For example: `('A', 'B', 1)`.
    """

    if count <= 0:
        return []

    if count == 1:
        return [(source, target, count)]

    auxilary = next(item for item in stacks if item not in (source, target))

    return (
        solve(source, auxilary, count - 1)
        + [(source, target, count)]
        + solve(auxilary, target, count - 1))


# 
# 
# 
#
#           #       
#           #       
#           #       
#           #       
#  ===     ===     ===
#
#
#
# solve('A', 'C', 3)
# 'A' => 'C' 1 
# 'A' => 'B' 2
# 'C' => 'B' 1
#
# 'A' => 'C' 3

# 'B' => 'A' 1
# 'B' => 'C' 2
# 'A' => 'C' 1
# 

#
# solve('A', 'B', 4)
#
# 'A' => 'C'
# 'A' => 'B'
# 'C' => 'B'
#
# 'A' => 'C'
# 'B' => 'A'
# 'B' => 'C'
# 'A' => 'C'
#
# 'A' => 'B'
# 'C' => 'A'
# 'C' => 'B'
# 'A' => 'C'
# 'B' => 'A'
# 'C' => 'A'
# 'C' => 'B'
# 'A' => 'C'
# 'A' => 'B'
# 'C' => 'B'
#
