import streamlit as st

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="Home | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# ---------------------------------------------------------
# PURPLE THEME
# ---------------------------------------------------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #7544B8 0%, transparent 35%),
        radial-gradient(circle at bottom right, #43206B 0%, transparent 40%),
        linear-gradient(135deg, #28103F, #13081F, #09040D);
    color: white;
}

h1 {
    color: white !important;
    text-align: center !important;
    font-size: 52px !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: white !important;
}

p {
    color: #EDE2F8 !important;
    line-height: 1.7 !important;
}

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(220, 190, 255, 0.45);
    background: linear-gradient(135deg, #9A5BCB, #60328A);
    color: white;
    font-size: 15px;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #B77BE0, #78469F);
    border-color: #E5D0FF;
    color: white;
}

[data-testid="stInfo"] {
    background-color: rgba(103, 56, 143, 0.35) !important;
    border: 1px solid rgba(210, 175, 245, 0.3) !important;
}

hr {
    border-color: rgba(220, 190, 255, 0.25) !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("BTS: THE JOURNEY")

st.markdown(
    '<p style="text-align: center; font-size: 20px; color: #EDE2F8;">'
    'Seven members. One extraordinary journey. 💜'
    '</p>',
    unsafe_allow_html=True
)
st.divider()

# ---------------------------------------------------------
# WELCOME
# ---------------------------------------------------------

st.header("💜 Welcome, ARMY")

st.write(
    "Welcome to BTS: The Journey — a place for new and old ARMYs "
    "to explore the story, music, members, achievements and memories "
    "of BTS."
)

st.info(
    "Explore the different sections below and discover the journey "
    "of seven members who created something extraordinary together."
)

st.divider()

# 🔎 Search Bar
st.header("🔎 Search BTS: The Journey")

search_query = st.text_input(
    "Search",
    placeholder="Search for RM, Jin, Dynamite, Wings, achievements...",
    label_visibility="collapsed"
)

if search_query:
    query = search_query.lower().strip()

    search_data = {
        "rm": "pages/04_rm.py",
        "kim namjoon": "pages/04_rm.py",
        "namjoon": "pages/04_rm.py",

        "jin": "pages/05_jin.py",
        "seokjin": "pages/05_jin.py",

        "suga": "pages/06_suga.py",
        "yoongi": "pages/06_suga.py",

        "j-hope": "pages/07_jhope.py",
        "jhope": "pages/07_jhope.py",
        "hoseok": "pages/07_jhope.py",

        "jimin": "pages/08_jimin.py",

        "v": "pages/09_v.py",
        "taehyung": "pages/09_v.py",

        "jungkook": "pages/10_jk.py",
        "jk": "pages/10_jk.py",

        "ot7": "pages/11_OT7.py",
        "members": "pages/03_Members.py",

        "music": "pages/12_music.py",
        "album": "pages/12_music.py",
        "albums": "pages/12_music.py",
        "songs": "pages/12_music.py",
        "dynamite": "pages/12_music.py",
        "butter": "pages/12_music.py",
        "wings": "pages/12_music.py",

        "achievement": "pages/13_achievements.py",
        "achievements": "pages/13_achievements.py",
        "awards": "pages/13_achievements.py",

        "timeline": "pages/14_timeline.py",
        "history": "pages/14_timeline.py",

        "stories": "pages/15_stories.py",
        "unknown stories": "pages/15_stories.py",

        "army": "pages/16_army_space.py",
        "army space": "pages/16_army_space.py",
    }

    if query in search_data:
        st.success(f"Opening results for: {search_query}")
        st.switch_page(search_data[query])

    else:
        # Partial search
        matches = []

        for keyword, page in search_data.items():
            if query in keyword:
                if page not in matches:
                    matches.append(page)

        if matches:
            st.info(f"Found {len(matches)} matching section(s).")

            for page in matches:
                if "04_rm" in page:
                    st.write("💜 RM")
                    if st.button("Open RM", key="search_rm"):
                        st.switch_page(page)

                elif "05_jin" in page:
                    st.write("💜 Jin")
                    if st.button("Open Jin", key="search_jin"):
                        st.switch_page(page)

                elif "06_suga" in page:
                    st.write("💜 SUGA")
                    if st.button("Open SUGA", key="search_suga"):
                        st.switch_page(page)

                elif "07_jhope" in page:
                    st.write("💜 J-Hope")
                    if st.button("Open J-Hope", key="search_jhope"):
                        st.switch_page(page)

                elif "08_jimin" in page:
                    st.write("💜 Jimin")
                    if st.button("Open Jimin", key="search_jimin"):
                        st.switch_page(page)

                elif "09_v" in page:
                    st.write("💜 V")
                    if st.button("Open V", key="search_v"):
                        st.switch_page(page)

                elif "10_jk" in page:
                    st.write("💜 Jungkook")
                    if st.button("Open Jungkook", key="search_jk"):
                        st.switch_page(page)

                elif "12_music" in page:
                    st.write("🎵 Music & Albums")
                    if st.button("Open Music", key="search_music"):
                        st.switch_page(page)

                elif "13_achievements" in page:
                    st.write("🏆 Achievements")
                    if st.button("Open Achievements", key="search_achievements"):
                        st.switch_page(page)

                elif "14_timeline" in page:
                    st.write("📅 Timeline")
                    if st.button("Open Timeline", key="search_timeline"):
                        st.switch_page(page)

                elif "15_stories" in page:
                    st.write("📖 Unknown Stories")
                    if st.button("Open Stories", key="search_stories"):
                        st.switch_page(page)

                elif "16_army_space" in page:
                    st.write("💜 ARMY Space")
                    if st.button("Open ARMY Space", key="search_army"):
                        st.switch_page(page)

        else:
            st.warning("No results found. Try searching for a member, album, song or section.")


# ---------------------------------------------------------
# EXPLORE BTS
# ---------------------------------------------------------

st.header("✨ Explore BTS")

# ---------------------------------------------------------
# MEMBERS + MUSIC
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Meet the Members")

    st.write(
        "Get to know RM, Jin, SUGA, J-Hope, Jimin, V and Jungkook. "
        "Explore their personalities, talents and individual journeys."
    )

    if st.button(
        "Explore Members →",
        key="members_home",
        use_container_width=True
    ):
        st.switch_page("pages/03_Members.py")

with col2:
    st.subheader("🎵 Albums & Music")

    st.write(
        "Explore BTS albums, releases, songs, Japanese music "
        "and member solo music."
    )

    if st.button(
        "Explore Music →",
        key="music_home",
        use_container_width=True
    ):
        st.switch_page("pages/12_music.py")

# ---------------------------------------------------------
# ACHIEVEMENTS + TIMELINE
# ---------------------------------------------------------

col3, col4 = st.columns(2)

with col3:
    st.subheader("🏆 Achievements")

    st.write(
        "Discover important milestones, awards, records and "
        "achievements from BTS's incredible career."
    )

    if st.button(
        "Explore Achievements →",
        key="achievements_home",
        use_container_width=True
    ):
        st.switch_page("pages/13_achievements.py")

with col4:
    st.subheader("📅 The Timeline")

    st.write(
        "Travel through BTS history from their debut in 2013 "
        "to their latest chapter."
    )

    if st.button(
        "Explore Timeline →",
        key="timeline_home",
        use_container_width=True
    ):
        st.switch_page("pages/14_timeline.py")

# ---------------------------------------------------------
# UNKNOWN STORIES + ARMY SPACE
# ---------------------------------------------------------

col5, col6 = st.columns(2)

with col5:
    st.subheader("🔮 Unknown Stories")

    st.write(
        "Discover interesting facts, lesser-known stories and "
        "memorable moments from BTS's journey."
    )

    if st.button(
        "Explore Stories →",
        key="stories_home",
        use_container_width=True
    ):
        st.switch_page("pages/15_stories.py")

with col6:
    st.subheader("💜 ARMY Space")

    st.write(
        "A special space for ARMYs to share memories, messages "
        "and moments connected with BTS."
    )

    if st.button(
        "Enter ARMY Space →",
        key="army_home",
        use_container_width=True
    ):
        st.switch_page("pages/16_army_space.py")

# ---------------------------------------------------------
# JOURNEY MESSAGE
# ---------------------------------------------------------

st.divider()

st.header("🌌 One Journey, Seven Stories")

st.write(
    "Every member has a different story, but together they created "
    "the story of BTS. This website is a journey through those "
    "stories, memories, music and moments."
)

st.info(
    "💜 Seven members • Countless memories • One extraordinary journey"
)
