# L09E01: Matrix rows mask
Vytvořte modul `matrix` obsahující funkci `iterate_rows(matrix, mask)`. Jako první argument funkce přijímá matici ve tvaru:

```python
matrix = [
    [1, 2, 3, 4],
    [6, 7, 8, 9].
    [4, 5, 6, 7]
]
```

A binární masku o délce počtu řádků, která určuje jaké řádky budou vybrány:

```python
# první a třetí řádek bude vybrán, druhý ne
mask = [True, False, True]
```

Následně vrací iterátor, který produkuje všechna sudá čísla, které řádky odpovídající masce obsahují.

```python
matrix = [
    [1, 2, 3, 4],
    [6, 7, 8, 9].
    [4, 5, 6, 7]
]

mask = [True, False, True]

list(iterate_rows(matrix, mask)

# [2, 4, 4, 6]
```

Funkci realizujte pouze pomoci iterátorů (balíček `itertools`) a dalších nástrojů představných na semináři. Nepoužívejte list comprehension ani jiné cykly.

## Lokální testování
Funkčnost řešení ověříte následujícím příkazem:

```bash
pytest tests.py
```