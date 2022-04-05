#!/usr/bin/env python3

'''
Satirical code.
How do I get this to work?
A bunch of duct tape.
''' 

from PIL import Image
import pytesseract
pytesseract.tesseract_cmd = "./automeme-venv/lib/python3.9/site-packages/pytesseract/pytesseract.py"
from gtts import gTTS
from moviepy.editor import *
import os

# ----------

mnames = ['demofile.jpg','demofile2.jpg'] # note to self: does NOT work with webp
maudio = 'memetts.mp3'
#TODO: Scrape memes from Reddit

for mname in mnames:
	#TODO: Memes to text
	# right now we have a meme for testing
	meme = Image.open('./scraped-memes/{}'.format(mname),mode='r')
	memetxt = pytesseract.image_to_string(meme)
	print(memetxt) #DELETE
	
	#TODO: Text to speech
	myobj = gTTS(text=memetxt, lang='en', slow=False)
	myobj.save(maudio)

	#TODO: Combine speech and image with moviepy
	audioclip = AudioFileClip(maudio)
	imageclip = ImageClip("./scraped-memes/{}".format(mname)).set_duration(audioclip.duration)

	print(type(imageclip)) #DELETE
	print(type(audioclip)) #DELETE

	videoclip = imageclip.set_audio(audioclip)
	videoclip.write_videofile('./meme-vids/{}.mp4'.format(mname),fps=24,audio=True)
	
print(os.listdir('./meme-vids/')) #DELETE
cliplist = []
for video in os.listdir('./meme-vids/'):
	clip1 = VideoFileClip('./meme-vids/{}'.format(video))
	cliplist.append(clip1)
final = CompositeVideoClip(cliplist,size=(1920,1080))
final.write_videofile("final.mp4")


#TODO: Make loopable, rinse and repeat ~50 times
#TODO: Upload to YT
