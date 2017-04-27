# coding: utf-8
__author__ = 'polly'

'''

'''

from app.models import Company
from app.models import Vacancy
from app import db


def get_company(id_company=1632763):
    #answer = Company.query.filter_by(id_company=id_company).first()
    answer = Company.query.get(id_company)
    print answer.id
    print answer.name


def get_vacancy(id_company=1632763):
    answer = Vacancy.query.filter_by(id_company=id_company).first()
    if answer is not 'None':
        print answer.job_title
    #print answer.id
    #print answer.job_title
    #print answer.info


def get_vacancy_info(id_vacancy=11863819):
    answer = Vacancy.query.get(id_vacancy)
    if answer is not 'None':
        print answer.id
        print answer.job_title
        print answer.info
        print answer.id_company
        print answer.spec
        print answer.spec_name


if __name__ == '__main__':
    #get_company()
    #get_vacancy()
    get_vacancy_info()