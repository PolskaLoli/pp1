def generate_number():
    import random
    return random.randint(1,9)


if __name__ == "__main__":
    # Testowanie funkcji, gdy skrypt jest uruchamiany bezpośrednio
    random_number = generate_number()
    print(f"Losowa liczba z zakresu <1, 9>: {random_number}")