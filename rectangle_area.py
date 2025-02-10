def calculate_area(length, width):

    """
    Menghitung luas persegi panjang.
    BUG: Saat ini menggunakan penjumlahan, seharusnya perkalian.
    """
    return length * width  # BUG: Seharusnya menggunakan length * width
    #ariiii

# Contoh penggunaan
if __name__ == "__main__":
    length = 2000
    width = 311
    print("Luas persegi panjang:", calculate_area(length, width))
