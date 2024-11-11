# ASCII étendu

Le codage ASCII est un codage sur 7 bits, pour les positions 0 à 127. 1 octet utilise 8 bits. Un codage ASCII étendu reprend le codage ASCII et définit les caractères correspondant aux codes 128 à 255.

Les principaux codages ASCII étendus utilisés actuellement :

- `ISO 8859-1`, par défaut sous Linux. Caractères absents : `€ Œ œ Ÿ`.
- `ISO 8859-15`, variante qui comprend les caractères suivants : `€ Œ œ Ÿ`
- `ANSI` ou `windows-1252` ou `cp1252` : jeu de caractères proche de ISO 8859-1. Très utilisé. Comprend presque tous les caractères utiles pour la typographie en langue française, y compris certains absents des normes ISO `•…†‡‰`, tiret demi-cadratin `–`, tiret cadratin `—` (exceptions : `U+202F` espace insécable étroite, pied-de-mouche `¶`).
- `cp1252` et `ISO 8859-1/ISO 8859-15` : sauf pour les caractères `Š,Œ,Ž,Ÿ`, le code de la lettre minuscule correspond au code de la lettre majuscule plus 32 (bit 5 à 0 ou 1), comme pour le codage ASCII.
- `437` : jeu de caractères par défaut dans les ancienes BIOS
- `850` : jeu de caractères français toujours utilisé dans Widnows

masOS est passé à Unicode et avant cela utilisait `macRoman`.

## Caractères

Tables de caractère ascii étendu, position `80 (128)` à `FF (255)`, selon les encodages `cp437`, `cp850`·, `windows-1252`, `iso 8859-1` et `iso 8859-15`.

```txt
            hex: 8               9                A               B
            hex: 0123456789ABCDEF0123456789ABCDEF 0123456789ABCDEF0123456789ABCDEF
      ext-cp437: ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜ¢£¥₧ƒ áíóúñÑªº¿⌐¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐
      ext-cp850: ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒ áíóúñÑªº¿®¬½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¢¥┐
 ext-iso-8859-1: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ␣¡¢£¤¥¦§¨©ª«¬⹀®¯°±²³´µ¶·¸¹º»¼½¾¿
ext-iso-8859-15: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ␣¡¢£€¥Š§š©ª«¬⹀®¯°±²³Žµ¶·ž¹º»ŒœŸ¿
     ext-cp1252: € ‚ƒ„…†‡ˆ‰Š‹Œ Ž  ‘’“”•–—˜™š›œ žŸ ␣¡¢£¤¥¦§¨©ª«¬⹀®¯°±²³´µ¶·¸¹º»¼½¾¿

            hex: C               D                E               F
            hex: 0123456789ABCDEF0123456789ABCDEF 0123456789ABCDEF0123456789ABCDEF
      ext-cp437: └┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀ αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡÷≈°∙·√ⁿ²■␣
      ext-cp850: └┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀ ÓßÔÒõÕµþÞÚÛÙýÝ¯´-­±‗¾¶§÷¸°¨·¹³²■␣
 ext-iso-8859-1: ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
ext-iso-8859-15: ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
     ext-cp1252: ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
```

## Quelques détails

`␣` représente un `espace insécable`

### Table de conversion caractère --> code

| Caractère | CP850 | windows-1252 | iso 8859-15 | utf-8    |
|-----------|-------|--------------|-------------|----------|
| **é**     | 82    | E9           | E9          | C3 A9    |
| **¤**     | CF    | A4           |             | C2 A4    |
| **€**     |       | 80           | A4          | E2 82 AC |
| **␣**     | FF    | A0           | A0          | C2 A0    |

> Le code hexadécimal du caractère `é` est `82` en `CP850`, `E9` en windows-1252 et `C3 A9` en `utf-8`.

### Table de conversion code --> caractère

| CODE | CP850 | windows-1252 | iso 8859-15 |
|------|-------|--------------|-------------|
| 80   | Ç     | €            | ?           |
| 82   | é     | ‚            | ?           |
| A0   | á     | ␣            | ␣           |
| A4   | ñ     | ¤            | €           |
| CF   | ¤     | Ï            | Ï           |
| E9   | Ú     | é            | é           |
| FF   | ␣     | ÿ            | ÿ           |

> Le code hexadécimal `82` qui correspond au caractère `é` en `CP850` correspond au caractère `‚`
> (Guillemet-Virgule inférieur, `U+201A`) en `windows-1252` et n'est pas défini en `iso 8859-15`.
>
> Le code hexadécimal `E9` qui correspond au caractère `é` en `windows-1252` correspond au caractère `Ú`  en `cp850`.

### Table de conversion codes utf-8 --> caractère

| CODE     | utf-8 | CP850 | windows-1252 | iso 8859-15 |
|----------|-------|-------|--------------|-------------|
| C2 A0    | ␣     | ┬á    | Â␣           | â?          |
| C2 A4    | ¤     | ┬ñ    | Â€           | Â           |
| C3 A9    | é     | ├®    | Ã©           | Ã©          |
| E2 82 AC | €     | Ôé¼   | â‚¬          | â?¬         |
