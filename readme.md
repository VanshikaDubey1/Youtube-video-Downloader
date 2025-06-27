# 🎥 YouTube Video Downloader (Flask + Pytube)

A simple web app built with **Flask** and **Pytube** that allows users to download YouTube videos directly by pasting a video link. It fetches the highest available resolution and saves the video locally.

---

## 🚀 Features

- Paste a YouTube video URL and download with one click.
- Highest video resolution is automatically selected.
- Simple and responsive UI using HTML/CSS.
- Built with Python, Flask, and Pytube.

---

## 📸 Preview

![screenshot](preview.png) <!-- Add an actual screenshot of your UI and name it preview.png -->

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Pytube
- HTML/CSS (no external frameworks)

---

## ⚙️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader

2. Create a Virtual Environment (optional but recommended)
python -m venv venv
Activate:

Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt
4. Run the App
python app.py


Then open your browser at:
http://127.0.0.1:5000/



📁 Project Structure
youtube-video-downloader/
│
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # UI template
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
📌 Notes
Videos are downloaded to the current project directory.

For audio download or playlist support, you can extend the functionality (see TODO below).

✅ TODO (Optional Enhancements)
 Add option to choose between video/audio download.

 Support playlist download.
 Show video thumbnail and title before download.

 Let user choose download location.


💡 Author
Vanshika Dubey
Feel free to connect or fork for improvements!

---

