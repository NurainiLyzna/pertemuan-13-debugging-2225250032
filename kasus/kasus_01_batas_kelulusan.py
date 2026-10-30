def status_lulus(nilai):
    if nilai > 60:  # Bug batas: nilai 60 seharusnya lulus
        return "Lulus"
    return "Tidak lulus"

print("Nilai 60:", status_lulus(60))
print("Nilai 59:", status_lulus(59))