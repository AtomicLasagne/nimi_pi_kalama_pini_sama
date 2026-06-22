"""pana e nimi lon kulupu ni: ona li jo e kalama pini sama."""

def nanpa_suli_pi_kalama_sama(a, b):
    n = 0
    for x, y in zip(reversed(a), reversed(b)):
        if x != y:
            break
        n += 1
    return n


def kulupu_kepeken_kalama_pini_sama(nimi_mute, sama_lili=2, awen_e_nimi_wan=False):
    if not nimi_mute:
        return {}

    nimi_lon_nasin_pona = sorted(nimi_mute, key=lambda w: w[::-1])

    kulupu = [[nimi_lon_nasin_pona[0]]]
    for prev, nimi_wan in zip(nimi_lon_nasin_pona, nimi_lon_nasin_pona[1:]):
        if nanpa_suli_pi_kalama_sama(prev, nimi_wan) >= sama_lili:
            kulupu[-1].append(nimi_wan)
        else:
            kulupu.append([nimi_wan])

    ijo_pini = {}
    for k in kulupu:
        if len(k) < 2 and not awen_e_nimi_wan:
            continue
        pini_nimi = k[0]
        for n in k[1:]:
            pini_nimi = pini_nimi[-nanpa_suli_pi_kalama_sama(pini_nimi, n):]
        ijo_pini[pini_nimi] = k
    return ijo_pini


if __name__ == "__main__":
    kulupu_nimi = ["a", "akesi", "ala", "alasa", "ale", "ali", "anpa",
                   "ante", "anu", "awen", "e", "en", "esun", "ijo", "ike",
                   "ilo", "insa", "jaki", "jan", "jelo", "jo", "kala", "kalama",
                   "kama", "kasi", "ken", "kepeken", "kili", "kiwen", "ko",
                   "kon", "kule", "kulupu", "kute", "la", "lape", "laso", "lawa",
                   "len", "lete", "li", "lili", "linja", "lipu", "loje", "lon",
                   "luka", "lukin", "lupa", "ma", "mama", "mani", "meli", "mi",
                   "mije", "moku", "moli", "monsi", "mu", "mun", "musi", "mute",
                   "nanpa", "nasa", "nasin", "nena", "ni", "nimi", "noka", "o"
                   "olin", "ona", "open", "pakala", "pali", "palisa", "pan",
                   "pana", "pi", "pilin", "pimeja", "pini", "pipi", "poka",
                   "poki", "pona", "pu", "sama", "seli", "selo", "seme",
                   "sewi", "sijelo", "sike", "sin", "sina", "sinpin", "sitelen",
                   "sona", "soweli", "suli", "suno", "supa", "suwi", "tan", "taso",
                   "tawa", "telo", "tenpo", "toki", "tomo", "tu", "unpa", "uta",
                   "utala", "walo", "wan", "waso", "wawa", "weka", "wile",
                   "namako", "kin", "oko", "kipisi", "leko", "monsuta",
                   "tonsi", "jasima", "kijetesantakalu", "soko", "meso",
                   "epiku", "kokosila", "lanpan", "n", "misikeke", "ku",]
    for pini_nimi, nimi in kulupu_kepeken_kalama_pini_sama(kulupu_nimi, sama_lili=4).items():
        print(f"-{pini_nimi}: {', '.join(nimi)}")