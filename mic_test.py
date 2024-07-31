import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("마이크로 말하세요...")
        recognizer.adjust_for_ambient_noise(source)  # 주변 소음으로부터 적응
        audio = recognizer.listen(source)

    try:
        print("음성 인식 중...")
        text = recognizer.recognize_google(audio, language="ko-KR")
        print(f"인식된 텍스트: {text}")
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"음성 인식 서비스에 접근할 수 없습니다: {e}")

if __name__ == "__main__":
    recognize_speech_from_mic()
