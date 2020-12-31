from Tool import app, db
import os
from Tool.forms import emailform , surveyform
from Tool.models import Survey
from flask import render_template, request, url_for, redirect, flash, abort
from sqlalchemy import desc, asc
import pandas as pd
import secrets
@app.route('/' , methods = ['GET' , 'POST'])
def index():
    return render_template('index.htm')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template("about.htm")

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
    y = Survey.query.with_entities(Survey.parents)
    parents_yes = 0
    parents_no = 0
    parents_maybe = 0
    for i in y:
        if i[0] == "Yes":
            parents_yes += 1
        elif i[0] == "No":
            parents_no += 1
        else:
            parents_maybe += 1

    y = Survey.query.with_entities(Survey.age_limit)
    age_yes = 0
    age_no = 0
    age_cant = 0
    for i in y:
        if i[0] == "Yes":
            age_yes += 1
        elif i[0] == "No":
            age_no += 1
        else:
            age_cant += 1

    y = Survey.query.with_entities(Survey.friend_stranger)
    stranger_yes = 0
    stranger_no = 0
    n = 0
    for i in y:
        if i[0] == "Yes":
            stranger_yes += 1
        elif i[0] == "No":
            stranger_no += 1

    y = Survey.query.with_entities(Survey.policies)
    n = 0
    policies_yes = 0
    policies_no = 0
    policies_cant = 0
    for i in y:
        if i[0] == "Yes":
            policies_yes += 1
        elif i[0] == "No":
            policies_no += 1
        else:
            policies_cant += 1
    y = Survey.query.with_entities(Survey.victim)
    victim_yes = 0
    victim_no = 0
    victim_prefer = 0
    for i in y:
        if i[0] == "Yes":
            victim_yes += 1
        elif i[0] == "No":
            victim_no += 1
        else:
            victim_prefer += 1

    y = Survey.query.with_entities(Survey.media)
    facebook = 0
    instagram = 0
    twitter = 0
    snapchat = 0
    youtube = 0
    whatsapp = 0
    discord = 0
    other = 0
    for i in y:
        if i[0]:
            for j in i[0].split(','):
                print(j)
                if j == "'Facebook'" or j == " 'Instagram'":
                    facebook += 1
                elif j == "'Instagram'" or j == " 'Instagram'":
                    instagram += 1
                elif j == "'Twitter'" or j == " 'Twitter'":
                    twitter += 1
                elif j == "'Snapchat'" or j == " 'Snapchat'":
                    snapchat += 1
                elif j == "'Youtube'" or j == " 'Youtube'":
                    youtube += 1
                elif j == "'Whatsapp'" or j == " 'Whatsapp'":
                    whatsapp += 1
                elif j == " 'Discord'" or j == "'Discord'":
                    discord += 1
                else:
                    other += 1
    return render_template('result.htm' , parents_yes = parents_yes , parents_no = parents_no , parents_maybe = parents_maybe,
                            age_yes = age_yes , age_no = age_no , age_cant = age_cant , stranger_no = stranger_no , stranger_yes = stranger_yes,
                            policies_no = policies_no , policies_yes = policies_yes , policies_cant = policies_cant , victim_yes = victim_yes,
                            victim_no = victim_no , victim_prefer = victim_prefer , facebook = facebook , twitter = twitter , instagram = instagram,
                            snapchat = snapchat , youtube = youtube , whatsapp = whatsapp , discord = discord , other = other)

if __name__ == '__main__':
    app.run(debug=True)
