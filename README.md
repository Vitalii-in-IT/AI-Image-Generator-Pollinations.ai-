AI Image Generator (Pollinations.ai)
A lightweight desktop application built with Python and Tkinter that allows users to generate high-quality images using the Pollinations AI API. The application features a user-friendly interface, automated translation of prompts, and persistent configuration storage.

🚀 Features
GUI Interface: Built with Tkinter for ease of use.
API Integration: Uses the Pollinations.ai (Flux model) to generate images.
Auto-Translation: Integrated deep-translator to automatically convert prompts from any language to English for better AI results.
Persistent Storage: Saves your API token and preferred download path in a config.json file, so you don't have to re-enter them.
Clipboard Support: Dedicated buttons to quickly paste tokens, paths, and prompts.
Smart Filenaming: Automatically saves images with a timestamp (YYYY-MM-DD_HH-MM-SS) to prevent overwriting.
Process Safety: The "START" button is disabled during the generation process to ensure sequence integrity.

🛠️ Technologies Used
Python 3.x
Tkinter (Standard GUI Library)
Requests (HTTP Library)
Deep-translator (Google Translator API)
JSON (Configuration management)

📋 Prerequisites
Before running the app, ensure you have the necessary libraries installed:

Bash
pip install requests deep-translator

🚀 How to Use
Clone the repository:

Bash
git clone https://github.com/your-username/ai-image-generator.git
cd ai-image-generator
Run the application:

Bash
python main.py
Setup:
Enter your Pollinations.ai API token.
Specify the folder path where images should be saved.
Click Save to store these settings.

Generate:
Paste your prompt into the text area.
Click START and wait for the image to be downloaded.
