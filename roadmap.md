
The Mask Roadmap V-10.00.01



💡 কীভাবে আপনি AI কে নির্দেশ দেবেন (আপনার জন্য প্রম্পট)?
শেষের এই কাজগুলো করার সময় AI কে নিচের প্রম্পটটি দিন:
"আমি The Mask প্রজেক্ট বানাচ্ছি। উপরের মাস্টার রোডম্যাপ থেকে [এখানে সাব-টাস্কের নাম লিখুন, যেমন: সাব-টাস্ক ১০.১] ইমপ্লিমেন্ট করতে চাই। আমার দেওয়া Strict Logic এবং File Path মেনে সম্পূর্ণ কোডটি লিখে দাও। ফাইলের নামগুলো যেন ঠিক থাকে। বিশেষ করে থ্রেডিং (Threading) এবং GUI আপডেটের সময় যেন root.after() ব্যবহার করা হয়, যাতে অ্যাপ ফ্রিজ না করে।"


Roadmap




🟢 ফিচার ১: বেস GUI, ভয়েস ইন্টিগ্রেশন এবং অ্যাডভান্সড API ম্যানেজার
এই ফিচারটিকে আমরা ৪টি ছোট টাস্কে ভাগ করব।
🛠️ সাব-টাস্ক ১.১: Core GUI এবং Database Setup
কীভাবে কাজ করবে: অ্যাপটি ওপেন করলে একটি সুন্দর ডার্ক মোড চ্যাট উইন্ডো আসবে। বাম পাশে একটি স্লাইডিং সাইডবার (Grok স্টাইল) থাকবে। ব্যবহারকারী যা চ্যাট করবে তা ডাটাবেসে সেভ হবে। অ্যাপ রিস্টার্ট করলে পুরনো মেসেজগুলো লোড হবে।
উদাহরণ: আপনি "Hello" লিখলেন, অ্যাপ সেটা ডাটাবেসে সেভ করবে এবং স্ক্রিনে দেখাবে।
নন-টেক মানুষের জন্য গাইড (ক্লিক-বাই-ক্লিক):
আপনার কম্পিউটারে TheMask নামে একটি ফোল্ডার তৈরি করুন।
AI-কে বলুন "সাব-টাস্ক ১.১ এর কোড দাও"।
AI যে কোড দেবে, সেটি TheMask.py ফাইলে সেভ করুন।
টার্মিনাল/CMD তে python TheMask.py লিখে এন্টার দিন। উইন্ডো ওপেন হবে।


AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/TheMask.py, TheMask/ui_components.py
Database: TheMask/TheMask.db (Table: conversations with columns: id, user_msg, assistant_msg, time).
Logic: Use customtkinter (dark-blue theme). Create class TheMask:. Initialize DB in __init__. Add a sliding sidebar. Load previous 30 messages from DB on startup. Ensure non-blocking threading for sending messages.


 সাব-টাস্ক ১.২: Advanced API Manager (13+ Providers, Category Tags & Auto-Test Colors)
কীভাবে কাজ করবে: সেটিংসে একটি বিশাল প্যানেল থাকবে যেখানে OpenAI, DeepSeek, HuggingFace, TogetherAI, StabilityAI, Replicate, Groq, ElevenLabs, Anthropic, XAI, Cohere সহ ১৩+ প্রোভাইডারের API বসানো যাবে। লিস্টে ↑ ↓ বাটন দিয়ে কোন API আগে ব্যবহার হবে তা (Priority) ঠিক করা যাবে।
ক্যাটাগরি ট্যাগিং: API সেভ করার সময় সিলেক্ট করা যাবে এটি কোন কাজের জন্য (General, Dev, Pentest/Uncensored)।
অটো-টেস্ট ও কালার কোড: ব্যাকগ্রাউন্ডে প্রতি ১ ঘণ্টায় API গুলো চেক হবে। চেক হওয়ার পর লিস্টে কালার দিয়ে স্ট্যাটাস বোঝাবে: 🟢 Active (সব ঠিক আছে), 🟡 Limit Reached (লিমিট শেষ), 🔴 Error (ভুল API বা কাজ করছে না)।
উদাহরণ: আপনি Grok-কে "Pentest" ট্যাগ দিয়ে রাখলেন। অ্যাপ প্রতি ঘণ্টায় চেক করে দেখবে Key টি '🟢 Active' নাকি '🟡 Limit Reached'। লিমিট শেষ হলে সে নিজে থেকেই পরের API তে শিফট করবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "সাব-টাস্ক ১.২ এর Category Tagging, 13+ Providers এবং Color Status Indicator (🟢🟡🔴) সহ কোড দাও"।
সেটিংস থেকে API Key বসিয়ে ট্যাগ সিলেক্ট করে সেভ করুন।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/api_manager.py, Config: TheMask/config.json
Logic: Support 13+ providers. Add a Category dropdown (General, Dev, Pentest). UI must have Up (↑) and Down (↓) buttons for priority. Run auto_check_and_test_apis() every 3600s. Update status labels dynamically using colors: 🟢 Active (Success), 🟡 Limit Reached (429/Quota limits), 🔴 Error (Auth/Other fails). Save tags and statuses in config.json.
🛠️ সাব-টাস্ক ১.৩: Smart Bulk API Import & Auto-Detector
কীভাবে কাজ করবে: সেটিংসে "Bulk Import" বাটনে ক্লিক করলে একটি বড় টেক্সট বক্স আসবে। সেখানে একসাথে এলোমেলোভাবে ২০-৩০টি API Key পেস্ট করলে, সিস্টেম নিজে নিজে স্ক্যান করবে।
কোন Key কোন প্রোভাইডারের (যেমন sk-or-... হলে OpenRouter, sk-ant-... হলে Anthropic) তা সে নিজে ধরে ফেলবে এবং ডিফল্ট মডেল বসিয়ে দেবে।
এরপর সবগুলো Key স্ক্যান করে টেস্ট করবে। যেগুলো 🟢 Active সেগুলো লিস্টে অ্যাড করে নেবে।
যেগুলো কাজ করবে না বা 🔴 Error, সেগুলোর একটি লিস্ট পপ-আপ মেসেজে দেখাবে (যেমন: "৩টি API কাজ করেনি: sk-abc... (Invalid Key)")।
উদাহরণ: আপনি একসাথে OpenAI এবং Gemini এর Key পেস্ট করলেন। অ্যাপ নিজে প্রোভাইডার বের করে টেস্ট করে সঠিকগুলো রেখে ভুলগুলোর লিস্ট আপনাকে দেখিয়ে দেবে।
নন-টেক মানুষের জন্য গাইড:
সেটিংসে গিয়ে "Bulk Import" এ ক্লিক করে অনেকগুলো Key দিন।
Import বাটনে ক্লিক করুন এবং স্ক্যান শেষ হলে রিপোর্ট দেখুন।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/api_manager.py
Logic: Function bulk_import_apis(keys_text). Extract keys using regex or splitting. Auto-detect provider based on key prefixes (e.g., sk-ant- -> Anthropic, sk-or- -> OpenRouter). Test each key concurrently or sequentially. Append valid keys to self.saved_apis with 🟢 Active. Collect invalid keys and display a messagebox.showwarning listing the exact keys and their error reasons.


🛠️ সাব-টাস্ক ১.৪: Voice I/O (ভয়েস কন্ট্রোল)
কীভাবে কাজ করবে: চ্যাট বক্সের পাশে একটি 'মাইক' আইকন থাকবে। সেখানে ক্লিক করে বাংলায় কথা বললে তা টেক্সট হয়ে যাবে। উত্তর আসার পর অ্যাপ সেটি বাংলায় পড়ে শোনাবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "ভয়েস ফিচার অ্যাড করো"।
মাইক আইকনে ক্লিক করে কথা বলুন।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/TheMask.py (UI update), TheMask/voice_engine.py (New file).
Logic: Use SpeechRecognition library for STT (Speech-to-Text) with language='bn-BD'. Use edge-tts (asynchronous) for TTS (Text-to-Speech) in Bengali (bn-BD-PradeepNeural). Run TTS in a separate thread to prevent GUI freezing.



🟢 ফিচার ২: ল্যাঙ্গুয়েজ ইঞ্জিন এবং টোকেন অপটিমাইজার
এই ফিচারটিকে ২টি সাব-টাস্কে ভাগ করব।
🛠️ সাব-টাস্ক ২.১: Translation Engine (BN ➔ EN ➔ BN)
কীভাবে কাজ করবে: ইউজার বাংলায় প্রশ্ন করলে, টোকেন ও খরচ বাঁচাতে সিস্টেম ব্যাকগ্রাউন্ডে তা ইংরেজিতে অনুবাদ করে API এর কাছে পাঠাবে। API ইংরেজিতে উত্তর দিলে, সিস্টেম আবার তা বাংলায় অনুবাদ করে ইউজারকে দেখাবে।
উদাহরণ: ইউজার: "তুমি কেমন আছো?" ➔ System translates: "How are you?" ➔ API responds: "I am fine" ➔ System translates & shows: "আমি ভালো আছি।"
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "সাব-টাস্ক ২.১ এর language_engine.py তৈরি করো"।
এরপর চ্যাট করে দেখুন বাংলা কতটা দ্রুত এবং নির্ভুল আসছে।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/language_engine.py
Logic: Create class Translator:. Use a free/fast API (like googletrans fallback, or Groq Llama-3 if configured) for translation. Methods: translate_to_english(bn_text) and translate_to_bengali(en_text). Integrate this transparently inside the send_message processing pipeline in TheMask.py.


