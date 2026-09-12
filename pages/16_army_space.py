import streamlit as st
import sqlite3
import os
import uuid
import re
import html
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
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="ARMY Space | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)


# =========================================================
# GOOGLE LOGIN
# =========================================================

if not getattr(st.user, "is_logged_in", False):

    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top, #6f42a5 0%, #321b50 40%, #140b20 100%);
        }

        .login-box {
            max-width: 650px;
            margin: 100px auto;
            padding: 45px;
            text-align: center;
            border-radius: 25px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.15);
            box-shadow: 0 15px 50px rgba(0,0,0,0.35);
        }

        .login-title {
            font-size: 48px;
            font-weight: 800;
            color: #ffffff;
        }

        .login-subtitle {
            font-size: 18px;
            color: #eadcf7;
            margin-bottom: 30px;
        }
        </style>

        <div class="login-box">
            <div class="login-title">💜 ARMY Space</div>
            <div class="login-subtitle">
                A safe little corner for ARMYs to share memories, messages and stories.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "💜 Continue with Google",
        use_container_width=True
    ):
        st.login()

    st.info(
        "Google login is required so users can manage only their own posts."
    )

    st.stop()


# =========================================================
# USER INFORMATION
# =========================================================

USER_ID = (
    st.user.get("sub")
    or st.user.get("email", "")
)

USER_EMAIL = (
    st.user.get("email", "")
).strip().lower()

DISPLAY_NAME = (
    st.user.get("name")
    or st.user.get("given_name")
    or "ARMY"
).strip()

ADMIN_EMAIL = st.secrets.get("ADMIN_EMAIL", "").strip().lower()

IS_ADMIN = (
    ADMIN_EMAIL != ""
    and USER_EMAIL == ADMIN_EMAIL
)


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(circle at top, #6f42a5 0%, #321b50 38%, #140b20 100%);
    }

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: white;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .main-subtitle {
        text-align: center;
        font-size: 19px;
        color: #eadcf7;
        margin-bottom: 35px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 750;
        color: white;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .rules-box {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 18px;
        padding: 22px;
        color: #eee5f7;
        margin-bottom: 25px;
    }

    .post-card {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.13);
        border-radius: 18px;
        padding: 22px;
        margin: 15px 0;
    }

    .post-name {
        color: #ffffff;
        font-size: 20px;
        font-weight: 700;
    }

    .post-date {
        color: #bca9d0;
        font-size: 13px;
    }

    .post-content {
        color: #eee5f7;
        font-size: 17px;
        line-height: 1.6;
        margin-top: 12px;
    }

    .post-type {
        color: #cdb5ec;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .admin-box {
        background: rgba(255, 210, 120, 0.08);
        border: 1px solid rgba(255, 210, 120, 0.25);
        border-radius: 18px;
        padding: 20px;
        margin-top: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DATABASE
# =========================================================

def get_connection():
    return sqlite3.connect(DATABASE_FILE)


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_type TEXT,
            name TEXT,
            content TEXT,
            file_path TEXT,
            owner_id TEXT,
            created_at TEXT
        )
        """
    )

    cursor.execute("PRAGMA table_info(posts)")
    columns = [column[1] for column in cursor.fetchall()]

    if "post_type" not in columns:
        cursor.execute(
            "ALTER TABLE posts ADD COLUMN post_type TEXT"
        )

    if "name" not in columns:
        cursor.execute(
            "ALTER TABLE posts ADD COLUMN name TEXT"
        )

    if "content" not in columns:
        cursor.execute(
            "ALTER TABLE posts ADD COLUMN content TEXT"
        )

    if "file_path" not in columns:
        cursor.execute(
            "ALTER TABLE posts ADD COLUMN file_path TEXT"
        )

    if "owner_id" not in columns:
        cursor.execute(
            "ALTER TABLE posts ADD COLUMN owner_id TEXT"
        )

    if "created_at" not in columns:
        cursor.execute(
            "ALTER TABLE posts ADD COLUMN created_at TEXT"
        )


    # Reports table

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER,
            reporter_id TEXT,
            reason TEXT,
            created_at TEXT,
            UNIQUE(post_id, reporter_id)
        )
        """
    )

    conn.commit()
    conn.close()


