import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import main

class TestMediaProcessor(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.open', new_callable=mock_open, read_data='http://example.com/image1.jpg\nhttp://example.com/image2.jpg')
    @patch('os.path.exists')
    @patch('time.sleep')  # Patch sleep to make tests run faster
    def test_process_links(self, mock_sleep, mock_exists, mock_file, mock_stdout):
        # Set up the test
        mock_exists.return_value = True
        
        # Run the function for a short time
        with patch('main.process_links', side_effect=KeyboardInterrupt):
            main.main()
        
        # Get the output
        output = mock_stdout.getvalue()
        
        # Verify the expected output contains key phrases
        self.assertIn("Simple Media Processor", output)
        self.assertIn("Processing link:", output)
        self.assertIn("Adding text overlay:", output)

if __name__ == '__main__':
    unittest.main()