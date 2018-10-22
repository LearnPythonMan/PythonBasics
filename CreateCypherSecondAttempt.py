a = "Hello, World!"
b = 4
#c = "H !e,Wdloollr"
c = 'utD ad!emar aroeeeoPeti t estesvu dcv  xosuiqefa  ninr aadou  !  p t ire t  aeiisilnn  fasieriiuirl s oc. efpakr nsei,spimtrsc,  uim uaeq  ginmaovrpa smcoiie uairu  tennixttisidteeeAeum eneuse msjuonrrirmrs it t eiitomdt oceteep !abaiatoVlpfiui'

d= 'Amet non facere minima iure unde, provident,     veritatis officiis asperiores ipsa eveniet sit! Deserunt     autem excepturi quibusdam iure unde! Porro alias distinctio     ipsam iure exercitationem molestiae. Voluptate fugiat quasi maiores!jk'
e = 49
f = 'noiiiaxsk!nDmaiqeit pi  iesonriea m paet aii s i oried eaimp  saoiiosfr rvteemcecmt njmn  iuxo !u a,l tnaeiuirecu eresde  tnpo  gaof!ti uqsatcaiteedrner ureirp uvuf rAse e,e mstsidia.ttn sfvtteeubVoir t aolmipsle u ssn r  eaerectuiuPdu aoii t m'
g = 'nomuvl tnaeiuirecu eresde  tnpo  gaof!ti uqsatdi iorner ureirp uvuf rAse e,e mstsidia.ttn sfb i!u  itVoir t aolmipsle u ssn r  eaerectuiuPdu a otirs iia teap m aeirnosei  ip tieqiamDn!ksxaioateet,xui  nmjn tmcecmeetvr rfsoiioas  pmiae deiae iec'

import numpy as np

def encode_rail_fence_cipher(string, n):
    x = int(np.ceil(len(string)/(n-1)))
    y = n
    codedMessage = np.full((y,x), '')

    i = j = 0
    for letter in string:
        if j % 2 == 0:
            codedMessage[i][j] = letter
        else:
            codedMessage[n-i-1][j] = letter
        if i == n-2:
            j += 1
            i = 0
        else:
            i += 1

    return ''.join(letter for letter in codedMessage.flatten())

def decode_rail_fence_cipher(string, n):
    x = int(np.ceil(len(string) / (n - 1)))
    y = n
    decodedMessage = np.full((y, x), '')
    tail = len(string)-1 % (n-1)

    i = j = 0
    for letter in string:
        if i == 0 and j % 2 == 0:
            decodedMessage[i][j] = letter
        elif i == n-1 and j % 2 == 1:
            decodedMessage[i][j] = letter
            tail = 1
        else:
            decodedMessage[i][j] = letter

        if tail > 0 and j == x-1:
            i += 1
            tail -= 1
            j = 0
        elif tail == 0 and j == x-2:
            i += 1
            j = 0
        else:
            j += 1

    i = j = 0
    message = ''
    for _ in range(x*y):
        if j % 2 == 0:
            message += decodedMessage[i][j]
        else:
            message += decodedMessage[n-i-1][j]
        if i == n-2:
            j += 1
            i = 0
        else:
            i += 1

    return message

print(encode_rail_fence_cipher(a,b))
print(decode_rail_fence_cipher(c,e))