create_database()


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def safe_text(text):
    """Protect displayed user content from HTML injection."""
    if not text:
        return ""

    return html.escape(str(text)).replace("\n", "<br>")


def contains_personal_contact_info(text):

    if not text:
        return False

    # Email addresses
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    # Phone-like numbers
    phone_pattern = r"(?<!\d)(?:\+?\d[\d\s().-]{8,}\d)(?!\d)"

    if re.search(email_pattern, text):
        return True

    if re.search(phone_pattern, text):
        return True

    return False


def add_post(
    post_type,
    name,
    content="",
    file_path=None
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO posts
        (
            post_type,
            name,
            content,
            file_path,
            owner_id,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            post_type,
            name,
            content,
            file_path,
            USER_ID,
            datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            )
        )
    )

    conn.commit()
    conn.close()


def get_posts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
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
        """
    )

    posts = cursor.fetchall()

    conn.close()

    return posts


def can_delete(owner_id):

    return (
        owner_id == USER_ID
        or IS_ADMIN
    )


def delete_post(post_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT owner_id, file_path
        FROM posts
        WHERE id = ?
        """,
        (post_id,)
    )

    result = cursor.fetchone()

    if not result:
        conn.close()
        return False

    owner_id = result[0]
    file_path = result[1]

    # Security check
    if not can_delete(owner_id):

        conn.close()
        return False

    # Delete uploaded file
    if file_path and os.path.exists(file_path):

        try:
            os.remove(file_path)
        except OSError:
            pass

    cursor.execute(
        "DELETE FROM posts WHERE id = ?",
        (post_id,)
    )

    # Remove reports associated with deleted post
    cursor.execute(
        "DELETE FROM reports WHERE post_id = ?",
        (post_id,)
    )

    conn.commit()
    conn.close()

    return True


def add_report(post_id, reason):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO reports
            (
                post_id,
                reporter_id,
                reason,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                post_id,
                USER_ID,
                reason,
                datetime.now().strftime(
                    "%d %b %Y, %I:%M %p"
                )
            )
        )

        conn.commit()

        result = True

    except sqlite3.IntegrityError:

        result = False

    conn.close()

    return result


