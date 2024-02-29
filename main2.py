from collections import defaultdict
import string

def count_word_pairs(text):
    word_pairs = defaultdict(int)
    words = text.split()
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        word_pairs[pair] += 1
    return word_pairs

def print_word_pairs(word_pairs):
    for pair, frequency in word_pairs.items():
        print(f"{pair}: {frequency}")


def print_sorted_first_n_items(dictionary, n, sort_by='value', descending=True):
    if sort_by == 'key':
        sorted_items = sorted(dictionary.items(), key=lambda x: x[0], reverse=descending)
    elif sort_by == 'value':
        sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=descending)
    else:
        raise ValueError("Invalid value for sort_by parameter. Use 'key' or 'value'.")
    
    for i in range(min(n, len(sorted_items))):
        key, value = sorted_items[i]
        print(f"{key}: {value}")



def read_file_to_string(filename):
    # Open the file for reading
    with open(filename, 'r') as file:
        # Read all lines from the file and join them into a single string
        text = ''.join(file.readlines())
        # Remove punctuation from the text
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        # Convert the text to lowercase
        text = text.lower()
        # Replace newline characters with spaces
        text = text.replace('\n', ' ')
        # Split the text into words
        words = text.split()
        # Join the words into a single string separated by spaces
        text = ' '.join(words)
    return text

    



def main():
    # text = "your input text goes here your input text goes here your input text goes here"
    filename = 'file.txt'  # Specify the path to your file here
    text = read_file_to_string(filename)
    word_pairs = count_word_pairs(text)
    # print_word_pairs(word_pairs)
    print_sorted_first_n_items(word_pairs, 50, sort_by='value')

if __name__ == "__main__":
    main()