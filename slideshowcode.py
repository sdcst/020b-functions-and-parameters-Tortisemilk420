#!python3
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Authenticate and build the service
SCOPES = ['https://www.googleapis.com/auth/presentations']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Replace with your service account credentials file
PRESENTATION_ID = 'YOUR_PRESENTATION_ID'  # Replace with your presentation ID

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('slides', 'v1', credentials=credentials)

def create_presentation():
    presentation = {
        'title': 'Brawl Stars Strategies and Gameplay'
    }
    presentation = service.presentations().create(body=presentation).execute()
    presentation_id = presentation.get('presentationId')
    return presentation_id

def create_slide(presentation_id, title, content):
    slide = {
        'title': title,
        'content': content
    }
    requests = [{
        'createSlide': {
            'slideLayoutReference': {
                'predefinedLayout': 'TITLE_AND_BODY'
            },
            'insertionIndex': '1',
            'slide': slide
        }
    }]
    response = service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': requests}).execute()

def add_text_to_slide(presentation_id, slide_id, text):
    requests = [
        {
            'insertText': {
                'objectId': slide_id,
                'insertionIndex': '0',
                'text': text
            }
        }
    ]
    response = service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': requests}).execute()

def main():
    presentation_id = create_presentation()
    print("Created presentation with ID:", presentation_id)

    # Your Brawl Stars strategies and gameplay content
    content = [
        "Introduction to Brawl Stars",
        "Brawler Selection Tips",
        "Game Modes Overview",
        "Showdown Strategies",
        "Gem Grab Tips",
        "Bounty Tactics",
        "Heist Strategies",
        "Brawl Ball Gameplay",
        "Siege Mode Guide",
        "Hot Zone Strategies",
        # Add more content as needed
    ]

    for i, topic in enumerate(content, start=1):
        create_slide(presentation_id, f"Slide {i}", topic)
        print(f"Added slide {i} - {topic}")

    print("Presentation creation complete!")

if __name__ == "__main__":
    main()
