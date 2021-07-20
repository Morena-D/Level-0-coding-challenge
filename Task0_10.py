def compare_words(word_1, word_2):
    results = ""
    for character in word_1.lower():    #Iterating within first string
        if character in word_2.lower():
            if character in results:
                    continue        #continue if character is in results
            results += character      #incrementing results with characters that exist in the two string  
    print(f"Common words: {(', '.join(results))}.")

word1 = "stink"
word2 = "Spring"
compare_words(word1, word2)
