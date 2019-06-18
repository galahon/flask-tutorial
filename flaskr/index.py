# !/python/Python36
#-*- coding:utf-8-*-

from flask import Flask,render_temlate
#app = Flask(__name__)

#@app.route('/')
#def index():
#	return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
#@app.route('/user/<username>')
#def profile(username):
#	  return '{}\'s pofile'.format(username)
	  
#with app.test_request_context():
#	print(url_for('index'))
#	print(url_for('login'))
#	print(url_for('login',next='/'))
#	print(url_for('profile',username='GALA'))


