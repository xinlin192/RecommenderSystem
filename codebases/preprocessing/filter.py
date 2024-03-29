############################################################
##    FILENAME:   filter.py    
##    VERSION:    1.0
##    SINCE:      2014-04-28
##    AUTHOR: 
##        Jimmy Lin (xl5224) - JimmyLin@utexas.edu  
##
############################################################
##    Edited by MacVim
##    Documentation auto-generated by Snippet 
############################################################

import csv
import sys

if __name__ == "__main__":
    minSupport = int(sys.argv[1])
    maxSupport = int(sys.argv[2])
    minDF = int(sys.argv[3])
    maxDFpercent = float(sys.argv[4])
    minLength = int(sys.argv[5])

    csvin = open ("./result.txt", "r")
    reader = csv.reader(csvin, delimiter=" ")

    for word, support, DF, maxTFIDF in reader:
        [support, DF, maxTFIDF] = [int(support), int(DF), float(maxTFIDF)]
        if len(word) < minLength: continue

        if support < minSupport or support > maxSupport: continue

        if DF > minDF and maxTFIDF < maxDFpercent:
            print word, support, DF, maxTFIDF
    csvin.close()
