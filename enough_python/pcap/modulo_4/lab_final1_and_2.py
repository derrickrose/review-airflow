from os import strerror
from collections import defaultdict

# file_path = input("Enter the file path: ")
file_path = "lab1.txt"
try:
    stream = open(file_path.strip(), "rt")
    char = stream.read(1).lower()
    collector = defaultdict(int)
    while char:
        collector[char] += 1
        char = stream.read(1).lower()
    stream.close()
except IOError as e:
    collector = None
    print(strerror(e.errno))

if collector:
    for char in sorted(collector.keys()):
        print(char, "->", collector[char])

    print("\n\nSorted by count:")
    for char, count in sorted(collector.items(), key=lambda x: x[1], reverse=True):
        print(char, "->", count)
