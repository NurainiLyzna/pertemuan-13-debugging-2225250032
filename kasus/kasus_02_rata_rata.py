def rata_rata(data):
    total = sum(data)
    return total / 5  # Bug: pembagi konstan 5, tidak dinamis

print(rata_rata([80, 90, 70]))