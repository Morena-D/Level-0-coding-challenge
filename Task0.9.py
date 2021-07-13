def vowel_identify(name):
    vowels = "aeiou"
    results = ""
    for character in name.lower():   #iterating within the string
        if character in vowels.lower():
            if character in results:
                continue
            results += character        #incrementing results with characters that exists between vowels and string
    return results
name = "UMUZI"
print(f"vowels: {vowel_identify(name)}")