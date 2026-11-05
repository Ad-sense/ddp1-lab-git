Nama = input("Masukkan Nama Anda: ")
NPM = input("Masukkan NPM Anda: ")
print(f"Nama: {Nama}")
print(f"NPM: {NPM}")

if NPM[-1] == '0' and Nama != Nama.isalpha():
    print("Identitas Anda tidak valid.")
else:
    pass
