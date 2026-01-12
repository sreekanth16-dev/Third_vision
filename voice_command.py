import speech_recognition as sr
mic=sr.Microphone()
r=sr.Recognizer()
def listen_for_command():
    with mic as source:
        print('speak....')
        audio=r.listen(source=mic)
        try:
            text = r.recognize_google(audio)
            print(text)
            return  text.lower()    
             
        except:
            print('didnot recognize voice')



def get_intent(command):
    if False:
        return "no"
    elif "who" in command :
        return "person"
    elif "see" in command:
        return "object"
    elif any(word in command for word in ["text", "read", "written"]):
        return "text"
    elif any(word in command for word in ["emotion", "feeling"]):
        return "emotion"
    elif "remember" in command:
        return "remember"
    else:
        return "other"
    




    



  