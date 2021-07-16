def vowel_identify(name):
    vowels = "aeiou"
    results = ""
    for character in name.lower():   #iterating within the string
        if character in vowels.lower():
            if character in results:
                continue
            results += character        #incrementing results with characters that exists between vowels and string
    print(f"vowels: {(', '.join(results))}.")
name = "UMUZI"
vowel_identify(name)
