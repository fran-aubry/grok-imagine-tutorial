from xai_sdk import Client
from dotenv import load_dotenv

# Load the API key
load_dotenv() 

# Initialize the xAI client
client = Client()

# Sending a video generation request
prompt = """
A person stands holding their phone, gazing at a stunning landscape 
photo on the screen. The image begins to subtly move and glow. 
Suddenly, the phone pulls them in, and they are sucked through the screen, 
transitioning seamlessly into the vast, breathtaking landscape itself.
"""

response = client.video.generate(
    prompt=prompt,
    model="grok-imagine-video",
    duration=15,
    aspect_ratio="9:16",
    resolution="480p",
)

# Display the URL of the video
print(f"Video URL: {response.url}")