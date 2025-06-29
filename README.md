# Wrocław City Girl

## Szymon Goździkowski

Student pierwszego roku matematyki stosowanej na PWr
Gra zrobiona w ramach projektu zaliczeniowego z kursu *Programowanie*

## Opis

Prosta, stylizowana na arkadową, gierka, gdzie gracz biegnie przez Wrocław. Należy unikać przeszkód (szczurów) i zdobywać punkty za łapanie bonusów. Z czasem tempo gry rośnie, co zwiększa poziom trudności

### Szczegóły gierki

- Gra przyspiesza co **15 sekund**
- Gracz traci życie po zderzeniu z przeszkodą
- Gra kończy się, gdy liczba żyć spadnie do zera
- Wynik jest zapisywany, jeśli gracz osiągnie **top 10**

(pełna logika rozgrywki zaszyta jest w plikach kodu – polecam zajrzeć ;))


## Technologie

- **Python 3.11+**
- **[Arcade 3.3.0](https://api.arcade.academy/en/3.3.0/)** 
- **pillow** – do wczytywania tekstur
- **random, os, json, dataclasses** – standardowe biblioteki Pythona
- Gra działa w pełni lokalnie, bez potrzeby dostępu do internetu

## Uruchomienie

1. Sklonuj repozytorium:
   
    ```bash
   git clone https://github.com/szymongozdzikowski15/programowanie-gra.git
   cd programowanie-gra
    ```

2. Zainstaluj dependencje
    ```
    pip install -r requirements.txt
    ```

3. Uruchom grę
    ```
    python src/main.py
    ```

Miłego grania!!!
