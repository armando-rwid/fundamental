daftar_buku = ['Seven Habits','First Things','How to Influence']
print(daftar_buku)


for buku in daftar_buku:
    print(buku)


print('\nTampilkan data buku 1')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1,'Kenji Vol 2', -3, 3.14]
print('\nTampilkan data buku 2')
for a in range(0, len(daftar_buku)):
    print(daftar_buku[a])

print('\nSebelum Tambah Kenzie')
data_person = ['Armando','Victoria','Gwyneth']
for i in range(0, len(data_person)):
    print(data_person[i])

print('\nSesudah Tambah Kenzie')
data_person.append('Kenzie')
for i in range(0, len(data_person)):
    print(data_person[i])