# coding: utf-8
__author__ = 'polly'

'''

'''

import requests
import json
from lxml import html
from insert_into_db import insert_company, insert_vacancy


def getCompanyId():
    base_url = "http://spb.hh.ru/employers_list?areaId=2&page=%s"
    for url in [base_url % i for i in xrange(13, 39)]:
        response = requests.get(url)
        parsed_body = html.fromstring(response.text)
        href = parsed_body.xpath("//div[@class='l-nopaddings']//a//@href")
        for item in href:
            company_id = item.replace('/employer/', '')
            #print 'company_id= %s' % company_id
            getCompanyInformation(company_id)
            getCompanyVacancyId(company_id)


def getCompanyInformation(company_id=922):
    employer_url = 'http://api.hh.ru/employers/%s/' % company_id
    response = requests.get(employer_url)
    if response.status_code == 200:
        try:
            parsed_json = json.loads(response.text)
            company_name = parsed_json['name']
            web_site = parsed_json['site_url']
            info = parsed_json['description']
            company_type = parsed_json['type']
            insert_company(company_id, company_name, web_site, info, company_type)
            #print company_name
            #print web_site
            #print description
            #print type
        except ValueError as e:
            print 'Value error({0}): {1}. Company: {2}'.format(e.errno, e.strerror, company_id)


def getCompanyVacancyId(companyId=922):
    employer_vacancy = 'http://spb.hh.ru/rss/employer.xml?employerId=%s' % str(companyId)
    namespaces = {'hhvac': 'http://hh.ru/spec/hhvac'}
    tree = etree.parse('%s' % employer_vacancy)
    links = tree.xpath('channel/item/hhvac:vacancyId/text()', namespaces=namespaces)
    for link in links:
        #print link
        getVacancyInformation(link)


def getVacancyInformation(vacancy_id=11798343):
    vanacy_url = 'https://api.hh.ru/vacancies/%s' % vacancy_id
    response = requests.get(vanacy_url)
    if response.status_code == 200:
        try:
            parsed_json = json.loads(response.text)
            id_company = parsed_json['employer']['id']
            url = parsed_json['alternate_url']
            job_title = parsed_json['name']
            info = parsed_json['description']
            spec = parsed_json['specializations'][0]['profarea_name']
            spec_name = parsed_json['specializations'][0]['name']
            insert_vacancy(vacancy_id, id_company, url, job_title, info, spec, spec_name)
            #print info
            #print job_title
            #print id_company
            #print url
            #print spec
            #print spec_name
        except ValueError as e:
            print 'Value error({0}): {1}. Vacancy: {2}'.format(e.errno, e.strerror, vacancy_id)


if __name__ == '__main__':
    getCompanyId()
    #getCompanyVacancyId()
    #getCompanyInformation()
    #getVacancyInformation()