🛠️ সাব-টাস্ক ২.২: Context Summarizer (Token Optimizer)
কীভাবে কাজ করবে: আপনার চ্যাট হিস্ট্রি যদি অনেক বড় হয়ে যায় (যেমন ৫০টা মেসেজ), তখন API তে পাঠালে অনেক খরচ হবে। তাই এটি পুরোনো মেসেজগুলোর একটি "সারসংক্ষেপ" (Summary) তৈরি করে পাঠাবে।
উদাহরণ: পুরোনো ২০টি মেসেজের বদলে শুধু একটি লাইন পাঠাবে: "ইউজার এবং AI এর মধ্যে অ্যাপ ডেভেলপমেন্ট নিয়ে কথা হচ্ছে"।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Context Summarizer" লজিক tools.py তে অ্যাড করতে।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/tools.py
Logic: Create function optimize_context(chat_history, max_tokens=2000). If character count > 8000, trigger a background LLM call saying: "Summarize the following chat history briefly". Replace the first N messages of chat_history with this summary before making the main API call.



🟢 ফিচার ৩: The Local Brain & Smart Routing
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব।

🛠️ সাব-টাস্ক ৩.১: The 5B Local Brain Analysis (স্মার্ট ডিসিশন মেকার)
কীভাবে কাজ করবে: ইউজারের ইনপুট আসার পর কোনো সাধারণ কিওয়ার্ড না খুঁজে, সিস্টেম একটি ছোট কিন্তু অত্যন্ত বুদ্ধিমান ৫B মডেল (যেমন: Qwen 2.5 3B/5B) দিয়ে এটি এনালাইসিস করবে।
ধাপসমূহ: ১. ইনপুট ইংরেজিতে ট্রান্সলেট হবে ➔ ২. ৫B মডেল এনালাইসিস করে বুঝবে এটি টাস্ক নাকি চ্যাট ➔ ৩. সে বুঝবে মেমোরি লাগবে কিনা ➔ ৪. সে বুঝবে নতুন কিছু শেখার আছে কিনা ➔ ৫. সে বুঝবে বড় মডেল লাগবে নাকি ফ্রি API/Scraping দিয়ে হবে ➔ ৬. এরপর সে মূল প্রম্পট তৈরি করে রাউট করবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Rule-based এর বদলে Ollama/llama.cpp দিয়ে 5B Local Brain Analysis এর কোড লেখো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/local_brain.py
Logic: Replace pure python rule-based routing. Use a lightweight local LLM (via ollama or llama.cpp). Feed the translated English input to the local model with a strict JSON system prompt. The model must return JSON: {"task_type": "BIG_TASK/CHAT", "needs_memory": true/false, "learning_extraction": "data", "requires_heavy_api": true/false, "routing_target": "API/Scraper/Local"}. Parse this JSON to direct the workflow.

🛠️ সাব-টাস্ক ৩.২: Smart API Routing & Fallback Logic
কীভাবে কাজ করবে: রাউটার সিদ্ধান্ত নেওয়ার পর দেখবে কোন API তে কাজ পাঠাবে। সে সবসময় আগে ফ্রি API (OpenRouter free) ট্রাই করবে। ফ্রি কাজ না করলে বা লিমিট শেষ হলে Paid API ট্রাই করবে।
উদাহরণ: OpenRouter Free তে সার্ভার ডাউন। সিস্টেম ক্র্যাশ না করে সাথে সাথে Gemini Free তে মেসেজ পাঠিয়ে উত্তর আনবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Smart API Fallback লজিক api_manager.py তে ইমপ্লিমেন্ট করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/api_manager.py
Logic: Update call_llm(prompt, category). Loop through self.saved_apis. Try the first status == "🟢 Active". Catch RateLimitError or ConnectionError. If error occurs, change that API's status to "🔴 Error", save config.json, and continue to the next API in the list.


🛠️ সাব-টাস্ক ৩.৩: Semantic Verification Loop (লোকাল মডেল দিয়ে ক্রস-চেক)
কীভাবে কাজ করবে: বড় মডেল বা ইন্টারনেট স্ক্র্যাপিং থেকে উত্তর আসার পর, সিস্টেম সরাসরি আপনাকে দেখাবে না। ছোট ৫B মডেলটি প্রথমে উত্তরটি পড়বে এবং ইউজারের মূল প্রশ্নের সাথে মিলিয়ে দেখবে উত্তরটি প্রাসঙ্গিক এবং সঠিক কিনা। যদি ভুল বা আবোল-তাবোল লাগে, সে নিজে নিজে বড় মডেলকে বলবে "তোমার উত্তর ভুল, আবার জেনারেট করো"।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "লোকাল মডেল দিয়ে Semantic Verification Loop তৈরি করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/local_brain.py
Logic: Method verify_response_semantically(user_prompt, api_response). Pass both to the 5B local model with the prompt: "Analyze if the api_response perfectly answers the user_prompt without hallucinations. Reply ONLY with YES or NO_BECAUSE:[reason]". If NO, loop the rejection reason back to the main API for a retry (max 3 times).

🛠️ সাব-টাস্ক ৩.৪: লোকাল মডেলের কন্টিনিউয়াস লার্নিং এবং অ্যাকুরেসি অপটিমাইজেশন (নতুন)
কীভাবে কাজ করবে: লোকাল ৫B মডেল প্রতিটি টাস্ক, রিফ্লেকশন, এরর লগ, এজেন্ট ফিডব্যাক থেকে অটোমেটিক লার্ন করবে। ফুল ফাইন-টিউনিং না করে RAG + Experience Layer (Layer 4) + synthetic reflection data ব্যবহার করে দ্রুত আপডেট হবে। এতে মডেল আরও ফাস্ট ও অ্যাকুরেট হয়।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন “সাব-টাস্ক ৩.৪ এর Continuous Learning লজিক local_brain.py তে অ্যাড করো”।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/local_brain.py
Logic: প্রতি ১০০ টাস্ক পর পর experience_layer থেকে নতুন synthetic training data তৈরি করে RAG index আপডেট করো। Fine-tuning এর পরিবর্তে “memory replay + reflection prompting” ব্যবহার করো যাতে মডেল নিজে নিজে আরও স্মার্ট হয়।

🟢 ফিচার ৪: অমর মেমোরি (৫-স্তরের ChromaDB RAG)
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব। এটি অ্যাপের "ব্রেইন" হিসেবে কাজ করবে।
🛠️ সাব-টাস্ক ৪.১: ChromaDB এবং ৫টি লেয়ার সেটআপ
কীভাবে কাজ করবে: অ্যাপের ভেতরে একটি ডাটাবেস তৈরি হবে যা টেক্সট মনে রাখতে পারে (Vector DB)। এখানে ৫টি আলাদা বাক্স (Layer) থাকবে: Identity, Knowledge, Tasks, Experience এবং Context। অ্যাপ প্রথমবার চালু হলে Identity বক্সে তার নিজের নাম ও রুলস সেভ হয়ে যাবে।
উদাহরণ: অ্যাপ জানবে তার নাম "The Mask" এবং তার কাজ বাংলায় হেল্প করা। অ্যাপ বন্ধ করে খুললেও সে এটা ভুলবে না।
নন-টেক মানুষের জন্য গাইড (ক্লিক-বাই-ক্লিক):
AI-কে বলুন "সাব-টাস্ক ৪.১ এর memory_manager.py এর কোড দাও"।
AI যে কোড দেবে, তা memory_manager.py ফাইলে সেভ করুন।
একবার মেইন অ্যাপ (TheMask.py) রান করুন, দেখবেন chroma_db নামে একটি ফোল্ডার নিজে নিজে তৈরি হয়েছে।


AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/memory_manager.py
Logic: Create class MemoryManager:. Use chromadb.PersistentClient(path="chroma_db"). Initialize 5 collections: layer1_identity, layer2_knowledge, layer3_tasks, layer4_experience, layer5_context. Write initialize_identity() to check if layer1_identity is empty; if yes, add the core system prompt ("তুমি The Mask...").


