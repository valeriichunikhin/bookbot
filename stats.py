def get_num_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        
    return word_count

def count_chars(text):
    chars = {}
    for char in text:  # Changed 'chat' to 'char'
        char = char.lower()  # Convert to lowercase
        if char in chars:  # Check if char is already in the dictionary
            chars[char] += 1  # Increment count
        else: 
            chars[char] = 1  # Initialize count to 1  
    return chars