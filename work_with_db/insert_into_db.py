# coding: utf-8
__author__ = 'polly'

'''

'''

from app.models import Company
from app.models import Vacancy
from app import db


def insert_company(id_company, name, web_site, info, company_type):
    exist_company = Company.query.get(int(id_company))
    if exist_company is None:
        c = Company(id_company, name, web_site, info, company_type)
        db.session.add(c)
        db.session.commit()


def insert_vacancy(id_vacancy, id_company, url, job_title, info, spec, spec_name):
    exist_vacancy = Vacancy.query.get(int(id_vacancy))
    if exist_vacancy is None:
        v = Vacancy(id_vacancy, id_company, url, job_title, info, spec, spec_name)
        db.session.add(v)
        db.session.commit()

if __name__ == '__main__':
    pass