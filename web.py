from flask import Flask, render_template, request
import giphypop
g = giphypop.Giphy()
app = Flask(__name__)

def get_giphy(search_term):
    results = g.search(search_term) # returns a list of objects
    return results

@app.route('/')
def index():
    name = request.values.get('name', 'Nobody')
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    search_term = request.values.get('search_term')
    message = 'GIFs tagged with "{}"'.format(search_term)
    results = get_giphy(search_term)
    return render_template('results.html', message=message, results = results)

app.run(debug=True)