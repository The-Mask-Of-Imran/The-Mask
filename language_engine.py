import requests

class LanguageEngine:
    """বাংলা ↔ ইংরেজি অনুবাদ ইঞ্জিন"""
    
    def __init__(self):
        self.use_gemini = True
    
    def translate_to_english(self, bengali_text):
        """বাংলা থেকে ইংরেজিতে অনুবাদ"""
        if not bengali_text or len(bengali_text.strip()) == 0:
            return bengali_text
        
        try:
            # গুগল ট্রান্সলেট API ব্যবহার (ফ্রি)
            url = "https://translate.googleapis.com/translate_a/single"
            params = {
                "client": "gtx",
                "sl": "bn",
                "tl": "en",
                "dt": "t",
                "q": bengali_text
            }
            response = requests.get(url, params=params, timeout=5)
            if response.status_code == 200:
                result = response.json()
                if result and result[0] and result[0][0]:
                    return result[0][0][0]
        except Exception as e:
            print(f"Translation error (BN->EN): {e}")
        
        return bengali_text
    
    def translate_to_bengali(self, english_text):
        """ইংরেজি থেকে বাংলায় অনুবাদ"""
        if not english_text or len(english_text.strip()) == 0:
            return english_text
        
        try:
            url = "https://translate.googleapis.com/translate_a/single"
            params = {
                "client": "gtx",
                "sl": "en",
                "tl": "bn",
                "dt": "t",
                "q": english_text
            }
            response = requests.get(url, params=params, timeout=5)
            if response.status_code == 200:
                result = response.json()
                if result and result[0] and result[0][0]:
                    return result[0][0][0]
        except Exception as e:
            print(f"Translation error (EN->BN): {e}")
        
        return english_text

language_engine = LanguageEngine()