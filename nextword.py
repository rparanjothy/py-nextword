#  Ram Paranjothy
#  Era of CoronaVirus 2019 - July 4 2020
#  An attempt to make an index which can help predict the next word.

from collections import defaultdict
import json
import requests
import random

def main(url=None, file=None, cluster=None):
    """
    Given a file, generate a dict with the list of words that followed the current word
    n => n+1
    n+1 => n+2
    Application: Can be used to predict the next word
    """
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n').strip('\t')
            wordsInLine = (x for x in line.split(" "))
            wordsInLineNext = (x for x in line.split(" "))
            try:
                # simulating a lead function, zipping list[N] with list[N-1]
                _ = next(wordsInLineNext)
                wpairs = zip(wordsInLine, wordsInLineNext)
                for word, nextWord in wpairs:
                    len(word) and len(nextWord) and cluster[word.lower()].add(nextWord.lower())
            except Exception as ex:
                print(f'{ex!s}')
        print(f"Clusters Count : {len(cluster.keys())}")

def autoSentence(limit=20):
    stmnt=""
    l=limit
    # print(l)
    data=list(wordCluster.keys())
    while l>=0 and data:
        cW=random.choice(data)
        stmnt = " ".join([stmnt,cW])
        data=list(wordCluster[cW])
        # print(cW,fW)
        l-=1
    return stmnt

def funSentences(wordCluster):
    # Fun Sentences..
    sent = ""
    nexEx = True
    w = None
    hasMore = False
    while nexEx:
        if not w:
            print("*"*40)
            for c in list(wordCluster.keys())[:10]:
                print(f'    > {c}')
            w = input("enter a word: ")
            sent = " ".join([sent, w])
        else:
            print(f"***{sent}")

        if wordCluster[w.lower()]:
            hasMore = True
            print(hasMore)

            for i, w in enumerate(wordCluster[w.lower()]):
                print(f'    {i} : {w}')
            print()
            print(sent)
        else:
            print(f'{w.lower()} - Cluster not found!')
            nexEx = False
            continue

        w = input("choice ? : ")
        if not wordCluster[w]:
            print("*"*10)
            print(f"***{sent}")
            print("*"*10)

            nexEx = False
        else:
            sent = " ".join([sent, w])

if __name__ == "__main__":
    wordCluster = defaultdict(set)
    main(cluster=wordCluster, file='data.txt')
    # main(cluster=wordCluster, file='data1.txt')
    # json.dump(wordCluster, open('outfile.json', 'w'), default=lambda x: isinstance(x, set) and list(x))
    json.dump({k: wordCluster[k] for k in sorted(wordCluster)}, open(
        'outfile.json', 'w'), default=lambda x: isinstance(x, set) and list(x))
    # funSentences(wordCluster)
    for i in range(10):
        print(autoSentence(100))
        print('-'*10)
