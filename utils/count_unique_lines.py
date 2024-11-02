import sys
from collections import Counter

def count_unique_lines(filename):
    # Read file and count each line's occurrences
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_counts = Counter(lines)

    # Display each unique line and its count
    for line, count in line_counts.most_common():
        print(f"{line.strip()}: {count}")

# Check if filename is provided as a command line argument
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_unique_lines.py <filename>")
    else:
        filename = sys.argv[1]
        count_unique_lines(filename)
