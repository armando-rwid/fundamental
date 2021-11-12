print('\nList Daftar Buku')

daftar_buku = ['Seven Habits', 'How to Influence', 'First Things', '4DX']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del')
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList Comprehension')
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList Comprehension Start')
daftar_buku = ['Seven Habits', 'How to Influence', 'First Things', '4DX']
del daftar_buku[0:2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList Comprehension Start dari belakang')
daftar_buku = ['Seven Habits', 'How to Influence', 'First Things', '4DX']
del daftar_buku[0:-2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList Comprehension Step')
daftar_buku = ['Seven Habits', 'How to Influence', 'First Things', '4DX']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
