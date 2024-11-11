
for c in ['€','🇫🇷','😀','👩‍❤️‍👨','👨🏼‍❤️‍👩🏿']:
    print(c)
    for encoding in (#'cp1252','iso8859-15','macroman'
                    'utf_8'
                    ,'utf_16_be'
                    ,'utf_32_be'
                    #,'utf_16','utf_16_be','utf_16_le'
                    #,'utf_32'
                    #,'utf_32_le'
                    ):
        print(encoding,c.encode(encoding))
