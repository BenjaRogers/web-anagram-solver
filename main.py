from flask import Flask, render_template, request
import anagram

app = Flask(__name__, template_folder='template')

@app.route('/')

def main():
    return render_template("main.html")

@app.route('/', methods=['POST'])
def get_post():
    text = request.form['string']
    anagrams = anagram.find_the_anagrams(text)
    anagram_string = ""
    for word in anagrams:
        anagram_string += word + " "
    return anagram_string
if __name__ =='__main__':
    app.run(port=8080)