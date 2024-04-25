from .controller import Controller
from flask import request, jsonify, session

class UserController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'username',
            'password',
            'name',
            'role',
        ])

    def login(self): 
        username = request.form.get('username')        
        password = request.form.get('password')

        user = self.service.login(username, password)

        if user:
            data = {
                'status': 'success',
                'message': 'Successfully login.',
                'item': user,
            }
            session['user'] = user
        else:
            data = {
                'status': 'error',
                'message': 'Invalid username or password.',
            }

        response = jsonify(data)

        return response, 200

    def me(self): 
        if 'user' in session:
            data = {
                'status': 'success',
                'message': 'You are logged in.',
                'item': session['user'],
            }
        else:
            data = {
                'status': 'error',
                'message': 'You are not logged in.',
            }

        response = jsonify(data)

        return response, 200
  
    def logout(self): 
        session.clear()
        data = {
            'status': 'success',
            'message': 'Successfully logged out',
        }

        response = jsonify(data)

        return response, 200
  


