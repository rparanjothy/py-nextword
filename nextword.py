#  Ram Paranjothy
#  An attempt to make an index which can help predict the next word.

from collections import defaultdict


def main():
    """
    Given a file, generate a dict with the list of words that followed the current word
    n => n+1
    n+1 => n+2
    """

    m = defaultdict(list)
    with open('data.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n').strip('\t')
            wordsInLine = (x for x in line.split(" "))
            wordsInLineNext = (x for x in line.split(" "))
            try:
                # simulating a lead function, zipping list[N] with list[N-1]
                _ = next(wordsInLineNext)
                wpairs = zip(wordsInLine, wordsInLineNext)
                for word, nextWord in wpairs:
                    len(word) and len(nextWord) and m[word].extend([nextWord])
            except Exception as ex:
                print(f'{ex!s}')
        print(m)


if __name__ == "__main__":
    main()
