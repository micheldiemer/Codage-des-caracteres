# Différences entre `widows-1252`, `ISO-8859-1` et `ISO-8859-15`

Les tables de caractères `widows-1252`, `ISO-8859-1` et `ISO-8859-15` se ressemblent beaucoup.

Voici les principales différences :

- les positions `A0-FF (160-255)`, `windows-1252` et `ISO-8859-1` sont identiques
- Norme ISO : les positions `80 (128)` à `9F (159)` correspondent au `codes de contrôle C1` (rarement utilisés en pratique)
- `windows-1252` : dans la plage `80-9F`, on trouve le symbole `€` ainsi que d’autres signes de ponctuation et 5 positions réservées pour un usage futur
- 8 caractères dont `€ Œ œ Ÿ` sont absents de la norme `ISO-8859-1`. La norme `ISO-8859-15` remplace 8 caractères de la norme `ISO-8859-1` et sont placés dans la plage `80-9F` en `windows-1252`.

## `ISO-8859-1` vs `ISO-8859-15`

| `Code`        | `A4` | `A6` | `A8` | `B4` | `B8` | `BC` | `BD` | `BE` |
| ------------- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| `ISO-8859-1`  |  ¤   |  ¦   |  ¨   |  ´   |  ¸   |  ¼   |  ½   |  ¾   |
| `ISO-8859-15` |  €   |  Š   |  š   |  Ž   |  ž   |  Œ   |  œ   |  Ÿ   |

## `windows-1252` vs `ISO-8859-1`

- `ISO-8859-1`positions `80-9F` : `code de contrôle C1`
- 27 caractères absents en `ISO-8859-1` dans les codes `80-9F` : `€ Š š Ž ž Œ œ Ÿ` `‚ ƒ „ … † ‡ ˆ ‰ ‹ ‘ ’ “ ” • – — ˜ ™ ›`

  |            |          |          |          |          |          |             |          |          |          |          |          |          |          |          |          |          |
  | ---------- | :------: | :------: | :------: | :------: | :------: | :---------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
  | **`Code`** | **`80`** | **`81`** | **`82`** | **`83`** | **`84`** |  **`85`**   | **`86`** | **`87`** | **`88`** | **`89`** | **`8A`** | **`8B`** | **`8C`** | **`8D`** | **`8E`** | **`8F`** |
  | `i1`       |   PAD    |   HOP    |   BPH    |   NBH    |   IND    | _**`NEL`**_ |   SSA    |   ESA    |   HTS    |   HTJ    |   VTS    |   PLD    |   PLU    |    RI    |   SS2    |   SS3    |
  | `w1252`    |    €     |          |    ‚     |    ƒ     |    „     |      …      |    †     |    ‡     |    ˆ     |    ‰     |    Š     |    ‹     |    Œ     |          |    Ž     |          |
  | **`Code`** | **`90`** | **`91`** | **`92`** | **`93`** | **`94`** |  **`95`**   | **`96`** | **`97`** | **`98`** | **`99`** | **`9A`** | **`9B`** | **`9C`** | **`9D`** | **`9E`** | **`9F`** |
  | `i1`       |   DCS    |   PU1    |   PU2    |   STS    |   CCH    |     MW      |   SPA    |   EPA    |   SOS    |   SGCI   |   SCI    |   CSI    |    ST    |   OSC    |    PM    |   APC    |
  | `w1252`    |          |    ‘     |    ’     |    “     |    ”     |      •      |    –     |    —     |    ˜     |    ™     |    š     |    ›     |    œ     |          |    ž     |    Ÿ     |

## `windows-1252` vs `ISO-8859-15`

- `ISO-8859-15` codes `80-9F` : `code de contrôle C1`
- 19 caractères absents en `ISO-8859-15`, dans les codes `80-9F` : `‚ ƒ „ … † ‡ ˆ ‰ ‹ ‘ ’ “ ” • – — ˜ ™ ›`
- 8 codes changés
- `windows1252` : 5 positions réservées : `81, 8D, 8F, 90, 9D`

| Caractère                                      |  €   |  Š   |  š   |  Ž   |  ž   |  Œ   |  œ   |  Ÿ   |
| ---------------------------------------------- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| `Code ISO-8859-15`                             | `A4` | `A6` | `A8` | `B4` | `B8` | `BC` | `BD` | `BE` |
| `Code windows-1252`                            | `81` | `8A` | `9A` | `8E` | `9E` | `8C` | `9C` | `9F` |
| `Code ISO-8859-15`<br>`Caractère windows-1252` |  ¤   |  ¦   |  ¨   |  ´   |  ¸   |  ¼   |  ½   |  ¾   |
