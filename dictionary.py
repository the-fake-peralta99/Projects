import json
import difflib

###########################################################
# data from json file stored in data(dictionary datatype) #
###########################################################
data = json.load(open("data.json"))

###########################################
# function to get the meaning of the word #
###########################################
def getMeaning(word):

    '''
    This function takes in the word as an argument and checks for it in the data .
    If not found in the data  check for close matches of the word entered and returns the meaning of the word after confirmation from the user.
     
    '''
    
    if word in data:
        return data[word]
    
    elif len(difflib.get_close_matches(word,data.keys())) > 0 :
        ans=input("Did you mean %s instead (Y?N)?"% difflib.get_close_matches(word,data.keys())[0])

        if ans in "yY":
            new_word = difflib.get_close_matches(word,data.keys())[0]
            return getMeaning(new_word) 

        else :
            return ["Word doesn't exists!!!"]

        
    return ["Not a word!!!"]

    
def userinput():

    flag =True
    ctr = 0   
    while(flag == True):
    
        if ctr :
            quit = input("Do you want to quit or continue (Q/C)?")

            if quit in "qQ":
                flag = False
                break
            else :
                pass
    
        word = input("Please enter the word:")

        meaning = getMeaning(word.lower())
        
        for item in meaning:
            print(item)
        
        ctr = ctr+1


if __name__ == "__main__" :   

    userinput()







    
    