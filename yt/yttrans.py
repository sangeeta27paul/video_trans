import whisper
import torch 
import os
from pytube import YouTube
# Set the device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the model 
whisper_model = whisper.load_model("small", device=device)

def video_to_audio(video_URL, destination, final_filename):

  # Get the video
  video = YouTube(video_URL)

  # Convert video to Audio
  audio = video.streams.filter(only_audio=True).first()

  # Save to destination
  output = audio.download(output_path = destination)

  _, ext = os.path.splitext(output)
  new_file = final_filename + '.mp3'

  # Change the name of the file
  os.rename(output, new_file)
  

# Video to audio
def speech_to_text(v_url):
   #n = request.GET.get('u')
   video_URL = v_url
   destination = "."
   final_filename = video_URL.split("=")[1]
   video_to_audio(video_URL, destination, final_filename)
   audio_file = f"{final_filename}.mp3"
   result = whisper_model.transcribe(audio_file)
   os.remove(audio_file)
   return result["text"]