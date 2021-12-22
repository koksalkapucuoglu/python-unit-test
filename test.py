import unittest

from app import update_user_information, add_user
from app.utiliy import hash_password, verify_password

def create_user_list():
    user_list = {
        'testuser1' : {
            'username': 'testuser1',
            'email': 'testuser1@example.com',
            'name': 'user1',
            'password': 'a00638c6ab4912422c7c89dac3b7e7152895698d671530354cff09bc4647de4fbac8f5f759c'
        },
        'testuser2' : {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'name': 'user2',
            'password': 'bc4647de4fbac8f5f759c5e5b709b51d7fe50b78d1e705bf03fc2d4aee4fe5100ea615ea3c'
        }
    }
    return user_list

class TestUser(unittest.TestCase):
    
    def test_key_is_added_successfully(self):
        """Test whether new key added or not"""
        user = {'name': 'koksal', 'age': 27}
        updated_user = update_user_information(user, height = 182, country = 'TUR')

        self.assertEqual(len(updated_user), 4)
        self.assertIn('height', updated_user.keys())
        self.assertIn('country', updated_user.keys())

    def test_is_key_value_change_instead_existing_key_value(self):
        """Test wheter existing key value, change or not"""
        user = {'name': 'koksal', 'age': 27}
        updated_user = update_user_information(user, name = 'test')

        self.assertEqual(len(updated_user), 2)
        self.assertIn('name', updated_user.keys())
        self.assertEqual('test', updated_user['name'])

    def test_is_user_add_to_userlist(self):
        """Test whether user add to user list or not"""
        userlist = create_user_list()
        user = {
            'name': 'koksal kapucuoglu', 
            'username': 'koksal',
            'email': 'koksal@example.com',
            'password': hash_password('testpass123')
        }
        new_userlist, detail = add_user(userlist, user['username'], user['email'], user['name'], user['password'])

        self.assertIn(user['username'], new_userlist.keys())
        self.assertEqual(user['username'], new_userlist[user['username']]['username'])
        self.assertEqual(user['email'], new_userlist[user['username']]['email'])
        self.assertEqual(user['name'], new_userlist[user['username']]['name'])
        self.assertTrue(verify_password(new_userlist[user['username']]['password'], user['password']))
        self.assertEqual(detail, 'New user adding succesfully')

    def test_get_error_existing_username(self):
        """Test whether existing user add to user list or not"""
        userlist = create_user_list()
        user = {
            'name': 'koksal kapucuoglu', 
            'username': 'testuser2',
            'email': 'koksal@example.com',
            'password': hash_password('testpass123')
        }
        new_userlist, detail = add_user(userlist, user['username'], user['email'], user['name'], user['password'])

        self.assertIn(user['username'], new_userlist.keys())
        self.assertEqual(user['username'], new_userlist[user['username']]['username'])
        self.assertEqual(detail, 'Adding user is failed because of existing username')

if __name__ == '__main__':
    unittest.main()