# mendefinisikan array dua dimensi
A = [
    [23,11,54,38,76],
    [14,12,20,22,21],
    [10,13,18,17,24],
    [35,33,39,32,29]
]

Baris = 4
Kolom = 5

def main():
    print('Isi array A:')
    # menampilkan elemen array dua dimensi
    i = 0
    while i < Baris:
        j = 0
        while j < Kolom :
            print('%d' %A[i][j], end=' ')
            j = j + 1
        i = i + 1
        print() #ganti baris

if __name__ == '__main__':
    main()