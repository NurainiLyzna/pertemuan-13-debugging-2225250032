def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Test cases
print("T1 (75):", status_lulus(75))  # Expected: Lulus
print("T2 (60):", status_lulus(60))  # Expected: Lulus
print("T3 (59):", status_lulus(59))  # Expected: Tidak lulus