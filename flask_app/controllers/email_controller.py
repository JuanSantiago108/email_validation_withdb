
from flask_app import app
from flask import redirect ,render_template, request, session
from flask_app.models.email_model import Email 


@app.route('/')
@app.route('/form')
def display_form():
    return render_template('form.html')


@app.route('/form/create', methods=['POST'])
def create_form():
    if not Email.validate(request.form):
        return redirect('/')
    Email.create_one(request.form)
    return redirect('/display/emails')


@app.route('/display/emails')
def display_all_emails():
    all_emails =Email.get_all()
    return render_template('emails.html',all_emails=all_emails)
