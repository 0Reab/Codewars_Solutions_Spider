import unittest
from unittest.mock import patch, MagicMock

from get_data import *
from file_ops import *


class TestCleanupFilename(unittest.TestCase):
    def test_cleanup_name_success(self):
        result = cleanup_filename('test!@#$%^&*()+')
        self.assertEqual(result, 'test')

    def test_no_bad_chars(self):
        result = cleanup_filename('valid_name')
        self.assertEqual(result, 'valid_name')

    def test_only_bad_chars(self):
        result = cleanup_filename('!@#$%^&*()')
        self.assertEqual(result, '')

    def test_empty_string(self):
        result = cleanup_filename('')
        self.assertEqual(result, '')

    def test_spaces_removed(self):
        result = cleanup_filename('name with spaces')
        self.assertEqual(result, 'namewithspaces')


class TestCreateDirs(unittest.TestCase):
    @patch("os.makedirs")
    def test_create_dirs_success(self, mock_makedirs):
        """Test if create_dirs calls os.makedirs correctly"""
        create_dirs()

        mock_makedirs.assert_any_call("Retired", exist_ok=True)

        for n in range(1,9):
            mock_makedirs.assert_any_call(f'{n}_kyu', exist_ok=True)

    @patch('os.makedirs', side_effect=PermissionError)
    def test_create_dirs_permission_error(self, mock_makedirs):
        with self.assertRaises(PermissionError):
            create_dirs()


class TestGetDescription(unittest.TestCase):
    @patch("requests.get")  # Mock requests.get
    def test_successful_request(self, mock_get):
        """Test if function returns description when API responds successfully"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"description": "This is a test kata"}

        result = get_description("1234", "https://api.example.com/kata/")
        self.assertEqual(result, "This is a test kata")

    @patch("requests.get")
    def test_failed_request(self, mock_get):
        """Test if function returns None when API responds with an error"""
        mock_get.return_value.status_code = 404  # Simulate failed request
        mock_get.return_value.json.return_value = {}

        result = get_description("1234", "https://api.example.com/kata/")
        self.assertIsNone(result)

    @patch("requests.get")
    def test_missing_description(self, mock_get):
        """Test if function handles missing 'description' key in response"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}  # No 'description' key

        result = get_description("1234", "https://api.example.com/kata/")
        self.assertIsNone(result)  # Should return None if 'description' key is missing


class TestFetchHtml(unittest.TestCase):
    @patch("get_data.webdriver.Firefox")
    def test_fetch_html(self, MockWebDriver):
        """Test if fetch_html correctly returns page source"""

        # instance
        mock_driver = MagicMock()
        MockWebDriver.return_value =  mock_driver
        mock_response = requests.Response()

        # setup mock behaviour
        mock_driver.page_source = "<html><body>Mock Page</body></html>"
        mock_driver.execute_script.return_value = 1000 # simulate scroll
        mock_driver.get.return_value = mock_response

        # func call
        result = fetch_html("https://www.example.com", {"session": "fake_cookie"})

        # asserts
        self.assertEqual(result, "<html><body>Mock Page</body></html>")
        mock_driver.get.assert_called_with("https://www.example.com")
        mock_driver.quit.assert_called_once() # check if quit properly


if __name__ == "__main__":
    unittest.main()