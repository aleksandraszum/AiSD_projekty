import numpy as np
import array_to_latex as a2l

def odl_levensztejna(napis1, napis2):
    wiersze = len(napis1)+1
    kolumny = len(napis2)+1
    dist = [[0 for x in range(kolumny)] for x in range(wiersze)]
    for i in range(1, wiersze):
        dist[i][0] = i
    for i in range(1, kolumny):
        dist[0][i] = i
    for k in range(1, kolumny):
        for w in range(1, wiersze):
            if napis1[w-1] == napis2[k-1]:
                cost = 0
            else:
                cost = 1
            dist[w][k] = min(
                dist[w-1][k] + 1,      # kasowanie
                dist[w][k-1] + 1,      # wstawienie
                dist[w-1][k-1] + cost  # zamiana
            )
    matrix = np.zeros((len(napis1)+1, len(napis2)+1))
    for w in range(wiersze):
        print(dist[w])
        matrix[w, :] = dist[w]
    return (matrix, dist[w][k])

oryginalna_sekwencja = "agaggtgtactgggaaagtcgggattgtccatgatgcggtggggtagggc"
mutacja1 = "agaggtgtcctgggaaaggaggcattatccaaggtacggtggggtaggat"
mutacja2 = "agaggcgtacgggcattttcaagattgtccatgatgcggtggagtagcgc"
mutacja3 = "agaggtgtactaggaaaatcgtgattatgcatgctgaggcggggtcgagc"

#matrix, odleglosc1 = odl_levensztejna(oryginalna_sekwencja, mutacja1)
#matrix2, odleglosc2 = odl_levensztejna(oryginalna_sekwencja, mutacja2)
matrix3, odleglosc3 = odl_levensztejna(oryginalna_sekwencja, mutacja3)

"""
matrix, odleglosc1 = odl_levensztejna(mutacja2, mutacja1)
print(odleglosc1)
matrix, odleglosc2 = odl_levensztejna(mutacja3, mutacja1)
print(odleglosc2)
matrix, odleglosc3 = odl_levensztejna(mutacja2, mutacja3)
print(odleglosc3)"""