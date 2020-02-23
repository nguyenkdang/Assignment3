from pathlib import Path
import json
import lxml.html
from lxml.html.clean import Cleaner
from Tokenizer import Token
from collections import defaultdict

def collectData(dictionary, data, docID):
    for word in dictionary.keys():
        data[word].append(docID)
    return

def convertDictionary(normalDict):
    data = defaultdict(list)
    for word, documentIDS in normalDict.items():
        #document IDs is always a list
        data[word] = documentIDS
    return data

def file_call( directory ):
    #Variables declared beforehand
    p = Path(directory)
    cleaner = Cleaner(page_structure = True, links = True, javascript = True, scripts = True, comments = True, style = True)
    tokenizer = Token()
    docID = 0
    #Declaration of the InvertedIndex File that will be JSON
    #Set a Dictionary to create data
    for folder in p.iterdir():
        invertedIndex = open("results\invertedIndex_"+ folder.name +".json", 'w+')
        if len(invertedIndex.read()) == 0:
            data = defaultdict(list)
        else:
            data = convertDictionary(json.load(invertedIndex)) # set to be a defaultdict
        #invertedIndex.truncate(0) # Might have a problem with efficiency by rewriting all the time
        for f in folder.iterdir():
            print(f)
            docID += 1 
            with f.open() as json_file:
                i = json.load(json_file)
                cleanedContent = ''.join(c for c in (i['content']) if valid_xml_char_ordinal(c))
                if(len(cleanedContent) > 1):
                    htmlElement = cleaner.clean_html(lxml.html.fromstring(cleanedContent.encode()))
                    tokenList = tokenizer.tokenize(htmlElement.text_content())
                    tokenDict = tokenizer.computeWordFrequencies(tokenList)
                    collectData(tokenDict, data, docID)

                    tokenList.clear()
                    tokenDict.clear()
        
        json.dump(data, invertedIndex)
        invertedIndex.close()
        data.clear()
    
    print("Amount of documents recorded ", docID)
    return docID
    #with open('invertedIndex.json') as invertedIndex:
    #    data = json.load(invertedIndex)
    #print("Amount of unique tokens", len(data))


def valid_xml_char_ordinal(c):
    #Solution to making sure a html string is pure for UTF-8 before passing it through Cleaner from lxml.html
    #Taken from https://stackoverflow.com/questions/8733233/filtering-out-certain-bytes-in-python
    codepoint = ord(c)
    # conditions ordered by presumed frequency
    return (
        0x20 <= codepoint <= 0xD7FF or
        codepoint in (0x9, 0xA, 0xD) or
        0xE000 <= codepoint <= 0xFFFD or
        0x10000 <= codepoint <= 0x10FFFF
    )

file_call("DEV")
