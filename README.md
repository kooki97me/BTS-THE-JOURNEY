# BTS: The Journey

BTS: The Journey is an interactive web application developed using Python and Streamlit. 
The project is designed for BTS fans to explore information about the seven members, 
music, achievements, timeline, stories, and an ARMY Space.

## Project Overview

The main idea behind this project is to bring different aspects of BTS's journey 
together in one interactive website.

The application provides separate sections for BTS members, music and albums, 
achievements, timeline, unknown stories, and ARMY Space.

## Features

### Welcome Page
- Introduction to BTS: The Journey
- Simple BTS-inspired purple and lavender interface
- Navigation to the main website

### Home
- Main navigation page
- Quick access to different sections of the website
- Interactive navigation buttons

### Members
Information about all seven BTS members:
- RM
- Jin
- SUGA
- J-Hope
- Jimin
- V
- Jungkook

Each member has a separate page with information about them.

### Music and Albums
- BTS music and album information
- Organized music section
- Easy navigation

### Achievements
- Major BTS achievements
- Important milestones from their career

### Timeline
- Chronological view of important events
- Major milestones from BTS's journey

### Unknown Stories
- Interesting BTS-related stories and facts
- Content for fans who want to explore more about BTS

### ARMY Space
ARMY Space is a community-style section where users can:
- Post messages
- Share images
- Share videos
- Delete their own posts
- Filter inappropriate language and contact information

The posts are stored using SQLite.

## Technologies Used

- Python
- Streamlit
- HTML
- CSS
- SQLite
- Pillow (PIL)
- GitHub
- Streamlit Community Cloud

## Project Structure

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
