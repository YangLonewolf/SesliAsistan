import os
import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime
import webbrowser
import arduino
import pyaudio
from selenium import webdriver
import requests
from bs4 import BeautifulSoup



kayit = sr.Recognizer()

def ses_kayit(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""

        try:
            ses = kayit.recognize_google(mikrofon,language="tr-TR")
        except sr.UnknownValueError:
            seslendirme("Yavşak yavşak konuşma")
        except sr.RequestError:
            print("Asistan: Sistem Bağlantısı Koptu")
            seslendirme("Sistem bağlantısı koptu")
        return ses

def seslendirme(metin):

    tts = gTTS(text=metin,lang="tr",slow=False)
    ses = "konusma.mp3"
    tts.save(ses)
    playsound("konusma.mp3")
    os.remove(ses)


def yanit(ses):
    if "merhaba" in ses:
        seslendirme("sanada merhaba dostum")
    if "çıkış" in ses:
        seslendirme("Allaha emanet ol namazlarını aksatma")
        exit()
    if "kafamı bozma" in ses:
        seslendirme("sen kes sesini")
    if "kötüyüm" in ses:
        seslendirme("Allah bazen kullarını imtihan eder bize sabretmek ve tevekkül etmek düşer hocam")
    if "dolar" in ses:
        webbrowser.open("https://www.google.com/search?q=dolar+tl&oq=dolar+&aqs=chrome.1.69i57j0i131i433i512l3j0i433i512j0i67j0i512j69i60.2652j0j7&sourceid=chrome&ie=UTF-8")
    if "teşekkür ederim" in ses or "teşekkürler" in ses:
        seslendirme("Rica Ederim")
    if "google" in ses or "arama yap" in ses:
        seslendirme("Ne aramamı isterseniz")
        veri = ses_kayit()
        seslendirme("{} için bulduklarım".format(veri))
        url = "https://www.google.com/search?q="+veri
        webbrowser.get().open(url)
    if "viedo aç" in ses or "müzik aç" in ses or "youtube aç" in ses:
        seslendirme("Ne açmamı isterseniz")
        veri = ses_kayit()
        seslendirme("{} açılıyor".format(veri))
        url = "https://www.youtube.com/results?search_query="+veri
        webbrowser.get().open(url)
    if "hava" in ses:
        seslendirme("Hava Durumunu Karşınıza Çıkarıyom")
        webbrowser.open("https://www.google.com/search?q=hava+durumu+istanbul&oq=hava+d&aqs=chrome.2.0i67i131i433i457j69i57j0i402l2j0i131i433l2j69i61j69i60.2531j1j7&sourceid=chrome&ie=UTF-8")
    if "hangi gündeyiz" in ses:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi başımın fesi"
        elif today == "Tuesday":
            today = "Salı sallanır"
        elif today == "Wednesday":
            today = "Çarşamba çarşafa dolanır"
        elif today == "Thursday":
            today = "Perşembe perişanlıktır"
        elif today == "Friday":
            today = "Cuma mübarek gündür"
        elif today == "Saturday":
            today = "Cumartesi resmi tatil"
        elif today == "Sunday":
            today = "Pazar resmi tatil"
        seslendirme(today)
    if "saat kaç" in ses:
        seslendirme(datetime.now().strftime("%H:%M"))
    if "namaz" in ses:
        webbrowser.open("https://www.sabah.com.tr/istanbul-namaz-vakitleri")
    if "uygulama aç" in ses:
        seslendirme("Hangi uygulama açılsın")
        runApp = ses_kayit()
        runApp = runApp.lower()
        if "valorant" in runApp:
            os.startfile("C:\Riot Games\Riot Client\RiotClientServices.exe")
        if "welcome to game 2" in runApp:
            os.startfile("steam://rungameid/720250")
        if "ses modu" in runApp:
            os.startfile("C:\Program Files\Voicemod Desktop\VoicemodDesktop.exe")
        if "team" in runApp:
            os.startfile("C:\Program Files\TeamViewer\TeamViewer.exe")
        if "brawlhalla" in runApp:
            os.startfile("steam://rungameid/291550")
        if "whatsapp" in runApp:
            webbrowser.open("https://web.whatsapp.com/")
        if "sptify" in runApp:
            webbrowser.open("https://open.spotify.com/playlist/1PgCypBArpgxRDIjoRDuDq")
    if "ışık aç" in ses:
        try:
            seslendirme("ışıkları açıyorum")
            arduino.led_islemleri(1)
        except:
            seslendirme("LED SİSTEMİ BAĞLI DEĞİL")

    elif "ışık kapat" in ses:
        try:
            seslendirme("ışıkları kapatıyorum")
            arduino.led_islemleri(0)
        except:
            seslendirme("LED SİSTEMİ BAĞLI DEĞİL")


seslendirme("Jarvis Hizmetinizde")
print("Başlatıldı")

while True:
    ses = ses_kayit()
    if bool(ses)==True:
        print(ses)
        ses = ses.lower()
        yanit(ses)
