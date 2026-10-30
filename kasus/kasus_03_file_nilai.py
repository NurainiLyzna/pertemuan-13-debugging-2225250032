def baca_nilai_file(nama_file):
    # Simulasi pembacaan file yang rentan error jika file kosong atau tidak ada
    file = open(nama_file, "r")
    data = [int(line.strip()) for line in file.readlines()]
    file.close()
    return data