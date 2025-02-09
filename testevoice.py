import pyttsx3
import webbrowser
import os
from pytube import Search
from dotenv import load_dotenv
import speech_recognition as sr

load_dotenv()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Fala direito peste.")
            return ""
        except sr.RequestError:
            speak("Desculpe, houve um problema com o serviço de reconhecimento de voz.")
            return ""

def perform_action(action):
    if "abrir youtube" in action:
        webbrowser.open("https://www.youtube.com")
        speak("Abrindo o YouTube para você.")
    elif "abrir google" in action:
        webbrowser.open("https://www.google.com")
        speak("Abrindo o Google.")
    elif "abrir github" in action:
        webbrowser.open("https://www.github.com")
        speak("Abrindo o GitHub.")
    elif "pesquisar" in action:
        search_query = action.split("pesquisar")[1].strip().replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Pesquisando {search_query} no Google.")
    elif "abrir bloco de notas" in action:
        os.system("notepad.exe")
        speak("Abrindo o Bloco de Notas.")
    elif "abrir calculadora" in action:
        os.system("calc.exe")
        speak("Abrindo a Calculadora.")
    elif "desligar" in action:
        os.system("shutdown /s /t 1")
        speak("Desligando o computador.")
    elif "reiniciar" in action:
        os.system("shutdown /r /t 1")
        speak("Reiniciando o computador.")
    elif "tocar" in action and "música" in action:
        song_name = action.split("tocar")[1].strip()
        play_youtube_music(song_name)
    elif "tocar playlist" in action:
        band_name = action.split("playlist")[1].strip()
        open_youtube_playlist(band_name)
    else:
        speak("Desculpe, não consegui entender o comando.")

def open_youtube_playlist(band_name):
    search_query = band_name.replace(" ", "+") + "+playlist"
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    speak(f"Procurando playlists de {band_name} no YouTube.")

def play_youtube_music(song_name):
    search_query = song_name.replace(" ", "+")
    yt_search = Search(search_query)
    video_url = yt_search.results[0].watch_url
    webbrowser.open(video_url)
    speak(f"Agora meu patrão")

if __name__ == "__main__":
    speak("Fala patrão")
    while True:
        command = get_input()
        if command:
            if command in ["sair", "parar", "encerrar"]:
                speak("")
                break
            else:
                perform_action(command)