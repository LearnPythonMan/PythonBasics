#in codewars you have dictionary MORSE_CODE

test = '.... . -.--   .--- ..- -.. .'

def decodeMorse(morse_code):
    ans = ''
    words = morse_code.strip().split('   ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            ans += MORSE_CODE.get(letter)
        ans += ' '
    return ans[:-1]
    # morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')

# def decodeMorse(morse_code):
#     return ' '.join(''.join(MORSE_CODE[letter] for letter in words.split(' ')) for words in morse_code.strip().split('   '))


print(decodeMorse(test))