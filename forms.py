from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired

class ResumeForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    experience = TextAreaField('Опыт', validators=[DataRequired()])
    skills = StringField('Навыки', validators=[DataRequired()])
    image_url = StringField('Изображение', validators=[DataRequired()])
    city = SelectField('Выберите свой город', choices=[
        ('1', 'Омск'),
        ('2', 'Брянск'),
        ('3', 'Челябинск'),
        ('4', 'Москва'),
        ('5', 'Сургут'),
        ('6', 'Йошкар-Ола'),
        ('7', 'Норильск'),
        ('8', 'Мухосранск'),
        ('9', 'Архангельск')
    ], validators=[DataRequired()])
    submit = SubmitField('Разместить резюме')
