def disemvowel(string):
    nothing = ""
    for char in string:
        if char.lower() == 'a':
            a = 1      
        elif char.lower() == 'e':
            a = 1 
        elif char.lower() == 'i':
            a = 1 
        elif char.lower() == 'o':
            a = 1
        elif char.lower() == 'u':
            a = 1 
        else:
            nothing = nothing + char 
    return nothing