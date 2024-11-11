import copy

ASCII_0 = "\x00"
ASCII_TAB = "\x09"
ASCII_CR = "\x0A"
ASCII_LF = "\x0D"
ASCII_ESC = "\033"

UNICODE_SHY_HYPHEN_CODE = "\u00AD"
UNICODE_SHY_HYPHEN_CHAR = "­"
UNICODE_EMQUAD_CODE = "\u2001"
UNICODE_EMQUAD_CHAR = " "
UNICODE_NBSP_CODE = "\u00A0"
UNICODE_NBSP_CHAR = " "
UNICODE_BLANK_SYMBOL = "␢"  # U+2422
UNICODE_OPEN_BOX = "␣"  # U+2423
UNICODE_NL = "␤"  # U+2424
UNICODE_SUB_2 = "␦"  # U+2423 ISO 2047 SUB
UNICODE_DEL_2 = "␥"  # U+2425			␦
UNICODE_FRACTION_SLASH_CODE = "\u2044"
UNICODE_FRACTION_SLASH_CHAR = "⁄"
UNICODE_APPLE_LOGO_CODE = "\uF8FF"
UNICODE_APPLE_LOGO_CHAR = ""  # "\uF8FF"
UNICODE_DOUBLE_HYPHEN_CHAR = "⹀"  # "\u2E40" DOUBLE HYPHEN
UNICODE_DOUBLE_HYPHEN_CODE = "\u2E40"  # "\u2E40" DOUBLE HYPHEN
UNICODE_APPLE_EMOJI = "🍎︎"
UNICODE_ONE_TENTH = "⅒"

ISO_2047_SPACE = "△"
ISO_2047_TAB = "⪫"
ISO_2047_CR = "⪪"
ISO_2047_LF = "≡"

MAC_ROMAN_APPLE_CODE = 0xF0
MAC_ROMAN_FRACTION_SLASH_CODE = 0xDA


FRACTION_SLASH_REPLACE = UNICODE_ONE_TENTH  # ⅒
APPLE_LOGO_REPLACE = "☼"  # OEM ASCII 15 SUN
SHY_HYPHEN_REPLACE = UNICODE_DOUBLE_HYPHEN_CHAR  # ⹀
TAB_REPLACE = "␉"
NBSP_REPLACE = UNICODE_OPEN_BOX  # "␣"

C_RAW = "raw"
C_MLW = "mac-lowascii"
C_CDS = "codes"
C_CRT = "caret"

C_UNC = "unicode"
C_OEM = "cp437"
C_I47 = "iso-2047"

C_O85 = "cp850"
C_MAC = "mac-roman"
C_ISO = "iso-8859-1"
C_I15 = "iso-8859-15"
C_W00 = "cp1252"
C_W01 = "cp1252_ext"
C_W02 = "cp1252_mix"


low_ascii = [C_OEM, C_UNC]
high_ascii = [C_OEM, C_O85, C_MAC, C_ISO, C_I15, C_W00, C_W01]


