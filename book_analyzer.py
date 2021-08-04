# function accepts the a book in the form of a named text file as input
# the function develops a number of results useful in analyzing the book
# the results include some simple numbers as well as lists and sets created from the book
import string
import numpy as np

def bookAnalysis(book):

    inFile = open(book,"r") # specify source documents

    # creates a base translation table to eliminate punctuation.

    tt = {}
    
    # eliminates punctuation
    for char in string.punctuation:
        tt[ord(char)] = 32
    
    # eliminates digits
    digits = {'0','1','2','3','4','5','6','7','8','9'}
    for char in digits:
        tt[ord(char)] = 32
        
    
    # initializes empty list to hold lines and set count of lines to 0.
    
    lines = []
    nlines = 0
    
    # iterates through the lines in the source document
    
    
    
    for line in inFile:
        if  len(line) > 1: # avoid blank lines
            
            # adds any non ascii characters to translation table
            
            for char in line:
                if ord(char) > 127:
                    tt[ord(char)] = 32
            line = line.translate(tt)        
            nlines = nlines + 1 # increment count of lines
            lines.append(line)  # add current line to list of lines
    
    
    
    
    
    # builds a list of words from the list of lines
    
    words = []
    problem_lines = []
    for line in lines:
        lineOK = True
        line = line.lower()
        words_line = line.split()
        words = words + words_line
    
    # creates a dictionary to capture the counts of the unique words in the text.
    
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word,0) + 1
    
    # gets a list of the unique values (counts) in the dictionary.
    
    counts = []
    for count in count_dict.values():
        if count not in counts:
            counts.append(count)
    
    # creates a list of the 100 largest values in counts
    
    counts.sort()               # sort the counts
    counts.reverse()            # convert to descending order
    top_counts = counts[:100]
    
    
    # build a list of lists of words in each place. Note that we have to allow for ties, so there is a list of words in each place.
    
    place_lists = []
    for i in range(50):
        count = top_counts[i]
        place_list = []
        for key in count_dict.keys():
            if count_dict[key] == count:
                place_list.append(key)
        place_lists.append(place_list)
        
    
    unique_words = list(count_dict.keys())
        
    No_unique_words = len(unique_words)
    Total_no_words = len(words)
    Ratio_unique_total = No_unique_words/Total_no_words 
    Ratio_total_unique = Total_no_words/No_unique_words
    
    lengths = []
    for word in words:
        lengths.append(len(word))
    
    cnt = list(count_dict.values())
    mean_word_length = np.mean(cnt)
    
    Out_dict = {}
    Out_dict['unique_words'] = unique_words
    Out_dict['No_unique_words'] = No_unique_words
    Out_dict['Total_no_words'] = Total_no_words
    Out_dict['Ratio_unique_total'] = Ratio_unique_total
    Out_dict["Word_list"] = words
    Out_dict['count_dict'] = count_dict
    Out_dict['Median uses per word'] = np.median(cnt)
    Out_dict["Book"] = book
    Out_dict["place_lists"] = place_lists
    Out_dict["lengths"] = lengths
    Out_dict["mean_word_length"] = np.mean(lengths)
    Out_dict["tt"] = tt
    return(Out_dict)
