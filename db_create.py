# coding: utf-8
__author__ = 'polly'

'''

'''

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path


db.create_all()