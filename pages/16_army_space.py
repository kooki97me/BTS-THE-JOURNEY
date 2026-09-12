import streamlit as st
import sqlite3
import os
import uuid
from datetime import datetime


# =========================================================
# PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

DATABASE_FILE = os.path.join(PROJECT_DIR, "army_space.db")
UPLOAD_FOLDER = os.path.join(PROJECT_DIR, "army_uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# =========================================================
# DATABASE
# =========================================================

def get_connection():
    return sqlite3.connect(DATABASE_FILE)


def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_type TEXT NOT NULL,
            name TEXT NOT NULL,
            content TEXT,
            file_path TEXT,
            owner_id TEXT,
            created_at TEXT
        )
    """)

    # Check existing columns
    cursor.execute("PRAGMA table_info(posts)")
    columns = [column[1] for column in cursor.fetchall()]

    # Add missing columns to older database
    if "post_type" not in columns:
        cursor.execute("ALTER TABLE posts ADD COLUMN post_type TEXT")

    if "name" not in columns:
        cursor.execute("ALTER TABLE posts ADD COLUMN name TEXT")

    if "content" not in columns:
        cursor.execute("ALTER TABLE posts ADD COLUMN content TEXT")

    if "file_path" not in columns:
        cursor.execute("ALTER TABLE posts ADD COLUMN file_path TEXT")

    if "owner_id" not in columns:
        cursor.execute("ALTER TABLE posts ADD COLUMN owner_id TEXT")

    if "created_at" not in columns:
        cursor.execute("ALTER TABLE posts ADD COLUMN created_at TEXT")

    conn.commit()
    conn.close()


def add_post(post_type, name, content="", file_path=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO posts
        (post_type, name, content, file_path, owner_id, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        post_type,
        name,
        content,
        file_path,
        st.session_state.owner_id,
        datetime.now().strftime("%d %b %Y, %I:%M %p")
    ))

    conn.commit()
    conn.close()


def get_posts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            post_type,
            name,
            content,
            file_path,
            owner_id,
            created_at
        FROM posts
        ORDER BY id DESC
    """)

    posts = cursor.fetchall()
    conn.close()

    return posts


def delete_post(post_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT file_path, owner_id FROM posts WHERE id = ?",
        (post_id,)
    )

    result = cursor.fetchone()

    if result:
        file_path, owner_id = result

        if owner_id == st.session_state.owner_id:

            if file_path and os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except OSError:
                    pass

            cursor.execute(
                "DELETE FROM posts WHERE id = ?",
                (post_id,)
            )

            conn.commit()

    conn.close()


create_database()


# =========================================================
# OWNER ID
# =========================================================

if "owner_id" not in st.session_state:
    st.session_state.owner_id = str(uuid.uuid4())


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ARMY Space | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* =======================================================
   MAIN PAGE
======================================================= */

.stApp {
    background: linear-gradient(
        135deg,
        #160021 0%,
        #241035 50%,
        #100017 100%
    );
    color: #F5EFFF;
}


/* =======================================================
   TITLE
======================================================= */

.main-title {
    text-align: center;
    color: #E8C7FF;
    font-size: 46px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #CDB9DA;
    font-size: 18px;
    margin-bottom: 30px;
}


/* =======================================================
   SECTION TITLES
======================================================= */

.section-title {
    color: #E8C7FF;
    font-size: 28px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 12px;
}


/* =======================================================
   ARMY SPACE RULES
======================================================= */

.info-box {
    background: rgba(95, 54, 120, 0.20);
    border: 1px solid rgba(190, 145, 220, 0.25);
    border-radius: 16px;
    padding: 16px 24px;
    color: #F2E8F7;
    max-width: 850px;
    margin: 0 auto;
    text-align: center;
}


/* =======================================================
   TYPING INPUT BOXES - FINAL FIX
======================================================= */

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    background-color: #FFFFFF !important;
    border: 1px solid #89B78AA !important;
    border-radius: 10px !important;
    box-shadow: none !important;
}


/* Text typed by ARMY */

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    background-color: #FFFFFF !important;

}



/* Placeholder text */

