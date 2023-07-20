alphabets = 'abcdefghijklmnopqrstuvwxyz'

def shift(i):
    return i%26
    


def encode(text='hello'):
    text = text
    output1 = ''
    for char in text:
        alpha_index = alphabets.find(char)
        output1 = output1 + alphabets[shift(alpha_index + 30)]
    return output1

p = encode('how are u')

