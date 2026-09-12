import streamlit as st
import sqlite3
import os
import re
import html
from datetime import datetime


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ARMY Space | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)


# =========================================================
# PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

DB_PATH = os.path.join(PROJECT_DIR, "army_space.db")
UPLOAD_DIR = os.path.join(PROJECT_DIR, "army_uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================================================
# USER ID
# =========================================================
# Simple local identity.
# Browser/session ke liye unique ID banega.

if "army_user_id" not in st.session_state:
    import uuid
    st.session_state.army_user_id = str(uuid.uuid4())

USER_ID = st.session_state.army_user_id


# =========================================================
# DATABASE
# =========================================================

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():

    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            display_name TEXT NOT NULL,
            post_type TEXT NOT NULL,
            content TEXT,
            file_path TEXT,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


initialize_database()


# =========================================================
# BASIC CONTENT FILTER
# =========================================================

BLOCKED_WORDS = {
    "fuck",
    "fucking",
    "shit",
    "bitch",
    "asshole",
    "bastard",
    "idiot",
    "stupid",
    "moron",
    "dumbass",
    "slut",
    "whore"
}


def contains_bad_language(text):

    if not text:
        return False

    text_lower = text.lower()

    for word in BLOCKED_WORDS:

        pattern = r"\b" + re.escape(word) + r"\b"

        if re.search(pattern, text_lower):
            return True

    return False


# =========================================================
# PERSONAL CONTACT FILTER
# =========================================================

def contains_contact_info(text):

    if not text:
        return False

    # Email
    email_pattern = (
        r"\b[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    # Phone numbers
    phone_pattern = (
        r"(?<!\d)"
        r"(?:\+?\d[\d\s().-]{8,}\d)"
        r"(?!\d)"
    )

    if re.search(email_pattern, text):
        return True

    if re.search(phone_pattern, text):
        return True

    return False


# =========================================================
# FILE TYPES
# =========================================================

IMAGE_TYPES = [
    "jpg",
    "jpeg",
    "png",
    "webp"
]

VIDEO_TYPES = [
    "mp4",
    "mov",
    "webm"
]

MAX_FILE_SIZE = 50 * 1024 * 1024


# =========================================================
# ADD POST
# =========================================================

def add_post(
    display_name,
    post_type,
    content,
    uploaded_file=None
):

    content = (content or "").strip()

    # -----------------------------------------------------
    # EMPTY POST
    # -----------------------------------------------------

    if not content and uploaded_file is None:

        return False, "Please write something or select a file."

    # -----------------------------------------------------
    # BAD LANGUAGE
    # -----------------------------------------------------

    if contains_bad_language(content):

        return (
            False,
            "Please keep the ARMY Space respectful and friendly. 💜"
        )

    # -----------------------------------------------------
    # CONTACT INFO
    # -----------------------------------------------------

    if contains_contact_info(content):

        return (
            False,
            "Please don't share phone numbers or email addresses here."
        )

    file_path = None

    # -----------------------------------------------------
    # FILE
    # -----------------------------------------------------

    if uploaded_file is not None:

        if uploaded_file.size > MAX_FILE_SIZE:

            return (
                False,
                "File size must be 50 MB or smaller."
            )

        extension = (
            uploaded_file.name
            .split(".")[-1]
            .lower()
        )

        if post_type == "photo":

            if extension not in IMAGE_TYPES:

                return (
                    False,
                    "Please upload JPG, JPEG, PNG or WEBP."
                )

        if post_type == "video":

            if extension not in VIDEO_TYPES:

                return (
                    False,
                    "Please upload MP4, MOV or WEBM."
                )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        filename = (
            f"{USER_ID}_{timestamp}.{extension}"
        )

        file_path = os.path.join(
            UPLOAD_DIR,
            filename
        )

        with open(file_path, "wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )

    # -----------------------------------------------------
    # DATABASE
    # -----------------------------------------------------

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO posts
        (
            user_id,
            display_name,
            post_type,
            content,
            file_path,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            USER_ID,
            display_name.strip() or "ARMY",
            post_type,
            content,
            file_path,
            datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            )
        )
    )

    conn.commit()
    conn.close()

    return True, "Posted successfully! 💜"


# =========================================================
# GET POSTS
# =========================================================

def get_posts():

    conn = get_connection()

    posts = conn.execute(
        """
        SELECT *
        FROM posts
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    return posts


# =========================================================
# DELETE POST
# =========================================================

def delete_post(post_id):

    conn = get_connection()

    post = conn.execute(
        """
        SELECT *
        FROM posts
        WHERE id = ?
        """,
        (post_id,)
    ).fetchone()

    if post is None:

        conn.close()

        return False, "Post not found."

    # -----------------------------------------------------
    # IMPORTANT:
    # ONLY OWNER CAN DELETE
    # -----------------------------------------------------

    if post["user_id"] != USER_ID:

        conn.close()

        return (
            False,
            "You can delete only your own post."
        )

    # -----------------------------------------------------
    # DELETE FILE
    # -----------------------------------------------------

    file_path = post["file_path"]

    if file_path:

        try:

            if os.path.exists(file_path):
                os.remove(file_path)

        except Exception:
            pass

    # -----------------------------------------------------
    # DELETE DATABASE RECORD
    # -----------------------------------------------------

    conn.execute(
        """
        DELETE FROM posts
        WHERE id = ?
        """,
        (post_id,)
    )

    conn.commit()
    conn.close()

    return True, "Post deleted."


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
        linear-gradient(
            135deg,
            #12071f 0%,
            #1c0c30 50%,
            #281348 100%
        );
        color: #F5EEFF;
    }

    .army-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        color: #E8D5FF;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .army-subtitle {
        text-align: center;
        color: #CDB8E8;
        font-size: 18px;
        margin-bottom: 35px;
    }

    .section-title {
        color: #E5CCFF;
        font-size: 28px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .post-card {
        padding: 20px;
        border-radius: 18px;
        background: rgba(255,255,255,0.055);
        border: 1px solid rgba(210,170,255,0.20);
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .post-name {
        color: #E9D7FF;
        font-size: 18px;
        font-weight: 700;
    }

    .post-date {
        color: #9F88B8;
        font-size: 12px;
        margin-top: 3px;
    }

    .post-text {
        color: #F4EDFA;
        font-size: 16px;
        line-height: 1.6;
        margin-top: 13px;
        white-space: pre-wrap;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="army-title">💜 ARMY SPACE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="army-subtitle">'
    'A little space for ARMYs to share their thoughts, '
    'memories and love for BTS.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# HOME BUTTON
# =========================================================

if st.button(
    "🏠 Back to Home",
    use_container_width=True
):

    st.switch_page(
        "pages/02_Home.py"
    )


# =========================================================
# CREATE POST
# =========================================================

st.markdown(
    '<div class="section-title">💬 Share with ARMY</div>',
    unsafe_allow_html=True
)


display_name = st.text_input(
    "Your ARMY name",
    placeholder="Enter the name you want to show"
)


post_type = st.selectbox(
    "What do you want to share?",
    [
        "message",
        "why_bts",
        "photo",
        "video"
    ]
)


# ---------------------------------------------------------
# PLACEHOLDER
# ---------------------------------------------------------

if post_type == "message":

    placeholder = (
        "Write something you'd like to share with ARMY..."
    )

elif post_type == "why_bts":

    placeholder = (
        "Why is BTS special to you?"
    )

elif post_type == "photo":

    placeholder = (
        "Write a caption for your photo..."
    )

else:

    placeholder = (
        "Write a caption for your video..."
    )


content = st.text_area(
    "Your message",
    placeholder=placeholder,
    height=130
)


# =========================================================
# FILE UPLOAD
# =========================================================

uploaded_file = None

if post_type == "photo":

    uploaded_file = st.file_uploader(
        "Choose a photo",
        type=IMAGE_TYPES
    )

elif post_type == "video":

    uploaded_file = st.file_uploader(
        "Choose a video",
        type=VIDEO_TYPES
    )


# =========================================================
# POST BUTTON
# =========================================================

if st.button(
    "💜 Post",
    type="primary",
    use_container_width=True
):

    if not display_name.strip():

        st.warning(
            "Please enter your ARMY name first."
        )

    else:

        success, message = add_post(
            display_name,
            post_type,
            content,
            uploaded_file
        )

        if success:

            st.success(message)
            st.rerun()

        else:

            st.error(message)


# =========================================================
# POSTS
# =========================================================

st.markdown(
    '<div class="section-title">💜 ARMY Posts</div>',
    unsafe_allow_html=True
)


posts = get_posts()


if not posts:

    st.info(
        "No posts yet. Be the first ARMY to share something! 💜"
    )


for post in posts:

    post_id = post["id"]

    # Escape user-generated text before displaying
    name = html.escape(
        post["display_name"] or "ARMY"
    )

    content_text = html.escape(
        post["content"] or ""
    )

    created_at = html.escape(
        post["created_at"] or ""
    )

    # -----------------------------------------------------
    # POST CARD
    # -----------------------------------------------------

    st.markdown(
        f"""
        <div class="post-card">

            <div class="post-name">
                💜 {name}
            </div>

            <div class="post-date">
                {created_at}
            </div>

            <div class="post-text">
                {content_text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # PHOTO
    # -----------------------------------------------------

    if (
        post["post_type"] == "photo"
        and post["file_path"]
        and os.path.exists(post["file_path"])
    ):

        st.image(
            post["file_path"],
            use_container_width=True
        )

    # -----------------------------------------------------
    # VIDEO
    # -----------------------------------------------------

    if (
        post["post_type"] == "video"
        and post["file_path"]
        and os.path.exists(post["file_path"])
    ):

        st.video(
            post["file_path"]
        )

    # -----------------------------------------------------
    # DELETE BUTTON
    # -----------------------------------------------------
    # Button sab posts par dikhega,
    # but server-side check ensure karega ki
    # sirf owner ka post delete ho.

    if st.button(
        "🗑️ Delete",
        key=f"delete_{post_id}",
        use_container_width=True
    ):

        success, message = delete_post(
            post_id
        )

        if success:

            st.success(message)
            st.rerun()

        else:

            st.error(message)

    st.divider()


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <p style="
        text-align:center;
        color:#9F88B8;
        font-size:13px;
        margin-top:30px;
    ">
        BTS: The Journey 💜 • ARMY Space
    </p>
    """,
    unsafe_allow_html=True
)
