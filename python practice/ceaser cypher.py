alphabets = 'abcdefghijklmnopqrstuvwxyz'
text = 'Hello World'

def shift(i):
    return i%26

def encrypt(text,shift_amt):
    '''assigning output and lowering text'''    
    output = ''
    text = text.lower()    

    for char in text:
        if char not in text:
            output = output + char
        else:    
            alpha_index = alphabets.find(char)
            output = output + alphabets[alpha_index + shift_amt]
    return output
