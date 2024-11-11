# https://int10h.org/oldschool-pc-fonts/fontlistlist/font?ibm_bios
import charlist

COL_WIDTH = 80
DEFAULT_RAW_FILENAME = "test.rawcp437"
DEFAULT_TXT_FILENAME = "test.cp437"
DEFAULT_U8_RFILENAME = "cp437_sample_2_as_utf-8.txt"
DEFAULT_437_WFILENAME = "test.utf8_to_cp437.cp437"


def read_cp437(filename=DEFAULT_TXT_FILENAME):
    print("+----------------------------------------+")
    print("|  READ PYTHON READLINES                 |")
    print("+----------------------------------------+")

    print("read_cp437: ", filename)
    file = open(filename, "r", encoding="cp437")
    lines = file.readlines()

    for line in lines:
        print(line, end="")
    file.close()

    print("+----------------------------------------+")
    print("|  READ BINARY                           |")
    print("+----------------------------------------+")

    (list_000_127, list_128_255, legend) = charlist.charlists()
    cp437 = (
        list_000_127[charlist.C_OEM][:32]
        + list_000_127[charlist.C_RAW][32:128]
        + list_128_255[charlist.C_OEM]
    )
    cp437_file = open(filename, "rb").read()
    # lines = file.readlines()

    out = ""
    size = len(cp437_file)
    for i in range(0, size):
        out += cp437[cp437_file[i]] if cp437_file[i] >= 32 else chr(cp437_file[i])
    print(out)


def python_convert_utf_8_cp437(
    rfilename=DEFAULT_U8_RFILENAME, wfilename=DEFAULT_437_WFILENAME
):
    rfile = open(rfilename, "r", encoding="utf-8")
    wfile = open(wfilename, "w", encoding="cp437")
    lines = rfile.readlines()
    for line in lines:
        wfile.write(line)
    rfile.close()
    wfile.close()

    read_cp437(wfilename)


