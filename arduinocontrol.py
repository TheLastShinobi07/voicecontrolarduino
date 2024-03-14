import serial
import time
import speech_recognition as sr


arduino = serial.Serial(port='COM3', baudrate=9600)
time.sleep(2)
def conn(state):
    if "on" in state:
        arduino.write(b'on')
    elif "off" in state:
        arduino.write(b'off')


def speech_rec():
    rec = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as mic:
                print("Listening.............")
                rec.adjust_for_ambient_noise(mic, duration=0.2)
                audio = rec.listen(mic)

                text = rec.recognize_google(audio)
                text = text.lower()
                conn(text)
                if text == "exit":
                    quit()
        except:
            rec = sr.Recognizer()
            continue

if __name__ == "__main__":
    speech_rec()