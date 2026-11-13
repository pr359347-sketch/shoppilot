---
name: multilingual-seo
description: Translate and localize a listing's title and 13 tags (optionally description) into Etsy's 9 languages — German, French, Italian, Spanish, Dutch, Portuguese, Polish, Japanese, Russian — keeping keyword intent, local search terms and limits. Use when the owner asks to translate a listing or target a specific country.
---

# Multilingual SEO — DE, FR, IT, ES, NL, PT, PL, JA, RU

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Why

Etsy auto-translates listings, but machine translations miss the words buyers actually search (e.g. German buyers type "Teppich Wolle handgetuftet", not a literal translation). Manually added translations are indexed for search in that language.

## Inputs

English title + 13 tags (from `etsy-listing-seo` or pasted) · rug facts (construction, material, sizes) · which languages (default: all 9; if the owner wants priority only → DE, FR, NL first — biggest EU rug markets on Etsy; use the shop's country split from reports if available).

## Rules

1. **Localize, don't translate word-for-word.** Translate the *search intent*: use the term locals type. Keep the same primary keyword position (first ~40 chars of the title).
2. **Limits stay the same in every language:** title ≤140 chars, 13 tags, each ≤20 chars. German/Dutch/Russian/Polish words are long — shorten the phrase, split across two tags, or use the compound noun. **Show the char count for every title and tag.** For Japanese, count characters (each kana/kanji = 1).
3. **Sizes:** lead with **cm** for all 9 languages (e.g. `150x240 cm`), keep ft only in the English version. Decimal comma where local (2,5 m).
4. **Honesty carries over:** "Moroccan style" → "im marokkanischen Stil / style marocain / stile marocchino…", never an origin claim. Construction terms must stay accurate (tufted ≠ knotted).
5. No brand names; no English filler unless locals use it ("Boho", "Vintage", "Kilim", "Shaggy" are used as-is in most EU languages).
6. Tags: same repeated-word discipline as English; use local long-tails rather than 13 translations of the English tags if a better local phrase exists (say which ones were swapped).
7. If unsure about a term's real-world usage, mark it `(?)` and give the safer alternative — don't present a guess as certain.

## Core glossary (use as base; adapt by context)

| EN | DE | FR | IT | ES | NL | PT | PL | JA | RU |
|---|---|---|---|---|---|---|---|---|---|
| rug / area rug | Teppich | tapis | tappeto | alfombra | vloerkleed / tapijt | tapete | dywan | ラグ / カーペット | ковер |
| wool rug | Wollteppich | tapis en laine | tappeto in lana | alfombra de lana | wollen vloerkleed | tapete de lã | dywan wełniany | ウールラグ | шерстяной ковер |
| handmade | handgefertigt / Handarbeit | fait main | fatto a mano | hecho a mano | handgemaakt | feito à mão | ręcznie robiony | ハンドメイド / 手作り | ручная работа |
| hand tufted | handgetuftet | tufté main | taftato a mano | tufting a mano (?) | handgetuft | tufado à mão (?) | ręcznie tuftowany | ハンドタフテッド | ручной тафтинг |
| hand knotted | handgeknüpft | noué main | annodato a mano | anudado a mano | handgeknoopt | atado à mão | ręcznie tkany (węzełkowy) | 手織り | ручной вязки |
| kilim / flatweave | Kelim / Flachgewebe | kilim / tissé à plat | kilim / tessitura piatta | kilim / tejido plano | kelim / platgeweven | kilim / tecelagem plana | kilim / płasko tkany | キリム / 平織り | килим / безворсовый ковер |
| runner | Läufer | tapis de couloir | passatoia | alfombra de pasillo | loper | passadeira | chodnik | ランナーラグ | ковровая дорожка |
| round rug | runder Teppich | tapis rond | tappeto rotondo | alfombra redonda | rond vloerkleed | tapete redondo | dywan okrągły | 円形ラグ | круглый ковер |
| living room | Wohnzimmer | salon | soggiorno | salón | woonkamer | sala de estar | salon | リビング | гостиная |
| bedroom | Schlafzimmer | chambre | camera da letto | dormitorio | slaapkamer | quarto | sypialnia | 寝室 | спальня |
| nursery / kids room | Kinderzimmer | chambre d'enfant | cameretta | habitación infantil | kinderkamer | quarto de bebé / infantil | pokój dziecięcy | 子供部屋 | детская |
| kids rug | Kinderteppich | tapis enfant | tappeto bambini | alfombra infantil | kindervloerkleed | tapete infantil | dywan dziecięcy | キッズラグ | детский ковер |
| hallway / entryway | Flur | couloir / entrée | corridoio / ingresso | pasillo / entrada | gang / hal | corredor / entrada | przedpokój | 玄関 / 廊下 | прихожая / коридор |
| boho | Boho | bohème | boho | boho | boho / bohemian | boho | boho | ボヘミアン | бохо |
| moroccan style | marokkanischer Stil / Berber Stil | style marocain / berbère | stile marocchino | estilo marroquí | Marokkaanse stijl / Berber stijl | estilo marroquino | styl marokański | モロッコ風 | марокканский стиль |
| scandinavian | skandinavisch / Skandi | scandinave | scandinavo | escandinavo / nórdico | Scandinavisch | escandinavo | skandynawski | 北欧 | скандинавский |
| modern | modern | moderne | moderno | moderno | modern | moderno | nowoczesny | モダン | современный |
| custom size | Wunschmaß / nach Maß | sur mesure | su misura | a medida | op maat | por medida | na wymiar | オーダーサイズ | на заказ |
| gift | Geschenk | cadeau | regalo | regalo | cadeau | presente / prenda | prezent | ギフト | подарок |
| housewarming gift | Einzugsgeschenk | cadeau de crémaillère | regalo per la casa nuova | regalo casa nueva | housewarming cadeau | presente casa nova | prezent na parapetówkę | 新築祝い | подарок на новоселье |

Local notes: DE compounds are powerful single tags ("Wollteppich", "Kinderteppich", "Flurläufer"). NL buyers search "vloerkleed" far more than "tapijt". PT: use European Portuguese by default ("tapete", "passadeira") and note the Brazilian variant only if asked. JA: mix katakana product words with kanji room words; no spaces needed. RU: provide it (Etsy language exists) but tell the owner it's lowest priority.

## Output format

Per language, a separate block (so the owner can paste into Etsy's translation fields):

```
🇩🇪 GERMAN (DE)
Title (118): Handgetufteter Wollteppich, Moderner Teppich Wohnzimmer, …
Tags:
1. wollteppich (11)
2. teppich wohnzimmer (18)
…13
Copy line: wollteppich, teppich wohnzimmer, …
Notes: swapped "housewarming gift" → "einzugsgeschenk"; sizes in cm.
```

If description translation is requested: translate the hook + details + sizes table (cm first) + care + shipping; keep it shorter than English; keep section headers in the local language.

End with **Next steps** (owner's language): Etsy → Shop Manager → Settings → Languages and translations → enable languages → open listing → add translation per language → paste title + tags. Suggest starting with the top 2–3 countries from the shop's country split and only the top 10 listings.

## Self-check

- [ ] Every title ≤140, every tag ≤20 (counted, not guessed — recount long German/Russian/Polish tags).
- [ ] Exactly 13 tags per language. Primary keyword leads the title.
- [ ] No false origin/construction claims introduced by translation.
