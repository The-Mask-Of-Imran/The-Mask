import json
import requests

class LocalBrain:
    """লোকাল মডেল ব্যবহার করে স্মার্ট রাউটিং ও ভেরিফিকেশন"""
    
    def __init__(self, model="qwen2.5:3b"):
        self.model = model
        self.ollama_url = "http://localhost:11434/api/generate"
    
    def is_ollama_running(self):
        """Ollama চালু আছে কিনা চেক করে"""
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def analyze_intent(self, prompt, debug_logger=None, session_id=None):
        """ইনপুটের ইনটেন্ট এনালাইসিস করে"""
        if not self.is_ollama_running():
            if debug_logger and session_id:
                debug_logger.add_step("⚠️ লোকাল ব্রেইন", {"স্ট্যাটাস": "Ollama চলছে না, রুল-বেসড মোড"})
            return self._rule_based_analysis(prompt)
        
        system_prompt = """You are The Mask's local brain. Analyze the user input and return ONLY JSON.
        Fields: task_type (CHAT or TASK), needs_memory (true/false), requires_api (true/false)
        """
        
        try:
            response = requests.post(self.ollama_url, json={
                "model": self.model,
                "prompt": f"{system_prompt}\nUser: {prompt}",
                "stream": False
            }, timeout=10)
            
            result = response.json().get("response", "")
            # JSON পার্স করার চেষ্টা
            json_start = result.find("{")
            json_end = result.rfind("}") + 1
            if json_start != -1 and json_end > json_start:
                return json.loads(result[json_start:json_end])
        except Exception as e:
            if debug_logger and session_id:
                debug_logger.add_step("⚠️ Ollama এরর", {"error": str(e)[:50]})
        
        return self._rule_based_analysis(prompt)
    
    def _rule_based_analysis(self, prompt):
        """ফলব্যাক রুল-বেসড এনালাইসিস"""
        prompt_lower = prompt.lower()
        task_keywords = ["বানাও", "তৈরি কর", "অ্যাপ", "সফটওয়্যার", "প্রজেক্ট", "build", "create", "make"]
        memory_keywords = ["মনে রাখ", "সেভ কর", "মেমোরি", "remember", "save"]
        
        return {
            "task_type": "TASK" if any(k in prompt_lower for k in task_keywords) else "CHAT",
            "needs_memory": any(k in prompt_lower for k in memory_keywords),
            "requires_api": True
        }
    
    def verify_response(self, user_prompt, response, debug_logger=None, session_id=None):
        """উত্তর ভেরিফিকেশন করে"""
        if not self.is_ollama_running():
            return True, None
        
        system_prompt = """Analyze if the response correctly answers the user prompt.
        Return JSON: {"correct": true/false, "reason": "why"}"""
        
        try:
            response_req = requests.post(self.ollama_url, json={
                "model": self.model,
                "prompt": f"{system_prompt}\nUser: {user_prompt}\nResponse: {response}",
                "stream": False
            }, timeout=10)
            
            result = response_req.json().get("response", "")
            json_start = result.find("{")
            json_end = result.rfind("}") + 1
            if json_start != -1 and json_end > json_start:
                data = json.loads(result[json_start:json_end])
                return data.get("correct", True), data.get("reason")
        except Exception as e:
            if debug_logger and session_id:
                debug_logger.add_step("⚠️ ভেরিফিকেশন এরর", {"error": str(e)[:50]})
        
        return True, None

local_brain = LocalBrain()