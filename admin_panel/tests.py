from django.test import TestCase
from django.contrib.auth.models import User

class UserAuthenticationTest(TestCase):
    def testCanRegisterAccount(self):
        response = self.client.post(
            '/sign_up/',
            {
                'username':'testuser',
                'email':'testuser@testing.com',
                'password1':'password123123',
                'password2':'password123123'
            },
            follow=True
        ) 
        self.assertRedirects(response, '/')
    
    def testCannotRegisterAccount_UsernameTaken(self):
        user = User.objects.create_user(username='testuser')
        user.set_password('password12345')
        user.save()
        response = self.client.post(
            '/sign_up/', 
            {
                'username':'testuser',
                'email':'testuser@testing.com',
                'password1':'password123123',
                'password2':'password123123'
            },
            follow=True
        ) 
        self.assertFormError(response, 'sign_up_form', 'username', 'This username is already taken.')
    
    def testCannotRegisterAccount_PasswordMismatch(self):
        response = self.client.post('/sign_up/', {
            'username':'testuser',
            'email':'testuser@testing.com',
            'password1':'password123123',
            'password2':'password123'
        }) 
        self.assertFormError(response, 'sign_up_form', 'password2', 'The passwords must match!')
    
    def testCanLogin(self):
        user = User.objects.create_user(username='testuser')
        user.set_password('password12345')
        user.save()
        response = self.client.post('/sign_in/', {
            'username':'testuser',
            'password':'password12345'
        }) 
        self.assertRedirects(response, '/')
