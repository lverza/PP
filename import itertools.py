import itertools

# Function to read words from a local file (or modify to read from a database)
def read_words_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file.readlines()]
    return words[:12] # Ensure we only take 12 words

# Generate all possible permutations of the words
def generate_combinations(words):
    return list(itertools.permutations(words))

# Example usage
filename = "words_alpha.txt" # Replace with your local database file
words = read_words_from_file(filename)

if len(words) == 12:
    combinations = generate_combinations(words)
    print(f"Generated {len(combinations)} combinations")
    for combo in combinations[:10]: # Print first 10 combinations (avoid massive output)
        print(combo)
else:
    print("Error: Ensure the file contains at least 12 words.")