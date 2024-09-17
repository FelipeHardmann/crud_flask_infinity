import os


class Config:
    SQLACHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+mysqlconnector://root:Felipe2015#@localhost/turma'
    )
