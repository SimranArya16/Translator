import winsound  # For beep sound (freq in Hz, duration in milliseconds)
import speech_recognition as sr  # Speech to text
from googletrans import Translator  # Translator API for multiple languages
from gtts import gTTS  # Text to speech
import os  # File operations
from langdetect import detect  # Language detection library

def user_command() :
    obj = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        obj.pause_threshold = 1 # Time take to anaylize the audio
        talk = obj.listen(source) # Listen to the speech

    try :
        print("Rcognizing....")
        txt = obj.recognize_google(talk , language = 'en -IN' ) # language 'en -IN' -----> english -Indian accent
        print(f"User : {txt}")
    except Exception as e:
        print("Speak again !")
        return None

    language_dic = {
    'english': 'en',
    'spanish': 'es',
    'french': 'fr',
    'german': 'de', 
    'italian': 'it',
    'portuguese': 'pt',
    'russian': 'ru',
    'japanese': 'ja',  
    'korean': 'ko', 
    'hindi': 'hi'   
    
    }
    print(language_dic.keys())
    lg = input("Choose a language  ").strip().lower()
    lang_code = language_dic[lg] 



    try:
        sp_lg = detect(txt)
        tr = Translator()
        lg_trans = tr.translate(txt, src=sp_lg, dest=lang_code)
        print(f"Translator({lg}) : {lg_trans.text}")
   
        
        res = gTTS(text=lg_trans.text , lang=lang_code, slow=False)   # slow (speed of audio) = false (normal) if true (speed will slow)
        res.save("speech1.mp3")  
        os.system("start speech1.mp3")  # Play audio
    
    except Exception as e:
        print(f"Translation Error: {e}")
    
 
  


user_command()

