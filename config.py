# coding: utf-8
__author__ = 'polly'

'''

'''

import os


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Facebook', 'url': 'http://facebook.com'},
    {'name': 'VK', 'url': 'http://vk.com'},
    {'name': 'LinkedIN', 'url': 'http://linkedin.com'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
]

basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'hh_spb.db') # mac os x
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'hh_spb.db') # win version
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['p.olifer@bk.ru']

#pagination
VACANCY_PER_PAGE = 25
COMPANY_PER_PAGE = 30
