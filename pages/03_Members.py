import streamlit as st
import os
from PIL import Image


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="BTS Members | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)


# =========================================================
# IMAGE PATH
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

IMAGE_DIR = os.path.join(BASE_DIR, "images")


# =========================================================
# BTS MEMBERS DATA
# =========================================================

members = [
    {
        "name": "RM",
        "full_name": "Kim Namjoon",
        "dob": "12 September 1994",
        "image": "rm.jpg",
        "page": "pages/04_rm.py"
    },
    {
        "name": "Jin",
        "full_name": "Kim Seokjin",
        "dob": "4 December 1992",
        "image": "jin.jpg",
        "page": "pages/05_jin.py"
    },
    {
        "name": "SUGA",
        "full_name": "Min Yoongi",
        "dob": "9 March 1993",
        "image": "suga.jpg",
        "page": "pages/06_suga.py"
    },
    {
        "name": "J-Hope",
        "full_name": "Jung Hoseok",
        "dob": "18 February 1994",
        "image": "jhope.jpg",
        "page": "pages/07_jhope.py"
    },
    {
        "name": "Jimin",
        "full_name": "Park Jimin",
        "dob": "13 October 1995",
        "image": "jimin.jpg",
        "page": "pages/08_jimin.py"
    },
    {
        "name": "V",
        "full_name": "Kim Taehyung",
        "dob": "30 December 1995",
        "image": "v.jpg",
        "page": "pages/09_v.py"
    },
    {
        "name": "Jungkook",
        "full_name": "Jeon Jungkook",
        "dob": "1 September 1997",
        "image": "jk.jpg",
        "page": "pages/10_jk.py"
    }
]


# =========================================================
# PURPLE THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #160021 0%,
        #241035 50%,
        #100017 100%
    );
    color: white;
}


/* Remove unnecessary top empty space */

.block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 1rem !important;
}


/* Main heading */

.members-title {
    text-align: center;
    color: #E8C7FF;
    font-size: 44px;
    font-weight: 800;
    margin-top: 0px;
    margin-bottom: 5px;
}


/* Subtitle */

.members-subtitle {
    text-align: center;
    color: #CDB9DA;
    font-size: 18px;
    margin-bottom: 35px;
}


/* Member card */

.member-card {
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(205, 170, 225, 0.16);
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 25px;
    text-align: center;
}


/* Photo frame */

.photo-frame {
    width: 260px;
    height: 300px;
    margin: 0 auto;
    border-radius: 15px;
    overflow: hidden;
    background: rgba(255, 255, 255, 0.04);
}


/* Image inside frame */

.photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    border-radius: 15px;
    display: block;
}


/* Member name */

.member-name {
    color: #E8C7FF;
    font-size: 27px;
    font-weight: 750;
    margin-top: 15px;
}


/* Full name */

.member-full-name {
    color: #CDB9DA;
    font-size: 16px;
    margin-top: 3px;
}


/* DOB */

.member-dob {
    color: #F0E3F5;
    font-size: 16px;
    margin-top: 10px;
}


/* Buttons */

.stButton > button {
    background-color: #5B3275 !important;
    color: white !important;
    border: 1px solid #80549A !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    background-color: #70418D !important;
    border-color: #A56CC1 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="members-title">💜 BTS MEMBERS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="members-subtitle">'
    'Meet the seven members of BTS'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# MEMBER CARDS
# =========================================================

for i in range(0, len(members), 3):

    cols = st.columns(3, gap="large")

    for j, col in enumerate(cols):

        index = i + j

        if index >= len(members):
            break

        member = members[index]

        image_path = os.path.join(
            IMAGE_DIR,
            member["image"]
        )

        with col:

            # -----------------------------
            # CARD START
            # -----------------------------

            st.markdown(
                '<div class="member-card">',
                unsafe_allow_html=True
            )

            # -----------------------------
            # PHOTO
            # -----------------------------

            if os.path.exists(image_path):

                image = Image.open(image_path).convert("RGB")

                # Convert image to base64
                import base64
                from io import BytesIO

                buffer = BytesIO()
                image.save(buffer, format="JPEG")

                image_base64 = base64.b64encode(
                    buffer.getvalue()
                ).decode()

                st.markdown(
                    f'''
                    <div class="photo-frame">
                        <img src="data:image/jpeg;base64,{image_base64}">
                    </div>
                    ''',
                    unsafe_allow_html=True
                )

            else:

                st.warning(
                    f"Image not found: {member['image']}"
                )

            # -----------------------------
            # MEMBER NAME
            # -----------------------------

            st.markdown(
                f'''
                <div class="member-name">
                    {member["name"]}
                </div>
                ''',
                unsafe_allow_html=True
            )

            # -----------------------------
            # FULL NAME
            # -----------------------------

            st.markdown(
                f'''
                <div class="member-full-name">
                    {member["full_name"]}
                </div>
                ''',
                unsafe_allow_html=True
            )

            # -----------------------------
            # DATE OF BIRTH
            # -----------------------------

            st.markdown(
                f'''
                <div class="member-dob">
                    🎂 <b>Born:</b> {member["dob"]}
                </div>
                ''',
                unsafe_allow_html=True
            )

            st.write("")

            # -----------------------------
            # EXPLORE BUTTON
            # -----------------------------

            if st.button(
                f"Explore {member['name']}",
                key=f"member_{index}",
                use_container_width=True
            ):

                st.switch_page(member["page"])

            # -----------------------------
            # CARD END
            # -----------------------------

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


# =========================================================
# BACK HOME
# =========================================================

st.write("")
st.markdown("---")

if st.button(
    "🏠 Back to Home",
    use_container_width=True
):

    st.switch_page("pages/02_Home.py")
