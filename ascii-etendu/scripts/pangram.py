
chars = list("àäâéèêëîïôöùûüÿæçœ«»…’§¶".lower())
chars_needed = set(chars)

pangrams = [
 	"Portez ce vieux whisky au juge blond qui fume",
	"Ma jolie boîte à bijoux, rêve d'exquises parures éthérées.",
	"Joyeux, ivre, un béguin exquis réchauffe deux petits âmes.",
	"Quoi de plus zélé pour l'exquis bruit de la forêt ?",
	"Voix ambiguë d'un cœur qui, au zéphyr, préfère les jattes de kiwis"
	]

pangram = "§ « Vous voyagez où ? — Ça et là, avec joie. Aÿ, Dubaï, Israël, Montparnasse–Bienvenüe. Croiser un æglé dans la forêt ind­ienne & après avoir mangé un Döner ou un kiwi, partir en canoë, c'est plus sûr. Entendre parler le Xârâcùù. Même faire un vœu sur la côte de l’île de Pâques. Éviter les piqûres et le Kärcher… »¶"

cp1252_ymbols = [
    "€ ¢ £ ¤ ¥ ƒ",
    "† ‡ • ­ – — · ™® ¦ § © ª º ° ¶ µ",
    "‚ … · ¡ ¿ ‹ › ‘ ’ „ “ “ ” « » ¸",
    "ˆ ˜ ¨ ¯ ˝ ´ ¸ ",
    "× ± ÷ ‰ ¹ ² ³ ½ ¼ ¾"


chars_pangram = set(list(pangram.lower()))


print((chars_needed.union(set(list(pangrams[0].lower())))) - chars_pangram)
