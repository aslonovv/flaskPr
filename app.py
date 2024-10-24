from flask import Flask, render_template, redirect, url_for
import sqlite3
from models import db, Article, Resume, app
from forms import ResumeForm



@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    articles = Article.query.all()  # Получаем все статьи из базы данных
    return render_template('articles.html', articles=articles)

@app.route('/freelance')
def freelance():
    resumes = Resume.query.all()
    return render_template('freelance.html', resumes=resumes)


@app.route('/submit_resume', methods=['GET', 'POST'])
def submit_resume():
    form = ResumeForm()
    if form.validate_on_submit():
        # Создание нового резюме с использованием URL изображения
        new_resume = Resume(
            name=form.name.data,
            experience=form.experience.data,
            skills=form.skills.data,
            image=form.image_url.data,
            city=dict(form.city.choices).get(form.city.data)
        )
        db.session.add(new_resume)
        db.session.commit()
        return redirect(url_for('submit_resume'))

    return render_template('submit_resume.html', form=form)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/developers')
def developers():
    return render_template('developers.html')


if __name__ == '__main__':
    app.run(debug=True)
