# Instagram Profile Viewer Pro 🔍

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A modern Python GUI application to view Instagram profiles with enhanced features including private account access (when authenticated).

**Created by [AmmarSaqib-programmer](https://github.com/Ammarsaqib-programmer)**

## 🌟 Features

- **Profile Analysis**: View followers, following, posts count, and bio
- **Private Account Access**: Attempts to access private profiles when authenticated
- **Elegant UI**: Clean interface with profile picture display
- **Multiple Tabs**: Organized view of profile info and statistics
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📸 Screenshot
(Add screenshot here after uploading)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Ammarsaqib-programmer/Instagram-Profile-Viewer.git
cd Instagram-Profile-Viewer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🔐 Authentication (For Private Accounts)

```bash
instaloader -l YOUR_INSTAGRAM_USERNAME
```
Then edit line 23 in the code with your username.

## 🚀 Usage
```bash
python instagram_viewer.py
```

## 📝 Requirements
- Python 3.8+
- Instaloader
- Pillow (PIL)
- Tkinter (usually included with Python)

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

## 📜 License
[MIT](https://choosealicense.com/licenses/mit/)
