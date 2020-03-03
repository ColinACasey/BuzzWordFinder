## Colin Casey
## Date 2-12-2020     2-29-20
## Project Find the Buzzwords

### Runs the class ###
def main():
    OutPutList = []
    OutPutList.append(filter())
    writer(OutPutList)

### open file and put words into list ###
def filter():
    InputFile = open("InputFile.txt","r")
    OutPutList = []
    finalList = []

    ## https://en.wikipedia.org/wiki/Most_common_words_in_English
    ## Found a list of the 100 most common used words
    FillerWords = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
                   "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
                   "this", "but", "his", "by", "from", "they", "we", "say",
                   "her", "she", "or", "an", "will", "my", "all",
                   "would", "there", "what", "so", "up", "out", "if", "about",
                   "who", "get", "which", "go", "me", "when", "make", "can",
                   "like", "time", "no", "just", "him", "know", "take", "people",
                   "into", "your", "good", "some", "could", "them", "see", "other",
                   "than", "now", "look", "only", "come", "its", "over", "think",
                   "also", "back", "after", "use", "our", "first", "well", "way",
                   "even", "new", "want", "because", "any", "these", "give", "day",
                   "most", "us", "try", "had", "says", "is", "work", "are", "somewhat"
                   "more", "things", "pick", "", "\n", "working", "reporting", "learning"
                   "lot", "maybe", "position", "solutions", "responsibilities:", "qualifications:",
                   "seeking", "&", ",", ".", "[", "]", "<", ">"]

    for line in InputFile:
        OutPutList.extend(line.split(" "))

    InputFile.close()
    
    return [elem for elem in OutPutList if ((elem.lower()).rstrip()) not in FillerWords]      

### Write the output lust into OutPut File###
def writer(theOutPutList):
    Outputfile = open("outputFile", "w")

    for item in theOutPutList:
        for word in item:
            Outputfile.write(word.rstrip())
            Outputfile.write(" ")
    
    Outputfile.close()


main()

