import json
import os
import requests
import urllib.parse
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from deep_translator import GoogleTranslator

CONFIG_FILE = "config.json"

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Image Generator")
        self.root.geometry("400x500")

        # Variables
        self.api_key = tk.StringVar()
        self.save_path = tk.StringVar()
        self.load_config()

        # --- UI: API KEY ---
        tk.Label(root, text="API Token (pollinations.ai):").pack(pady=(10, 0))
        self.token_entry = tk.Entry(root, textvariable=self.api_key, width=40)
        self.token_entry.pack()
        
        tk.Button(root, text="Paste from clipboard", command=lambda: self.paste(self.api_key)).pack()
        tk.Button(root, text="Save the token", command=self.save_config).pack(pady=(0, 10))

        # --- UI: PATH ---
        tk.Label(root, text="Save path (e.g., images):").pack()
        self.path_entry = tk.Entry(root, textvariable=self.save_path, width=40)
        self.path_entry.pack()
        
        tk.Button(root, text="Paste from clipboard", command=lambda: self.paste(self.save_path)).pack()
        tk.Button(root, text="Save the path", command=self.save_config).pack(pady=(0, 10))

        # --- UI: PROMPT ---
        tk.Label(root, text="Prompt (image description):").pack()
        self.prompt_text = tk.Text(root, height=4, width=40)
        self.prompt_text.pack()
        tk.Button(root, text="Paste prompt from clipboard", command=self.paste_to_text).pack(pady=5)

        # --- UI: START ---
        self.start_btn = tk.Button(root, text="START", bg="green", fg="white", 
                                   font=('bold'), command=self.generate_image)
        self.start_btn.pack(pady=20, fill=tk.X, padx=50)

    def paste(self, var):
        var.set(self.root.clipboard_get())

    def paste_to_text(self):
        try:
            self.prompt_text.insert(tk.END, self.root.clipboard_get())
        except:
            pass

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                self.api_key.set(data.get("api_key", ""))
                self.save_path.set(data.get("save_path", "images"))
        else:
            self.save_path.set("images")

    def save_config(self):
        data = {"api_key": self.api_key.get(), "save_path": self.save_path.get()}
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f)
        messagebox.showinfo("Success", "Data stored in JSON!")

    def generate_image(self):
        prompt = self.prompt_text.get("1.0", tk.END).strip()
        if not prompt or not self.api_key.get():
            messagebox.showerror("Error", "Enter token and prompt!")
            return

        self.start_btn.config(state=tk.DISABLED, text="Generating...")
        self.root.update()

        try:
            # Translation and preparation
            translated = GoogleTranslator(source='auto', target='en').translate(prompt)
            final_prompt = f"{translated}, cinematic style, minimalistic, no text, no people"
            encoded = urllib.parse.quote(final_prompt)
            
            url = f"https://gen.pollinations.ai/image/{encoded}?model=flux&key={self.api_key.get()}"
            
            # Downloading
            response = requests.get(url, timeout=90)
            if response.status_code == 200:
                if not os.path.exists(self.save_path.get()):
                    os.makedirs(self.save_path.get())
                
                # File name: date_time_seconds
                filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
                file_path = os.path.join(self.save_path.get(), filename)
                
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                # messagebox.showinfo("Success", f"Saved as: {filename}")
            else:
                messagebox.showerror("Error", f"API Status: {response.status_code}")

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.start_btn.config(state=tk.NORMAL, text="START")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()