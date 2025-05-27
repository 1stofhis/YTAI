from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_video():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    credentials = flow.run_local_server(port=0)
    youtube = build("youtube", "v3", credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "AI Took My Job – Here’s How I Made $10,000 Anyway",
                "description": script,
                "tags": ["AI", "Passive Income", "ChatGPT"],
            },
            "status": {"privacyStatus": "private"},  # Change to "public" later
        },
        media_body="final_video.mp4"
    )
    response = request.execute()
    print(f"Video uploaded: https://youtu.be/{response['id']}")

upload_video()