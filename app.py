from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')

@app.route('/')
def main():
	# return "Welcome!"
	return render_template('blank.html')

if __name__ == "__main__":
	# webbrowser.open('http://localhost:5000')
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.config['DEBUG'] = True
	app.run()