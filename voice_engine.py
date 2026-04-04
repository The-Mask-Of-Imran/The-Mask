import speech_recognition as sr
import edge_tts
import asyncio
import pygame
import tempfile
import os
import threading
import time

class VoiceEngine:
    VOICES = {
        "পুরুষ (Pradeep)": "bn-BD-PradeepNeural",
        "নারী (Tanishaa)": "bn-BD-TanishaaNeural",
        "সাবলীল (Nabanita)": "bn-IN-NabanitaNeural"
    }
    
    def __init__(self, app):
        self.app = app
        self.recognizer = sr.Recognizer()
        try:
            self.microphone = sr.Microphone()
        except:
            self.microphone = None
            print("⚠️ মাইক্রোফোন পাওয়া যায়নি")
        self.current_voice = "bn-BD-PradeepNeural"
        pygame.mixer.init()

    def set_voice(self, voice_name):
        if voice_name in self.VOICES:
            self.current_voice = self.VOICES[voice_name]
            return f"✅ ভয়েস পরিবর্তন: {voice_name}"
        return "❌ ভয়েস খুঁজে পাওয়া যায়নি"

    def listen_and_transcribe(self):
        if not self.microphone:
            self.app.status_var.set("❌ মাইক্রোফোন নেই")
            return
        
        try:
            self.app.status_var.set("🎤 শুনছি... বাংলায় কথা বলুন")
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            text = self.recognizer.recognize_google(audio, language="bn-BD")
            self.app.status_var.set(f"✅ শুনলাম: {text[:50]}")
            self.app.send_message(text)
        except sr.UnknownValueError:
            self.app.status_var.set("❌ বুঝতে পারিনি, আবার বলুন")
        except sr.RequestError:
            self.app.status_var.set("❌ ইন্টারনেট দরকার")
        except Exception as e:
            self.app.status_var.set(f"⚠️ ভয়েস এরর: {str(e)[:30]}")

    def speak(self, text):
        if text is None:
            text = "উত্তর পাওয়া যায়নি।"
        elif not isinstance(text, str):
            text = str(text)
        
        if not text or len(text.strip()) == 0:
            text = "উত্তর পাওয়া যায়নি।"
        
        try:
            self.app.status_var.set("🔊 উত্তর বলছি...")
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_path = tmp_file.name
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            communicate = edge_tts.Communicate(text, self.current_voice, rate="+5%", volume="+50%")
            loop.run_until_complete(communicate.save(tmp_path))
            loop.close()
            
            for attempt in range(3):
                try:
                    pygame.mixer.music.load(tmp_path)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(0.1)
                    break
                except:
                    time.sleep(0.5)
            
            try:
                os.unlink(tmp_path)
            except:
                pass
                
            self.app.status_var.set("✅ প্রস্তুত")
        except Exception as e:
            self.app.status_var.set(f"⚠️ TTS ব্যর্থ: {str(e)[:30]}")