🛠️ সাব-টাস্ক ৪.২: Save & Retrieve Logic (মেমোরি সেভ ও খোঁজার নিয়ম)
কীভাবে কাজ করবে: যখনই গুরুত্বপূর্ণ কথা হবে, সিস্টেম নিজে থেকে তা সঠিক লেয়ারে সেভ করবে। আবার নতুন প্রশ্ন এলে সে ডাটাবেস থেকে প্রাসঙ্গিক পুরনো কথা খুঁজে বের করবে (RAG - Retrieval-Augmented Generation)।
উদাহরণ: আপনি বললেন, "আমার প্রিয় রং লাল।" সিস্টেম এটি Layer 2-তে সেভ করবে। ২ দিন পর জিজ্ঞেস করলে সে ডাটাবেস থেকে খুঁজে বলবে, "আপনার প্রিয় রং লাল।"
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "memory_manager.py তে Save এবং Retrieve ফাংশন যুক্ত করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/memory_manager.py
Logic: Add save_memory(layer, text, metadata) to add documents with timestamps. Add retrieve_relevant(query, n_results=5) which queries the collections (primarily Layer 2, 3, and 4) using ChromaDB’s built-in embedding and returns a concatenated string of the most relevant past contexts.


🛠️ সাব-টাস্ক ৪.৩: মেমোরি ইন্টিগ্রেশন (মেইন চ্যাটের সাথে যুক্ত করা)
কীভাবে কাজ করবে: আপনি কিছু লিখলে, মেসেজটি API-এর কাছে যাওয়ার ঠিক আগে, মেমোরি থেকে খুঁজে পাওয়া তথ্যগুলো মেসেজের সাথে লুকিয়ে জুড়ে দেওয়া হবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "মেইন চ্যাট প্রসেসিং-এ RAG মেমোরি ইন্টিগ্রেট করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/TheMask.py
Logic: In the process(user_input) thread, before calling self.api.call_llm(), call self.memory.retrieve_relevant(user_input). Append this retrieved context to the system_prompt dynamically: f"System: ...\n\nRelevant Past Memory: {retrieved_memory}\n\nUser: {user_input}".


🛠️ সাব-টাস্ক ৪.৪: Memory Pruning & Decay (স্মার্ট মেমোরি ক্লিনআপ)
কীভাবে কাজ করবে: সিস্টেম নিজে থেকে প্রতি ২৪ ঘণ্টা পর পর মেমোরি চেক করবে। চ্যাটের পুরনো কথাগুলো (যা আর দরকার নেই) সে নিজে থেকে ডিলিট করে দেবে এবং সামারি করে ছোট করে রাখবে, যাতে ডাটাবেস কখনো স্লো না হয়।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন "ChromaDB এর জন্য Auto-Pruning এবং Memory Decay লজিক memory_manager.py তে অ্যাড করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/memory_manager.py
Logic: Implement a background thread prune_memory(). For layer5_context, delete messages older than 48 hours. For layer4_experience, summarize older logs using the local 5B model and move the summary to layer2_knowledge, then delete the raw logs from layer 4.


🟢 ফিচার ৫: টাস্ক ব্রেকডাউন + জিরো-এরর রিফ্লেকশন লুপ
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব। এটি স্বাধীনভাবে কাজ করার ইঞ্জিন।
🛠️ সাব-টাস্ক ৫.১: Task Database & Goal Breakdown (কাজ ভাঙা)
কীভাবে কাজ করবে: আপনি বড় কাজ দিলে (যেমন: "একটি গেম বানাও"), সিস্টেম নিজে নিজে এটিকে ৫-৬টি ছোট ছোট সাব-টাস্কে ভাগ করবে এবং SQLite ডাটাবেসে সেভ করবে।
উদাহরণ: গেম বানানোর টাস্ক ভাঙবে: ১. ফোল্ডার বানানো, ২. UI ডিজাইন, ৩. গেম লজিক, ৪. টেস্টিং।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "সাব-টাস্ক ৫.১ এর টাস্ক ব্রেকডাউন লজিক এবং ডাটাবেস টেবিল তৈরি করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_dev.py (New file) and TheMask/TheMask.py (DB init).
Logic: Create SQLite table tasks (id INTEGER PRIMARY KEY, goal TEXT, subtask TEXT, status TEXT, attempts INTEGER). Write function breakdown_task(goal) that prompts the LLM to return a JSON array of subtasks. Parse the JSON and insert rows into the tasks table with status "Pending".


🛠️ সাব-টাস্ক ৫.২: Execution & Reflection Loop (কাজ করা ও চেক করা)
কীভাবে কাজ করবে: সিস্টেম ডাটাবেস থেকে প্রথম "Pending" কাজ নেবে। কাজটা করবে। তারপর সে নিজেই নিজেকে প্রশ্ন করবে, "কাজটা কি ঠিক হলো?" যদি ঠিক হয়, স্ট্যাটাস হবে "Completed"। ভুল হলে আবার করবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Execution and Reflection Loop কোড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_dev.py
Logic: Create run_agent_loop(). SELECT * FROM tasks WHERE status='Pending' LIMIT 1. Pass the subtask to LLM. Then, pass the LLM's output to a Reflection prompt: "Evaluate this output. Is it complete and error-free? Answer YES or NO with reasons". If YES, UPDATE status='Completed'. If NO, increment attempts.


🛠️ সাব-টাস্ক ৫.৩: 10-Try Rule & Model Fallback (নাছোড়বান্দা লজিক)
কীভাবে কাজ করবে: যদি কোনো কাজ বারবার ভুল হয় (Reflection এ NO আসে), সে ৩ বার একই API দিয়ে ট্রাই করবে। ৩ বারেও না পারলে সে অন্য API (যেমন Gemini থেকে OpenRouter) তে সুইচ করবে। মোট ১০ বার চেষ্টা করবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "১০ বারের রুল এবং মডেল ফলব্যাক লজিক যুক্ত করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_dev.py
Logic: In the run_agent_loop(), if attempts >= 3, trigger self.api.switch_to_next_provider(). If attempts >= 10, change status to "Failed_Needs_Human" and alert the GUI. Save all reflections in Memory Layer 4 (Experience) so it learns what not to do next time.



🟢 ফিচার ৬: টুল কলিং এবং সফটওয়্যার ডেভেলপমেন্ট এজেন্ট
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব। এর মাধ্যমে AI কম্পিউটারে ফাইলের কাজ করতে পারবে।
🛠️ সাব-টাস্ক ৬.১: Basic Tool Setup (File I/O & Web Browse)
কীভাবে কাজ করবে: AI চাইলে আপনার কম্পিউটারে টেক্সট ফাইল তৈরি করতে পারবে, পড়তে পারবে এবং ইন্টারনেট থেকে ওয়েবসাইটের তথ্য পড়ে আসতে পারবে।
উদাহরণ: আপনি বললেন, "আজকের খবর একটি text ফাইলে সেভ করো।" সে ইন্টারনেট থেকে খবর পড়ে news.txt নামে সেভ করবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "File Read/Write এবং Web Browse টুল tools.py তে অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/tools.py
Logic: Create class ToolManager:. Add functions: write_file(path, content), read_file(path), and browse_web(url). Use requests and BeautifulSoup for browse_web to extract plain text. Ensure file paths are restricted to the projects/ or current working directory for safety.


🛠️ সাব-টাস্ক ৬.২: Code Execution Sandbox (নিরাপদ কোড রানার)
কীভাবে কাজ করবে: AI যদি পাইথন কোড লেখে, সে নিজেই সেটি রান করে দেখবে এরর (Error) আছে কিনা। ব্যাকগ্রাউন্ডে একটি নিরাপদ জায়গায় (subprocess) কোড রান হবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Code Execution Tool তৈরি করো tools.py তে"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/tools.py
Logic: Add function execute_code(script_path). Use python's subprocess.run(..., capture_output=True, text=True, timeout=15). Return stdout if successful, or stderr if it crashes. This output will be fed back to the Reflection Loop (Sub-task 5.2) so the AI can debug its own errors.


🛠️ সাব-টাস্ক ৬.৩: Software Generation Pipeline (প্রজেক্ট ফোল্ডার মেকার)
কীভাবে কাজ করবে: যখন আপনি বড় কোনো প্রজেক্ট বানাতে দেবেন, এটি projects/ ফোল্ডারের ভেতর ওই প্রজেক্টের নামে নতুন ফোল্ডার খুলবে এবং সবগুলো ফাইল (যেমন: main.py, ui.py, requirements.txt) সেখানে তৈরি করে সেভ করবে।
উদাহরণ: "টুডু অ্যাপ বানাও" ➔ projects/todo_app/ ফোল্ডার তৈরি হবে এবং ভেতরে সব কোড থাকবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "সফটওয়্যার জেনারেশন পাইপলাইন এবং ফোল্ডার মেকার তৈরি করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_dev.py
Logic: Create function setup_project_workspace(project_name). Create a directory TheMask/projects/{project_name}. Instruct the LLM in the system prompt: "You are an expert developer. You must use the write_file tool to save your code into projects/{project_name}/...". Validate that all requested files exist after the task loop finishes.

