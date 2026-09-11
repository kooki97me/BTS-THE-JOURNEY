import streamlit as st


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Timeline | BTS: The Journey",
    page_icon="📅",
    layout="wide"
)


# =========================================================
# PURPLE THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #6F3FA8 0%, transparent 34%),
        radial-gradient(circle at bottom right, #3F1E61 0%, transparent 40%),
        linear-gradient(135deg, #241034, #12081B, #08040C);
    color: white;
}

h1 {
    color: white !important;
    text-align: center !important;
    font-size: 52px !important;
    font-weight: 800 !important;
    letter-spacing: 2px !important;
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
    background: linear-gradient(135deg, #9155C1, #5D3380);
    color: white;
    font-size: 15px;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #B276D8, #75469B);
    border-color: #E5D0FF;
    color: white;
}

[data-testid="stInfo"] {
    background-color: rgba(91, 48, 126, 0.35) !important;
    border: 1px solid rgba(210, 175, 245, 0.3) !important;
}

[data-testid="stExpander"] {
    background-color: rgba(61, 30, 86, 0.40);
    border: 1px solid rgba(210, 175, 245, 0.25);
    border-radius: 15px;
}

hr {
    border-color: rgba(220, 190, 255, 0.25) !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.title("📅 BTS: THE JOURNEY")

st.write(
    "From seven young artists beginning their journey in 2013 "
    "to becoming global music icons, explore the important moments "
    "that shaped BTS year by year."
)

st.divider()


# =========================================================
# 2013
# =========================================================

with st.expander("💜 2013 — The Beginning", expanded=True):

    st.subheader("June 13, 2013 — BTS Debut")

    st.write(
        "BTS officially debuted with the single album "
        "**2 COOL 4 SKOOL** and the title track **No More Dream**."
    )

    st.write(
        "Seven members — RM, Jin, SUGA, j-hope, Jimin, V and Jungkook — "
        "began a journey that would eventually reach audiences around "
        "the world."
    )

    st.info(
        "🌟 Every legendary journey has a beginning. "
        "For BTS, it started with seven members, one stage and a dream."
    )

    st.subheader("Later in 2013")

    st.write(
        "BTS released their first mini album **O!RUL8,2?** "
        "and began establishing their identity in the Korean music scene."
    )

    st.write(
        "They also received their first major rookie awards."
    )


# =========================================================
# 2014
# =========================================================

with st.expander("💜 2014 — Finding Their Identity"):

    st.subheader("SKOOL LUV AFFAIR")

    st.write(
        "BTS released **SKOOL LUV AFFAIR**, continuing their early "
        "school trilogy and exploring themes of youth and love."
    )

    st.subheader("DARK & WILD")

    st.write(
        "Their first full-length Korean studio album, "
        "**DARK & WILD**, showed a stronger musical identity."
    )

    st.subheader("First Japanese Chapter")

    st.write(
        "BTS began expanding into Japan and released Japanese music "
        "alongside their Korean releases."
    )


# =========================================================
# 2015
# =========================================================

with st.expander("💜 2015 — The Most Beautiful Moment in Life"):

    st.subheader("The Most Beautiful Moment in Life Pt.1")

    st.write(
        "BTS entered a new era with **I NEED U**, beginning "
        "The Most Beautiful Moment in Life series."
    )

    st.subheader("The Most Beautiful Moment in Life Pt.2")

    st.write(
        "The second part of the series introduced **RUN** and "
        "continued the story of youth, friendship and uncertainty."
    )

    st.info(
        "✨ This era became an important turning point in BTS's career."
    )


# =========================================================
# 2016
# =========================================================

with st.expander("💜 2016 — WINGS"):

    st.subheader("Young Forever")

    st.write(
        "The Most Beautiful Moment in Life: Young Forever "
        "completed the HYYH era."
    )

    st.subheader("WINGS")

    st.write(
        "BTS released **WINGS**, their second Korean studio album, "
        "and began exploring themes of temptation, growth and identity."
    )

    st.write(
        "The album became a major commercial and artistic milestone "
        "for BTS."
    )

    st.subheader("First Major Daesang Era")

    st.write(
        "BTS began receiving major year-end grand prizes, marking "
        "their transition from rising artists to major Korean acts."
    )


# =========================================================
# 2017
# =========================================================

with st.expander("💜 2017 — The World Starts Watching"):

    st.subheader("You Never Walk Alone")

    st.write(
        "BTS expanded the WINGS era with **You Never Walk Alone** "
        "and released songs including **Spring Day** and **Not Today**."
    )

    st.subheader("Billboard Music Awards")

    st.write(
        "BTS won **Top Social Artist** at the Billboard Music Awards."
    )

    st.info(
        "🌎 This was a historic moment: BTS became the first Korean act "
        "to win the Billboard Music Award."
    )

    st.subheader("LOVE YOURSELF Begins")

    st.write(
        "The **LOVE YOURSELF** era began with "
        "**LOVE YOURSELF 承 'Her'** and the hit song **DNA**."
    )


# =========================================================
# 2018
# =========================================================

with st.expander("💜 2018 — A Global Breakthrough"):

    st.subheader("LOVE YOURSELF 轉 'Tear'")

    st.write(
        "BTS released **FAKE LOVE** and their album "
        "**LOVE YOURSELF 轉 'Tear'**."
    )

    st.subheader("Billboard 200 No. 1")

    st.write(
        "LOVE YOURSELF 轉 'Tear' reached No. 1 on the Billboard 200, "
        "making BTS the first K-pop act to top the US albums chart."
    )

    st.subheader("United Nations")

    st.write(
        "RM delivered BTS's first major speech at the United Nations "
        "as part of the UNICEF LOVE MYSELF campaign."
    )

    st.subheader("Order of Cultural Merit")

    st.write(
        "The members received the Hwagwan Order of Cultural Merit "
        "for their contribution to Korean culture."
    )

    st.subheader("LOVE YOURSELF 結 'Answer'")

    st.write(
        "The LOVE YOURSELF series concluded with "
        "**LOVE YOURSELF 結 'Answer'**."
    )


# =========================================================
# 2019
# =========================================================

with st.expander("💜 2019 — MAP OF THE SOUL"):

    st.subheader("MAP OF THE SOUL: PERSONA")

    st.write(
        "BTS began a new era with **Boy With Luv**, featuring "
        "Halsey, and the album MAP OF THE SOUL: PERSONA."
    )

    st.subheader("Global Stadium Shows")

    st.write(
        "BTS expanded their touring scale and performed major "
        "stadium shows around the world."
    )

    st.subheader("BTS WORLD")

    st.write(
        "The mobile game BTS WORLD was released, featuring "
        "BTS-related stories and music."
    )


# =========================================================
# 2020
# =========================================================

with st.expander("💜 2020 — A Historic Year"):

    st.subheader("MAP OF THE SOUL: 7")

    st.write(
        "BTS released **MAP OF THE SOUL: 7**, one of their most "
        "ambitious albums."
    )

    st.subheader("Dynamite")

    st.write(
        "BTS released **Dynamite**, their first English-language "
        "single."
    )

    st.info(
        "💜 Dynamite reached No. 1 on the Billboard Hot 100 and "
        "became a landmark moment for BTS and K-pop."
    )

    st.subheader("BE")

    st.write(
        "BTS released **BE**, featuring **Life Goes On**, which "
        "also reached No. 1 on the Billboard Hot 100."
    )

    st.subheader("GRAMMY Nomination")

    st.write(
        "Dynamite earned BTS their first GRAMMY nomination."
    )


# =========================================================
# 2021
# =========================================================

with st.expander("💜 2021 — Butter & Permission to Dance"):

    st.subheader("Butter")

    st.write(
        "BTS released **Butter**, which became another massive "
        "global hit."
    )

    st.subheader("Permission to Dance")

    st.write(
        "BTS released **Permission to Dance**, continuing their "
        "English-language global success."
    )

    st.subheader("My Universe")

    st.write(
        "BTS collaborated with Coldplay on **My Universe**."
    )

    st.subheader("American Music Awards")

    st.write(
        "BTS achieved major success at the American Music Awards, "
        "including Artist of the Year."
    )


# =========================================================
# 2022
# =========================================================

with st.expander("💜 2022 — PROOF & A New Chapter"):

    st.subheader("PROOF")

    st.write(
        "BTS released **PROOF**, an anthology album looking back "
        "at their journey while opening the door to a new chapter."
    )

    st.subheader("Yet to Come")

    st.write(
        "The title track **Yet to Come** reflected on BTS's past "
        "while looking toward their future."
    )

    st.subheader("Individual Activities")

    st.write(
        "The members began focusing more on individual music, "
        "projects and personal artistic activities."
    )

    st.info(
        "💜 The group journey continued, even as each member "
        "began exploring their own artistic path."
    )


# =========================================================
# 2023
# =========================================================

with st.expander("💜 2023 — Seven Individual Paths"):

    st.subheader("Solo Releases")

    st.write(
        "The members released major solo projects and explored "
        "different musical styles."
    )

    st.write(
        "RM, Jin, SUGA, j-hope, Jimin, V and Jungkook each "
        "continued building their individual artistic identities."
    )

    st.subheader("Take Two")

    st.write(
        "BTS released **Take Two**, a special group single celebrating "
        "their journey and connection with ARMY."
    )

    st.subheader("Jungkook — GOLDEN")

    st.write(
        "Jungkook released his solo album **GOLDEN**, following "
        "the global success of his solo singles."
    )


# =========================================================
# 2024
# =========================================================

with st.expander("💜 2024 — Solo Chapters Continue"):

    st.subheader("Jin")

    st.write(
        "Jin continued his solo activities and later released "
        "his solo album **Happy**."
    )

    st.subheader("RM")

    st.write(
        "RM released **Right Place, Wrong Person**, expanding "
        "his individual musical world."
    )

    st.subheader("Jimin")

    st.write(
        "Jimin continued his solo journey with music including "
        "his album **MUSE**."
    )

    st.subheader("J-Hope")

    st.write(
        "j-hope continued his solo activities and music projects."
    )

    st.subheader("V")

    st.write(
        "V continued releasing music and special projects while "
        "serving his individual artistic chapter."
    )


# =========================================================
# 2025
# =========================================================

with st.expander("💜 2025 — The Members Move Toward Reunion"):

    st.write(
        "The members continued their individual activities and "
        "military-service related schedules while preparing for "
        "the next chapter of BTS."
    )

    st.subheader("Solo Music Continues")

    st.write(
        "Individual releases, performances and collaborations "
        "continued to keep BTS connected with fans around the world."
    )

    st.info(
        "💜 Seven individual journeys were still connected by "
        "one shared history."
    )


# =========================================================
# 2026
# =========================================================

with st.expander("💜 2026 — BTS Returns"):

    st.subheader("A New BTS Chapter")

    st.write(
        "BTS entered a new group chapter after the members completed "
        "their individual service periods and activities."
    )

    st.subheader("ARIRANG")

    st.write(
        "BTS released **ARIRANG**, beginning another major chapter "
        "in their group discography."
    )

    st.info(
        "🌟 Seven members. One group. A new chapter begins."
    )


# =========================================================
# THE JOURNEY
# =========================================================

st.divider()

st.header("💜 The Journey in One Story")

st.write(
    "2013 gave BTS their first stage."
)

st.write(
    "2015 gave them the beginning of the HYYH era."
)

st.write(
    "2017 opened the door to a much larger international audience."
)

st.write(
    "2018 proved that a Korean group could stand at the top "
    "of the US albums chart."
)

st.write(
    "2020 brought historic global chart success."
)

st.write(
    "2022 opened a new chapter of individual growth."
)

st.write(
    "And 2026 brought another chapter for all seven members together."
)

st.success(
    "💜 Seven members • Thirteen years of memories • One extraordinary journey"
)


# =========================================================
# NAVIGATION
# =========================================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "← Back to Achievements",
        key="back_achievements",
        use_container_width=True
    ):
        st.switch_page("pages/13_achievements.py")


with col2:

    if st.button(
        "Next: Unknown Stories →",
        key="next_stories",
        use_container_width=True
    ):
        st.switch_page("pages/15_stories.py")


# =========================================================
# FOOTER
# =========================================================

st.write("")

st.caption(
    "💜 BTS: The Journey • From 2013 to the next chapter."
)