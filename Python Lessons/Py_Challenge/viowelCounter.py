
# Count the number of times viowels appeared in a given statement

def viowelCounter(statement) :
    
    counters = 0
    for letter in statement :
        for viowel in viowels :
            if viowel == letter :
                counters +=1 
    
    print(f"The viowels apperared {counters} times")
        

statements = "This statements contains viowels and consonants that will be checked"
viowels = ["a", "e", "i", "o", "u"]
viowelCounter(statements)