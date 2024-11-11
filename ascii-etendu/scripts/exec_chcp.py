import os


def print_bytes_with_chcp():
    if os.name != "nt":
        print("This script is for Windows only.")
        return

    print("+--------------------------------------------+")
    print("| Affichage de caractères binaires avec chcp |")
    print("+--------------------------------------------+")
    print()
    os.system("chcp 850 > nul")

    __hex_digits__ = "0123456789ABCDEF"
    __header__ = __hex_digits__ * 2 + " " + __hex_digits__ * 2

    octets_32_63 = bytes(range(32, 64))
    octets_64_95 = bytes(range(64, 96))
    octets_96_126 = bytes(range(96, 127))
    print("         hex:", __header__)
    print("  ascii 0-63:", " " * 32, octets_32_63.decode("ascii"))
    print()
    print("ascii 64-126:", octets_64_95.decode("ascii"), octets_96_126.decode("ascii"))

    octets_128_159 = bytes(range(128, 160))
    octets_128_159_1252 = bytes(
        [128, 63]
        + list(range(130, 141))
        + [63, 142, 63, 63]
        + list(range(145, 157))
        + [63, 158, 159]
    )
    octets_160_191 = bytes(range(160, 192))
    octets_192_223 = bytes(range(192, 224))
    octets_224_255 = bytes(range(224, 255))

    os.system("chcp 437 > nul")
    print(
        "       cp437:",
        octets_128_159.decode("cp437"),
        octets_160_191.decode("cp437"),
    )
    os.system("chcp 850 > nul")
    print(
        "       cp850:",
        octets_128_159.decode("cp850") + "",
        octets_160_191.decode("cp850"),
    )
    os.system("chcp 1252 > nul")
    print(
        "      cp1252:",
        octets_128_159_1252.decode("cp1252"),
        octets_160_191.decode("cp1252"),
    )
    os.system("chcp 10000 > nul")
    print(
        "   mac-roman:",
        octets_128_159.decode("mac-roman"),
        octets_160_191.decode("mac-roman"),
    )
    os.system("chcp 28591 > nul")
    print("  iso-8859-1:", end="")
    print(" " * 32, end="")
    print(octets_160_191.decode("iso-8859-1"))

    os.system("chcp 28605 > nul")
    print("  iso-8859-1:", end="")
    print(" " * 32, end="")
    print(octets_160_191.decode("iso-8859-15"))

    print()

    print("         hex:", __header__)
    os.system("chcp 437 > nul")
    print(
        "       cp437:",
        octets_192_223.decode("cp437") + "",
        octets_224_255.decode("cp437"),
    )
    os.system("chcp 850 > nul")
    print(
        "       cp850:",
        octets_192_223.decode("cp850") + "",
        octets_224_255.decode("cp850"),
    )
    os.system("chcp 1252 > nul")
    print(
        "      cp1252:",
        octets_192_223.decode("cp1252"),
        octets_224_255.decode("cp1252"),
    )
    os.system("chcp 10000 > nul")
    print(
        "   mac-roman:",
        octets_192_223.decode("mac-roman"),
        octets_224_255.decode("mac-roman"),
    )
    os.system("chcp 28591 > nul")
    print(
        "  iso-8859-1:",
        octets_192_223.decode("iso-8859-1"),
        octets_224_255.decode("iso-8859-1"),
    )
    os.system("chcp 28605 > nul")
    print(
        " iso-8859-15:",
        octets_192_223.decode("iso-8859-15"),
        octets_224_255.decode("iso-8859-15"),
    )


if __name__ == "__main__":
    print_bytes_with_chcp()
