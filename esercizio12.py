def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return("0" * (32 - l)) + b


def main ():
    address = "10.172.23.57"

    groups = address.split(".")

    groups = [int(group) for group in groups]
    groupsBin = [bin(group) for group in groups]#stampa anche '0b' per indicare che è un numero binario

    print(groups)
    print(groupsBin)
    print(completa8bit(groupsBin[3]))

    groups_strbin = [completa8bit(strbin) for strbin in groupsBin]
    print(groups_strbin)

    print(".".join(groups_strbin))

if __name__ == "__main__":
    main()