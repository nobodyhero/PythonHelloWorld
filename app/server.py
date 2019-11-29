# Module import 
from flask import Flask, render_template, request, redirect, url_for
import os

# 自身の名称を app という名前でインスタンス化する
app = Flask( __name__ )

# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT
cf_port = os.getenv("PORT")

# Route / & /entry ===============================================================
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
	return render_template('entry.html',
							the_title='Welcome to My First Python Page by Flask!')

# Route /viewlog ================================================================
@app.route('/results', methods=['POST'])
def do_predict() -> 'html':
	phrase = request.form['phrase']
	title = 'This is what you have input: '

	return render_template('results.html',
						   the_title = title,
						   the_phrase = phrase,)

# Run the applicaiton ===============================================================
if __name__ == '__main__':
	if cf_port is None:
		app.run( host='0.0.0.0', port=5000, debug=True )
	else:
		app.run( host='0.0.0.0', port=int(cf_port), debug=True )