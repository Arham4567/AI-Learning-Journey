#poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.

words_stats={}

with open("poem.txt","r") as file:
    for line in file:
        words = line.split(' ')
        # print(words)
        for word in words:
            if word in words_stats:
                words_stats[word] +=1
            else:
                words_stats[word] = 1

occurence=list(words_stats.values())
max_occurence=max(occurence)
print("Maximum occurance of any word is =",max_occurence,"and the words are:")

for word,count in words_stats.items():
    if count == max_occurence:
        print(word)





