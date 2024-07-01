import speech_recognition as sr
import webbrowser as web 

# Creamos los objetos para el reconocimiento de voz y el micrófono
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Capturamos el audio desde el micrófono
with mic as source:
    audio = recognizer.listen(source)

# Utilizamos el reconocimiento de voz de Google para convertir el audio en texto
text = recognizer.recognize_google(audio, language="ES")

# Abrimos el navegador web predeterminado y buscamos en Google
# o YouTube según lo que se haya dicho
if text.lower() in ("abre google"):
    web.open("https://www.google.com")
elif text.lower() in ("abre youtube"):
    web.open("https://www.youtube.com")
elif text.lower() in ("abre pl"):
    web.open("https://www.platzi.com")

print(f'Haz dicho: {text}')