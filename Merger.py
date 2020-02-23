from pathlib import Path
from collections import defaultdict
import json
from Indexer import convertDictionary

def merger(directory):
    #Read through resulting json dictionary file, and merge them into one dictionary, return the dictionary
    #Also print out the legnth of the dictionary.
    p = Path(directory)
    data = defaultdict(list)
    for f in p.iterdir():
        with f.open() as json_file:
            buf = convertDictionary(json.load(json_file))
            for word, IDs in buf.items():
                for id in IDs:
                    data[word].append(id)
    
    print("Amount of unique tokens", len(data))
    #print(data)
    return data


merger("Results")