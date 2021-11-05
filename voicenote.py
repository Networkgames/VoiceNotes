# This Python file uses the following encoding: utf-8
import speech_recognition as sr
from gtts import gTTS
import os


while True:
    # wake up call
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Spreche..")
        audio = r.listen(source)
        try:
            print("Die Spracherkennung denkt du sagst: " + r.recognize_google(audio, language="de-DE"))
            data = str(r.recognize_google(audio, language="de-DE"))

            while True:
                # wakeup st
                if "neue notiz" in data or "Neue Notiz" in data:
                    text = "Wie soll deine neue Notiz heißen?"
                    speech = gTTS(lang="de", text=text)
                    speech.save("notiz.mp3")
                    os.system("start notiz.mp3")

                    # wakeup nd
                    with sr.Microphone() as source:
                        print("Spreche..")
                        audio = r.listen(source)
                        try:
                            print("Die Spracherkennung denkt du sagst: " + r.recognize_google(audio, language="de-DE"))
                            data = str(r.recognize_google(audio, language="de-DE"))

                            text = f"Dein Name ist {data}, richtig?"
                            speech = gTTS(lang="de", text=text)
                            speech.save("notiz.mp3")
                            os.system("start notiz.mp3")

                            # wakeup rd
                            with sr.Microphone() as source:
                                print("Spreche..")
                                audio = r.listen(source)
                                try:
                                    print("Die Spracherkennung denkt du sagst: " +
                                          r.recognize_google(audio, language="de-DE"))
                                    data = str(r.recognize_google(audio, language="de-DE"))

                                    if "ja" in data:
                                        text = "Welcher Text soll deine Notiz beinhalten?"
                                        speech = gTTS(lang="de", text=text)
                                        speech.save("notiz.mp3")
                                        os.system("start notiz.mp3")

                                        file = open("notiz.txt", "w")
                                        file.write(data)
                                        file.close()
                                    else:
                                        break
                                except sr.UnknownValueError:
                                    print("Die Spracherkennung konnte das Audio nicht verstehen")
                                except sr.RequestError as e:
                                    print(
                                        "Ergebnisse vom Google-Spracherkennungsdienst konnten nicht angefordert werden; {0}".format(
                                            e))

                        except sr.UnknownValueError:
                            print("Die Spracherkennung konnte das Audio nicht verstehen")
                        except sr.RequestError as e:
                            print(
                                "Ergebnisse vom Google-Spracherkennungsdienst konnten nicht angefordert werden; {0}".format(
                                    e))


        except sr.UnknownValueError:
            print("Die Spracherkennung konnte das Audio nicht verstehen")
        except sr.RequestError as e:
            print("Ergebnisse vom Google-Spracherkennungsdienst konnten nicht angefordert werden; {0}".format(e))
