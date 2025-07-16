
def get_word_count(p):
    from contents import get_book_text
    document = get_book_text(p)
    words = document.split()
    return len(words)


def get_character_count(p):
    from contents import get_book_text
    document = get_book_text(p)
    characters ={"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    for i in document.lower():
        if i == "a":
            characters["a"] +=1
        elif i == "b":
            characters["b"] +=1
        elif i == "c":
            characters["c"] +=1
        elif i == "d":
            characters["d"] +=1
        elif i == "e":
            characters["e"] +=1
        elif i == "f":
            characters["f"] +=1
        elif i == "g":
            characters["g"] +=1
        elif i == "h":
            characters["h"] +=1
        elif i == "i":
            characters["i"] +=1
        elif i == "j":
            characters["j"] +=1
        elif i == "k":
            characters["k"] +=1
        elif i == "l":
            characters["l"] +=1
        elif i == "m":
            characters["m"] +=1
        elif i == "n":
            characters["n"] +=1
        elif i == "o":
            characters["o"] +=1
        elif i == "p":
            characters["p"] +=1
        elif i == "q":
            characters["q"] +=1
        elif i == "r":
            characters["r"] +=1
        elif i == "s":
            characters["s"] +=1
        elif i == "t":
            characters["t"] +=1
        elif i == "u":
            characters["u"] +=1
        elif i == "v":
            characters["v"] +=1
        elif i == "w":
            characters["w"] +=1
        elif i == "x":
            characters["x"] +=1
        elif i == "y":
            characters["y"] +=1
        elif i == "z":
            characters["z"] +=1
    return characters

def sort_on(items):
    return items["num"]

def report(p):
    from contents import get_book_text
    document = get_book_text(p)
    all_char_counts = {}
    character_count = []

    for i in document.lower():
        if not i.isalpha():
            continue
        if i in all_char_counts:
            all_char_counts[i] += 1
        else:
            all_char_counts[i] = 1
    
    for i in all_char_counts:
        count_dict = {"char": i, "num": all_char_counts[i]}
        character_count.append(count_dict)
   
    character_count.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {p}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(p)} total words")
    print("--------- Character Count -------")
    for item in character_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
