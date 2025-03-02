import itertools
import os

# File to store generated combinations
output_file = "combinations.txt"

# Function to read 12 words from a local file
def read_words_from_file(dictionary):
    with open(dictionary, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file.readlines()]
    return words[:12] # Ensuring we only use 12 words

# Function to load previously generated combinations from file
def load_existing_combinations():
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file)
    return set()

# Function to generate and store unique combinations
def generate_and_store_combinations(words):
    existing_combinations = load_existing_combinations() # Load previous data
    total_combinations = set(itertools.permutations(words)) # Generate all permutations

    new_combinations = total_combinations - existing_combinations # Remove already processed ones

    if new_combinations:
        with open(output_file, 'a', encoding='utf-8') as file:
            for combo in new_combinations:
                file.write(" ".join(combo) + "\n") # Write new combinations in real time

        print(f"Added {len(new_combinations)} new combinations.")
    else:
        print("No new combinations found.")

# Main execution
input_file = "words_alpha.txt" # Replace with your local file
words = read_words_from_file(input_file)

if len(words) == 12:
    generate_and_store_combinations(words)
else:
    print("Error: Ensure the file contains at least 12 words.")