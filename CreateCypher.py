a = "Hello, World!"
b = 4
c = "H !e,Wdloollr"

d= 'Amet non facere minima iure unde, provident,     veritatis officiis asperiores ipsa eveniet sit! Deserunt     autem excepturi quibusdam iure unde! Porro alias distinctio     ipsam iure exercitationem molestiae. Voluptate fugiat quasi maiores!jk'
e = 49
f = 'noiiiaxsk!nDmaiqeit pi  iesonriea m paet aii s i oried eaimp  saoiiosfr rvteemcecmt njmn  iuxo !u a,l tnaeiuirecu eresde  tnpo  gaof!ti uqsatcaiteedrner ureirp uvuf rAse e,e mstsidia.ttn sfvtteeubVoir t aolmipsle u ssn r  eaerectuiuPdu aoii t m'
g = 'nomuvl tnaeiuirecu eresde  tnpo  gaof!ti uqsatdi iorner ureirp uvuf rAse e,e mstsidia.ttn sfb i!u  itVoir t aolmipsle u ssn r  eaerectuiuPdu a otirs iia teap m aeirnosei  ip tieqiamDn!ksxaioateet,xui  nmjn tmcecmeetvr rfsoiioas  pmiae deiae iec'



def encode_rail_fence_cipher(string, n):
    elements = []
    elementsInOrder = []
    element = ''
    for index, letter in enumerate(string):
        element += letter
        if index % (n - 1) == n - 2 or (index == len(string) - 1 and len(element) > 0):
            elements.append(element)
            element = ''

    for _ in range(n):
         elementsInOrder.append(element)

    for index, element in enumerate(elements):
        if index % 2 == 0:
            for index, letter in enumerate(element):
                elementsInOrder[index] += letter
        else:
            for index, letter in enumerate(element):
                elementsInOrder[n - index - 1] += letter

    return ''.join(element for element in elementsInOrder)


def decode_rail_fence_cipher(string, n):
    elementsAmountwithTile = elementsAmount = len(string) // (n - 1)
    stringTileLenght = len(string) % (n - 1)
    elements = []
    element = ''

    for _ in range(elementsAmount):
        elements.append(element)
    if stringTileLenght > 0:
        elements.append(element)
        elementsAmountwithTile = elementsAmount+1
        stringTileLenght -= 1

    for position in range(elementsAmountwithTile):
        if position % 2 == 0:
            elements[position] += string[0]
            string = string[1:]
        elif len(elements) % 2 == 1:
            elements[len(elements) -1 -position] += string[len(string)-1]
            string = string[0:len(string)-1]
        else:
            elements[len(elements) - position] += string[len(string) - 1]
            string = string[0:len(string) - 1]

    while stringTileLenght > 0:
        for position in range(elementsAmountwithTile):
            if position % 2 == 0:
                elements[position] += string[0]
                string = string[1:]
            else:
                elements[position] = elements[position][0]+string[0] + elements[position][1:]
                string = string[1:]
        stringTileLenght -= 1

    while string != '':
        for position in range(elementsAmount):
            if string == '':
                break
            if position % 2 == 0:
                elements[position] += string[0]
                string = string[1:]
            else:
                elements[position] = elements[position][0]+string[0] + elements[position][1:]
                string = string[1:]

    return ''.join(element for element in elements)


print(encode_rail_fence_cipher(f,e))
print(decode_rail_fence_cipher(f,e))

#  for index, letter in enumerate(string):
#         if index%(2*n-2) == 0:
#             beg += letter
#             mid = mid[::-1]
#             i += 1
#         elif index % (n-1) == 0:
#             end += letter
#             mid = mid[::-1]
#             #i += 1
#         else:
#             mid = mid[:index % (n-1)+i] + letter + mid[index % (n-1)+i:]
#     return beg+mid+end


#print(encode_rail_fence_cipher(a,b))
#print(c)
#print(c == encode_rail_fence_cipher(a,b))