def get_reports():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            reports.id,
            reports.post_id,
            reports.reporter_id,
            reports.reason,
            reports.created_at,
            posts.name,
            posts.content
        FROM reports
        LEFT JOIN posts
        ON reports.post_id = posts.id
        ORDER BY reports.id DESC
        """
    )

    reports = cursor.fetchall()

    conn.close()

    return reports


def clear_report(report_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM reports WHERE id = ?",
        (report_id,)
    )

    conn.commit()
    conn.close()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">💜 ARMY Space</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'A little corner for ARMYs to share their BTS journey.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# USER / LOGOUT
# =========================================================

col1, col2 = st.columns([4, 1])

with col1:

    st.markdown(
        f"### 💜 Welcome, {html.escape(DISPLAY_NAME)}!"
    )

with col2:

    if st.button(
        "Logout",
        use_container_width=True
    ):
        st.logout()


# =========================================================
# RULES
# =========================================================

st.markdown(
    '<div class="section-title">🌷 ARMY Space Rules</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="rules-box">

    💜 Be respectful to other ARMYs.<br><br>

    🌷 Do not share phone numbers, email addresses,
    passwords or other private information.<br><br>

    🎵 Do not upload copyrighted content that you
    do not have permission to share.<br><br>

    🚫 No harassment, hate, spam or impersonation.<br><br>

    🔗 Official BTS links are welcome.<br><br>

    🛡️ If you see something inappropriate, use the
    Report option.

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MESSAGE WALL
# =========================================================

st.markdown(
    '<div class="section-title">💌 Leave a Message</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    message_name = st.text_input(
        "Your ARMY name",
        placeholder="Enter your name or ARMY nickname",
        key="message_name"
    )

    message_text = st.text_area(
        "Your message",
        placeholder="Write something for the ARMY community...",
        height=140,
        key="message_text"
    )

    if st.button(
        "💜 Post Message",
        use_container_width=True
    ):

        name = message_name.strip()
        content = message_text.strip()

        if not name or not content:

            st.warning(
                "Please enter both your ARMY name and message."
            )

        elif contains_personal_contact_info(
            name + " " + content
        ):

            st.error(
                "Please don't share email addresses or phone numbers."
            )

        elif len(content) > 2000:

            st.error(
                "Your message is too long. Please keep it under 2000 characters."
            )

        else:

            add_post(
                "message",
                name,
                content
            )

            st.success(
                "Your message has been posted. 💜"
            )

            st.rerun()


# =========================================================
# PHOTO / VIDEO UPLOAD
# =========================================================

st.markdown(
    '<div class="section-title">📸 Share a Memory</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    media_name = st.text_input(
        "Your ARMY name",
        placeholder="Enter your name or ARMY nickname",
        key="media_name"
    )

    uploaded_file = st.file_uploader(
        "Upload an image or video",
        type=[
            "jpg",
            "jpeg",
            "png",
            "webp",
            "mp4",
            "mov",
            "webm"
        ],
        key="media_upload"
    )

    media_caption = st.text_area(
        "Caption",
        placeholder="Write something about this memory...",
        height=100,
        key="media_caption"
    )

    st.caption(
        "Maximum file size: 50 MB."
    )

    if st.button(
        "📤 Post Memory",
        use_container_width=True
    ):

        name = media_name.strip()
        caption = media_caption.strip()

        if not name:

            st.warning(
                "Please enter your ARMY name."
            )

        elif not uploaded_file:

            st.warning(
                "Please select an image or video."
            )

        elif uploaded_file.size > 50 * 1024 * 1024:

            st.error(
                "This file is larger than 50 MB."
            )

        elif contains_personal_contact_info(
            name + " " + caption
        ):

            st.error(
                "Please don't share email addresses or phone numbers."
            )

        else:

            file_extension = os.path.splitext(
                uploaded_file.name
            )[1].lower()

            unique_name = (
                str(uuid.uuid4())
                + file_extension
            )

            save_path = os.path.join(
                UPLOAD_FOLDER,
                unique_name
            )

            with open(save_path, "wb") as file:

                file.write(
                    uploaded_file.getbuffer()
                )

            if uploaded_file.type.startswith(
                "image/"
            ):

                post_type = "photo"

            else:

                post_type = "video"

            add_post(
                post_type,
                name,
                caption,
                save_path
            )

            st.success(
                "Your memory has been posted. 💜"
            )

            st.rerun()


# =========================================================
# WHY BTS
# =========================================================

st.markdown(
    '<div class="section-title">💜 Why BTS?</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    story_name = st.text_input(
        "Your ARMY name",
        placeholder="Enter your name or ARMY nickname",
        key="story_name"
    )

    story_text = st.text_area(
        "Your BTS story",
        placeholder="Tell us why BTS is special to you...",
        height=160,
        key="story_text"
    )

    if st.button(
        "🌷 Share My Story",
        use_container_width=True
    ):

        name = story_name.strip()
        content = story_text.strip()

        if not name or not content:

            st.warning(
                "Please enter your name and story."
            )

        elif contains_personal_contact_info(
            name + " " + content
        ):

            st.error(
                "Please don't share email addresses or phone numbers."
            )

        elif len(content) > 3000:

            st.error(
                "Please keep your story under 3000 characters."
            )

        else:

            add_post(
                "why_bts",
                name,
                content
            )

            st.success(
                "Your BTS story has been shared. 💜"
            )

            st.rerun()


# =========================================================
# MESSAGE WALL POSTS
# =========================================================

st.markdown(
    '<div class="section-title">💜 ARMY Message Wall</div>',
    unsafe_allow_html=True
)

posts = get_posts()


if not posts:

    st.info(
        "No posts yet. Be the first ARMY to share something! 💜"
    )


for post in posts:

    (
        post_id,
        post_type,
        name,
        content,
        file_path,
        owner_id,
        created_at
    ) = post

    safe_name = safe_text(
        name or "ARMY"
    )

    safe_content = safe_text(
        content or ""
    )

    type_label = {
        "message": "💌 Message",
        "why_bts": "💜 Why BTS",
        "photo": "📸 Photo",
        "video": "🎥 Video"
    }.get(
        post_type,
        "💜 ARMY Post"
    )

    st.markdown(
        f"""
        <div class="post-card">

            <div class="post-type">
                {type_label}
            </div>

            <div class="post-name">
                {safe_name}
            </div>

            <div class="post-date">
                {html.escape(created_at or "")}
            </div>

            <div class="post-content">
                {safe_content}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # PHOTO
    # =====================================================

    if post_type == "photo":

        if file_path and os.path.exists(file_path):

            st.image(
                file_path,
                use_container_width=True
            )

        else:

            st.warning(
                "This image is no longer available."
            )


    # =====================================================
    # VIDEO
    # =====================================================

    elif post_type == "video":

        if file_path and os.path.exists(file_path):

            st.video(file_path)

        else:

            st.warning(
                "This video is no longer available."
            )


    # =====================================================
    # DELETE / REPORT
    # =====================================================

    action_col1, action_col2 = st.columns(2)


    # Own post OR admin
    if can_delete(owner_id):

        with action_col1:

            if st.button(
                "🗑️ Delete this post",
                key=f"delete_{post_id}",
                use_container_width=True
            ):

                if delete_post(post_id):

                    st.success(
                        "Post deleted successfully. 💜"
                    )

                    st.rerun()

                else:

                    st.error(
                        "You don't have permission to delete this post."
                    )


    # Report someone else's post
    if owner_id != USER_ID:

        with action_col2:

            with st.popover(
                "🚩 Report"
            ):

                reason = st.selectbox(
                    "Why are you reporting this post?",
                    [
                        "Spam",
                        "Harassment",
                        "Personal information",
                        "Inappropriate content",
                        "Impersonation",
                        "Copyright concern",
                        "Other"
                    ],
                    key=f"reason_{post_id}"
                )

                if st.button(
                    "Submit Report",
                    key=f"report_{post_id}",
                    use_container_width=True
                ):

                    submitted = add_report(
                        post_id,
                        reason
                    )

                    if submitted:

                        st.success(
                            "Report submitted. Thank you. 💜"
                        )

                    else:

                        st.info(
                            "You have already reported this post."
                        )


