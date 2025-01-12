import requests
import sys
import json

def get_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Failed to fetch user activity. Status code: {response.status_code}")
        return None

def display_Activity(activity_data):
    for event in activity_data:
        event_type = event["type"]
        repo_name = event.get("repo", {}).get("name")

        message = f"- {event_type}"
        if repo_name:
            message += f" in {repo_name}"
        print(message)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        activity_data = get_user_activity(username)
        if activity_data:
            display_Activity(activity_data)
        else:
            print("Usage: python github_activity.py <username>")


