from collections import defaultdict
from stop_words import IS_STOP_WORD
from PorterStemmer import PorterStemmer

class Token:

    def __init__(self):
        return
    def tokenize(self,html_file) -> list:
        #tokenize follows a O(N) runtime complexity as it iterates through each character of the file(n chars). Any other statements
        #inside of tokenize follows a O(1) runtime complexity, which does no affect the linear regression. 
        stemmer = PorterStemmer()
        tokenAlpha = []
        token = ""
        for i in html_file:
            if i.isalnum():
                token += i 
            else:
                if len(token) >1  and token not in IS_STOP_WORD and not token.isdigit():
                    token = stemmer.stem(token, 0, len(token)-1).lower() 
                    tokenAlpha.append(token)
                token = ""
        tokenAlpha.append(token)
        return tokenAlpha


    def computeWordFrequencies(self, token_list:list) -> dict:
        #computewordFrequencies goes through a O(N) runtime complexity as there is only one iteration for token_list.
        #frequencyDict is created before as a defaultdict in order to limit and simplify code. The statements inside the for loop
        #follow a O(1) runtime complexity.

        frequencyDict = defaultdict(int)
        for i in token_list:
            frequencyDict[i] +=1
        return frequencyDict