div[data-baseweb="input"] input::placeholder,
div[data-baseweb="textarea"] textarea::placeholder {
    color: #D8C7E8 !important;
    -webkit-text-fill-color: #D8C7E8 !important;
    opacity: 1 !important;
}

/* Focus */

 div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"] > div:focus-within {
    border-color: #A56CC1 !important;
    box-shadow: 0 0 0 1px #A56CC1 !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"] > div:focus-within {
    border-color: #A56CC1 !important;
    box-shadow: 0 0 0 1px #A56CC1 !important;
}


/* =======================================================
   LABELS
======================================================= */

label,
.stTextInput label,
.stTextArea label,
.stFileUploader label {
    color: #E8D9EF !important;
}


/* =======================================================
   FILE UPLOADER
======================================================= */

section[data-testid="stFileUploaderDropzone"] {
    background-color: #2B1640 !important;
    border: 1px dashed #79528E !important;
    border-radius: 12px !important;
}


/* =======================================================
   BUTTONS
======================================================= */

.stButton > button {
    background-color: #5B3275 !important;
    color: #FFFFFF !important;
    border: 1px solid #80549A !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background-color: #70418D !important;
    border-color: #A56CC1 !important;
    color: #FFFFFF !important;
}


/* =======================================================
   POST CARD
======================================================= */

.post-card {
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(205, 170, 225, 0.14);
    border-radius: 16px;
    padding: 18px;
    margin-top: 10px;
    margin-bottom: 5px;
}

.post-name {
    color: #E7C5FF;
    font-size: 19px;
    font-weight: 700;
}

.post-time {
    color: #AFA0B9;
    font-size: 13px;
    margin-top: 2px;
}

.post-content {
    color: #F2EAF5;
    font-size: 16px;
    line-height: 1.6;
    margin-top: 10px;
}


/* =======================================================
   DIVIDER
======================================================= */

hr {
    border-color: rgba(205, 170, 225, 0.15) !important;
}


/* =======================================================
   ALERTS
======================================================= */

