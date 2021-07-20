def vowel_identify(name):
    vowels = "aeiou"
    results = ""
    for character in name.lower():   
        if character in vowels.lower():
            if character in results:
                continue
            results += character        
    print(f"vowels: {(', '.join(results))}.")
name = "UMUZI"
vowel_identify(name)
