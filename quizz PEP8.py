def get_harmonic_mean(numbers):
    """Calcule la moyenne harmonique qu'une suite de nombres."""
    try:
        total = 0
        for number in numbers:
            total += 1 / number
        return len(numbers) / total
    except ZeroDivisionError:   #except Exception:
        print("Warning! Division by zero!")
        return None

suite_de_nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
moyenne = get_harmonic_mean(suite_de_nombres)
print(moyenne)
print()

suite_de_nombres2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
moyenne2 = get_harmonic_mean(suite_de_nombres2)
print(moyenne2)
