from statistics import mean
import matplotlib.pyplot as plt

textToDecode = "JRDMCQLEGASNAHSHJEVWAVGJSUDWPNUPELWGUAJFZWQRFXVWMWNNIZZWYFKMCMLIKWVCQUIQW" \
    "GRGHXBYVAXZMRXILQUMGSXIWFWRFGOZWYAWJOQKTBMVVWLVRLVADSMYJIMIJUHSFLMNSHKEVMR" \
    "JNAXPZWYIWHEXWVFWZEZSRPWITLWPBYMQCWTBMVDMUSQWVCMEIFKEGMKIPJITJJEIGTOCJ" \
    "ZBLVELWXRJQIVSXVGRLIUVLHXOOJECZMEMKXHFERBSRPAINYMMEWQOVLINDENBAUHAXE" \
    "NWPVUMTILMBFWVWMWZSMTZAWRRQAQFXRFENBDIFTESMKHHULINXVREINBVIIAKEVWVRUISGKXREI" \
    "AMLIVFZEVLINMWEQRMREISQWGYWFRINSCGYRINSVJTEZUIPWQYALIEWPAKJCCLENIDCFWHEUSRQW" \
    "HETSTNLMEVUISWPIKAXNLMOVKZBMWADWDYWWCWETRLINKWWAWGEAKEVJISXGYEUSNBARHWV" \
    "DIFWPWXTMNSVWFRINSRFGOZW"


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

def decode(clef, text):
#TODO



def main():
    ICs = []
    for i in range(26):
        temp = []
        for j in range(i+1):
            temp.append (calc_IC(textToDecode[j::i + 1]))
        ICs.append([i+1,mean(temp)])

    length_key = min(ICs, key = lambda x : abs(x[1]-0.0778))[0]
    print(length_key)
    #On trouve 21 comme longueur de clé, or ce n'est pas 3, 7 est aussi proche de la bonne fréquence.
    length_key = 7

    freqs = []
    for i in range(length_key):
        tmp = sort(analyze_frq(textToDecode[i::length_key]))
        freqs.append(tmp)
        plt.figure()
        plt.plot(tmp[:][1])
    clef = "DMRDAHR"
    decode(textToDecode,clef)
    pass


if __name__ == '__main__':
    main()


