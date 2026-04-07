import os, requests
from groq import Groq
from datetime import date

client = Groq(api_key=os.environ["GROQ_API_KEY"])

today = date.today().strftime("%B %d, %Y")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{
        "role": "user",
        "content": f"You are a tech news summarizer. Today is {today}. Summarize the top 5 most important AI and tech news stories from today. Format each story for Discord with an emoji, bold title, 2 sentence summary, and source link. Separate each story with ---"
    }]
)

message = response.choices[0].message.content[:1900]  # Truncate to Discord limit
response_discord = requests.post(os.environ["DISCORD_WEBHOOK"], json={"content": f"📰 **AI & Tech News — {today}**\n\n{message}"})
print(f"Discord response: {response_discord.status_code}")
print(f"Discord response body: {response_discord.text}")
