def calculeaza_probabilitati_conditionate(probabilitati):
    p_cuvant = probabilitati[0]
    numar_candidati = 5
    probabilitate_prior = 1 / numar_candidati
    probabilitati_conditionate = {}

    for i in range(1, numar_candidati + 1):
        p_cuvant_din_candidat = probabilitati[i]
        p_conditionat = (p_cuvant_din_candidat * probabilitate_prior) / p_cuvant
        probabilitati_conditionate[f'Candidat_{i}'] = p_conditionat

    return probabilitati_conditionate


def clasifica_discurs(probabilitati):
    probabilitati_conditionate = calculeaza_probabilitati_conditionate(probabilitati)

    candidat_predicted = max(probabilitati_conditionate, key=probabilitati_conditionate.get)

    return candidat_predicted, probabilitati_conditionate


def clasifica_discurs_nou(cuvinte_cheie_discurs_nou, date_candidati):
    scoruri_candidati = {f'Candidat_{i}': 0 for i in range(1, 6)}

    for cuvant in cuvinte_cheie_discurs_nou:
        if cuvant in date_candidati:
            probabilitati = date_candidati[cuvant]

            candidat_predicted, probabilitati_conditionate = clasifica_discurs(probabilitati)

            for candidat, scor in probabilitati_conditionate.items():
                scoruri_candidati[candidat] += scor

    candidat_final_predicted = max(scoruri_candidati, key=scoruri_candidati.get)

    return candidat_final_predicted, scoruri_candidati

def sorter(t):
    return t[1]


def actualizare(dict, word):
    while len(word) > 0 and str.isalpha(word[-1]) == False:
        word = word[:-1]
    word = word.upper()
    if len(word) > 0:
        if word not in dict:
            dict.update({word: 1})
        else:
            dict[word] += 1


def analiza_discurs(f):
    dict = {}
    discurs = f.read()
    discurs = discurs.split(" ")
    for word in discurs:
        word.strip("\n")
        if "\n" in word:
            word_list = word.split("\n")
            for w in word_list:
                actualizare(dict, w)
        else:
            actualizare(dict, word)
    return dict


def actualizeaza_total(d_total, d):
    for cheie in d.keys():
        if cheie in d_total:
            d_total[cheie] += d[cheie]
        else:
            d_total.update({cheie: d[cheie]})
    return d_total


nume_candidati = ["m_ciolacu", "n_ciuca", "e_lasconi", "g_simion", "m_geoana"]
fd_candidati = []
for i in range(len(nume_candidati)):
    fd_candidati.append(open(nume_candidati[i] + ".txt", "r"))
g = open("out1.txt", "w")
d_candidati = []
nrcuv_candidati = []
for i in range(len(nume_candidati)):
    d_candidati.append(analiza_discurs(fd_candidati[i]))
d_total = {}
for d in d_candidati:
    d_total = actualizeaza_total(d_total, d)
    nrcuv_candidati.append(sum(d.values()))
nrcuv_total = sum(d_total.values())
lista_ponderi = [[], [], [], [], []]
cuvinte_cheie = []
date_candidati = {}
for cuvant in d_total.keys():
    procente = []
    nr_aparitii = 0
    for i in range(len(d_candidati)):
        if cuvant not in d_candidati[i]:
            procente.append(0)
        else:
            nr_aparitii += 1
            procente.append(d_candidati[i][cuvant] / nrcuv_candidati[i])
    if nr_aparitii >= 2:
        for i in range(len(d_candidati)):
            lista_ponderi[i].append((cuvant, procente[i] / ((sum(procente) - procente[i]) / 4)))
            if procente[i] / ((sum(procente) - procente[i]) / 4) > 10:
                date_candidati.update({cuvant: [d_total[cuvant] / nrcuv_total, procente[0], procente[1], procente[2],
                                                procente[3], procente[4]]})
                cuvinte_cheie.append(cuvant)
    else:
        cuvinte_cheie.append(cuvant)
        date_candidati.update({cuvant: [d_total[cuvant] / nrcuv_total, procente[0], procente[1], procente[2],
                                        procente[3], procente[4] ]})



for i in range(len(d_candidati)):
    lista_ponderi[i] = sorted(lista_ponderi[i], key=sorter, reverse=True)
for i in range(len(d_candidati)):
    g.write(nume_candidati[i][0].upper() + " " + nume_candidati[i][2:].upper())
    g.write("\n")
    for t in lista_ponderi[i]:
        g.write(t[0])
        g.write(" ")
        g.write(str(t[1]))
        g.write("\n")

discurs_test = open("ciolacu_test.txt", "r")
d_test = analiza_discurs(discurs_test)

cuvinte_discurs_nou = [cheie for cheie in d_test.keys() if cheie in cuvinte_cheie]

if cuvinte_discurs_nou:
    candidat_final_predicted, scoruri_candidati = clasifica_discurs_nou(cuvinte_discurs_nou, date_candidati)

    print(
        f"Discursul este cel mai probabil al candidatului: {nume_candidati[int(candidat_final_predicted.split('_')[1]) - 1]}")
    print("Scorurile finale pentru fiecare candidat:")
    for i, (candidat, scor) in enumerate(scoruri_candidati.items()):
        print(f"{nume_candidati[i]}: {scor:.4f}")
else:
    print("Nu s-au gasit suficiente cuvinte cheie pentru a clasifica discursul.")
