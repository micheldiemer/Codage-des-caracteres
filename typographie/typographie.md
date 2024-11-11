---
title: "Typographie"
author:
  - Michel Diemer
date: 2022-07-10
keywords:
  - Unicode
  - Tiret
      - Espace
  - Caractère
  - Émoji
lang: fr-FR
papersize: a4
geometry: margin=1in
toc: true
toc-depth: 3.0
pagenumbering: true
...

# Typographie

## Lettres de la langue française

`ABCDEFGHIJKLMNOPQRSTUVWXYZ ÀÂÄ Ç ÉÈÊË ÎÏ ÔÖ ÙÛÜ Ÿ Æ Œ espace - '`  
`abcdefghijklmnopqrstuvwxyz àâä ç éèêë îï ôö ùûü ÿ æ œ espace - '`  
`pas d'espace ni avant ni après -`  
`pas d'espace multiples`  
Cf. [Insee ChaineFrancaisOfficielMajuscule](https://xml.insee.fr/schema/commun.html#ChaineFrancaisOfficielMajuscule_stype)  
Nb : le `ñ Ñ` ne fait pas officiellement partie des signes diacritiques de la langue française.  
Il n'est plus autorisé dans les noms de famille.

## Typographie langue française

`symboles de ponctuation , ; : . … ? ! « » ( ) [ ] * / - ’`  
`trait d'union - tiret demi-cadratin  Oo–Oo tiret cadratin  Oo—Oo`  
`espace          espace demi-cadratin Oo Oo espace cadratin Oo Oo`  
`trait d'union conditionnel - U+00AD : « malaise » se coupe en mal-aise (nm) ou en ma-laise (nf)`  
`trait d'union insécable - U+2011 ‑`  
`espace fine insécable U+202F Oo Oo espace insécable Oo Oo`  
`numéro = Nº qui est comme un o exposant, différent de degré °`  
`degré ° et aussi ℃ ℉ K`  
`# † ‡ ‘ ’ • § ™ © ® µ ¶`  
`% @ + - * / \ < > = ² × ÷ ¼ ½ ¾ ‰ _ ¤ $ £ ƒ`  
`↉ ⅟ ½ ⅓ ¼ ⅕ ⅙ ⅐ ⅛ ⅑ ⅒ ⅔ ⅖ ¾ ⅗ ⅜ ⅘ ⅚ ⅝ ⅞ % ‰ ‱`  
`“” «» ‘’ ‚‛ ‹›`

Ressources

- [Wikipedia Ponctuation en français](https://fr.wikipedia.org/wiki/Ponctuation#En_fran%C3%A7ais)
- [Caractères et symboles Unicode](http://david.carella.free.fr/fr/typographie/caracteres-et-symboles-unicode.html)

## Indicateur ordinal

- 1<sup>er</sup> 2<sup>e</sup> 2<sup>d</sup> 2<sup>de</sup> 1<sup>ers</sup> 1<sup>res</sup> 2<sup>es</sup> 2<sup>ds</sup>
- `U+00BA º` MASCULINE ORDINAL INDICATOR (&ordm;) `1º 2º 3º`
- `U+00AA ª` FEMININE ORDINAL INDICATOR (&ordf;)
- Different from
  - `U+00B0 °` DEGREE SIGN
  - `U+02DA ˚` RING ABOVE
  - `U+1D52 ᵒ` MODIFIER LETTER SMALL O
  - `U+1D3C ᴼ` MODIFIER LETTER CAPITAL O
  - `U+2070 ⁰` SUPERSCRIPT ZERO
  - `U+1D43 ᵃ` MODIFIER LETTER SMALL A

## Mathématiques

### Symboles courants

- `+ - / \* =
- `+ ‒ ÷ × = ¬ ≊ ≅ ≈ > ≥ < ≤ ∞ ∑ ∏ ≠ √ ∛ ∜ 𝜋 𝛑 ± ǁ`
- `− (U+2212 MINUS SIGN)` ne pas confondre avec `‒ (U+2012 FIGURE DASH/TIRET NUMÉRIQUE)`
- `≡ ≢ ⩵ ⩶ ∥ ∦ ∟ ⊾ ∠ ∡ ∢ ⟀`
- `⊕ (XOR) ⇒ ⇔`
- `⁄ (U+2044 FRACTION BAR) ⌖ ∧ ∨`
- `∩ ∪ ∋ ∌ ∅ ∖ ∄ ∃ ∈ ∉ ∀ ⊂ ⊃ ⊄ ⊅`
- `⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁿ`
- `ℕ ℤ ⅅ ℚ ℝ ℂ ℍ ℙ 𝕊`
- `ℯ ⅇ ℇ ᵠ 𝜑 ⅈ ⅉ ∞ 𝞅`
- `∏ ∑ 𝛌 𝜆 𝝀 𝓍 𝒳 𝑓 𝑦 ∫ ∬ ∭ ε |`
- `𝑦 = 𝑓(𝓍)`
- `｜𝓍｜ U+FF5C`

### Codes Unicode

- `× U+00D7` multiply
- `÷ U+00F7` divide
- `− U+2212` minus sign
- `∗ U+2217` asterisk operator
- `⁄ U+2044` barre de fraction
- `≈ U+2248` Presque égal à
- `≃ U+2243` Asymptotiquement égal à
- `𝜋 U+1D70B` [Mathematical Italic Small Pi](<https://en.wikipedia.org/wiki/Pi_(letter)>)
- `𝛑 U+1D6D1` Mathematical Bold Small Pi
- `π U+03C0`
- `ℯ U+212F` Euler number
- `ℇ U+2107` Euler constant
- `ⅈ U+2148`
- `φ U+03D5` [Greek Phi Symbol](https://en.wikipedia.org/wiki/Phi)
- `∞ U+221E`

Cf. [Unicode Symbole mathématique](https://www.compart.com/fr/unicode/category/Sm)

### Chiffres romains

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 50 | 100 |
|---|---|---|---|---|---|---|---|---|----|----|----|----|-----|
| Ⅰ | Ⅱ | Ⅲ | Ⅳ | Ⅴ | Ⅵ | Ⅶ | Ⅷ | Ⅸ | Ⅹ  | Ⅺ  | Ⅻ  | Ⅼ  | Ⅽ   |
| ⅰ | ⅱ | ⅲ | ⅳ | ⅴ | ⅵ | ⅶ | ⅷ | ⅸ | ⅹ  | ⅺ  | ⅻ  | ⅼ  | ⅽ   |

| 500  | 1 000   | 5 000    | 10 000     | 50 000    | 100 000      |
|------|---------|----------|------------|-----------|--------------|
| Ⅾ ⅠↃ | Ⅿ ⅭⅠↃ ↀ | ↁ ⅠↃↃ V̅ | ↂ ⅭⅭⅠↃↃ X̅ | ↇ ⅠↃↃↃ L̅ | ↈ ⅭⅭⅭⅠↃↃↃ C̅ |
| ⅾ ⅰↄ | ⅿ ⅽⅰↄ ↀ | ↁ ⅰↄↄ v̅ | ↂ ⅽⅽⅰↄↄ x̅ | ↇ ⅰↄↄↄ l̅ | ↈ ⅽⅽⅽⅰↄↄↄ c̅ |


## Tirets et espaces

### Tirets–traits d'union

| Caractère                           | Symbole | Unicode       | HTML               |
|-------------------------------------|---------|---------------|--------------------|
| trait d’union / signe moins / tiret | Oo-Oo   | U+002D        | \&#x2D;            |
| trait d'union conditionnel          | Oo-­-Oo | U+00AD        | \&#xAD;            |
| trait d’union                       | Oo‐Oo   | U+2010        | \&#x2010;          |
| trait d’union insécable             | Oo‑Oo   | U+2011        | \&#x2011;          |
| tiret numérique / figure dash       | Oo‒Oo   | U+2012        | \&#x2012;          |
| tiret demi-cadratin ou tiret moyen  | Oo–Oo   | U+2013        | \&#x2013;          |
| tiret cadratin ou tiret long        | Oo—Oo   | U+2014        | \&#x2014;          |
| tiret double cadratin               | Oo⸺Oo   | U+2E3A        | \&#x2E3A;          |
| tiret triple cadratin               | Oo⸻Oo   | U+2E3B        | \&#x2E3B;          |
| barre horizontale                   | Oo―Oo   | U+2015        | \&#x2015;          |
| puce trait d’union                  | Oo⁃Oo   | U+2043        | \&#x2043;          |
| signe moins                         | Oo−Oo   | U+2212        | \&#x2212;          |
| filet horizontal                    | Oo─Oo   | U+2500        | \&#x2500;          |
| filet horizontal double             | Oo──Oo  | U+2500,U+2500 | \&#x2500;\&#x2500; |
| Tiret cadratin minuscule            | O﹘Oo    | U+FE58        | \&#xFE58;          |
| Tiret minuscule                     | O﹣Oo    | U+FE63        | \&#xFE63;          |
| Tiret pleine chasse                 | Oo－Oo   | U+FF0D        | \&#xFF0D;          |

Source :

- [Tiret](https://www.compart.com/fr/unicode/category/Pd)
- [Tiret - Wikipedia](https://fr.wikipedia.org/wiki/Tiret)
- [Dash = Tiret](https://en.wikipedia.org/wiki/Dash)
- [Trait d’Union - Wikipedia](https://fr.wikipedia.org/wiki/Trait_d%27union)
- [Hyphen = Trait d’Union](https://en.wikipedia.org/wiki/Hyphen)
- [Signe Plus et Moins](https://fr.wikipedia.org/wiki/Signes_plus_et_moins)
- [Plus Minus sign](https://en.wikipedia.org/wiki/Plus_and_minus_signs)

#### Trait d'union conditionnel : exemple

##### anticonstitutionnellement

anticonstitutionnellement anticonstitutionnellement anticonstitutionnellement anticonstitutionnellement
anticonstitutionnellement anticonstitutionnellement anticonstitutionnellement anticonstitutionnellement
anticonstitutionnellement anticonstitutionnellement anticonstitutionnellement anticonstitutionnellement

##### anti-consti-tution-nellemement

anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement anti­consti­tution­nellement

##### a-n-t-i-c-o-n-s-t-i-t-u-t-i-o-n-n-e-l-l-e-m-e-m-e-n-t

a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­ a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­ a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­ a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­ a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­ a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­
a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­ a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­
a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­ a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­
a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­ a­n­t­i­c­o­n­s­t­i­t­u­t­i­o­n­n­e­l­l­e­m­e­n­t­

### Espaces

| Caractère                      | Symbole | Unicode      | HTML           | Description                                                                                                                                                                                                |
|--------------------------------|---------|--------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tabulation                     | Oo Oo   | U+0009       | \&tab;         |                                                                                                                                                                                                            |
| line feed                      | ⸻LF     | U+000A       |                |                                                                                                                                                                                                            |
| line tabulation / vertical tab | ⸻VT     | U+000B       |                |                                                                                                                                                                                                            |
| form feed                      | ⸻FF     | U+000C       |                |                                                                                                                                                                                                            |
| carriage return                | —CR LF  | U+000D       |                |                                                                                                                                                                                                            |
| CR LF                          | -CRLF   | U+000DU+000A |                |                                                                                                                                                                                                            |
| next line                      | ⸻NEL    | U+0085       |                |                                                                                                                                                                                                            |
| espace                         | Oo Oo   | U+0020       |                | espace normale, espace sécable, dite aussi « espace-mot »                                                                                                                                                  |
| espace insécable               | Oo Oo   | U+00A0       | \&nbsp;        | no-break space en anglais, pour espace insécable.                                                                                                                                                          |
| ogham space mark               | Oo Oo   | U+1680       |                | Used for interword separation in Ogham text. Normally a vertical line in vertical text or a horizontal line in horizontal text, but may also be a blank space in "stemless" fonts. Requires an Ogham font. |
| en quad                        | Oo Oo   | U+2000       |                | équivalent à U+2002                                                                                                                                                                                        |
| em quad                        | Oo Oo   | U+2001       |                | équivalent à U+2003                                                                                                                                                                                        |
| espace demi-cadratin           | Oo Oo   | U+2002       | \&ensp;        |                                                                                                                                                                                                            |
| espace cadratin                | Oo Oo   | U+2003       | \&emsp;        | de la largeur d’un M, normalement, \&#x2003; (ou \&#8195;)                                                                                                                                                 |
| 1⁄3 cadratin                   | Oo Oo   | U+2004       | \&emsp13;      |                                                                                                                                                                                                            |
| 1⁄4 cadratin                   | Oo Oo   | U+2005       | \&emsp14;      |                                                                                                                                                                                                            |
| 1⁄6 de cadratin                | Oo Oo   | U+2006       |                |                                                                                                                                                                                                            |
| figure space                   | Oo Oo   | U+2007       | \&numsp;       | Figure space. In fonts with monospaced digits, equal to the width of one digit. HTML/XML named entity:                                                                                                     |
| punctuation space              | Oo Oo   | U+2008       | \&numsp;       | As wide as the narrow punctuation in a font, i.e. the advance width of the period or comma.\[2\] HTML/XML named entity:                                                                                    |
| espace fine sécable            | Oo Oo   | U+2009       | \&thinsp;      | thin space en anglais                                                                                                                                                                                      |
| espace ultra-fine              | Oo Oo   | U+200A       | \&hairsp;      |                                                                                                                                                                                                            |
| line separator                 | ⸻       | U+2028       |                |                                                                                                                                                                                                            |
| paragraph separator            | ⸻       | U+2029       |                |                                                                                                                                                                                                            |
| espace fine insécable          | Oo Oo   | U+202F       | \&nnbsp;       | espace insécable étroite dans la traduction française d’Unicode ; Narrow Non Breaking Space                                                                                                                |
| medium mathematical space      | Oo Oo   | U+205F       | \&mediumSpace; | Used in mathematical formulae. Four-eighteenths of an em.                                                                                                                                                  |
| ideographic space              | Oo 　 Oo | U+3000       |                | As wide as a CJK character cell (fullwidth). Used, for example, in tai tou.                                                                                                                                |
| espace, symbole 1              | Oo␢Oo   | U+2422       |                | Ce glyphe est une représentation visuelle, utilisée lorsque l'on souhaite matérialiser graphiquement une espace. Nommé en Unicode symbole visuel pour l'espace (ou blank symbol, en anglais).              |
| espace, symbole 2              | Oo␣Oo   | U+2423       | \&blank;       | Ce glyphe est une représentation visuelle, utilisée lorsque l'on souhaite matérialiser graphiquement une espace. Nommé en Unicode boîte ouverte (ou open box, en anglais)                                  |

Pour aller plus loin :

- [Unicode Classe WS](https://www.compart.com/fr/unicode/bidiclass/WS)
- [Unicode Catégorie Zs](https://www.compart.com/fr/unicode/category/Zs)
- [NewLine](https://en.wikipedia.org/wiki/Newline#Unicode)
- [WhiteSpace Character](https://en.wikipedia.org/wiki/Whitespace_character#:~:text=In%20computer%20programming%2C%20whitespace%20is,an%20area%20on%20a%20page.)
- [Unicode Space Separator](https://www.compart.com/en/unicode/category/Zs)
- [Unicode General Punctuation](https://unicode-explorer.com/b/2000)

## Symboles

`🇫🇷` DRAPEAU FRANÇAIS

- U+1F1EB U+1F1F7 Regional Indicator Symbol Letter F Regional Indicator Symbol Letter R
- [emoji](https://unicode.org/emoji/charts/full-emoji-list.html)

## Fullwidth

- `➕❌🖊️🔲⚪✅💑`
- [Fullwidth Halfwidth](https://www.fileformat.info/info/unicode/block/halfwidth_and_fullwidth_forms/list.htm)

## Divers

```html
<pre>

    Char Number Comment
    ← &#x2190; &#8592; left arrow / APL WIKIPEDIA
    ↑ &#x2191; &#8593; up arrow
    → &#x2192; &#8594; right arrow
    ↓ &#x2193; &#8595; down arrow

    ⟵ U+27F5 https://unicode-table.com/fr/sets/arrow-symbols/
    ⟶ U+27F6
    ⇒ U+21D2 https://unicode-table.com/en/sets/mathematical-signs/
    ⇐ U+21D0
    ⇔ U+21D4

    ✓ &#x2198; &#8600;
    □ &#x25A1; &#9633;
    ■ &#x25A0; &#9632;

    ✅ U+2705
    ✓ U+2713
    ✔ U+2714
    ☑ U+2611
    🗸 U+1F5F8 &#128504;


    ❌ U+274C &#10060;
    ❎ U+274E &#10062;
    ✖ U+2716
    ✗ U+2717
    ✘ U+2718
    ☒ U+2612
    𐄂 U+10102


    https://unicode-table.com/en/emoji/people-and-body/

    👍 U+1F44D
    ♂ U+2642 Male
    ♀ U+2640 Female Femelle
    ⚥ U+26A5 Male Female
    ⚭ U+26AD Mariage
    👦 U+1F466 Garçon
    👧 U+1F467 Fille
    👨 U+1F468 Homme
    👩 U+1F469 Femme
    🤰 U+1F930 Pregnant Woman Femme enceinte

    0 1 2 3 4 5 6 7 8 9 A B C D E F
    U+1F600 😀 😁 😂 😃 😄 😅 😆 😇 😈 😉 😊 😋 😌 😍 😎 😏
    U+1F610 😐 😑 😒 😓 😔 😕 😖 😗 😘 😙 😚 😛 😜 😝 😞 😟
    U+1F620 😠 😡 😢 😣 😤 😥 😦 😧 😨 😩 😪 😫 😬 😭 😮 😯
    U+1F630 😰 😱 😲 😳 😴 😵 😶 😷 😸 😹 😺 😻 😼 😽 😾 😿
    U+1F640 🙀 🙁 🙂 🙃 🙄 🙅 🙆 🙇 🙈 🙉 🙊 🙋 🙌 🙍 🙎 🙏
</pre>
```

## Cartes

|         | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | A  | B  | C  | D  | E  | F  |
|---------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| U+1F0Ax | 🂠 | 🂡 | 🂢 | 🂣 | 🂤 | 🂥 | 🂦 | 🂧 | 🂨 | 🂩 | 🂪 | 🂫 | 🂬 | 🂭 | 🂮 |    |
| U+1F0Bx |    | 🂱 | 🂲 | 🂳 | 🂴 | 🂵 | 🂶 | 🂷 | 🂸 | 🂹 | 🂺 | 🂻 | 🂼 | 🂽 | 🂾 | 🂿 |
| U+1F0Cx |    | 🃁 | 🃂 | 🃃 | 🃄 | 🃅 | 🃆 | 🃇 | 🃈 | 🃉 | 🃊 | 🃋 | 🃌 | 🃍 | 🃎 | 🃏 |
| U+1F0Dx |    | 🃑 | 🃒 | 🃓 | 🃔 | 🃕 | 🃖 | 🃗 | 🃘 | 🃙 | 🃚 | 🃛 | 🃜 | 🃝 | 🃞 | 🃟 |
| U+1F0Ex | 🃠 | 🃡 | 🃢 | 🃣 | 🃤 | 🃥 | 🃦 | 🃧 | 🃨 | 🃩 | 🃪 | 🃫 | 🃬 | 🃭 | 🃮 | 🃯 |
| U+1F0Fx | 🃰 | 🃱 | 🃲 | 🃳 |    | 🃴 | 🃵 |    |    |    |    |    |    |    |    |    |

```text
    ♥ U+2665 ♡ U+2661
    ♠ U+2660 ♤ U+2664
    ♦ U+2666 ♢ U+2662
    ♣ U+2663 ♧ U+2667
```

## Sources

(Compart.com)[https://www.compart.com/fr/unicode/]
