def calculate_area(length, width):
    """
    Menghitung luas persegi panjang.
    BUG: Saat ini menggunakan penjumlahan, seharusnya perkalian.
    """
    return length + width  # BUG: Seharusnya menggunakan 
    return length * width

# Contoh penggunaan
if __name__ == "__main__":
    length = 5
    width = 3
    print("Luas persegi panjang:", calculate_area(length, width))