# =========================================================
# ADMIN MODERATION
# =========================================================

if IS_ADMIN:

    st.markdown(
        '<div class="section-title">🛡️ Admin Moderation</div>',
        unsafe_allow_html=True
    )

    reports = get_reports()

    st.markdown(
        f"""
        <div class="admin-box">
            <b>Admin account</b><br>
            {html.escape(USER_EMAIL)}<br><br>
            Reported posts: <b>{len(reports)}</b>
        </div>
        """,
        unsafe_allow_html=True
    )


    if reports:

        for report in reports:

            (
                report_id,
                reported_post_id,
                reporter_id,
                reason,
                report_date,
                reported_name,
                reported_content
            ) = report

            st.markdown(
                f"""
                <div class="post-card">

                    <b>🚩 Report #{report_id}</b><br>

                    <b>Reason:</b>
                    {html.escape(reason or "")}<br>

                    <b>Reporter:</b>
                    {html.escape(reporter_id or "Unknown")}<br>

                    <b>Date:</b>
                    {html.escape(report_date or "")}<br><br>

                    <b>Post by:</b>
                    {html.escape(reported_name or "ARMY")}<br>

                    <b>Content:</b><br>
                    {safe_text(reported_content or "")}

                </div>
                """,
                unsafe_allow_html=True
            )

            admin_col1, admin_col2 = st.columns(2)

            with admin_col1:

                if st.button(
                    "🗑️ Delete reported post",
                    key=f"admin_delete_{report_id}",
                    use_container_width=True
                ):

                    if delete_post(
                        reported_post_id
                    ):

                        st.success(
                            "Reported post deleted."
                        )

                        st.rerun()

            with admin_col2:

                if st.button(
                    "✅ Dismiss report",
                    key=f"dismiss_{report_id}",
                    use_container_width=True
                ):

                    clear_report(
                        report_id
                    )

                    st.success(
                        "Report dismissed."
                    )

                    st.rerun()

    else:

        st.info(
            "No reports right now. 💜"
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <p style="text-align:center; color:#bca9d0;">
        BTS: The Journey 💜 &nbsp;•&nbsp;
        Made by ARMY, for ARMY
    </p>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

st.markdown("###")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "← Back to Stories",
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
