import os
import json

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory

from flask.ext.security import login_required

from coineast_exchange import app
from coineast_exchange.core import security, db
from coineast_exchange.utils import update_view_instructions, btc_price_in_pkr, btc_price_in_usd

price_pk = btc_price_in_pkr()
price_usd = btc_price_in_usd()

app.jinja_env.globals.update(btc_pkr_price=price_pk, btc_usd_price=price_usd)


"""
# Create a user to test with
@app.before_first_request
def create_user():
    user_datastore.create_user(email='test@redbrick.com', password='password')
"""


# This processor is added to all templates
@security.context_processor
def security_context_processor():
    return dict(hello="world")

# This processor is added to only the login view
@security.login_context_processor
def login_context_processor():
    return dict(test="something")

# This processor is added to all emails
@security.mail_context_processor
def security_mail_processor():
    return dict(hello="world")

# app controllers
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user-profile')
@login_required
def user_profile():
    return render_template('user_profile.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/deposit')
@login_required
def deposit():
	return render_template('deposit.html')

@app.route('/withdraw')
@login_required
def withdraw():
	return render_template('withdraw.html')

@app.route('/buy')
@login_required
def buy():
	return render_template('buy.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/user_agreement')
def user_agreement():
	return render_template('user_agreement.html')

# special file handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

@app.route('/account')
@login_required
def account():
	return render_template('account.html')

@app.route('/view-instructions' , methods=['GET', 'POST'])
@login_required
def view_instructions():
	email = request.args.get('email')
	if not email:
		return render_template('view_instructions.html')
	status = True
	update_view_instructions(email, status)
	return redirect(url_for('account'))

# error handlers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
