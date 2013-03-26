# Check whether the given assertion holds for all elements of
# the given collection.
#   - The given collection must be effective and the assertion
#     must be a function involving a single argument and
#     returning a boolean.
#   - Returns true if and only if the given assertion is true
#     for all the elements of the given collection.
def for_all(collection,assertion):
    for element in collection:
        if not assertion(element):
            return False
    return True

# Check whether the given assertion holds for at least one
# element of the given collection.
#   - The given collection must be effective and the assertion
#     must be a function involving a single argument and
#     returning a boolean.
#   - Returns true if and only if the given assertion is true
#     for at least one element of the given collection.
def for_some(collection,assertion):
    for element in collection:
        if assertion(element):
            return True
    return False

# Check whether the given assertion holds for the given number
# of elements of the given collection.
#   - The given collection must be effective, the given number
#     must be an integer number and the assertion must be
#     a function involving a single argument and returning
#     a boolean.
#   - Returns true if and only if the given assertion is true
#     for exactly the given number of elements of the given collection.
def for_n(collection,n,assertion):
    nb_matches = 0
    for element in collection:
        if assertion(element):
            nb_matches += 1
    return nb_matches == n

# Check whether the given premise implies the given conclusion.
#   - Both the premise and the conclusion must be functions
#     involving no argument and returning a boolean.
#   - Returns true if and only if the given premise is false or
#     if both the given premise and the given conclusion are true.
def if_then(premise,conclusion):
    return (not premise()) or (premise() and conclusion())
