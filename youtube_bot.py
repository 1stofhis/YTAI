import os
from dotenv import load_dotenv
load_dotenv()  # Loads from .env file
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
# ===== youtube_bot.py - COMPLETE VERSION =====
import os
import pickle
import requests
import openai
from elevenlabs.client import ElevenLabs
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# ===== CONFIGURATION =====
CONFIG = {
    "OPENAI_KEY": "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",          # Get from platform.openai.com
    "ELEVENLABS_KEY": "sk_cf697c7a40541437321a99b600fa909f8500a01a3a546401",  # Get from elevenlabs.io
    "PEXELS_KEY": "TDupi3QJiDh1VVrO3uq1Eer6b6ZzdfczAbI1bTOr44Z5ABb7zS46GMbk",          # Get from pexels.com/api
    "VIDEO_TOPIC": "Top 5 AI Tools for Passive Income in 2024",
    "PRIVACY_STATUS": "private",  # "public", "private", or "unlisted"
    "TAGS": ["AI", "Make Money Online", "ChatGPT"]
}

# ===== 1. SCRIPT GENERATION =====
def generate_script():
    try:
        openai.api_key = CONFIG["OPENAI_KEY"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"Write a 1000-word YouTube script about {CONFIG['VIDEO_TOPIC']} with a hook, 5 key points, and call-to-action."
            }]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ Script generation failed: {str(e)}")
        return None
# ===== 1. First generate your script (keep your existing code) =====
import openai
openai.api_key = "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"
script = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Write a YouTube script about..."}]
).choices[0].message.content
# ===== 1. First generate your script with ChatGPT =====
script = """Hey everyone, welcome back to the channel!
Today, we’re diving into something everyone’s asking:
"How do I make real money online in 2025?"
Not scams. Not get-rich-quick schemes. Just real, proven methods you can start today — no matter where you live.
Let’s go!

First up — Freelancing.
Platforms like Upwork, Fiverr, and Toptal are still booming in 2025.
But here’s the secret: AI + Skill = $$$.

Are you a writer? Use tools like ChatGPT to outline faster.

Designer? Combine Canva and Midjourney for high-end visuals.

Coder? AI pair-programming saves hours.

👉 Focus on niches: short-form video scripts, email marketing, AI prompt engineering — they’re hot right now.

📱 [2. Content Creation 

Number two — Content Creation.
This isn't just for influencers anymore. You can earn by:

Starting a YouTube channel (ad revenue + sponsorships)

Creating TikToks or Instagram Reels and joining affiliate programs

Writing newsletters with Substack or monetizing Medium articles

💡 Pro Tip: Build your content around problems people search on Google or YouTube. Be the solution.

🛍️ [3. Selling Digital Products 

Next — Digital Products.

Ebooks

Online courses

Notion templates

AI prompt bundles

PLR products (Private Label Rights)

Set up shop on Gumroad, Payhip, or CRESTAR HQ if you want international exposure.
Create once, sell forever. That’s the power of digital.

🪙 [4. Crypto & Microtasks – 2:45]

Now let’s talk about crypto earning & microtasks.

Platforms like Sweatcoin, Taskmate, or Honeygain pay in crypto for simple tasks.

Try bounty hunting or testnet participation — helping test new blockchain projects can earn you free tokens.

⚠️ But remember: research before investing time or money. Scams are still out there.

🚚 [5. On-Demand Services 

Number five: Offer on-demand services.

Use platforms like CRESTAR HQ, TaskRabbit, or even Facebook Marketplace to offer:

Delivery services

Virtual assistant tasks

Translations

Local errands or tech help

Even if it’s offline, you can find jobs and get paid online — especially if you live in a growing digital economy.

🤝 [6. Affiliate Marketing

And of course, Affiliate Marketing.
In 2025, even beginners can get started — no blog needed.

Share product links on TikTok, Instagram, or in your WhatsApp groups.

Join affiliate programs from Amazon, Jumia, ClickBank, or new platforms like CRESTAR HQ’s affiliate system.

💰 You earn a % every time someone buys through your link.

🧠 [Bonus: Build Your Brand –

Want long-term income? Build your brand.

Whether you're selling, freelancing, or teaching — put your name or alias out there.
Trust = Sales.
And in 2025, your online reputation is currency.

📝 [Conclusion – 

So there you go —
6 legit ways to make money online in 2025:

Freelancing

Content Creation

Digital Products

Crypto & Microtasks

On-Demand Services

Affiliate Marketing

Choose one. Start small. Build momentum.
Let the internet work for you. 🌍💻

If you found this helpful, drop a like, hit subscribe, and let me know in the comments:
Which method are YOU starting with today?

Catch you in the next one!"""  # From your OpenAI code

# ===== 2. ElevenLabs Text-to-Speech =====
from elevenlabs.client import ElevenLabs
from elevenlabs import save  # For saving audio

# Initialize client (replace with your API key from elevenlabs.io)
client = ElevenLabs(api_key="sk_cf697c7a40541437321a99b600fa909f8500a01a3a546401") 

# Generate voiceover
audio = client.generate(
    text=script[:5000],  # Using first 5000 chars to stay within free tier
    voice="Rachel",      # Default female voice
    model="eleven_monolingual_v1"
)

# Save audio file
save(audio, "voiceover.mp3")
print("✅ Voiceover saved as voiceover.mp3")

