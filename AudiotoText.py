#import library
import os

import speech_recognition as sr
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
directory = r'D:\Projects\Text-to-Speech(Tacotron2)\audios'
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
for filename in os.listdir(directory):
    if filename.endswith('.wav'):  # Adjust this condition based on the audio file format
        filepath = os.path.join(directory, filename)

        with sr.AudioFile(filepath) as source:
            audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
                # using google speech recognition
                text = r.recognize_google(audio_text)
                print(text)
            except:
                 print('Sorry.. run again...')