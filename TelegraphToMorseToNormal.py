#test = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
test = '10001'

def decodeBits(bits):
    bits = bits.strip('0')
    previousSignal = '1'
    info = ''
    signals = []
    for signal in bits+'0':
        if signal != previousSignal:
            signals.append(info)
            info = ''
        info += signal
        previousSignal = signal
    minSignalLenght = len(min(signals, key=len))
    return bits.replace(minSignalLenght * 7 * '0', '  ').replace(minSignalLenght * 3 * '1', '-').replace(
        minSignalLenght * 3 * '0', ' ').replace(minSignalLenght*'1', '.').replace(minSignalLenght * '0', '')

# Best practice:
# def decodeBits(bits):
#     import re
#
#     # remove trailing and leading 0's
#     bits = bits.strip('0')
#
#     # find the least amount of occurrences of either a 0 or 1, and that is the time hop
#     time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
#
#     # hop through the bits and translate to morse
#     return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')
#
# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))

#if len(max(signals)) != len(min(signals)):


#    bits = bits.strip('0')
#     firstSignal = bits[0:bits.find('0')]
#     if len(firstSignal) < 1:
#         firstSignal = bits
#     if bits.find(firstSignal+'1') == -1 and bits.find(firstSignal[0:-1]) != -1 and len(firstSignal) > 1:
#         firstSignal = '1' * (len(firstSignal) // 3)
#     return bits.strip('0').replace(len(firstSignal * 7) * '0', '  ').replace(firstSignal * 3, '-').replace(
#            len(firstSignal * 3) * '0', ' ').replace(firstSignal, '.').replace(len(firstSignal) * '0', '')

#def decodeMorse(morse_code):
#    return ' '.join(''.join(MORSE_CODE(letter) for letter in words.split(' ')) for words in morse_code.split('  '))

print(decodeBits(test))

# 11 00 11 00 11 00 11 ....
# 000000
# 11 .
# 000000
# 111111 00 11 00 111111 00 111111 -.--
# 00000000000000
# 11 00 111111 00 111111 00 111111
# 000000
# 11 00 11 00 111111
# 000000
# 111111 00 11 00 11
# 000000
# 11