# coding: utf-8
__author__ = 'polly'

'''

'''

from flask import render_template, flash, redirect, session, url_for, request
from app import app, db
from models import Company, Vacancy
from config import VACANCY_PER_PAGE, COMPANY_PER_PAGE, PICTURE_PER_PAGE
from forms import FindVacancy, PictureList

"""
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user

"""
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html', title='')


@app.route('/company', methods=['GET', 'POST'])
@app.route('/company/', methods=['GET', 'POST'])
@app.route('/company/<int:page>', methods=['GET', 'POST'])
def get_company(page=1):
    companies = Company.query.paginate(page, COMPANY_PER_PAGE, False)
    return render_template('company.html', title='Company', companies=companies)


@app.route('/vacancy', methods=['GET', 'POST'])
@app.route('/vacancy/', methods=['GET', 'POST'])
@app.route('/vacancy/<int:page>', methods=['GET', 'POST'])
def get_vacancy(page=1):
    form = FindVacancy()
    if not form.search.data is None:
        vacancies = db.session.query(Vacancy.id, Vacancy.url, Vacancy.job_title, Vacancy.id_company, Company.name, Company.web_site).\
            join(Company).\
            filter(Vacancy.info.like('%' + form.search.data + '%')).\
            order_by(Company.name).\
            all()
        return render_template('vacancy.html', title='Vacancy', vacancies=vacancies, form=form)
    else:
        vacancies = db.session.query(Vacancy.id, Vacancy.url, Vacancy.job_title, Vacancy.id_company, Company.name, Company.web_site).\
            join(Company).\
            order_by(Company.name).\
            all()
        return render_template('vacancy.html', title='Vacancy', vacancies=vacancies, form=form)
    #vacancies = db.session.query(Vacancy.id, Vacancy.url, Vacancy.job_title, Vacancy.id_company, Company.name, Company.web_site).\
    #        join(Company).\
    #        order_by(Company.name).\
    #        all()
    #return render_template('vacancy.html', title='Vacancy', vacancies=vacancies, form=form)


@app.route('/picture', methods=['GET', 'POST'])
@app.route('/picture/', methods=['GET', 'POST'])
@app.route('/picture/<int:page>', methods=['GET', 'POST'])
def get_picture(page=1):
    form = PictureList()
    return render_template('picture.html', title='Picture', form=form)

"""
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
"""