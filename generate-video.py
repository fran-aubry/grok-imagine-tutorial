from xai_sdk import Client
from dotenv import load_dotenv

# Load the API key
load_dotenv() 

# Initialize the xAI client
client = Client()

# Sending a video generation request
prompt = """
A pixel art cat playing with a ball.
"""

response = client.video.generate(
    prompt=prompt,
    model="grok-imagine-video",
)

# Display the URL of the video
print(f"Video URL: {response.url}")