def compare_words(word_1, word_2):
    results = " "
    for character in word_1.lower():    #Iterating within first string
        if character in word_2.lower():
            if character in results:
                    continue        #continue if character is in results
            results += character      #incrementing results with characters that exist in the two string  
    return results

word1 = "Stink"
word2 = "Spring"
print(f"common words:{compare_words(word1, word2)}")