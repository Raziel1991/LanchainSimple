import time
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


def check_internet_connection(url: str = "http://www.google.com", timeout: int = 5) -> bool:
    """
    Check if there is an active internet connection by trying to access a specified URL.

    Args:
        url (str): The URL to check for connectivity. Defaults to "http://www.google.com".
        timeout (int): The timeout in seconds for the request. Defaults to 5 seconds.

    Returns:
        bool: True if the internet connection is active, False otherwise.
    """
    print(f"Checking internet connection to {url} with a timeout of {timeout} seconds...RAZ")
    try:
        request = Request(url)
        response = urlopen(request, timeout=timeout)
        print("Internet connection is active.")
        return True
    except (URLError, HTTPError):
        print("No internet connection available.")
        return False
        return False


def check_internet_download_speed(url: str = "http://www.google.com", timeout: int = 5) -> float:
    """
    Check the download speed of the internet connection by measuring the time taken to download a small file.

    Args:
        url (str): The URL of a small file to download for speed testing. Defaults to "http://www.google.com".
        timeout (int): The timeout in seconds for the request. Defaults to 5 seconds.

    Returns:
        float: The download speed in bytes per second. Returns -1 if the download fails.
    """
    print(f"Checking internet download speed from {url} with a timeout of {timeout} seconds...RAZ")
    try:
        start_time = time.time()
        request = Request(url)
        response = urlopen(request, timeout=timeout)
        data = response.read()
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        download_speed = len(data) / elapsed_time  # bytes per second
        print(f"Download speed: {download_speed} bytes/second")
        return download_speed
    except (URLError, HTTPError):
        print("Failed to download the test file.")
        return -1.0