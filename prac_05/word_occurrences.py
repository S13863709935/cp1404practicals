"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""

def count_words(text):
    """Count occurrences of each word in text."""
    word_counts = {}
    for word in text.split():
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def main():
    """Main function to process user input and display word counts."""
    text = input("Text: ")
    word_counts = count_words(text)
    max_length = max(len(word) for word in word_counts)
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_length}} : {count}")

if __name__ == "__main__":
    main()