🛠️ সাব-টাস্ক ৬.৪: Virtual Environment (venv) & Auto-Dependency Installer
কীভাবে কাজ করবে: সিস্টেম যখন কোনো সফটওয়্যার বানাবে, তখন সে ওই প্রজেক্টের ভেতরে একটি আলাদা 'venv' তৈরি করবে এবং নিজে নিজেই প্রয়োজনীয় লাইব্রেরি (pip install) করে নেবে। এতে আপনার মূল কম্পিউটারের কোনো ক্ষতি হবে না।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন "Python venv creation এবং requirements.txt auto-install লজিক agent_dev.py তে অ্যাড করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_dev.py, TheMask/tools.py
Logic: Before executing code in sandbox, run python -m venv venv inside the projects/{project_name} directory. Parse the generated requirements.txt and run venv/bin/pip install -r requirements.txt. All execute_code() calls must use the python executable inside this isolated venv.


🟢 ফিচার ৭: মাল্টি-এজেন্ট UI (Grok-Style) এবং স্পেশালাইজড এজেন্টস
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব। এর ফলে অ্যাপের ভেতরে আলাদা আলাদা কাজের জন্য আলাদা "AI কর্মী" (Agent) তৈরি করা যাবে।
🛠️ সাব-টাস্ক ৭.১: Multi-Agent UI (সাইডবারে আলাদা চ্যাট উইন্ডো)
কীভাবে কাজ করবে: বাম পাশের সাইডবারে "New Agent" বাটনে ক্লিক করলে একটি পপ-আপ আসবে। সেখানে আপনি এজেন্টের নাম (যেমন: "Developer Agent") দিয়ে নতুন একটি চ্যাট সেশন খুলতে পারবেন। মেইন চ্যাট এবং অন্য এজেন্টের চ্যাট আলাদা থাকবে।
উদাহরণ: মেইন চ্যাটে আপনি সাধারণ কথা বলছেন, আর "Video Agent"-এর চ্যাটে ভিডিও বানানোর নির্দেশ দিয়ে রেখেছেন। দুটো আলাদাভাবে কাজ করবে।
নন-টেক মানুষের জন্য গাইড (ক্লিক-বাই-ক্লিক):
AI-কে বলুন "সাব-টাস্ক ৭.১ এর মাল্টি-এজেন্ট সাইডবার UI ইমপ্লিমেন্ট করো"।
কোডটি বসিয়ে অ্যাপ রান করুন। সাইডবারে 'New Agent' বাটনে ক্লিক করে নতুন সেশন তৈরি করে দেখুন।


AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/TheMask.py, TheMask/ui_components.py
Logic: Update the UI to handle multiple chat sessions. Maintain a dictionary self.agent_sessions = {"Main": chat_history_list}. Clicking "New Agent" creates a new button in the sidebar. Clicking an agent's button clears the current CTkTextbox and loads that specific agent's history. Ensure threading does not overlap between agents.


🛠️ সাব-টাস্ক ৭.২: Advanced YouTube Automation (ভয়েসওভার, মিউজিক ও শিডিউলিং)
কীভাবে কাজ করবে: এটি ৫ মিনিটের ভিডিওর স্ক্রিপ্টকে ৫ সেকেন্ডের ছোট প্রম্পটে ভাঙবে ➔ API দিয়ে ভিডিও বানাবে ➔ ElevenLabs দিয়ে ভয়েসওভার বানাবে ➔ ফ্রি ব্যাকগ্রাউন্ড মিউজিক (BGM) অ্যাড করবে ➔ moviepy দিয়ে সব জোড়া লাগাবে ➔ থাম্বনেইল বানাবে ➔ এবং শিডিউল সেট করে আপলোড করবে।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন "YouTube Agent-এ ElevenLabs Voiceover এবং BGM mixing অ্যাড করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_youtube.py
Logic: Extend the pipeline: Add generate_voiceover(script) using ElevenLabs API. Use moviepy.editor.AudioFileClip to merge the generated video clips, voiceover, and a low-volume looping BGM track.


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/local_brain.py
Logic: Method verify_response_semantically(user_prompt, api_response). Pass both to the 5B local model with the prompt: "Analyze if the api_response perfectly answers the user_prompt without hallucinations. Reply ONLY with YES or NO_BECAUSE:[reason]". If NO, loop the rejection reason back to the main API for a retry (max 3 times).


🛠️ সাব-টাস্ক ৭.৩: Deep Cyber Security Agent (সোর্স কোড এনালাইসিস ও রোডম্যাপ)
কীভাবে কাজ করবে: এই এজেন্ট শুধু লিনাক্স কমান্ড চালাবে না। আপনি কোনো সফটওয়্যারের ফাইল দিলে সে পুরো সোর্স কোড পড়ে সিকিউরিটি বাগ বের করবে। সে নিজে নিজে হ্যাকিংয়ের একটি রোডম্যাপ বানাবে। কাজ শেষে সে লোকাল মডেলকে (Local Brain) রিপোর্ট করবে। লোকাল মডেল চেক করে যদি দেখে কাজ ঠিক হয়নি, তবে এজেন্টকে আবার নতুন রোডম্যাপ দিয়ে কাজ করতে পাঠাবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Cyber Security Agent-এ Source Code Analysis এবং Local Model Verification Loop যুক্ত করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_cyber.py
Logic: Implement SAST (Static Application Security Testing) by allowing the agent to recursively read directory files. The agent must first generate a pentest_roadmap.json. After execution, the output is sent to local_brain.py for verification. If the local brain detects false positives or incomplete execution, it generates an updated prompt and re-triggers the agent. Use APIs tagged with Pentest.




🟢 ফিচার ৮: লাইভ ব্রাউজার এজেন্ট ও ডেটা স্ক্র্যাপিং (Playwright)
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব। এটি অ্যাপকে ইন্টারনেটে মানুষের মতো ব্রাউজ করার ক্ষমতা দেবে।
🛠️ সাব-টাস্ক ৮.১: Playwright Setup & Basic Scraping (ব্রাউজার খোলা ও ডেটা নেওয়া)
কীভাবে কাজ করবে: আপনি বললে অ্যাপ ব্যাকগ্রাউন্ডে বা সামনে গুগল ক্রোম (বা অন্য ব্রাউজার) খুলে কোনো ওয়েবসাইটে যাবে এবং সেখান থেকে তথ্য কপি করে আনবে।
উদাহরণ: "দারাজ থেকে আইফোন ১৫ এর দাম কত দেখো।" অ্যাপ নিজে দারাজে যাবে, সার্চ করবে এবং দাম বের করে আনবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "সাব-টাস্ক ৮.১ এর Playwright বেসিক স্ক্র্যাপিং browser_agent.py তে তৈরি করো"।
টার্মিনালে pip install playwright এবং playwright install লিখে রান করে নিন।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/browser_agent.py (New file)
Logic: Create class BrowserAgent:. Use playwright.sync_api. Implement functions: open_browser(), navigate_to(url), extract_text(selector). Run the Playwright instance inside a separate thread so it doesn't block the customtkinter GUI.


🛠️ সাব-টাস্ক ৮.২: Human-like Interaction & Captcha Handling (মানুষের মতো ব্রাউজিং ও ক্যাপচা)
কীভাবে কাজ করবে: ওয়েবসাইটে যেন একে রোবট মনে না হয়, তাই এটি মাউস আঁকাবাঁকা করে চালাবে এবং টাইপ করার সময় একটু দেরি (delay) করবে। যদি ওয়েবসাইটের ক্যাপচা (Robot check) আসে, তবে সে সেখানে থেমে যাবে এবং আপনাকে বলবে, "স্যার, ক্যাপচা এসেছে, দয়া করে সলভ করে দিন।"
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Human-like interaction এবং Captcha handling লজিক অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/browser_agent.py
Logic: Add random delays time.sleep(random.uniform(0.5, 2.0)) between actions. Add simulated mouse movements. Implement detect_captcha() which looks for common iframe selectors (e.g., reCAPTCHA, Cloudflare turnstile). If detected, pause the script, send a message to TheMask.py GUI to alert the user, and wait for a UI button "Captcha Solved" to resume execution.


🛠️ 🛠️ সাব-টাস্ক ৮.৩: Autonomous Practice & Self-Learning Loop
কীভাবে কাজ করবে: আপনি যদি তাকে বলেন, "অমুক ওয়েবসাইটে গিয়ে এই কাজটা করো", আর সে যদি ব্যর্থ হয়, তবে সে হাল ছাড়বে না। সে ব্যাকগ্রাউন্ডে ব্রাউজার খুলে নতুন নতুন উপায় বের করে ট্রাই করতে থাকবে (দরকার হলে লোকাল ও বড় মডেলের সাথে আলোচনা করে)। যতক্ষণ না সে সফল হচ্ছে, ততক্ষণ সে প্র্যাকটিস করবে এবং সফল হলে পুরো ধাপ মেমোরিতে সেভ করে রাখবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "ব্যাকগ্রাউন্ডে Autonomous Retry এবং Self-Learning Loop ইমপ্লিমেন্ট করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/browser_agent.py, TheMask/agent_dev.py
Logic: If a task fails (e.g., scraping fails due to DOM changes), do not drop the task. Move it to a Background_Practice queue. Create a background thread where the agent calls the LLM with the error: "I failed to click X. Here is the new DOM. Propose a new Playwright strategy." It loops this silently until success, then logs the successful locator sequence to layer4_experience.



