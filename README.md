# 💜 BTS: The Journey

**BTS: The Journey** is an interactive web application built with Python and Streamlit for exploring the journey of BTS and discovering information about its seven members.

The website brings together BTS members, music, achievements, timeline, stories, and an ARMY Space in one interactive platform with a purple/lavender BTS-inspired design.

---

## 🌟 Project Overview

BTS: The Journey is designed as an interactive fan-oriented website for both new and existing ARMYs.

The project provides different sections to explore BTS, including member information, music, achievements, important moments, interesting stories, and a community-style ARMY Space where users can share messages and media.

---

## ✨ Features

### 💜 Welcome Page
- Introduction to **BTS: The Journey**
- BTS-inspired purple/lavender interface
- Entry point to explore the website

### 🏠 Home
- Central navigation hub
- Quick access to different sections
- Interactive exploration buttons

### 👤 Meet the Members
Information pages for all seven BTS members:

- RM
- Jin
- SUGA
- J-Hope
- Jimin
- V
- Jungkook

Each member has a dedicated page with personal and BTS-related information.

### 🎵 Music & Albums
- Explore BTS music and albums
- Organized music-related information
- Easy navigation through the music section

### 🏆 Achievements
- Explore major BTS achievements
- Highlights important milestones from their career

### 📅 Timeline
- Explore BTS's journey chronologically
- Important events and milestones from their career

### 📖 Unknown Stories
- Interesting BTS-related stories and facts
- Created especially for fans who want to discover more about their journey

### 💬 ARMY Space
A community-style section where users can:
- Post messages
- Share images
- Share videos
- Delete their own posts
- Receive basic filtering for inappropriate language and contact information

Posts are stored using SQLite.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **Streamlit** | Web application development |
| **HTML & CSS** | UI customization and styling |
| **SQLite** | Storing ARMY Space posts |
| **Pillow (PIL)** | Image processing |
| **GitHub** | Source code management |
| **Streamlit Community Cloud** | Web application deployment |

---

## 📁 Project Structure

```text
BTS_THE_JOURNEY/
│
├── images/
│   └── BTS images
│
├── pages/
│   ├── 01_Welcome.py
│   ├── 02_Home.py
│   ├── 03_Members.py
│   ├── 04_rm.py
│   ├── 05_jin.py
│   ├── 06_suga.py
│   ├── 07_jhope.py
│   ├── 08_jimin.py
│   ├── 09_v.py
│   ├── 10_jk.py
│   ├── 11_OT7.py
│   ├── 12_music.py
│   ├── 13_achievements.py
│   ├── 14_timeline.py
│   ├── 15_stories.py
│   └── 16_army_space.py
│
├── app.py
├── requirements.txt
└── army_space.db
