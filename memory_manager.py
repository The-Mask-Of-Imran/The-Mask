import chromadb
from datetime import datetime
import json
import os

class MemoryManager:
    def __init__(self):
        try:
            # ChromaDB পাথ ঠিক করা
            chroma_path = os.path.join(os.getcwd(), "chroma_db")
            self.client = chromadb.PersistentClient(path=chroma_path)
        except Exception as e:
            print(f"ChromaDB error: {e}")
            import tempfile
            self.client = chromadb.PersistentClient(path=tempfile.mkdtemp())
        
        try:
            self.collections = {
                "identity": self.client.get_or_create_collection("layer1_identity"),
                "knowledge": self.client.get_or_create_collection("layer2_knowledge"),
                "tasks": self.client.get_or_create_collection("layer3_tasks"),
                "experience": self.client.get_or_create_collection("layer4_experience"),
                "context": self.client.get_or_create_collection("layer5_context")
            }
        except:
            self.collections = {}
        
        self.initialize_identity()

    def initialize_identity(self):
        try:
            if "identity" in self.collections:
                existing = self.collections["identity"].get()
                if len(existing.get("documents", [])) == 0:
                    identity_text = """তুমি The Mask।
তোমার নাম: The Mask
তুমি একটি হিউম্যান-লাইক পার্সোনাল AI অ্যাসিস্ট্যান্ট।
সবসময় বাংলায় সুন্দর, সংক্ষিপ্ত এবং স্পষ্ট উত্তর দাও।"""
                    
                    self.collections["identity"].add(
                        documents=[identity_text],
                        metadatas=[{"timestamp": datetime.now().isoformat(), "type": "identity"}],
                        ids=["identity_core"]
                    )
        except Exception as e:
            print(f"Identity init warning: {e}")

    def save_memory(self, layer: str, text: str, metadata: dict = None):
        if layer not in self.collections:
            return
        if metadata is None:
            metadata = {"timestamp": datetime.now().isoformat()}
        try:
            self.collections[layer].add(
                documents=[text],
                metadatas=[metadata],
                ids=[f"{layer}_{datetime.now().timestamp()}"]
            )
        except:
            pass

    def retrieve_relevant(self, query: str, layer: str = None, n_results: int = 5):
        try:
            if layer and layer in self.collections:
                results = self.collections[layer].query(query_texts=[query], n_results=n_results)
                return results.get("documents", [[]])[0] if results else []
            else:
                all_results = []
                for name, coll in self.collections.items():
                    try:
                        res = coll.query(query_texts=[query], n_results=2)
                        if res.get("documents"):
                            all_results.extend(res["documents"][0])
                    except:
                        pass
                return all_results[:n_results]
        except Exception:
            return []

    def get_all_tasks(self):
        try:
            if "tasks" in self.collections:
                tasks = self.collections["tasks"].get()
                return tasks.get("documents", []) if tasks else []
        except:
            return []
        return []