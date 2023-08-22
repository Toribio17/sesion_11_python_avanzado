from app.utils.utils import Utils

class Users(Utils):
    def get_users(self):

        users_json = [
            {'id': self.get_user_id('emailexample@avanzado.com'), 'name': 'avanzado', 'email': 'emailexample@avanzado.com'},
            {'id': self.get_user_id('emailexample2@avanzado.com'), 'name': 'avanzadoe', 'email': 'emailexample@avanzado.com'}
        ]
        return users_json