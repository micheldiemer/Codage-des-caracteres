import charlist

COL_1_PAD = 17


def print_hex_header(p_minval=0, lpad=0):
    print()
    print(" hex: ".rjust(lpad), end="")
    for d in range(4):
        print(f"{(p_minval + d):X}".ljust(16), end="")
        print((" " if d % 2 and d > 0 == 0 else ""), end="")
    print()
    print("hex: ".rjust(lpad), end="")
    for d in range(2):
        print("0123456789ABCDEF0123456789ABCDEF", end=" ")
    print()


def print_charlists():
    list_128_255 = list()
    (list_000_127, list_128_255, legend) = charlist.charlists()

    for z in range(2):
        print()
        for hd in [(" dec:",""),(" hex:","X")]:
    
            print(hd[0].rjust(COL_1_PAD - 1), end="")
            for j in range(2):
                for i in range(8):
                    val = z*16+j*8+i
                    num_str = f"{val:02X}" if hd[1]=="X" else f"{val}"
                    print(num_str.rjust(4), end="")
                print(" ", end="")
            num_str = f"{127:02X}" if hd[1]=="X" else f"{127}"
            print((num_str.rjust(3) if z==1 else ""))
                

        for p in [
            charlist.C_CDS,
            charlist.C_UNC,
            charlist.C_CRT,
            charlist.C_OEM,
            charlist.C_I47,
        ]:
            cpt = 0
            col1 = ("ascii-" if p not in [charlist.C_I47,charlist.C_OEM] else "") + p + ": "
            print(col1.rjust(COL_1_PAD), end="")
            for v in list_000_127[p][z * 16 + 0 : z * 16 + 8]:
                print(v.rjust(3), end=" ")
                cpt = cpt + 1
            print("", end=" ")
            for v in list_000_127[p][z * 16 + 8 : z * 16 + 16]:
                cpt = cpt + 1
                sep = " " if (z==0 or cpt < 16) else list_000_127[p][32]
                print(v.rjust(3), end=sep)


            print(list_000_127[p][33].rjust(3) if z==1 else "")

    for z in range(2):
        print_hex_header(z*4, COL_1_PAD)
        for p in charlist.low_ascii:
            col1 = ("ascii-" if p not in [charlist.C_I47,charlist.C_OEM] else "") + p + ": "
            print(col1.rjust(COL_1_PAD), end="")
            #if z == 1:
            #    pjoin = list_000_127[p][32]
            #    pjoin = pjoin + "".join(list_000_127[p][z * 64 + 1 : z * 64 + 32])
            #else
            pjoin = ""
            if z==0:
                pjoin = "".join(list_000_127[p][z * 64 + 0 : z * 64 + 32])
                pjoin = pjoin + " " + list_000_127[p][32] + "".join(list_000_127[charlist.C_RAW][z * 64 + 33 : z * 64 + 64])
            else:
                pjoin = "".join(list_000_127[charlist.C_RAW][z * 64 + 0 : z * 64 + 32])
                pjoin = pjoin + " " + "".join(list_000_127[charlist.C_RAW][z * 64 + 32 : z * 64 + 64])
            print(pjoin)
            

    for step in range(0, 2):
        print_hex_header((step + 2) * 4, COL_1_PAD)

        for p in charlist.high_ascii:
            if (p == charlist.C_W01 or p == charlist.C_W02) and step > 0:
                continue
            print(("ext-" + p + ": ").rjust(COL_1_PAD), end="")
            minval = step * 64
            print("".join(list_128_255[p][minval : minval + 32]), end=" ")
            minval = minval + 32
            print("".join(list_128_255[p][minval : minval + 32]))

    print()
    print("".rjust(COL_1_PAD - 3) + "Légende")
    print("".rjust(COL_1_PAD - 3) + "-------")
    for litem in legend.items():
        print((litem[0] + " :").rjust(COL_1_PAD), end=" ")
        print(litem[1])


if __name__ == "__main__":
    print_charlists()
