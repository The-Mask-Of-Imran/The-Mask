import threading
import time
from datetime import datetime
from collections import OrderedDict

class DebugLogger:
    """প্রত্যেকটি রিকোয়েস্টের ডিটেইলস লগ রাখে"""
    
    def __init__(self, max_logs=100):
        self.logs = OrderedDict()
        self.max_logs = max_logs
        self.current_session = None
        self.lock = threading.Lock()
    
    def start_session(self, user_input):
        """নতুন সেশন শুরু"""
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        with self.lock:
            self.current_session = session_id
            self.logs[session_id] = {
                "user_input": user_input,
                "start_time": datetime.now(),
                "end_time": None,
                "status": "running",
                "steps": []
            }
            # পুরনো লগ মুছে ফেলা
            while len(self.logs) > self.max_logs:
                self.logs.popitem(last=False)
        return session_id
    
    def add_step(self, step_name, details=None):
        """একটি স্টেপ লগে যোগ করে"""
        if self.current_session is None:
            return
        
        timestamp = datetime.now()
        time_str = timestamp.strftime("%H:%M:%S.%f")[:-3]
        
        step = {
            "step": step_name,
            "time": time_str,
            "details": details or {}
        }
        
        with self.lock:
            if self.current_session in self.logs:
                self.logs[self.current_session]["steps"].append(step)
        
        # প্রিন্ট করা (ডিবাগিং এর জন্য)
        print(f"[{time_str}] {step_name}")
        if details:
            print(f"    └─ {details}")
    
    def end_session(self, success=True, response=None):
        """সেশন শেষ"""
        if self.current_session is None:
            return
        
        with self.lock:
            if self.current_session in self.logs:
                self.logs[self.current_session]["end_time"] = datetime.now()
                self.logs[self.current_session]["status"] = "success" if success else "failed"
                self.logs[self.current_session]["response"] = response
    
    def get_session_logs(self, session_id):
        """একটি সেশনের সম্পূর্ণ লগ ফেরত দেয়"""
        with self.lock:
            if session_id in self.logs:
                return self.logs[session_id]
        return None
    
    def get_all_logs(self):
        """সব লগ ফেরত দেয়"""
        with self.lock:
            return dict(self.logs)
    
    def format_for_display(self, session_id):
        """লগকে ইউজারের জন্য ফরম্যাট করা টেক্সটে রূপান্তর"""
        session = self.get_session_logs(session_id)
        if not session:
            return "No logs found"
        
        lines = []
        lines.append(f"📋 **প্রশ্ন:** {session['user_input']}")
        lines.append(f"⏰ **শুরু:** {session['start_time'].strftime('%H:%M:%S')}")
        lines.append("")
        lines.append("🔍 **প্রসেসিং স্টেপস:**")
        lines.append("")
        
        for i, step in enumerate(session["steps"], 1):
            lines.append(f"   {i}. {step['step']}  ({step['time']})")
            if step.get("details"):
                for key, val in step["details"].items():
                    if val:
                        lines.append(f"      └─ {key}: {val}")
        
        lines.append("")
        lines.append(f"✅ **স্ট্যাটাস:** {session['status']}")
        if session.get("response"):
            lines.append(f"💬 **উত্তর:** {session['response'][:200]}...")
        
        return "\n".join(lines)

# গ্লোবাল ইনস্ট্যান্স
debug_logger = DebugLogger()