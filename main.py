from stats import get_num_words
from stats import count_chars

def main():
    path = "books/frankenstein.txt"
    
    # Read the file content
    with open(path) as f:
        text = f.read()
    
    # Get word count
    word_count = get_num_words(path)
    
    # Get character counts
    char_counts = count_chars(text)
    
    # Print results
    print(f"{word_count} words found in the document")
    print(f"Character counts: {char_counts}")

main()