🟢 ফিচার ৯: সিকিউরিটি, পাওয়ারশেল এবং অ্যাডমিন গেটকিপিং
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব। এর মাধ্যমে আপনার কম্পিউটারের নিরাপত্তা নিশ্চিত করা হবে।
🛠️ সাব-টাস্ক ৯.১: Security Settings Panel & Database (নিরাপত্তা সেটিংস)
কীভাবে কাজ করবে: সেটিংস উইন্ডোতে নতুন একটি ট্যাব থাকবে "Security"। সেখানে কিছু অন/অফ সুইচ থাকবে: ১. ইন্টারনেট এক্সেস,
🛠️ সাব-টাস্ক ৯.১.১: Strict Path Confinement (স্যান্ডবক্সিং)
কীভাবে কাজ করবে: আপনি সেটিংসে যে ফোল্ডারের (যেমন: D:\MyProjects) পারমিশন দেবেন, এজেন্ট শুধুমাত্র সেই ফোল্ডারের ভেতরেই ফাইল ডিলিট, তৈরি বা কোড রান করতে পারবে। সে যদি ভুল করেও C: ড্রাইভ বা উইন্ডোজের সিস্টেম ফাইলে হাত দিতে চায়, সিস্টেম সাথে সাথে অ্যাক্সেস ডিনাইড করে দেবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Directory Whitelisting এবং Strict Path Confinement লজিক tools.py তে অ্যাড করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/tools.py
Logic: Maintain a list of allowed_directories. Before executing write_file, delete_file, or run_powershell, resolve the target path using os.path.abspath. Verify if the resolved path starts with any of the allowed_directories. If not, raise a PermissionError and return it to the LLM.

 ২. কোড রান করার পারমিশন, ৩. ফাইল ডিলিট করার পারমিশন।
উদাহরণ: আপনি যদি "ফাইল ডিলিট" অপশনটি অফ করে রাখেন, তবে AI শত চেষ্টা করলেও আপনার কম্পিউটারের কোনো ফাইল কাটতে বা মুছতে পারবে না।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "সাব-টাস্ক ৯.১ এর Security Settings UI এবং Database টেবিল তৈরি করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/TheMask.py (DB creation), TheMask/ui_components.py
Logic: Create a new SQLite table security_settings (setting_name TEXT PRIMARY KEY, status BOOLEAN). Add a new tab/window in the UI with ctk.CTkSwitch for "Allow Code Exec", "Allow File Delete", "Allow Internet". Fetch and update these values in the database instantly when toggled.


🛠️ সাব-টাস্ক ৯.২: PowerShell / CMD Execution (সিস্টেম কমান্ড চালানো)
কীভাবে কাজ করবে: AI চাইলে উইন্ডোজের পাওয়ারশেল বা কমান্ড প্রম্পটে স্ক্রিপ্ট রান করে কম্পিউটারের বিভিন্ন কাজ করতে পারবে (যেমন: নতুন ফোল্ডার বানানো, আইপি চেক করা)।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "পাওয়ারশেল এক্সিকিউশন টুল tools.py তে অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/tools.py
Logic: Add function run_powershell(command). Use subprocess.run(["powershell", "-Command", command], capture_output=True, text=True). Crucial: Before running, the function MUST query the security_settings table. If code execution is disabled, return an error message to the LLM immediately without running anything.


🛠️ সাব-টাস্ক ৯.৩: Admin Gatekeeping (অ্যাডমিন পারমিশন পপ-আপ)
কীভাবে কাজ করবে: যদি AI এমন কোনো কমান্ড চালাতে চায় যার জন্য অ্যাডমিন পাওয়ার দরকার (যেমন সিস্টেম ফাইল এডিট করা), সে নিজে নিজে চালাবে না। আপনার স্ক্রিনে একটি এলার্ট আসবে: "অ্যাডমিন কমান্ড চালাতে চাই। অনুমতি দেবেন?" আপনি 'Yes' দিলে চলবে, 'No' দিলে চলবে না।
উদাহরণ: AI অ্যান্টিভাইরাস বন্ধ করতে চাইলে পপ-আপ আসবে। আপনি 'No' দিলে সে থেমে যাবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Admin Gatekeeping এবং Permission Pop-up অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/tools.py, TheMask/TheMask.py
Logic: In the tool router, if the LLM requests execution of commands known to require elevation (or if a specific flag requires_admin=True is passed by the LLM), pause the execution thread. Trigger a tkinter.messagebox.askyesno("Admin Permission Request", "The Mask wants to run an admin command:\n\n" + command + "\n\nAllow?") on the main GUI thread. Only proceed if the user clicks Yes.

🟢 ফিচার ১০: স্বাধীন এজেন্ট মোড (Autonomous Mode)
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব। এর ফলে অ্যাপকে একবার কাজ দিলে সে মানুষের সাহায্য ছাড়াই টানা কাজ শেষ করে আউটপুট দেবে।

🛠️ সাব-টাস্ক ১০.১: Continuous Execution Loop (টানা কাজের লুপ)
কীভাবে কাজ করবে: আপনি একবার "একটি ওয়েবসাইট বানাও" বললে, সিস্টেম ডাটাবেসের "Pending" টাস্কগুলো একটা একটা করে ধরবে। একটা কাজ শেষ হলে সে আপনার উত্তরের অপেক্ষা না করে নিজে নিজেই পরের কাজ শুরু করবে।
উদাহরণ: ওয়েবসাইট বানানোর ৫টি টাস্ক আছে। সে ১ নম্বর কাজ শেষ করে আপনাকে শুধু নোটিফিকেশন দেবে "টাস্ক ১ শেষ, টাস্ক ২ শুরু করছি" এবং কাজ চালিয়ে যাবে।
নন-টেক মানুষের জন্য গাইড (ক্লিক-বাই-ক্লিক):
AI-কে বলুন "সাব-টাস্ক ১০.১ এর Continuous Execution Loop তৈরি করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/agent_dev.py, TheMask/TheMask.py
Logic: Implement a while True: or while pending_tasks: loop inside a background thread in autonomous_agent_loop(). It should continuously query the SQLite tasks table for status='Pending'. Once a task is marked Completed, immediately fetch the next without breaking the loop or waiting for user input.


🛠️ সাব-টাস্ক ১০.২: Auto-Debugging (নিজে নিজে ভুল শোধরানো)
কীভাবে কাজ করবে: কোড রান করতে গিয়ে যদি কোনো Error আসে, সে আপনাকে না বলে ওই Error-টা নিজেই পড়বে এবং ঠিক করে আবার রান করবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Auto-Debugging লজিক অ্যাড করো, যেন Error পেলে সে নিজেই ফিক্স করতে পারে"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_dev.py, TheMask/tools.py
Logic: When execute_code() returns stderr, pass that exact error trace back into the LLM context with the prompt: "The code execution failed with this error: {stderr}. Fix the code and return only the corrected code." Run this in a loop up to 5 times before giving up.


🛠️ সাব-টাস্ক ১০.৩: Smart Interrupt (জরুরি প্রয়োজনে থামা)
কীভাবে কাজ করবে: সে নিজে নিজে কাজ করলেও, যদি এমন কোনো কাজ আসে যেটা আপনার জন্য ক্ষতিকর হতে পারে (যেমন: ফাইল ডিলিট বা অ্যাডমিন পারমিশন), শুধু তখনই সে কাজ থামিয়ে আপনার পারমিশন চাইবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Smart Interrupt লজিক যুক্ত করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_dev.py
Logic: Ensure that the execution loop checks the requires_admin or destructive_action flags from the tools. If triggered, pause the while loop using a threading Event (threading.Event().wait()), prompt the GUI, and only resume Event.set() if the user approves.



🟢 ফিচার ১১: অ্যাসিঙ্ক্রোনাস প্রসেসিং (Async/Await GUI Optimization)
এই ফিচারটিকে ২টি সাব-টাস্কে ভাগ করব। এর ফলে আপনার অ্যাপ কখনো হ্যাং বা "Not Responding" হবে না।
🛠️ সাব-টাস্ক ১১.১: Background Threading (ব্যাকগ্রাউন্ডে কাজ করা)
কীভাবে কাজ করবে: বড় কোনো কাজ (যেমন: API থেকে উত্তর আনা, ফাইল লেখা, কোড রান করা) করার সময় অ্যাপ যেন আটকে না যায়, সেজন্য মূল উইন্ডো ঠিক রেখে কাজগুলো ব্যাকগ্রাউন্ডে (পর্দার আড়ালে) হবে।
উদাহরণ: আপনি কাজ দিয়ে অন্য ট্যাবে বা চ্যাটে যেতে পারবেন, অ্যাপ একদম স্মুথ চলবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "সব API কল এবং ভারী কাজের জন্য Threading ইমপ্লিমেন্ট করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/TheMask.py
Logic: Wrap all api.call_llm, agent_loop, and playwright actions in threading.Thread(target=..., daemon=True).start(). Ensure no heavy I/O operations happen on the main Tkinter thread.