def charlists():
    cp1252_unused = [0x81, 0x8D, 0x8F, 0x90, 0x9D]

    charlist = {}

    charlist[C_MLW] = ["HT", "CR", "LF"]

    charlist[C_RAW] = list(
        ""
        + "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
        + "\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F"
        + " !\"#$%&'()*+,-./0123456789:;<=>?"
        + "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"
        + "`abcdefghijklmnopqrstuvwxyz{|}~ \x7F"
    )
    charlist[C_CDS] = [
        "NUL",
        "SOH",
        "STX",
        "ETX",
        "EOT",
        "ENQ",
        "ACK",
        "BEL",
        "BS",
        "HT",
        "LF",
        "VT",
        "FF",
        "CR",
        "SO",
        "SI",
        "DLE",
        "DC1",
        "DC2",
        "DC3",
        "DC4",
        "NAK",
        "SYN",
        "ETB",
        "CAN",
        "EM",
        "SUB",
        "ESC",
        "FS",
        "GS",
        "RS",
        "US",
        " ",
        "DEL"
    ]

    charlist[C_I47] = list("⎕⌈⊥⌋⌁⊠✓⍾⤺⪫≡⩛↡⪪⊗⊙⊟◷◶◵◴⍻⎍⊣⧖⍿␦⊖◰◱◲◳△▨")
    charlist[C_UNC] = list("␀␁␂␃␄␅␆␇␈␉␊␋␌␍␎␏␐␑␒␓␔␕␖␗␘␙␚␛␜␝␞␟ ␡")
    charlist[C_OEM] = list(" ☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ ⌂")
    charlist[C_CRT] = list("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^")

    charlist[C_CRT] = list("^" + c for c in charlist[C_RAW][64:96]) + [" ","^?"]

    list_128_255 = {}
    list_128_255[C_RAW] = list(range(128, 256))
    list_128_255[C_OEM] = list(
        ""
        + "ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒ"
        + "áíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐"
        + "└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀"
        + "αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■␣"
    )
    # NBSP ␣
    list_128_255[C_O85] = list(
        ""
        + "ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒ"
        + "áíóúñÑªº¿®¬½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐"
        + "└┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀"
        + "ÓßÔÒõÕµþÞÚÛÙýÝ¯´­±‗¾¶§÷¸°¨·¹³²■␣"
    )
    list_128_255[C_MAC] = list(
        ""
        + "ÄÅÇÉÑÖÜáàâäãåçéèêëíìîïñóòôöõúùûü"
        + "†°¢£§•¶ß®©™´¨≠ÆØ∞±≤≥¥µ∂∑∏π∫ªºΩæø"
        + "¿¡¬√ƒ≈∆«»…␣ÀÃÕŒœ–—“”‘’÷◊ÿŸ⅒€‹›ﬁﬂ"
        + "‡·‚„‰ÂÊÁËÈÍÎÏÌÓÔÒÚÛÙıˆ˜¯˘˙˚¸˝˛ˇ"
    )
    #  FRACTION_SLASH 7⁄8 ／ ⅞ ⅞ 7⁄8 --> ⅒
    #  APPLE_LOGO
    list_128_255[C_MAC][MAC_ROMAN_APPLE_CODE - 128] = APPLE_LOGO_REPLACE
    list_128_255[C_MAC][MAC_ROMAN_FRACTION_SLASH_CODE - 128] = FRACTION_SLASH_REPLACE

    # ⹀ SHY_HYPHEN
    list_128_255[C_ISO] = list(
        "^" * 32
        + "␣¡¢£¤¥¦§¨©ª«¬⹀®¯°±²³´µ¶·¸¹º»¼½¾¿"
        + "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"
        + "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
    )
    list_128_255[C_I15] = list(
        "".join(list_128_255[C_ISO][:32])
        + "␣¡¢£€¥Š§š©ª«¬⹀®¯°±²³Žµ¶·ž¹º»ŒœŸ¿"
        + "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"
        + "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
    )
    list_128_255[C_W00] = list(
        ""
        + "€ ‚ƒ„…†‡ˆ‰Š‹Œ Ž  ‘’“”•–—˜™š›œ žŸ"
        + "␣¡¢£¤¥¦§¨©ª«¬⹀®¯°±²³´µ¶·¸¹º»¼½¾¿"
        + "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"
        + "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
    )

    list_128_255["cp1252_ext"] = list(
        ""
        + "○■↑↓→←║═╔╗╚╝░▒►◄"
        + "│─┌┐└┘├┤┴┬♦┼█▄▀▬"
        + "                "
        + "                "
    )

    list_128_255[C_W02] = copy.copy(list_128_255[C_W00])
    for i in cp1252_unused:
        j = i - 128
        list_128_255[C_W00][j] = " "
        list_128_255[C_W02][j] = list_128_255[C_W01][j]

    allchars = {" "}
    for name, lcharlist in charlist.items():
        allchars |= set(lcharlist)
    for name, lcharlist in list_128_255.items():
        allchars |= set(lcharlist)
    allchars |= set({"\xa0", "🍎︎", "⁄", "\uf8ff"})

    manual_allchars = set()
    manual_allchars |= set(range(128, 256))
    manual_allchars |= set(charlist[C_RAW])
    manual_allchars |= set(charlist[C_I47])
    manual_allchars |= set(charlist[C_CRT])
    manual_allchars |= set(charlist[C_CDS])
    manual_allchars |= set(charlist[C_MLW])

    manual_allchars |= set(list("␀␁␂␃␄␅␆␇␈␉␊␋␌␍␎␏␐␑␒␓␔␕␖␗␘␙␚␛␜␝␞␟␡"))
    manual_allchars |= set(list("☺☻♥◊♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼⌂"))
    manual_allchars |= set(list("!\"#$%&'()*+,-./0123456789:;<=>?"))
    manual_allchars |= set(list(" "))
    manual_allchars |= set(list("ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÒÓÔÕÖŒÙÚÛÜÝŸ"))
    manual_allchars |= set(list("àáâãäåæçèéêëìíîïòóôõöœùúûüýÿ"))
    manual_allchars |= set(list("⌐¬≠×÷√ƒ≈∆÷⅒ΓπΣασµτΦΘΩ∂δ∞φε∩≡±≥≤⌠⌡÷≈¹²³½¼¾∏∫‰∑∏ⁿ"))
    manual_allchars |= set(list("£ƒ¤€¥₧¢©®™") + [UNICODE_APPLE_EMOJI])
    manual_allchars |= set(list("ŠšŽžÞß¿¡øðñþﬁﬂÑÐØı"))
    manual_allchars |= set(list("¸¨ˆ˜¯˘˙˚˝˛ˇ´ "))
    manual_allchars |= set(list("«»…–—„“”‘’‚‘‹›¶°·∙␣‗ªº†‡¦­"))
    manual_allchars |= set(list("│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌"))
    manual_allchars |= set(list("■█▄▌▐▀░▒▓"))
    manual_allchars |= set(
        [
            UNICODE_SHY_HYPHEN_CODE,
            SHY_HYPHEN_REPLACE,
            UNICODE_NBSP_CODE,
            NBSP_REPLACE,
            UNICODE_FRACTION_SLASH_CODE,
            FRACTION_SLASH_REPLACE,
            UNICODE_APPLE_LOGO_CODE,
        ]
    )

    if allchars - manual_allchars:
        raise Exception("allchars - manual_allchars", allchars - manual_allchars)

    if manual_allchars - allchars:
        raise Exception("manual_allchars - allchars", manual_allchars - allchars)

    if manual_allchars != allchars:
        raise Exception("manual_allchars != allchars")

    str1 = "FRACTION_SLASH (mac-roman) "
    str1 = str1 + "oO " + UNICODE_FRACTION_SLASH_CHAR + "Oo ½¼"
    str2 = "LOGO APPLE (mac-roman) oO " + UNICODE_APPLE_LOGO_CHAR + " Oo"
    str3 = "SHY HYPHEN TRAIT D'UNION DISCRET +oO" + UNICODE_SHY_HYPHEN_CHAR + "Oo"
    str4 = "NBSP (espace insécable) oO" + UNICODE_NBSP_CHAR + "Oo"
    str5 = "ISO C1 CONTROL"
    legend = {
        " ": "POSITION NON DÉFINIE",
        FRACTION_SLASH_REPLACE: str1,
        APPLE_LOGO_REPLACE: str2,
        SHY_HYPHEN_REPLACE: str3,
        NBSP_REPLACE: str4,
        "^^^^": str5
    }

    return charlist, list_128_255, legend
