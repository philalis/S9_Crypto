from statistics import mean
import matplotlib.pyplot as plt
from sympy import principal_branch
from sympy.physics.units import length

textToDecode = "JRDMCQLEGASNAHSHJEVWAVGJSUDWPNUPELWGUAJFZWQRFXVWMWNNIZZWYFKMCMLIKWVCQUIQW" \
    "GRGHXBYVAXZMRXILQUMGSXIWFWRFGOZWYAWJOQKTBMVVWLVRLVADSMYJIMIJUHSFLMNSHKEVMR" \
    "JNAXPZWYIWHEXWVFWZEZSRPWITLWPBYMQCWTBMVDMUSQWVCMEIFKEGMKIPJITJJEIGTOCJ" \
    "ZBLVELWXRJQIVSXVGRLIUVLHXOOJECZMEMKXHFERBSRPAINYMMEWQOVLINDENBAUHAXE" \
    "NWPVUMTILMBFWVWMWZSMTZAWRRQAQFXRFENBDIFTESMKHHULINXVREINBVIIAKEVWVRUISGKXREI" \
    "AMLIVFZEVLINMWEQRMREISQWGYWFRINSCGYRINSVJTEZUIPWQYALIEWPAKJCCLENIDCFWHEUSRQW" \
    "HETSTNLMEVUISWPIKAXNLMOVKZBMWADWDYWWCWETRLINKWWAWGEAKEVJISXGYEUSNBARHWV" \
    "DIFWPWXTMNSVWFRINSRFGOZW"


dict_letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,"L": 11, "M": 12,
                             "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22,"X": 23, "Y": 24, "Z": 25}
str_number_to_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def calc_IC(text):
    freq = {}
    for i in text:
        freq[i] = freq.get(i, 0) + 1
    IC = 0
    for i in freq:
        IC += freq[i] * (freq[i] - 1)
    IC /= len(text) * (len(text) - 1)
    return IC


def analyze_frq(text):
    freq = {}
    for i in text:
        freq[i] = freq.get(i, 0) + 1/len(text)
    return freq


def sort(dicts):
    ret = []
    for key,value in dicts.items():
        ret.append((key, value))
    ret.sort(key=lambda x: x[1], reverse=True)
    return ret


def decode_text(key, text):
    current_key_index = 0
    new_text = ""
    #new_text2 = ""
    for i in range(len(text)):
        text_value = dict_letter_to_number[text[i].upper()]
        key_value = dict_letter_to_number[key[current_key_index]]
        new_text += str_number_to_letter[ (text_value - key_value) % len(str_number_to_letter) ]
        current_key_index = (current_key_index + 1) % len(key)
    '''for i in range(len(text)//2, len(text)):
        new_text2 += str_number_to_letter[dict_letter_to_number[text[i].upper()] + dict_letter_to_number[key[current_key_index]]]
        current_key_index = (current_key_index + 1) % len(key)
        '''
    return new_text



def decode_with_IC():
    ICs = []
    for i in range(26):
        temp = []
        for j in range(i+1):
            temp.append (calc_IC(textToDecode[j::i + 1]))
        ICs.append([i+1,mean(temp)])
    print("Indice de cohérence du texte initial :", ICs[0][1])
    length_key = min(ICs, key = lambda x : abs(x[1]-0.0778))[0]
    print(length_key)
    #On trouve 21 comme longueur de clé, or ce n'est pas 3, 7 est aussi proche de la bonne fréquence. On suppose donc que la clé est de longueur 7.
    length_key = 7

    freqs = []
    for i in range(length_key):
        tmp = sort(analyze_frq(textToDecode[i::length_key]))
        freqs.append(tmp)
        plt.figure()
        plt.plot(tmp[:][1])
    clef = "ENSEAIS"
    print("Texte décodé :\n" + decode_text(clef,textToDecode))




def decode_with_Kasiski():
    list_diff = []
    previous_value = 0
    for i in textToDecode:
        list_diff.append(dict_letter_to_number[i]-previous_value)
        previous_value = dict_letter_to_number[i]

    all_repetition = {}
    for i in range(len(list_diff)-4):
        all_repetition[(list_diff[i],list_diff[i+1],list_diff[i+2],list_diff[i+3])] = all_repetition.setdefault((list_diff[i],list_diff[i+1],list_diff[i+2],list_diff[i+3]),[])
        all_repetition[(list_diff[i],list_diff[i+1],list_diff[i+2],list_diff[i+3])].append(i)

    actual_repetition = []
    for key,value in all_repetition.items():
        if (len(value) > 1):
            actual_repetition.append((key,value))
            print("\n")
            for i in range(len(value)-1):
                print(textToDecode[value[i]:value[i]+10])
                print("Distance = ", value[i+1] - value[i])
            print(textToDecode[value[i+1]:value[i+1] + 10]) #Python so value of i is kept

    # On regarde les diviseurs des distances (133, 427) => la longueur de la clé est 7.
    # On refait ensuite une analyse par IC pour avoir les valeurs de la clé.

    pass


def main():
    #decode_with_IC()
    decode_with_Kasiski()

if __name__ == '__main__':
    main()


