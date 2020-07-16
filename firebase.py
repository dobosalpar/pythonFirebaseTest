import firebase_admin


class FireBaseService:
    def __init__(self):

        # An environmental variable with the name GOOGLE_APPLICATION_CREDENTIALS needs to be defined
        # It should contain the path to the google service account json
        self.__firebase_admin = firebase_admin.initialize_app()
