import os
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def garbage_collector(max_storage_mb, directory):
    """
    Garbage collects files in the specified directory to maintain a maximum storage size.

    :param max_storage_mb: Maximum storage size in megabytes
    :param directory: Path to the directory containing the files
    """

    # Convert MB to bytes for size comparison
    max_storage_bytes = max_storage_mb * 1024 * 1024

    # Check if the directory exists
    if not os.path.exists(directory):
        logging.error(f"Directory does not exist: {directory}")
        return

    try:
        # Get all files in the directory with their paths and sizes
        files = [(file, os.path.getsize(file), os.path.getmtime(file)) for file in Path(directory).glob('*')]
        
        # Sort files by modification time (newest first)
        files.sort(key=lambda x: x[2], reverse=True)

        total_size = 0
        for file, size, _ in files:
            total_size += size

            # If the total size exceeds the maximum storage limit, delete the file
            if total_size > max_storage_bytes:
                os.remove(file)
                logging.info(f"Deleted: {file}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage
# garbage_collector(100, '/path/to/metrics')  # Adjust the path as needed
