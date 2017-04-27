# coding: utf-8
__author__ = 'polly'

'''

'''

import requests
import json
from lxml import html
from insert_into_db import insert_company, insert_vacancy


def getCompanyId():
    base_url = "http://www.superjob.ru/clients/?ruf=1&town=14&no_vac=off&page=%s"
    for url in [base_url % i for i in xrange(1, 2)]:
        response = requests.get(url)
        if response.status_code == 200:
            parsed_body = html.fromstring(response.text)
            href = parsed_body.xpath("//div[@class='searchres_comp']/a/@href")
            for item in href:
                print 'company_url= %s' % (item)


def getCompanyInformation(company_url):
    response = requests.get(company_url)
    if response.status_code == 200:
        try:
            parsed_json = json.loads(response.text)
            company_name = parsed_json['name']
            web_site = parsed_json['site_url']
            info = parsed_json['description']
            company_type = parsed_json['type']
            #print company_name
            #print web_site
            #print description
            #print type
        except ValueError as e:
            print 'Value error({0}): {1}.'.format(e.errno, e.strerror)


def getCompanyVacancyList(company_url='http://www.superjob.ru/clients/dockers-640594.html?town=14'):
    base_url = 'http://www.superjob.ru'
    response = requests.get(company_url)
    if response.status_code == 200:
        page = '&page=%s'
        parsed_body = html.fromstring(response.text)
        links = parsed_body.xpath("//div[@class='navnums']//a//text()")
        if links != []:
            paginated_url = company_url + page
            last_page = int(links[-1]) + 1
            print last_page
            for link in [i for i in xrange(1, last_page)]:
                vacancy_url_list = paginated_url % link
                print vacancy_url_list
                response = requests.get(vacancy_url_list)
                if response.status_code == 200:
                    body = html.fromstring(response.text)
                    vacancy_url = body.xpath("//div[@class='overflow_inner']//a/@href")
                    for item in vacancy_url:
                        print base_url + item
        else:
            print 'Pager class is empty'
            vacancy_url = parsed_body.xpath("//div[@class='overflow_inner']//a/@href")
            for item in vacancy_url:
                print item


def getVacancyInformation(vacancy_url='http://www.superjob.ru/rabota/vacancy-27310828.html'):
    response = requests.get(vacancy_url)
    if response.status_code == 200:
        parsed_body = html.fromstring(response.text)
        vacancy_description = parsed_body.xpath("//div[@class='VacancyView_details']//text()")
        for item in vacancy_description:
            item = item.strip()
            if item <> '':
                print item

        vacancy_name = (parsed_body.xpath("//div[@class='VacancyView_main']/h1/text()"))
        for i in vacancy_name:
            print i.strip()


if __name__ == '__main__':
    #getCompanyId()
    #getCompanyVacancyList()
    getVacancyInformation()