🛠️ সাব-টাস্ক ১১.২: Safe GUI Update (নিরাপদে স্ক্রিন আপডেট)
কীভাবে কাজ করবে: ব্যাকগ্রাউন্ডের কাজ শেষ হলে সে যখন চ্যাটবক্সে লেখা দেখাবে, তখন যেন অ্যাপ ক্র্যাশ না করে, সেটার জন্য একটি সেফ মেকানিজম তৈরি করা হবে। স্ট্যাটাস বারে সুন্দর অ্যানিমেশন (যেমন: "কাজ চলছে...") দেখাবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Safe GUI Update এবং Status Animation নিশ্চিত করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/TheMask.py, TheMask/ui_components.py
Logic: Since Tkinter is not thread-safe, ANY update to the UI (inserting text, changing status labels) from a background thread MUST use self.root.after(0, lambda: target_function(...)). Implement the animated status bar to show processing time.





🟢 ফিচার ১২: Self-Update & Auto-Rollback System (নিজে নিজে আপডেট হওয়া)
এই ফিচারের মাধ্যমে অ্যাপটি নিজের কোড নিজে লিখতে, মডিফাই করতে এবং রিস্টার্ট করে নতুন ভার্সনে চলতে পারবে।
🛠️ সাব-টাস্ক ১২.১: Code Editor Agent & Launcher Setup
কীভাবে কাজ করবে: অ্যাপটি সরাসরি নিজেকে মডিফাই করবে না (কারণ রানিং অবস্থায় ফাইল এডিট করলে ক্র্যাশ করে)। এর বদলে launcher.py নামের একটি ছোট ফাইল থাকবে, যে মূল অ্যাপটিকে রান করাবে। অ্যাপ নিজে তার কোড এডিট করে TheMask_new.py নামে সেভ করবে।
উদাহরণ: আপনি বললেন, "ফেসবুক অটোমেশন ফিচার যুক্ত করো।" সে কোড লিখে agent_facebook.py নামে নতুন ফাইল বানাবে এবং TheMask_new.py-তে সেটি কানেক্ট করবে।
নন-টেক মানুষের জন্য গাইড (ক্লিক-বাই-ক্লিক):
AI-কে বলুন "সাব-টাস্ক ১৩.১ এর launcher.py এবং সেলফ-এডিট লজিক তৈরি করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/launcher.py (New), TheMask/self_updater.py (New)
Logic: Create a launcher.py that uses subprocess to run TheMask.py in a while True: loop. In self_updater.py, allow the LLM to write new feature code to a temporary directory (temp_build/).


🛠️ সাব-টাস্ক ১২.২: Sandbox Testing & Validation
কীভাবে কাজ করবে: নতুন কোড লেখার পর সে ব্যাকগ্রাউন্ডে সেটি রান করে দেখবে। যদি কোডে কোনো Error থাকে, সে মূল অ্যাপ পরিবর্তন করবে না। নিজে নিজে এরর সলভ করে আবার টেস্ট করবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "নতুন ফিচারের জন্য ব্যাকগ্রাউন্ড স্যান্ডবক্স টেস্টিং যুক্ত করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/self_updater.py
Logic: Run subprocess.run(["python", "-m", "py_compile", "temp_build/TheMask_new.py"]) to check syntax. Then run it for 10 seconds. If it crashes (stderr), feed the error back to the LLM to fix. If it survives, proceed to replace.


🛠️ সাব-টাস্ক ১২.৩: Version Control & Rollback (পুরনো ভার্সনে ফেরা)
কীভাবে কাজ করবে: নতুন ভার্সন রান করার পর যদি কখনো অ্যাপ ফ্রিজ হয়ে যায়, launcher.py বুঝতে পারবে এবং আগের ভার্সন রিস্টোর করে দেবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "ভার্সন কন্ট্রোল এবং অটো-রোলব্যাক লজিক launcher.py তে অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/launcher.py
Logic: Before replacing TheMask.py, backup the current version to backups/TheMask_v[timestamp].py. If the new subprocess exits with code 1 within 60 seconds, print "Update failed, rolling back...", restore the backup, and restart.



🟢 ফিচার ১৩: The Agent Swarm (সোশ্যাল মিডিয়া ও ডেভেলপমেন্ট অটোমেশন)
এই ফিচারের মাধ্যমে সে বিভিন্ন সোশ্যাল মিডিয়া এবং ডেভেলপমেন্ট প্ল্যাটফর্মে আলাদা আলাদা এজেন্টের মতো কাজ করবে।
🛠️ সাব-টাস্ক ১৩.১: Playwright Social Automation (FB, X, TikTok, Ads)
কীভাবে কাজ করবে: API-এর লিমিটেশন এড়াতে এটি Playwright ব্যবহার করে মানুষের মতো ব্রাউজার খুলে ফেসবুক পোস্ট, টিকটক আপলোড বা অ্যাডস ম্যানেজারে ক্যাম্পেইন রান করবে।
উদাহরণ: "ফেসবুকে আমার পেইজে একটি এঙ্গেজিং পোস্ট দাও।" সে ব্রাউজার খুলে আপনার পেইজে গিয়ে পোস্ট করে আসবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Social Media Playwright Automation agent_social.py তে অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_social.py
Logic: Extend browser_agent.py. Create specific functions like post_to_facebook(text, media_path), upload_tiktok(video_path), create_fb_ad_campaign(budget, target). Save session cookies so it doesn't need to log in every time.


🛠️ সাব-টাস্ক ১৩.২: Messaging & Telegram Hub (WA, Messenger, TG)
কীভাবে কাজ করবে: টেলিগ্রামের জন্য অফিসিয়াল Telethon/Pyrogram ব্যবহার করবে। হোয়াটসঅ্যাপের জন্য playwright (WhatsApp Web) ব্যবহার করে মেসেজ পড়বে এবং উত্তর দেবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Messaging এবং Telegram Bot Automation যুক্ত করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/agent_messaging.py
Logic: Implement Telegram user-bot using Telethon. Implement WhatsApp auto-reply using Playwright listening to DOM changes on web.whatsapp.com. Integrate with local_brain.py to draft responses.


🛠️ সাব-টাস্ক ১২.৩: Version Control, Graceful Restart & Rollback
কীভাবে কাজ করবে: অ্যাপ আপডেট হওয়ার সময় স্ক্রিনে সুন্দর একটি অ্যানিমেশন আসবে "System Upgrading... Please Wait"। সফল হলে রিস্টার্ট হবে। যদি নতুন ভার্সন ফ্রিজ হয়, তবে launcher.py আগের ভার্সন রিস্টোর করে দেবে।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন "Graceful UI Restart Screen এবং Rollback লজিক launcher.py তে অ্যাড করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/launcher.py, TheMask/ui_components.py
Logic: Before replacing files, trigger a UI state show_upgrade_screen(). Backup the current version to backups/. Spawn the new subprocess. If it exits with code 1 within 60s, restore the backup, log the failure to capabilities.json as a failed upgrade attempt, and restart the old version.



🟢 ফিচার ১৪: Android Companion App (The Jarvis Experience)
এটি আপনার মোবাইলকে পিসির সাথে সার্বক্ষণিক কানেক্টেড রাখবে।

🛠️ সাব-টাস্ক ১৪.১: PC Backend API & Secure Tunnel (পিসির ব্রেইন কানেকশন)
কীভাবে কাজ করবে: আপনার পিসির The Mask একটি লোকাল সার্ভার হিসেবে কাজ করবে। মোবাইল অ্যাপটি ইন্টারনেটের মাধ্যমে পিসির সাথে যুক্ত হবে।
উদাহরণ: আপনি বাইরে বসে মোবাইলে টাইপ করলেন, পিসির AI প্রসেস করে উত্তর মোবাইলে পাঠাল।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "পিসিতে FastAPI সার্ভার এবং Ngrok টানেল সেটআপ করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/pc_server.py
Logic: Create a FastAPI app that exposes endpoints /chat, /status, /upload_audio. Run pyngrok to get a public URL so the Android app can connect securely anywhere.


🛠️ সাব-টাস্ক ১৪.২: Always-On Background Audio & Summarization (সারাদিনের রেকর্ড)
কীভাবে কাজ করবে: মোবাইলের অ্যাপটি ব্যাকগ্রাউন্ডে মাইক অন রাখবে (বা নির্দিষ্ট সময় পরপর)। এটি আপনার কথোপকথন রেকর্ড করে পিসিতে পাঠাবে। পিসি সেটি টেক্সটে রূপান্তর করে সারসংক্ষেপ (Summary) বানাবে এবং ChromaDB-তে সেভ করবে।
উদাহরণ: রিক্সাভাড়া দেওয়ার সময় কথা রেকর্ড হলো। পিসি সেভ করল: "আজকে ঘিওর থেকে এসে ২০ টাকা ভাড়া দেওয়া হয়েছে।"
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "অ্যান্ড্রয়েড অ্যাপের জন্য Background Audio Recording এবং পিসির STT Summarization লজিক লেখো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: AndroidApp/MainService.kt (Mobile side), TheMask/audio_processor.py (PC side)
Logic: Mobile: Create a Foreground Service in Flutter/Kotlin that records audio chunks (e.g., every 5 mins) and POSTs to /upload_audio. PC: Use Whisper to transcribe. Feed transcript to LLM: "Extract key events (e.g., expenses, promises, tasks)". Save output to ChromaDB Layer 4 (Experience).


