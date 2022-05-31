from flask import Flask, render_template, request, redirect, flash
from logic.word import word

app = Flask(__name__)
app.config['SECRET_KEY'] = 'E1E2E5EF7E626E1B2E6FD98ED175C94A30377D3F50CAD28D591F7CA38C2BFAD6'

currentWord = word(9, 1)
difficulty_level = 0


@app.route('/', methods=['POST', 'GET'])
def index():
    global currentWord
    global difficulty_level
    if request.method == "GET":
        return render_template('index.html')
    else:
        ncharAlphabet = request.form['ncharAlphabet']
        endPoint = request.form['endPoint']
        if ncharAlphabet == "":
            flash('Nie podano długości alfabetu', category='error')
            return render_template('index.html')
        elif int(ncharAlphabet) < 1:
            flash('Zła długość alfabetu', category='error')
            return render_template('index.html')
        elif endPoint == "":
            flash('Nie podano długości gry', category='error')
            return render_template('index.html')

        currentWord = word(int(ncharAlphabet), int(endPoint))
        difficulty_level = request.form['difficulty']
        return redirect('/game')


@app.route('/game', methods=['POST', 'GET'])
def game():
    global currentWord
    indexesPre = currentWord.check_repetition()[1:]
    end = currentWord.length >= currentWord.endPoint
    if indexesPre:
        indexes = list(range(indexesPre[0] - indexesPre[1] + 1, indexesPre[0] + 2))
        indexes2 = list(range(indexesPre[0] + 2, indexesPre[0] + indexesPre[1] + 3))
    else:
        indexes = None
        indexes2 = None
    letters = currentWord.letters

    if currentWord.check_repetition()[0]:
        flash('Zwycięstwo!', category='information')
    elif end:
        flash('Osiągnięto długość krytyczną. Przegrana!', category='error')
    return render_template('game.html', letters=letters, indexes=indexes, indexes2=indexes2, end=end)


@app.route('/add/<int:id>')
def add(id):
    global currentWord
    global difficulty_level
    if request.method == 'POST':
        return redirect('/game')
    else:
        if difficulty_level == "Easy":
            currentWord.computer_move(id)
        else:
            # change method below for harder mode
            currentWord.ext_computer_move(id)
        return redirect('/game')


@app.route('/reset')
def reset():
    global currentWord
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
