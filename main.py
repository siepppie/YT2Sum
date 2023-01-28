from pytube import YouTube
from revChatGPT.ChatGPT import Chatbot
import whisper
import os

# Ask user for youtube link'
link = YouTube(input("Enter the link of YouTube video you want to summarize: "))

video = link.streams.filter(only_audio=True).first()

out = video.download()
print("Downloaded")

base, ext = os.path.splitext(out)
os.rename(out, "audio.mp3")

model = whisper.load_model('base')
print("Model loaded")

result = model.transcribe("audio.mp3", fp16=False)

print("Audio transcribed")

# delete the mp3 file
os.remove("audio.mp3")

chatbot = Chatbot({
  "session_token": "YOUR_SESSION_TOKEN",
}, conversation_id=None, parent_id=None) # You can start a custom conversation

response = chatbot.ask("The following text is the transcript of a YouTube video. Provide me with a summary which consists of bullet points. \n \n '" + result['text'] + "'", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

# Write the response to a txt file with only the response text
with open("response.txt", "w") as f:
    f.write(response['message'])
    f.close()

print("The summary is saved in the file 'summary.txt'")