text = open("zen.txt")
content = text.read()
#pseudo code: 

    #find method which removes special car and leaves only alphanum. 
    #counting spaces 
    #count the num of words by loop (for each word in content.. i +=1)? is it the most optimal solution to use the loop? Will be slow for really big texts.is there a count words integrated func or parsing like analysis?
    #return to the original content  and create a new var on its base:
        #use method "replace" to replace "is" by "should be" in another var
        #uppercase that another var
    #print out the new var

"""

   3.  Transform the new text into UPPER CASE.
   4.  Display the result of your modifications in the terminal. The punctuation and special characters have to be there as well!
"""
######## TASK 1  - WORDS COUNT ######################################################################################################
#create new empty string
newtext = ""
i = 1  #starts from 1 to compensate the absence of last "new line", a last word will not be counted otherwise
for element in content:
    if element.isalnum() == False:       #if we deal with a non-alphanumerical caracter (perhaps element.isalpha() would be enough)
        if  element == "." or element == ",":   #need keep punctioation in new text for readability purposes, no impact on words count
            newtext +=str(element)
        elif element.isspace() == True:  #alternatively can use   element == " " or element == "\n"; we keep spaces
            i += 1                      #counting spaces is enough to count words! "it's" is still a one word, not two
            newtext +=str(element)
        else:
            pass        #thus, all special car (except for ,.spaces) are not integrated in newtext
    else:   
        newtext += str(element)
#print(newtext)

#translate the string into list with .split() methon, then count number of items in list
print("The number of words in zen.txt is " + str(len(newtext.split())  )  )
######## TASK 2 - IS TO BECOME SHOULD BE ######################################################################################################

string = str(content)
string1 = string.replace(" is "," should be ")
string2 = string1.replace(" it's "," it should be ")   #could also introduce same change for various grammatical forms like "are >should" etc+all negations
print(string2)

######## TASK 3 - ALL TO UPPERCASE ######################################################################################################
 
string2_upper = string2.upper()


######## TASK 4 - PRINT OUT ######################################################################################################
print(string2_upper)

text.close()