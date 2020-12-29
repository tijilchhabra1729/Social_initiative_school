from Tool import app, db
import os
from Tool.forms import emailform , surveyform
from Tool.models import Survey
from flask import render_template, request, url_for, redirect, flash, abort
from sqlalchemy import desc, asc

@app.route('/' , methods = ['GET' , 'POST'])
def index():

    return render_template('index.htm')

@app.route('/survey/first/step' , methods = ['GET' , 'POST'])
def email():
    form = emailform()
    if form.validate_on_submit():
        user = Survey(email = form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('survey' , id = user.id))
    return render_template('email_form.htm' , form = form)

@app.route('/survey/<id>' , methods = ['GET' , 'POST'])
def survey(id):
    form = surveyform()
    survey = Survey.query.get(id)
    if form.validate_on_submit():
        survey.gender=form.gender.data
        survey.media=str(form.profile_sites.data)[1:-1]
        survey.age_limit=form.age_aware.data
        survey.information=str(form.information.data)[1:-1]
        survey.friend_stranger=form.friend_stranger.data
        survey.policies=form.policies.data
        survey.victim=form.victim.data
        survey.government=form.government.data
        survey.social_sites=form.social_sites.data
        survey.parents=form.parents.data
        survey.school=form.school.data
        survey.opinion=form.opinion.data
        db.session.commit()
        return redirect(url_for('result'))
    return render_template('form.htm' , form = form)

@app.route('/result', methods = ['GET' ,'POST'])
def result():
    gender = Survey.query.filter_by(gender = 'Male')
    n = 0
    for i in gender:
        n +=1
    return render_template('result.htm')

if __name__ == '__main__':
    app.run(debug=True)