🛠️ সাব-টাস্ক ১৪.৩: Proactive Context & Camera Integration (স্মার্ট রিকল ও ছবি তোলা)
কীভাবে কাজ করবে: ফোন পকেটেই লক করা আছে, কিন্তু আপনি ব্লুটুথ হেডফোনে বললেন "The Mask, এর একটা ছবি তুলে রাখো।" ফোন নিজে থেকে ছবি তুলে পিসিতে পাঠাবে। আবার আপনি জিজ্ঞেস করলে সে পুরনো মেমোরি থেকে উত্তর দেবে।
উদাহরণ: "আজকে কি কোনো কাজ আছে?" ➔ সিস্টেম ChromaDB খুঁজবে ➔ বলবে "গতকাল xx কে বলেছিলেন কাজটা দেখবেন।"
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "মোবাইল ক্যামেরা ট্র্রিগার এবং Proactive ChromaDB Recall সিস্টেম অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/pc_server.py and TheMask/memory_manager.py
Logic: If PC detects intent "take_picture", send a WebSocket command to Android app to trigger camera.takePicture() in the background service and send the image back for Vision API analysis. For recall, PC queries layer4_experience with current date/time context and responds via TTS to the mobile app.

🛠️ সাব-টাস্ক ১৪.৪: Wake-Word Detection (হ্যান্ডস-ফ্রি অ্যাক্টিভেশন)
কীভাবে কাজ করবে: আপনার ফোন পকেটে থাকলেও আপনি যদি শুধু বলেন "হ্যালো মাস্ক", তখন অ্যাপটি নিজে থেকে জেগে উঠবে এবং আপনার পরবর্তী কমান্ড শোনার জন্য বীপ (Beep) সাউন্ড করবে।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন "অ্যান্ড্রয়েড অ্যাপে Porcupine বা PocketSphinx দিয়ে Offline Wake-Word Detection যুক্ত করো"।
AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: AndroidApp/WakeWordService.kt
Logic: Implement a lightweight, offline wake-word listener using Picovoice Porcupine or similar library. It should run continuously with minimal battery drain. Once the wake-word is detected, it triggers the main audio recording intent and wakes the screen/vibrates .


🟢 ফিচার ১৫: নিজস্ব ক্ষমতা যাচাই এবং স্মার্ট আপগ্রেড প্রস্তাব
🛠️ সাব-টাস্ক ১৫.১: Capability Registry (নিজস্ব ক্ষমতার তালিকা তৈরি)
কীভাবে কাজ করবে: সিস্টেমের ভেতরে একটি ডাইনামিক তালিকা থাকবে (JSON ফাইল), যেখানে লেখা থাকবে সে বর্তমানে ঠিক কী কী কাজ করতে পারে (যেমন: Playwright আছে, File Read/Write আছে, Facebook Automation আছে)।
উদাহরণ: সিস্টেম জানবে সে ব্রাউজার চালাতে পারে, কিন্তু ড্রোন ওড়ানোর কোনো কোড তার কাছে নেই।
নন-টেক মানুষের জন্য গাইড (ক্লিক-বাই-ক্লিক):
AI-কে বলুন "সাব-টাস্ক ১৬.১ এর capability_manager.py তৈরি করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/capability_manager.py, TheMask/capabilities.json
Logic: Create a class that reads all available tools and scripts in the TheMask/ directory and maintains an updated capabilities.json. This JSON must be injected into the system prompt of local_brain.py so the AI explicitly knows its physical code boundaries.


🛠️ সাব-টাস্ক ১৫.২: Pre-Task Analysis Gate (কাজ শুরুর আগে ক্ষমতা যাচাই)
কীভাবে কাজ করবে: আপনি কোনো টাস্ক দিলে, মূল কাজ শুরু করার আগে Local Brain একটি "ভেরিফিকেশন" করবে। সে নিজের লিস্ট চেক করে দেখবে এই কাজ করার মতো টুল তার কাছে আছে কিনা।
উদাহরণ: আপনি বললেন, "আমার এসি-টার টেম্পারেচার কমিয়ে দাও।" সে চেক করে দেখবে Smart Home বা IoT কন্ট্রোলের কোনো কোড তার কাছে নেই। সে সাথে সাথে কাজ থামিয়ে দেবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "local_brain.py তে Pre-Task Capability Analysis লজিক যুক্ত করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/local_brain.py
Logic: Add function evaluate_capability(goal, capabilities_json). Make a fast, low-temperature LLM call with a strict prompt: "Based strictly on the provided capabilities_json, can you achieve the goal? Reply only with YES or NO|Missing_Feature_Name|Estimated_Time." This prevents hallucination.


🛠️ সাব-টাস্ক ১৫.৩: Auto-Upgrade Proposal & Execution (আপগ্রেড প্রস্তাব দেওয়া)
কীভাবে কাজ করবে: যদি যাচাইয়ের রেজাল্ট 'NO' হয়, সে কোনো ভুল উত্তর না দিয়ে সরাসরি আপনার শেখানো ডায়ালগটি বলবে এবং অনুমতির জন্য অপেক্ষা করবে। অনুমতি পেলে সে ১৩ নাম্বার ফিচার (Self-Update System) ব্যবহার করে নতুন কোড লেখা শুরু করবে।
উদাহরণ: সে বলবে: "এই কাজ করার ক্ষমতা আমার এই মুহূর্তে নেই। এর জন্য আমাকে 'IoT AC Controller' ফিচারে আপগ্রেড করতে হবে। আপগ্রেড করলে আমি পরবর্তীতে সব স্মার্ট ডিভাইস কন্ট্রোল করতে পারব। আপনি চাইলে ফিচারটি অ্যাড করা শুরু করতে পারি। ২ ঘন্টা সময় লাগতে পারে। কমপ্লিট হওয়ার পর আমি এসির কাজটা করে রাখব।"
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "Hallucination Prevention এবং Upgrade Proposal UI ট্রিগার অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/TheMask.py (UI integration)
Logic: In the main process() thread, if evaluate_capability returns NO, halt the standard workflow. Parse the Missing_Feature_Name and display the exact pre-defined Bengali text requested by the user. Generate two UI buttons in the chat: [আপগ্রেড শুরু করো] and [বাতিল করো]. If approved, push the missing feature request to the self_updater.py queue, and queue the original user request to execute after the update completes.


🟢 ফিচার ১৬: প্যাকেজিং এবং ফাইনাল রিলিজ
এই ফিচারটিকে ৩টি সাব-টাস্কে ভাগ করব। এর মাধ্যমে আপনি কোড ফাইলগুলোকে একটি ডাবল-ক্লিকেবল .exe সফটওয়্যারে রূপান্তর করবেন।
🛠️ সাব-টাস্ক ১৬.১: Path Resolution (ফাইল লোকেশন ঠিক করা)
কীভাবে কাজ করবে: অ্যাপ যখন .exe ফাইলে রূপান্তর হবে, তখন যেন সে তার মেমোরি, ডাটাবেস এবং আইকনগুলো হারিয়ে না ফেলে, সেজন্য ফাইলের ঠিকানাগুলো (Path) ডাইনামিক করা হবে।
নন-টেক মানুষের জন্য গাইড:
AI-কে বলুন "PyInstaller-এর জন্য sys._MEIPASS Path Resolution অ্যাড করো"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask/TheMask.py, TheMask/ui_components.py
Logic: Write a helper function resource_path(relative_path) that uses sys._MEIPASS when frozen by PyInstaller, and os.path.abspath() when running as a python script. Apply this to all image loading, SQLite DB connections, and ChromaDB directory paths.


🛠️ সাব-টাস্ক ১৬.২: PyInstaller Compilation (.exe বানানো)
কীভাবে কাজ করবে: একটি কমান্ডের মাধ্যমে আপনার সমস্ত কোড, লাইব্রেরি এবং মেমোরি একসাথে প্যাক হয়ে TheMask.exe নামের একটি ফাইল তৈরি হবে। এটি আপনি যেকোনো কম্পিউটারে পেনড্রাইভে করে নিয়ে চালাতে পারবেন।
নন-টেক মানুষের জন্য গাইড:
টার্মিনালে বা CMD তে লিখুন: pip install pyinstaller
এরপর AI-কে বলুন "PyInstaller Compilation কমান্ড এবং .spec ফাইল লিখে দাও"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: TheMask.spec (New build configuration file)
Logic: Generate a command or script: pyinstaller --onefile --windowed --icon=image/logo/icon.ico --add-data "chroma_db;chroma_db" --add-data "image;image" --add-data "config.json;." TheMask.py. Handle CustomTkinter assets properly by adding CustomTkinter's library path in --add-data.


