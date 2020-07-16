import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin.db import reference


class FireBaseService:
    def __init__(self):

        # An environmental variable with the name GOOGLE_APPLICATION_CREDENTIALS needs to be defined
        # It should contain the path to the service account.
        # The service account needs the proper roles in order to read, write the database
        certificate = credentials.Certificate(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
        firebase_app = firebase_admin.initialize_app(certificate, {
            'databaseURL': 'https://reactcms-37d59.firebaseio.com/'
        })
        self.__database_ref = reference(path='/', app=firebase_app)

    def get_data(self):
        database = self.__database_ref.get()
        print(database)


fire_base_service = FireBaseService()
fire_base_service.get_data()
