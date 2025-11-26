from Cryptodome.Hash import SHA1
from Cryptodome.Hash import MD5

def main():
    print('MD5 :')
    for i in [b"ENSEA", b"eNSEA", b"eNSeA", b"EN5EA",] :
        h = MD5.new()
        h.update(i)
        print(str(i) + ', hachage : ' +h.hexdigest())
    print('\nSHA1 :')
    for i in [b"ENSEA", b"eNSEA", b"eNSeA", b"EN5EA",] :
        h = SHA1.new()
        h.update(i)
        print(str(i) + ', hachage : ' +h.hexdigest())
    print()
    text_long = "David comprenait très bien où voulait en venir Prélude. Lorsqu’il l’avait créé, il détestait ce monde. S’il avait eu la possibilité de le changer, il l’aurait certainement fait. Il l’aurait fait en pensé, mais pas en geste. David n’était pas du genre méchant. Jamais il n’aurait fait de mal à qui que ce soit, mais il avait certainement mis cette idée dans la programmation de Prélude sans le vouloir."
    for i in text_long:
        h = MD5.new()
        h.update(bytes(i, 'utf-8'))
    print('Hachage long texte MD5 : ' + h.hexdigest())
    print()
    for i in text_long:
        h = SHA1.new()
        h.update(bytes(i, 'utf-8'))
    print('Hachage long texte SHA1 : ' + h.hexdigest())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