# ===== 3. Continue with video creation =====
# ... (your existing video assembly code using MoviePy)
# ===== 2. NEW: Add ElevenLabs TTS here =====
from elevenlabs.client import ElevenLabs
from elevenlabs import save  # For saving audio

# Initialize client (sk_cf697c7a40541437321a99b600fa909f8500a01a3a546401)
client = ElevenLabs(api_key="sk_cf697c7a40541437321a99b600fa909f8500a01a3a546401") 

# Generate voiceover
audio = client.generate(
    text=script,  # Uses the script from ChatGPT
    voice="Rachel",  # Default female voice
    model="eleven_monolingual_v1"
)

# Save audio file for video editing
save(audio, "voiceover.mp3")

# ===== 3. Continue with your video creation =====
from moviepy.editor import *
# ... (rest of your video merging code)
# ===== 2. VOICEOVER GENERATION =====
def create_voiceover(script):
    try:
        set_api_key(CONFIG["ELEVENLABS_KEY"])
        audio = generate(
            text=script,
            voice="Rachel",
            model="eleven_monolingual_v1"
        )
        with open("voiceover.mp3", "wb") as f:
            f.write(audio)
        return True
    except Exception as e:
        print(f"❌ Voiceover failed: {str(e)}")
        return False

# ===== 3. VIDEO CREATION =====
def create_video():
    try:
        # Download stock footage (using first video from Pexels search)
        headers = {"Authorization": CONFIG["PEXELS_KEY"]}
        search_url = f"https://api.pexels.com/videos/search?query={CONFIG['VIDEO_TOPIC']}&per_page=1"
        video_data = requests.get(search_url, headers=headers).json()
        video_url = video_data["videos"][0]["video_files"][0]["link"]
        
        # Download and save video
        video_path = "stock_video.mp4"
        with requests.get(video_url, stream=True) as r:
            r.raise_for_status()
            with open(video_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        # Combine with voiceover
        video = VideoFileClip(video_path).subclip(0, 60)  # First 60 seconds
        audio = AudioFileClip("voiceover.mp3")
        final_video = video.set_audio(audio)
        final_video.write_videofile("final_video.mp4", codec="libx264", audio_codec="aac")
        return True
    except Exception as e:
        print(f"❌ Video creation failed: {str(e)}")
        return False
# ===== 1. IMPORTS SECTION (Add these at the top) =====
import requests
from bs4 import BeautifulSoup
import urllib.parse  # For URL encoding

# ===== 2. AMAZON SCRAPER FUNCTION (Place with other functions) =====
def get_amazon_affiliate_link(product_name, affiliate_tag="1stofhis-20"):
    """Get first Amazon product link with your affiliate tag"""
    try:
        # Search Amazon
        search_url = f"https://www.amazon.com/s?k={urllib.parse.quote(product_name)}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract first product link
        first_result = soup.find('a', {'class': 'a-link-normal s-no-outline'})
        if not first_result:
            return f"https://www.amazon.com/s?k={urllib.parse.quote(product_name)}&tag={affiliate_tag}"
        
        product_path = first_result['href']
        return f"https://www.amazon.com{product_path.split('?')[0]}?tag={affiliate_tag}"
    
    except Exception as e:
        print(f"⚠️ Amazon scrape failed: {e}")
        return f"https://www.amazon.com/s?k={urllib.parse.quote(product_name)}&tag={affiliate_tag}"

# ===== 3. INTEGRATION POINT (In main workflow) =====
# Add this RIGHT BEFORE YouTube upload:
affiliate_links = "\n".join([
    get_amazon_affiliate_link("AI Tools Book"),
    get_amazon_affiliate_link("USB Microphone")
])

final_description = f"""
{script}

--- PRODUCT LINKS ---
{affiliate_links}

DISCLAIMER: As an Amazon Associate I earn from qualifying purchases.
"""
# ===== 4. YOUTUBE UPLOAD =====
def youtube_authenticate():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json",
                ["https://www.googleapis.com/auth/youtube.upload"]
            )
            creds = flow.run_local_server(port=0)
        
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    
    return build("youtube", "v3", credentials=creds)

def upload_video():
    try:
        youtube = youtube_authenticate()
        
        request_body = {
            "snippet": {
                "title": CONFIG["VIDEO_TOPIC"],
                "description": script,
                "tags": CONFIG["TAGS"],
                "categoryId": "28"  # Science & Technology
            },
            "status": {
                "privacyStatus": CONFIG["PRIVACY_STATUS"],
                "selfDeclaredMadeForKids": False
            }
        }
        
        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body="final_video.mp4"
        ).execute()
        
        print(f"✅ Upload successful! Video ID: {response['id']}")
        print(f"👉 Preview: https://youtu.be/{response['id']}")
        return True
    except Exception as e:
        print(f"❌ Upload failed: {str(e)}")
        return False

# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("=== Starting YouTube Bot ===")
    
    # Step 1: Generate script
    print("\n1. Generating script...")
    script = generate_script()
    if not script:
        exit()
    
    # Step 2: Create voiceover
    print("2. Creating voiceover...")
    if not create_voiceover(script):
        exit()
    
    # Step 3: Create video
    print("3. Creating video...")
    if not create_video():
        exit()
    
    # Step 4: Upload to YouTube
    print("4. Uploading to YouTube...")
    if not upload_video():
        exit()
    
    print("\n=== Process completed successfully! ===")
