# ESC [ 48 ; 2 ; <r> ; <g> ; <b> m
# 48 ; 5 ; <s> m
# ESC [ 0 m


# for p in [C_OEM, C_O85, C_MAC, C_ISO, C_I15, C_W00, C_W01, C_W02]:
#     print("ext-" + p + ": ")
#     print(set(list_128_255[p]) - manual_allchars)

# '\u2001' : EM QUAD espacement 55 em quad em space 1.0 em fixed width
#            Em also called mutton Quad An em. Also called mutton quad.
#            EM : linear measurement QUAD : linear measurement
# ı i sans point

# print(allchars - manual_allchars)
# out_list = []
# idx_out = -1
# idx_pos = -1
# next_special = False
# for i in fileContent:
#     idx_pos = idx_pos + 1
#     idx_out = idx_out + 1
#     out_list.append(values[i] if not (next_special and i == 13) else ovalues[i])
#     if next_special and i == 13:
#         next_special = False
#     if i == 6:
#         next_special = True

# print("".join(out_list))
