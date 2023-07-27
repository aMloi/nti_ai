# -*- coding: utf-8 -*-
"""trans_spe_2_spe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fM3-itd2KjulkdpxAPHKfhjQAG3WFuax
"""

pip install SpeechRecognition

import speech_recognition as sr

r=sr.Recognizer()

filename= '16-122828-0002.wav'

with sr.AudioFile(filename) as source:
  audio_data = r.record(source)
  text = r.recognize_google(audio_data,language='en')
  print(text)

!pip install googletrans==4.0.0-rc1

from googletrans import Translator

translator = Translator()
text_to_translate = text
target_language = "ar"  # Change to the desired target language code
translated_text = translator.translate(text_to_translate, dest=target_language)

print("Translated Text:", translated_text.text)

pip install gtts

from gtts import gTTS

mytest = translated_text.text
mytest

language = 'ar'

myobj=gTTS(text=mytest,lang=language,slow=False)

myobj.save('s32s.mp3')





