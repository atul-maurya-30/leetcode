import requests
import json
import base64

# Replace with your actual username and the session cookie
LEETCODE_USERNAME = 'atulsrnvm9235'
LEETCODE_SESSION = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNjIyMjQ4MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImIzOGQ0NTllMWU0ZjRlMGJlNzk2ZWI4Y2E0ZDIxZWViM2RhNjc4Mzk1ZWQ5NTg1MDZlNTg3ZDExMDg5NmUyODgiLCJpZCI6NjIyMjQ4MiwiZW1haWwiOiJhdHVsc3Judm05MjM1QGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiYXR1bHNybnZtOTIzNSIsInVzZXJfc2x1ZyI6ImF0dWxzcm52bTkyMzUiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY2OTUwMzE4OC5wbmciLCJyZWZyZXNoZWRfYXQiOjE3Mjk5NjQzOTksImlwIjoiNDIuMTA1LjEyOS4xNDYiLCJpZGVudGl0eSI6Ijc2NzVkNTliNWU4NGUwYTg3OGVlNmYwYTk3ZjkwNTZmIiwic2Vzc2lvbl9pZCI6NzY3NTU0NDYsImRldmljZV93aXRoX2lwIjpbIjZhZmY4NjMyMjIzNDFlZDYyOGMzNzQ5MTkzZDMyODViIiwiNDIuMTA1LjEyOS4xNDYiXX0.uQMLBdDMxSiIjWejMKfc-ZG5Wa8FcOCJF7O5NGiXA74'  # Replace with your session cookie

# Replace with your GitHub details
GITHUB_USERNAME = 'atul-maurya-30'
GITHUB_TOKEN = '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'  # Replace with your GitHub token
GITHUB_REPO = 'leetcode'  # Replace with your GitHub repository name
FILE_PATH = 'leetcode_solutions.json'  # Name of the file to be created in the repo

def fetch_leetcode_solutions():
    url = f"https://leetcode.com/api/submissions/?username={LEETCODE_USERNAME}"
    cookies = {'LEETCODE_SESSION': LEETCODE_SESSION}
    response = requests.get(url, cookies=cookies)

    if response.status_code != 200:
        print(f"Error: {response.json()}")
        return []

    data = response.json()

    if 'submissions_dump' in data:
        # Return only accepted submissions
        return [
            {
                'title': submission['title'],
                'url': f"https://leetcode.com/problems/{submission['title_slug']}/",
                'code': submission['code']
            }
            for submission in data['submissions_dump']
            if submission['status'] == 'accepted'
        ]
    else:
        print("Error: No submissions found in the response.")
        return []

def upload_to_github(file_path, content):
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/contents/{file_path}'
    
    # Get the current file content if it exists
    response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    
    if response.status_code == 200:
        sha = response.json()['sha']  # Get the SHA of the existing file for update
    else:
        sha = None  # If the file does not exist, we don't need SHA

    # Create the payload for the request
    payload = {
        'message': 'Update LeetCode solutions',
        'content': base64.b64encode(json.dumps(content).encode()).decode(),  # Encode the content in base64
    }

    if sha:
        payload['sha'] = sha  # Add SHA to update the existing file

    response = requests.put(url, headers={'Authorization': f'token {GITHUB_TOKEN}'}, json=payload)

    if response.status_code in [201, 200]:
        print("File uploaded successfully!")
    else:
        print(f"Failed to upload file: {response.json()}")

if __name__ == "__main__":
    solutions = fetch_leetcode_solutions()
    if solutions:
        upload_to_github(FILE_PATH, solutions)
