from collections import defaultdict

class Token:

    def __init__(self):
        return
    def tokenize(self,filePath) -> list:
        #tokenize follows a O(N) runtime complexity as it iterates through each character of the file(n chars). Any other statements
        #inside of tokenize follows a O(1) runtime complexity, which does no affect the linear regression. 
        f = open(filePath, encoding = "ascii", errors = "surrogateescape")
        tokenAlpha = []
        for line in f: 
            token = ""
            for i in line:
                if i.isalnum():
                    token += i 
                else:
                    if len(token) != 0:
                        tokenAlpha.append(token)
                        token = ""
        tokenAlpha.append(token)
        f.close()
        return tokenAlpha


    def computeWordFrequencies(self, token_list:list) -> dict:
        #computewordFrequencies goes through a O(N) runtime complexity as there is only one iteration for token_list.
        #frequencyDict is created before as a defaultdict in order to limit and simplify code. The statements inside the for loop
        #follow a O(1) runtime complexity.

        frequencyDict = defaultdict(int)
        for i in token_list:
            frequencyDict[i] +=1
        return frequencyDict

    def print(self, frequency:defaultdict) -> None:
        #print goes through a O(N) runtime complexity as it iterates through all the pair values in the frequency dictionary. 
        #The following statement(sort) follows a N log N, so precedence in terms of significance at
        #higher data count goes to O(2N)
        tokenList = list() 
        for k,v in frequency.items(): 
            tokenList.append((k,v)) 
        tokenList.sort(key = lambda x:  -x[1]) 
        for i in tokenList: 
            print(f"<{i[0]}>\t<{i[1]}>") # We're trying to use the global print right here

