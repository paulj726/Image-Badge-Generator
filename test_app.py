# Import required libraries
import unittest
import app


class TestApp(unittest.TestCase):

    # Set up Flask test client
    app.app.testing = True
    client = app.app.test_client()
    
    def test_homepage(self):
        # Test that the homepage loads
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generate Badge', response.data)
        
    def test_badge_generation(self):
        # Test that badge is generated with custom text
        response = self.client.post('/', data={'text': 'TEST BADGE', 'font-style': 'OpenSans-Bold.ttf', 'font-size': 70, 'emboss': False, 'circle-color': 'blue', 'size': 300})
        self.assertEqual(response.status_code, 200)
        
    
if __name__ == '__main__':
    unittest.main()
