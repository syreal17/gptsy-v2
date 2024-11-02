from collections import Counter

def count_words(filename):
    """Reads a file and returns a Counter object with word counts."""
    with open(filename, 'r') as file:
        words = file.read().split()
    return Counter(words)

def compare_word_counts(file1, file2):
    # Get word counts for both files
    counts1 = count_words(file1)
    counts2 = count_words(file2)

    # Find shared and unique words
    shared_words = set(counts1.keys()).intersection(set(counts2.keys()))
    unique_to_file1 = set(counts1.keys()) - shared_words
    unique_to_file2 = set(counts2.keys()) - shared_words

    # Sort shared words by the sum of their counts across both files
    shared_words = sorted(shared_words, key=lambda word: counts1[word] + counts2[word], reverse=True)

    print("Shared Words (Word: Count in File1 vs. Count in File2):")
    for word in shared_words:
        print(f"{word}: {counts1[word]} vs. {counts2[word]}")

    print("\nUnique to File1 (Word: Count):")
    for word in sorted(unique_to_file1, key=lambda word: counts1[word], reverse=True):
        print(f"{word}: {counts1[word]}")

    print("\nUnique to File2 (Word: Count):")
    for word in sorted(unique_to_file2, key=lambda word: counts2[word], reverse=True):
        print(f"{word}: {counts2[word]}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python diff_sum_words.py <file1> <file2>")
    else:
        file1, file2 = sys.argv[1], sys.argv[2]
        compare_word_counts(file1, file2)