div[data-testid="stAlert"] {
    background-color: rgba(65, 35, 85, 0.55) !important;
    color: #F1E6F7 !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">💜 ARMY SPACE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A little corner for ARMYs to share memories, thoughts and love for BTS.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# ARMY SPACE RULES
# =========================================================

st.markdown("""
<div class="info-box">

💜 <b>ARMY Space Rules</b>

<br><br>

Be kind and respectful to other ARMYs.<br>
No hate, bullying or personal information.<br>
Share only things you are comfortable making public.

</div>
""", unsafe_allow_html=True)

st.write("")


# =========================================================
# MESSAGE WALL
# =========================================================

st.markdown(
    '<div class="section-title">💬 ARMY Message Wall</div>',
    unsafe_allow_html=True
)

name = st.text_input(
    "Your ARMY name",
    placeholder="Example: PurpleMoon"
)

message = st.text_area(
    "Your message",
    placeholder="Write something you want to share with ARMY..."
)


if st.button(
    "💜 Post Message",
    use_container_width=True
):

    if not name.strip():
        st.warning("Please enter your ARMY name.")

    elif not message.strip():
        st.warning("Please write a message.")

    else:
        add_post(
            post_type="message",
            name=name.strip(),
            content=message.strip()
        )

        st.success("Your message has been posted! 💜")
        st.rerun()


# =========================================================
# POSTS
# =========================================================

st.write("")
st.markdown("---")

st.markdown(
    '<div class="section-title">💜 ARMY Posts</div>',
    unsafe_allow_html=True
)

posts = get_posts()


if posts:

    for post in posts:

        (
            post_id,
            post_type,
            post_name,
            content,
            file_path,
            owner_id,
            created_at
        ) = post


        st.markdown(
            '<div class="post-card">',
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # MESSAGE
        # -------------------------------------------------

        if post_type == "message":

            st.markdown(
                f'<div class="post-name">💜 {post_name}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="post-time">{created_at}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="post-content">{content}</div>',
                unsafe_allow_html=True
            )


        # -------------------------------------------------
        # WHY BTS
        # -------------------------------------------------

        elif post_type == "why_bts":

            st.markdown(
                f'<div class="post-name">💜 {post_name}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="post-time">{created_at}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="post-content">'
                f'✨ <b>Why BTS is special to me:</b><br><br>'
                f'{content}'
                f'</div>',
                unsafe_allow_html=True
            )


        # -------------------------------------------------
        # PHOTO
        # -------------------------------------------------

        elif post_type == "photo":

            st.markdown(
                f'<div class="post-name">📸 {post_name}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="post-time">{created_at}</div>',
                unsafe_allow_html=True
            )

            if file_path and os.path.exists(file_path):

                st.image(
                    file_path,
                    use_container_width=True
                )

            if content:

                st.markdown(
                    f'<div class="post-content">{content}</div>',
                    unsafe_allow_html=True
                )


        # -------------------------------------------------
        # VIDEO
        # -------------------------------------------------

        elif post_type == "video":

            st.markdown(
                f'<div class="post-name">🎥 {post_name}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="post-time">{created_at}</div>',
                unsafe_allow_html=True
            )

            if file_path and os.path.exists(file_path):

                st.video(file_path)

            if content:

                st.markdown(
                    f'<div class="post-content">{content}</div>',
                    unsafe_allow_html=True
                )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # DELETE MY POST
        # -------------------------------------------------

        if owner_id == st.session_state.owner_id:

            if st.button(
                "🗑️ Delete my post",
                key=f"delete_{post_id}",
                use_container_width=True
            ):

                delete_post(post_id)

                st.success("Your post has been deleted. 💜")
                st.rerun()


else:

    st.info(
        "No posts yet. Be the first ARMY to share something! 💜"
    )


# =========================================================
# SHARE PHOTO / VIDEO
# =========================================================

st.write("")
st.markdown("---")

st.markdown(
    '<div class="section-title">📸 Share a BTS Memory</div>',
    unsafe_allow_html=True
)

media_name = st.text_input(
    "Your ARMY name",
    key="media_name",
    placeholder="Example: PurpleMoon"
)

uploaded_file = st.file_uploader(
    "Choose a photo or video",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp",
        "mp4",
        "mov",
        "avi"
    ]
)

caption = st.text_input(
    "Caption (optional)",
    key="caption",
    placeholder="Add a small caption..."
)


if st.button(
    "💜 Share Memory",
    use_container_width=True
):

    if not media_name.strip():

        st.warning("Please enter your ARMY name.")

    elif uploaded_file is None:

        st.warning("Please choose a photo or video.")

    else:

        extension = os.path.splitext(
            uploaded_file.name
        )[1].lower()

        unique_filename = (
            str(uuid.uuid4()) + extension
        )

        saved_path = os.path.join(
            UPLOAD_FOLDER,
            unique_filename
        )

        with open(saved_path, "wb") as file:

            file.write(
                uploaded_file.getbuffer()
            )


        if uploaded_file.type.startswith("video"):

            post_type = "video"

        else:

            post_type = "photo"


        add_post(
            post_type=post_type,
            name=media_name.strip(),
            content=caption.strip(),
            file_path=saved_path
        )

        st.success("Your memory has been shared! 💜")
        st.rerun()


# =========================================================
# WHY BTS?
# =========================================================

st.write("")
st.markdown("---")

st.markdown(
    '<div class="section-title">💜 Why BTS?</div>',
    unsafe_allow_html=True
)

why_name = st.text_input(
    "Your ARMY name",
    key="why_name",
    placeholder="Example: PurpleMoon"
)

why_bts = st.text_area(
    "Tell us what BTS means to you",
    key="why_bts",
    placeholder="Write your story..."
)


if st.button(
    "💜 Share My Story",
    use_container_width=True
):

    if not why_name.strip():

        st.warning("Please enter your ARMY name.")

    elif not why_bts.strip():

        st.warning("Please write your story.")

    else:

        add_post(
            post_type="why_bts",
            name=why_name.strip(),
            content=why_bts.strip()
        )

        st.success("Your story has been shared! 💜")
        st.rerun()


# =========================================================
# NAVIGATION
# =========================================================

st.write("")
st.markdown("---")

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "← Back to Unknown Stories",
        use_container_width=True
    ):

        st.switch_page(
            "pages/15_stories.py"
        )


with col2:

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):

        st.switch_page(
            "pages/02_Home.py"
        )
