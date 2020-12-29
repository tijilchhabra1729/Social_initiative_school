from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField , RadioField ,widgets, SelectMultipleField , TextAreaField
from wtforms.validators import DataRequired, Email

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class surveyform(FlaskForm):
    gender = RadioField('What is your gender? ' , choices=[('Male','Male'),('Female','Female'),('Other' , 'Other/ Prefer not to say')])
    profile_sites = MultiCheckboxField('Please select all the social networking sites for which you have created a profile (you can choose many options) :', choices= [('Facebook' , 'Facebook') , ('Instagram' , 'Instagram') , ('Twitter' , 'Twitter'),( 'Snapchat', 'Snapchat') , ('Youtube' , 'Youtube') , ('Whatsapp' , 'Whatsapp') ,( 'Discord' , 'Discord') , ('Any other' , 'Any other')])
    age_aware = RadioField('Are you aware of the age limits for using various social networking sites?', choices = [('Yes' , 'Yes') , ('No' , 'No') , ("Can't say" , "Can't say")])
    information = MultiCheckboxField('What information do you include on your social networking profile (you can choose many options) ? ' , choices = [('E-mail' , 'E-mail') , ('Address' , 'Address') , ('Mobile Number' , 'Mobile Number') , ('Date of Birth' , 'Date of Birth') , ('Other' , 'Other')])
    friend_stranger = RadioField('Do you accept friend requests from strangers?' , choices = [('Yes' , 'Yes') , ('No' , 'No')])
    policies = RadioField('Do you think that privacy policies are effective in social networking sites?' , choices = [('Yes' , 'Yes') , ('No' , 'No') , ("Can't say" , "Can't say")])
    victim  = RadioField('Have you ever been a victim of cyber crime?' , choices = [('Yes' , 'Yes') , ('No' , 'No') , ("Prefer not to say" , "Prefer not to say")])
    government = RadioField('Are you aware of the Government Policies that provide protection against cyber crimes?' ,  choices = [('Yes' , 'Yes') , ('No' , 'No') , ("Maybe" , "Maybe")])
    social_sites = RadioField('Do you think that cyber crimes are increasing with the advent of technology and greater usage of social networking sites? ' ,  choices = [('Yes' , 'Yes') , ('No' , 'No') , ("Maybe" , "Maybe")])
    parents = RadioField('Are your parents aware of your profile on such social networking sites?' ,  choices = [('Yes' , 'Yes') , ('No' , 'No') , ("Maybe" , "Maybe")])
    school = RadioField('Does your school organize workshops and webinars related to cyber security?' , choices = [('Yes' , 'Yes') , ('No' , 'No')])
    opinion = TextAreaField('In your opinion, what measures can one take to prevent and decrease cyber crimes?')
    submit = SubmitField('Submit')

class emailform(FlaskForm):
    email = StringField('Email' , validators=[Email() , DataRequired()])
    submit = SubmitField('Submit')
