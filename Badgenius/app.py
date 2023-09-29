# Function to reduce a 40-character string to 20-character string using secret code A to D
def reduce_string(original_string):
    secret_code = {
        'A': 'B', 'B': 'C', 'C': 'D', 'D': 'A',
        'AA': 'B', 'BA': 'C', 'CA': 'D', 'DA': 'A',
        'AB': 'B', 'BB': 'C', 'CB': 'D', 'DB': 'A',
        'AC': 'B', 'BC': 'C', 'CC': 'D', 'DC': 'A',
        'AD': 'B', 'BD': 'C', 'CD': 'D', 'DD': 'A',
    }

    reduced_string = ""
    for char in original_string:
        if char in secret_code:
            reduced_string += secret_code[char]
        else:
            reduced_string += char

    return reduced_string[:20]


# Function to convert the reduced 20-character string back to the original 40-character string
def expand_string(reduced_string):
    secret_code = {
        'B': 'A', 'C': 'B', 'D': 'C', 'A': 'D',
        'AB': 'A', 'AC': 'B', 'DD': 'C', 'AA': 'D',
        'BB': 'A', 'BC': 'B', 'AD': 'C', 'BA': 'D',
        'CB': 'A', 'CC': 'B', 'BD': 'C', 'CA': 'D',
        'DB': 'A', 'DC': 'B', 'CD': 'C', 'DA': 'D'
    }

    expanded_string = ""
    for char in reduced_string:
        if char in secret_code:
            expanded_string += secret_code[char]
        else:
            expanded_string += char

    return expanded_string


# Example usage
original_string = "ABCDAABBCCDDAABBDACBCCDBACDDBAAADBCDBACBDACBDADDBCACBBDACBDDABCBCBCBDABCBAACBDC"
reduced_string = reduce_string(original_string)
print("Reduced String:", reduced_string)

expanded_string = expand_string(reduced_string)
print("Expanded String:", expanded_string)