🛠️ সাব-টাস্ক ১৬.৩: Setup Wizard (ইন্সটলার তৈরি - ঐচ্ছিক)
কীভাবে কাজ করবে: বড় বড় সফটওয়্যারের মতো "Next -> Next -> Install" উইজার্ড তৈরি করা।
নন-টেক মানুষের জন্য গাইড:
ইনো সেটআপ (Inno Setup) নামের একটি ফ্রি সফটওয়্যার পিসিতে নামিয়ে নিন।
AI-কে বলুন "Inno Setup এর জন্য একটি .iss কনফিগারেশন স্ক্রিপ্ট লিখে দাও"।


AI কোডারের জন্য লজিক ও ডিরেকশন:
File Path: setup_script.iss
Logic: Write a standard Inno Setup script that points to the dist/TheMask.exe, creates a desktop shortcut, and creates an empty projects/ directory in the user's AppData or installation folder.



🟢 ফিচার ১৭: অ্যাডভান্সড মাল্টি-এজেন্ট সোয়ার্ম কোলাবোরেশন (Admin + Developer Agent Swarm)
কীভাবে কাজ করবে: বড় টাস্ক (যেমন: টুডো অ্যাপ, ওয়েবসাইট, পেনটেস্টিং) আসলে মেইন ব্রেইন অটোমেটিক সোয়ার্ম তৈরি করবে। Admin Agent-১ ফিচার ব্রেকডাউন ও প্রম্পট লিস্ট করবে, Developer Agent কোড জেনারেট করবে, Admin Agent-২ ভেরিফিকেশন + ফাইল তৈরি + পারমিশন নেবে। প্রতিটি স্টেপে লোকাল ব্রেইন দিয়ে ক্রস-ভেরিফিকেশন চলবে।
উদাহরণ: “একটি টুডো অ্যাপ বানাও” → Admin Agent 1 ফিচার লিস্ট করে → Developer Agent কোড দেয় → Admin Agent 1 রিচেক করে ভুল থাকলে স্পেসিফিক গাইডলাইন দিয়ে ফেরত পাঠায় → সব ঠিক হলে Admin Agent 2 ফাইল তৈরি করে।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন “সাব-টাস্ক ১৭.১ এর Agent Swarm লজিক তৈরি করো”।

🛠️ সাব-টাস্ক ১৭.১: Agent Role Assignment & Swarm Initialization
কীভাবে কাজ করবে: বড় টাস্ক ডিটেক্ট করার সাথে সাথে মেইন ব্রেইন সোয়ার্ম শুরু করে। Admin Agent 1-কে ফিচার ব্রেকডাউনের রোল, Developer Agent-কে কোড জেনারেশনের রোল, Admin Agent 2-কে ফাইল + পারমিশনের রোল অ্যাসাইন করে। সোয়ার্মের সদস্য সংখ্যা স্বয়ংক্রিয়ভাবে টাস্কের সাইজ অনুসারে নির্ধারণ হয় (২-৫ জন)।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন “সাব-টাস্ক ১৭.১ এর Swarm Initialization কোড দাও”।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/agent_swarm.py (New), TheMask/TheMask.py
Logic: agent_swarm.initialize_swarm(goal) ফাংশনে local_brain দিয়ে JSON রেসপন্স নিয়ে Agent roles অ্যাসাইন করো। সব এজেন্টের চ্যাট হিস্ট্রি আলাদা রাখো।

🛠️ সাব-টাস্ক ১৭.২: Admin-Developer Collaboration & Verification Loop
কীভাবে কাজ করবে: Admin Agent 1 Developer Agent-কে প্রম্পট দেয় → Developer Agent API কল করে কোড/আউটপুট দেয় → Admin Agent 1 লোকাল ব্রেইন দিয়ে ভেরিফাই করে → ভুল থাকলে স্পেসিফিক ফিক্স গাইডলাইন দিয়ে ফেরত পাঠায় (max 3 iterations)।
উদাহরণ: Developer Agent ভুল কোড দিলে Admin Agent 1 বলবে “এই লাইনে Button ক্লিক হ্যান্ডলার মিসিং, এভাবে ফিক্স করো”।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন “সাব-টাস্ক ১৭.২ এর Collaboration Loop ইমপ্লিমেন্ট করো”।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/agent_swarm.py
Logic: while verification == "NO": loop চালাও। প্রতিবার local_brain.verify_response_semantically() ব্যবহার করো।
🛠️ সাব-টাস্ক ১৭.৩: File Creation & Permission Gatekeeping by Admin Agent 2
কীভাবে কাজ করবে: সব ভেরিফিকেশন পাস হলে Admin Agent 2 মেইন এডমিনের কাছ থেকে পাওয়ারশেল/ফাইল পারমিশন নিয়ে ফাইল তৈরি করে।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন “সাব-টাস্ক ১৭.৩ এর File Creation লজিক দাও”।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/agent_swarm.py, TheMask/tools.py
Logic: Admin Agent 2 টুল কল করে write_file() + run_powershell() চালাবে শুধুমাত্র security_settings অনুমোদিত হলে।


🟢 ফিচার ১৮: ডিটেইলস লগিং সিস্টেম (Transparency & Full Process Log)
কীভাবে কাজ করবে: প্রতিটি উত্তরের পাশে “Details” ছোট বাটন থাকবে। ক্লিক করলে পুরো প্রসেসের টাইমস্ট্যাম্পসহ লগ দেখাবে। সব লগ আলাদা JSON ফাইলে সেভ হয়।
উদাহরণ: “তোমার নাম কি” প্রশ্নের লগে দেখাবে — ইনপুট → ট্রান্সলেশন → মেমোরি → লোকাল ব্রেইন → API কল → ফলব্যাক → ভেরিফিকেশন → আউটপুট।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন “সাব-টাস্ক ১৮.১ এর Details Logging সিস্টেম তৈরি করো”।

🛠️ সাব-টাস্ক ১৮.১: Logging Engine & Step-by-Step Tracker
কীভাবে কাজ করবে: প্রতিটি প্রসেস স্টেপে logger.log_step() কল হয়। লগগুলো session_[timestamp].json ফাইলে সেভ হয়।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/logging_engine.py (New)
Logic: class ProcessLogger: def log_step(self, step_name, timestamp, details)। প্রতিটি মেইন প্রসেসে (translate, memory, local_brain, api_call ইত্যাদি) এটি কল করো।

🛠️ সাব-টাস্ক ১৮.২: UI Details Button & Log Viewer
কীভাবে কাজ করবে: চ্যাটবক্সে প্রতি মেসেজের পাশে “Details” বাটন। ক্লিক করলে নতুন উইন্ডোতে পুরো লগ দেখাবে।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/TheMask.py, TheMask/ui_components.py
Logic: প্রতি message bubble-এ CTkButton(text="Details") যুক্ত করো। বাটন ক্লিকে CTkToplevel খুলে logging_engine থেকে লগ লোড করে দেখাও।

🟢 ফিচার ১৯: The Mask Doctor – সেলফ হিলিং প্রসেস
কীভাবে কাজ করবে: সেটিংসে “The Mask Doctor” অপশন। অ্যাপ কোনো সমস্যা ডিটেক্ট করলে (এরর, ফ্রিজ, কনফিগ ইস্যু) অটোমেটিক ডাক্তারকে কল করার অনুমতি চাইবে। ডাক্তার পুরো সিস্টেম ডায়াগনোসিস করে রিপোর্ট দিয়ে সেলফ-হিলিং চালাবে।
নন-টেক মানুষের জন্য গাইড: AI-কে বলুন “সাব-টাস্ক ১৯.১ এর The Mask Doctor তৈরি করো”।
🛠️ সাব-টাস্ক ১৯.১: Diagnosis Engine
কীভাবে কাজ করবে: doctor.run_diagnosis() চালিয়ে config, DB, chroma_db, API status, threads, memory সব চেক করে।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/doctor.py (New)
Logic: প্রতিটি কম্পোনেন্টের জন্য চেক ফাংশন তৈরি করো এবং রিপোর্ট জেনারেট করো।

🛠️ সাব-টাস্ক ১৯.২: Auto-Fix & Self-Healing
কীভাবে কাজ করবে: রিপোর্ট অনুসারে অটো ফিক্স চালায় (config reset, DB repair, thread restart ইত্যাদি)।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/doctor.py
Logic: auto_fix() ফাংশনে প্রতিটি সমস্যার জন্য নির্দিষ্ট ফিক্স লজিক রাখো।

🛠️ সাব-টাস্ক ১৯.৩: Doctor UI & Permission Flow
কীভাবে কাজ করবে: সমস্যা ডিটেক্ট হলে GUI-তে পপ-আপ আসবে “The Mask Doctor কে ডাকব?” → Yes হলে ডায়াগনোসিস + হিলিং শুরু হয়।
AI কোডারের জন্য লজিক ও ডিরেকশন (Strict Prompt for AI):
File Path: TheMask/TheMask.py, TheMask/ui_components.py
Logic: tkinter.messagebox.askyesno দিয়ে পারমিশন নাও এবং doctor.run_full_healing() কল করো।





----------------------------------------------------------------------------------------------





