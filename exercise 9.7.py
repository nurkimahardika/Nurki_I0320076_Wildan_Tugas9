#mengonversi string kedalam array.array
import array
string = 'Python'
B = array.array('c')
B.fromstring(string)


for karakter in B:
    print('%c'%karakter, end=' ')