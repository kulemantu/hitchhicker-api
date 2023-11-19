import unittest
import os
import tempfile
import shutil
from garbage_collector import garbage_collector

class TestGarbageCollector(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Clean up the directory after tests
        shutil.rmtree(self.test_dir)

    def create_temp_file(self, name, size):
        # Helper function to create a temp file with a specific size
        file_path = os.path.join(self.test_dir, name)
        with open(file_path, 'wb') as f:
            f.write(b'x' * size)
        return file_path

    def test_garbage_collector_with_nonexistent_directory(self):
        # Test with a non-existent directory
        non_existent_dir = os.path.join(self.test_dir, 'nonexistent')
        garbage_collector(100, non_existent_dir)
        # Check if the directory still doesn't exist
        self.assertFalse(os.path.exists(non_existent_dir))

    def test_garbage_collector_with_empty_directory(self):
        # Test with an empty directory
        garbage_collector(100, self.test_dir)
        # Check if the directory is still empty
        self.assertEqual(len(os.listdir(self.test_dir)), 0)

    def test_garbage_collector_with_files_exceeding_limit(self):
        # Create files exceeding the limit
        self.create_temp_file('file1', 1024 * 1024 * 60)  # 60 MB
        self.create_temp_file('file2', 1024 * 1024 * 50)  # 50 MB
        self.create_temp_file('file3', 1024 * 1024 * 10)  # 10 MB

        # Run garbage collector with a limit of 100 MB
        garbage_collector(100, self.test_dir)

        # Check if only the oldest file is deleted
        remaining_files = os.listdir(self.test_dir)
        self.assertIn('file2', remaining_files)
        self.assertIn('file3', remaining_files)
        self.assertNotIn('file1', remaining_files)

# Run the tests
if __name__ == '__main__':
    unittest.main()
