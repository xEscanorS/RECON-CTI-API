import unittest
from unittest.mock import patch, mock_open
from projeto.cti.reconCTI import requestVT, requestCensys

class TestCTIMan(unittest.TestCase):

    @patch('requests.get')
    def test_requestVT_success(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'some content'

        with patch('builtins.open', mock_open()) as mocked_file:
            requestVT('fake_api_key', 'fake_hash')
            mock_get.assert_called_once_with(
                'https://www.virustotal.com/api/v3/files/fake_hash',
                headers={
                    "Accept": "application/json",
                    "x-apikey": "fake_api_key"
                }
            )
            mocked_file.assert_called_once_with('VT-CTI.csv', 'wb')
            mocked_file().write.assert_called_once_with(b'some content')

    @patch('requests.get')
    def test_requestCensys_success(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'some content'

        with patch('builtins.open', mock_open()) as mocked_file:
            requestCensys('fake_api_key', 'fake_ip')
            mock_get.assert_called_once_with(
                'https://search.censys.io/api/v2/hosts/fake_ip',
                headers={
                    "Accept": "application/json",
                    "Authorization": "Basic fake_api_key"
                }
            )
            mocked_file.assert_called_once_with('CENSYS-CTI.csv', 'wb')
            mocked_file().write.assert_called_once_with(b'some content')

if __name__ == '__main__':
    unittest.main()