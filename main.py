from Cryptodome.Hash import SHA1
from Cryptodome.Hash import MD5

def main():
    for i in [b"ENSEA", b"eNSEA", b"eNSeA", b"EN5EA"] :
        h = MD5.new()
        h.update(i)
        print(h.hexdigest())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
