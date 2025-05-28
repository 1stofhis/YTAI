from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_video():
    credentials = Credentials.from_authorized_user_file("credentials.json", SCOPES)
    youtube = build("youtube", "v3", credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "AI Took My Job – Here’s How I Made $10,000 Anyway",
                "description": "Your video description here.",
                "tags": ["AI", "Passive Income", "ChatGPT"],
            },
            "status": {"privacyStatus": "private"},
        },
        media_body="final_video.mp4"
    )
    response = request.execute()
    print(f"Video uploaded: https://youtu.be/{response['id']}")

if __name__ == "__main__":
    upload_video()