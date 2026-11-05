Nama = input("Masukkan Nama Anda: ")
NPM = input("Masukkan NPM Anda: ")
Alamat= input ("Masukan alamat rumah: ")
print(f"Nama: {Nama}")
print(f"NPM: {NPM}")

if NPM[-1] == '0' and Nama != Nama.isalpha() and Alamat != Alamat.isalpha():
    print("Identitas Anda tidak valid.")
else:
    print("Identitas Anda valid.")

for num in NPM:
    if type(num) != int:
        raise ValueError
    else:
        pass

if Nama[0] == "R" or Nama[0] == "G":
    print("Anda adalah orang VIP.")
else:
    pass