# KNS
Kombinatoryka na słowach

# Uruchomienie (Linux)

Instalacja virtualenv:

__$ pip install virtualenv__

Otwórz terminal w folderze z projektem i uruchom:

__$ virtualenv env__

Później:

__$ .\env\Scripts\activate__

Instalacja pakietów:

__$ (env) pip install -r requirements.txt__

Uruchomienie aplikacji:

__$ (env) python app.py__

Aplikacja uruchomi się domyślnie na porcie 5000. Żeby zmienić port należy edytować plik main.py:

if \__name__ == "\__main__":
    app.run(debug=True, port=\<desired port\>)
