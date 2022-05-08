# KNS
Kombinatoryka na słowach

# Uruchomienie (Linux)

Instalacja virtualenv:

$ pip install virtualenv

Otwórz terminal w folderze z projektem i uruchom:

$ virtualenv env

Później:

$ .\env\Scripts\activate

Instalacja pakietów:

$ (env) pip install -r requirements.txt

Uruchomienie aplikacji:

$ (env) python app.py

Aplikacja uruchomi się domyślnie na porcie 5000. Żeby zmienić port należy edytować plik main.py:

if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
