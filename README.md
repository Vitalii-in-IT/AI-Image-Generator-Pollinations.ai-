# 🖼️ AI Image Generator (Pollinations.ai)

A lightweight desktop application built with Python and Tkinter that allows users to generate high-quality images using the Pollinations AI API.

The application features a user-friendly interface, automated translation of prompts, and persistent configuration storage.

---

## Features

- 🖥️ **GUI Interface**  
  Built with Tkinter for ease of use.

- **API Integration**  
  Uses Pollinations.ai (Flux model) to generate images.

- **Auto-Translation**  
  Integrated deep-translator to automatically convert prompts from any language to English for better AI results.

- **Persistent Storage**  
  Saves your API token and preferred download path in a `config.json` file.

- **Clipboard Support**  
  Dedicated buttons to quickly paste tokens, paths, and prompts.

- **Smart File Naming**  
  Automatically saves images with timestamps (`YYYY-MM-DD_HH-MM-SS`) to prevent overwriting.

- **Process Safety**  
  The "START" button is disabled during generation to ensure stable execution.

---

## Technologies Used

- Python 3.x  
- Tkinter (Standard GUI Library)  
- Requests (HTTP Library)  
- deep-translator (Google Translator API)  
- JSON (Configuration management)

---

## Prerequisites

Install required libraries:

```bash
pip install requests deep-translator
