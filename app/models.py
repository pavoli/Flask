# coding: utf-8
__author__ = 'polly'

'''

'''

from app import db


class Company(db.Model):
    __tablename__ = 'Company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, index=True)
    web_site = db.Column(db.String(50))
    info = db.Column(db.String(500))
    company_type = db.Column(db.String(100))

    def __init__(self, id_company, name, web_site, info, company_type):
        self.id = id_company
        self.name = name
        self.web_site = web_site
        self.info = info
        self.company_type = company_type


class Vacancy(db.Model):
    __tablename__ = 'Vacancy'

    id = db.Column(db.Integer, primary_key=True)
    id_company = db.Column(db.Integer, db.ForeignKey('Company.id'))
    url = db.Column(db.String(150))
    job_title = db.Column(db.String(50))
    info = db.Column(db.String(2000))
    spec = db.Column(db.String(300))
    spec_name = db.Column(db.String(300))

    def __init__(self, id_vacancy, id_company, url, job_title, info, spec, spec_name):
        self.id = id_vacancy
        self.id_company = id_company
        self.url = url
        self.job_title = job_title
        self.info = info
        self.spec = spec
        self.spec_name = spec_name

    def __repr__(self):
        return 'Vacancy %r' % self.job_title