def read_rawcp437(col_width=COL_WIDTH, filename=DEFAULT_RAW_FILENAME):
    cp437_file = open(filename, "rb").read()
    (list_000_127, list_128_255, legend) = charlist.charlists()
    cp437 = (
        list_000_127[charlist.C_OEM][:32]
        + list_000_127[charlist.C_RAW][32:128]
        + list_128_255[charlist.C_OEM]
    )

    out = ""
    size = len(cp437_file)
    for i in range(0, size):
        out += cp437[cp437_file[i]]

    for i in range(0, (size + col_width - 1) // col_width):
        print(out[i * col_width : i * col_width + col_width])


def write_cp437(wfilename=DEFAULT_TXT_FILENAME):
    lines = [
        # "1234567890123456789012345678901234567890"
        "#A quick brown fox jumps over the lazy",
        " dog.",
        " 0123456789 ¿?¡!`'\"., <>()[]{} &@%*^#$\\/",
        "#* Wieniläinen sioux'ta puhuva ökyzombie",
        " diggaa Åsan roquefort-tacoja.",
        "#* Ça me fait peur de fêter noël là, sur",
        " cette île bizarroïde où une mère et sa",
        "#môme essaient de me tuer avec un gâteau",
        " à la cigüe brûlé.",
        "#* Zwölf Boxkämpfer jagten Eva quer über ",
        " den Sylter Deich." "den Sylter Deich.",
        "#* El pingüino Wenceslao hizo kilómetros",
        " bajo exhaustiva lluvia y frío, añoraba",
        "#a su querido cachorro.",
    ]
    lines2 = [
        " ┌─┬─┐ ╔═╦═╗ ╒═╤═╕ ╓─╥─╖                ",
        " │ │ │ ║ ║ ║ │ │ │ ║ ║ ║                ",
        " ├─┼─┤ ╠═╬═╣ ╞═╪═╡ ╟─╫─╢                ",
        " └─┴─┘ ╚═╩═╝ ╘═╧═╛ ╙─╨─╜                ",
        "                                        ",
        " ░░░░░ ▐▀█▀▌ .·∙  °  ∙·.                ",
        " ▒▒▒▒▒ ▐ █ ▌                            ",
        " ▓▓▓▓▓ ▐▀█▀▌  $ ¢ £ ¥ ₧                 ",
        " █████ ▐▄█▄▌                            ",
        " ⌠               ",
        " │dx ≡ Σ √x²ⁿ·δx ",
        " ⌡               ",
    ]

    encoding_to = "cp437"
    with open(wfilename, "w", encoding=encoding_to) as fw:
        for line in lines + [" "] + [" "] + lines2:
            fw.write(line[1:] + ("\n" if line[0] != "#" else ""))


def write_rawcp437(col_width=COL_WIDTH, wfilename=DEFAULT_RAW_FILENAME):
    encoding_to = "cp437"
    new_filename = wfilename

    lines = [
        # "1234567890123456789012345678901234567890"
        "#A quick brown fox jumps over the lazy",
        " dog.",
        " 0123456789 ¿?¡!`'\"., <>()[]{} &@%*^#$\\/",
        "#* Wieniläinen sioux'ta puhuva ökyzombie",
        " diggaa Åsan roquefort-tacoja.",
        "#* Ça me fait peur de fêter noël là, sur",
        " cette île bizarroïde où une mère et sa",
        "#môme essaient de me tuer avec un gâteau",
        " à la cigüe brûlé.",
        "#* Zwölf Boxkämpfer jagten Eva quer über ",
        " den Sylter Deich." "den Sylter Deich.",
        "#* El pingüino Wenceslao hizo kilómetros",
        " bajo exhaustiva lluvia y frío, añoraba",
        "#a su querido cachorro.",
    ]
    lines2 = [
        " ┌─┬─┐ ╔═╦═╗ ╒═╤═╕ ╓─╥─╖                ",
        " │ │ │ ║ ║ ║ │ │ │ ║ ║ ║                ",
        " ├─┼─┤ ╠═╬═╣ ╞═╪═╡ ╟─╫─╢                ",
        " └─┴─┘ ╚═╩═╝ ╘═╧═╛ ╙─╨─╜                ",
        "                                        ",
        " ░░░░░ ▐▀█▀▌ .·∙░░°░░∙·.                ",  # .·∙•○°○•∙·.
        " ▒▒▒▒▒ ▐ █ ▌                            ",  # ☺☻ ♥♦♣♠ ♪♫☼",
        " ▓▓▓▓▓ ▐▀█▀▌  $ ¢ £ ¥ ₧                 ",
        " █████ ▐▄█▄▌                            ",  # ◄►▲▼ ←→↑↓↕↨←→↑↓↕↨",
        " ⌠               ",
        " │dx ≡ Σ √x²ⁿ·δx ",
        " ⌡               ",
    ]
    pal = ".·∙" + "\x07" + "\x09"
    lines2[5] = (" ░░░░░ ▐▀█▀▌ " + pal + "°" + pal[::-1]).ljust(COL_WIDTH)
    lines2[6] = (
        " ▒▒▒▒▒ ▐ █ ▌"
        + " "
        + "\x01"
        + "\x02"
        + "\x03"
        + "\x04"
        + "\x05"
        + "\x06"
        + " "
        + "\x0D"
        + "\x0E"
        + "\x0F"
    )
    lines2[8] = " █████ ▐▄█▄▌ " + "\x11\x10\x1E\x1F \x1B\x1A\x18\x19\x12\x17"

    cpt = 0
    one_line = ""
    with open(new_filename, "w", encoding=encoding_to) as fw:
        for line in lines + [" "] + [" "] + lines2:
            dowrite = True
            if line[0] == "#":
                one_line = line[1:]
                dowrite = False
            else:
                one_line = (one_line + line[1:]).ljust(COL_WIDTH)
                dowrite = True
            if dowrite:
                fw.write(one_line)
                one_line = ""
                dowrite = False


if __name__ == "__main__":
    col_width = COL_WIDTH
    write_rawcp437(col_width)
    read_rawcp437(col_width)
    write_cp437()
    read_cp437()
    python_convert_utf_8_cp437()
