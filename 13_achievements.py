import streamlit as st
from urllib.parse import quote_plus


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Achievements | BTS: The Journey",
    page_icon="🏆",
    layout="wide"
)


# =========================================================
# PURPLE THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #7544B8 0%, transparent 34%),
        radial-gradient(circle at bottom right, #43206B 0%, transparent 40%),
        linear-gradient(135deg, #28103F, #13081F, #09040D);
    color: white;
}

h1 {
    color: #FFFFFF !important;
    text-align: center !important;
    font-size: 52px !important;
    font-weight: 800 !important;
    letter-spacing: 2px !important;
}

h2, h3 {
    color: #FFFFFF !important;
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

[data-testid="stSuccess"] {
    background-color: rgba(83, 58, 115, 0.38) !important;
}

[data-testid="stExpander"] {
    background-color: rgba(62, 30, 88, 0.38);
    border: 1px solid rgba(210, 175, 245, 0.25);
    border-radius: 15px;
}

hr {
    border-color: rgba(220, 190, 255, 0.25) !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HELPER
# =========================================================

def search_link(text):
    query = quote_plus(f"BTS {text}")
    return f"https://www.google.com/search?q={query}"


def achievement_item(title, description):
    st.markdown(f"**🏆 {title}**")
    st.write(description)


# =========================================================
# TITLE
# =========================================================

st.title("🏆 BTS: ACHIEVEMENTS")

st.write(
    "From their first rookie award in 2013 to becoming one of the "
    "most influential music groups in the world, BTS have created "
    "a remarkable collection of awards, records, milestones and "
    "individual achievements."
)

st.divider()


# =========================================================
# THE FIRST AWARD
# =========================================================

st.header("💜 Where It All Began")

st.subheader("🏆 BTS's First Major Award — 2013")

st.write(
    "Before the stadiums, world records and historic chart moments, "
    "there were seven young artists standing on a stage with their "
    "first award in their hands."
)

st.write(
    "At the 2013 Melon Music Awards, BTS won the "
    "**Male New Artist Award**."
)

st.info(
    "🌟 Their first award was not the biggest trophy they would ever "
    "receive. But it was the beginning of something much bigger — "
    "the first little proof that the seven boys who had started "
    "with a dream were finally being seen."
)

st.write(
    "Years later, the same seven members would stand on some of the "
    "world's biggest stages. But every journey has a first step, and "
    "for BTS, this was one of those unforgettable beginnings. 💜"
)

if st.button(
    "See the 2013 Award →",
    key="first_award",
    use_container_width=True
):
    st.link_button(
        "Open 2013 Melon Music Awards",
        search_link("2013 Melon Music Awards BTS Male New Artist"),
        use_container_width=True
    )


# =========================================================
# GROUP AWARDS
# =========================================================

st.divider()

st.header("🏆 Group Awards & Major Honors")

group_awards = {

    "2013–2015 | Rookie Era": [
        (
            "2013 Melon Music Awards",
            "Male New Artist Award — BTS's first major award."
        ),
        (
            "2013 Golden Disc Awards",
            "BTS began collecting major rookie recognition during their debut era."
        ),
        (
            "2014–2015 Rookie Awards",
            "BTS continued receiving major rookie and new-artist recognition in Korea and internationally."
        )
    ],

    "2016–2017 | The Breakthrough": [
        (
            "2016 Melon Music Awards",
            "Album of the Year for The Most Beautiful Moment in Life: Young Forever."
        ),
        (
            "2016 MAMA",
            "Artist of the Year — a major turning point in BTS's career."
        ),
        (
            "2017 Billboard Music Awards",
            "Top Social Artist — BTS became the first Korean act to win the award."
        ),
        (
            "2017 MAMA",
            "BTS continued their rise with major year-end awards and international recognition."
        )
    ],

    "2018–2019 | Global Recognition": [
        (
            "2018 Billboard Music Awards",
            "Top Social Artist — BTS won the award again."
        ),
        (
            "2018 American Music Awards",
            "Favorite Social Artist."
        ),
        (
            "2019 Billboard Music Awards",
            "Top Social Artist and Top Duo/Group."
        ),
        (
            "2019 American Music Awards",
            "BTS received multiple major awards, including Artist of the Year."
        )
    ],

    "2020–2021 | Worldwide Dominance": [
        (
            "2020 Billboard Music Awards",
            "Top Social Artist — continuing BTS's record-setting run."
        ),
        (
            "2020 American Music Awards",
            "Favorite Social Artist and Favorite Duo or Group."
        ),
        (
            "2021 American Music Awards",
            "Artist of the Year, Favorite Pop Duo or Group and Favorite Pop Song."
        ),
        (
            "2021 Billboard Music Awards",
            "Top Selling Song for Dynamite and additional major recognition."
        )
    ],

    "2022–2026 | New Chapters": [
        (
            "2022–2023",
            "BTS and its members continued receiving major nominations, awards and chart recognition during the group's individual-activity period."
        ),
        (
            "2023",
            "Take Two marked BTS's group return to the charts during the group's individual-focus period."
        ),
        (
            "2026",
            "BTS returned to group activities with their new chapter and continued global recognition."
        )
    ]
}

for period, awards in group_awards.items():

    with st.expander(f"🏆 {period}"):

        for title, description in awards:
            achievement_item(title, description)


# =========================================================
# BILLBOARD & CHART ACHIEVEMENTS
# =========================================================

st.divider()

st.header("📊 Historic Chart Achievements")

chart_achievements = [

    (
        "First K-pop act to reach No. 1 on the US albums chart",
        "Love Yourself: Tear made BTS the first K-pop act to reach No. 1 on the Billboard 200."
    ),

    (
        "First K-pop act to reach No. 1 on the US Artist 100",
        "BTS became the first K-pop act to top Billboard's all-genre Artist 100 chart."
    ),

    (
        "Billboard Hot 100 No. 1",
        "Dynamite became BTS's first Billboard Hot 100 No. 1 and made BTS the first Korean act to achieve the milestone."
    ),

    (
        "Multiple Billboard 200 No. 1 albums",
        "BTS repeatedly reached No. 1 on the Billboard 200 with major albums."
    ),

    (
        "Multiple Hot 100 No. 1 songs",
        "BTS achieved multiple No. 1 singles on the Billboard Hot 100."
    ),

    (
        "Simultaneous Billboard 200 and Hot 100 No. 1",
        "BTS became the first group to top both major Billboard charts in the same week."
    ),

    (
        "Global chart success",
        "BTS reached No. 1 on major music charts in Korea, the United States, Japan, the UK and many other markets."
    )
]

for title, description in chart_achievements:
    achievement_item(title, description)


# =========================================================
# GUINNESS & WORLD RECORDS
# =========================================================

st.divider()

st.header("🌍 Guinness World Records & World Records")

records = [

    (
        "First K-pop act to reach No. 1 on the US albums chart",
        "BTS achieved the milestone with Love Yourself: Tear in 2018."
    ),

    (
        "First K-pop act to reach No. 1 on the US Artist 100",
        "BTS topped Billboard's Artist 100 in 2018."
    ),

    (
        "First K-pop group to reach the US singles Top 10",
        "Fake Love helped BTS become the first K-pop group to reach the US singles Top 10."
    ),

    (
        "Most weeks at No. 1 on Billboard Social 50",
        "BTS accumulated an extraordinary run at No. 1 on the Social 50 chart."
    ),

    (
        "Major Spotify group records",
        "BTS have held Guinness-recognized records connected with streaming and Spotify."
    ),

    (
        "Major livestream concert records",
        "BTS achieved major records for online concert attendance and livestream ticket sales."
    ),

    (
        "Best-selling album in South Korea",
        "Map of the Soul: 7 became one of BTS's major sales milestones and was recognized by Guinness."
    ),

    (
        "Multiple MAMA Grand Prize records",
        "BTS accumulated an exceptional number of grand-prize awards at the Mnet Asian Music Awards."
    )
]

for title, description in records:
    achievement_item(title, description)

if st.button(
    "🌍 Explore Guinness Records →",
    key="guinness",
    use_container_width=True
):
    st.link_button(
        "Open Guinness World Records",
        "https://www.guinnessworldrecords.com/",
        use_container_width=True
    )


# =========================================================
# GRAMMY
# =========================================================

st.divider()

st.header("🎤 GRAMMY Recognition")

st.write(
    "BTS became the first K-pop act to receive a GRAMMY nomination."
)

grammy_items = [

    (
        "63rd GRAMMY Awards",
        "Dynamite — Best Pop Duo/Group Performance nomination."
    ),

    (
        "64th GRAMMY Awards",
        "Butter — Best Pop Duo/Group Performance nomination."
    ),

    (
        "65th GRAMMY Awards",
        "BTS received nominations connected with Yet To Come, My Universe and Music of the Spheres."
    ),

    (
        "Overall GRAMMY record",
        "BTS have received five GRAMMY nominations and, as of the current GRAMMY artist record, have not won a GRAMMY."
    )
]

for title, description in grammy_items:
    achievement_item(title, description)

if st.button(
    "🎤 View BTS GRAMMY Record →",
    key="grammy",
    use_container_width=True
):
    st.link_button(
        "Open GRAMMY",
        "https://www.grammy.com/artists/bts/287749",
        use_container_width=True
    )


# =========================================================
# INTERNATIONAL ACHIEVEMENTS
# =========================================================

st.divider()

st.header("🌎 International Milestones")

international = [

    (
        "American Music Awards",
        "BTS became the first Korean act to win major categories at the American Music Awards and later achieved Artist of the Year."
    ),

    (
        "Billboard Music Awards",
        "BTS became the first Korean act to win a Billboard Music Award."
    ),

    (
        "United Nations",
        "BTS members delivered multiple speeches connected with UNICEF and the LOVE MYSELF campaign."
    ),

    (
        "Stadium Tours",
        "BTS became one of the first K-pop acts to successfully conduct major stadium-scale tours around the world."
    ),

    (
        "Global Pop Culture",
        "BTS helped expand the worldwide visibility and commercial reach of Korean popular music."
    )
]

for title, description in international:
    achievement_item(title, description)


# =========================================================
# CULTURAL & SOCIAL IMPACT
# =========================================================

st.divider()

st.header("💜 Cultural & Social Impact")

cultural = [

    (
        "Order of Cultural Merit",
        "The members received the Hwagwan Order of Cultural Merit in 2018 for their contribution to Korean culture."
    ),

    (
        "LOVE MYSELF Campaign",
        "BTS and BIGHIT partnered with UNICEF for the LOVE MYSELF campaign."
    ),

    (
        "UN General Assembly",
        "BTS participated in UN-related events and delivered speeches encouraging young people to value their own voices."
    ),

    (
        "Korean cultural representation",
        "BTS became major global representatives of Korean music and culture."
    ),

    (
        "21st Century Pop Icons",
        "Their worldwide influence has led BIGHIT to describe BTS as '21st century pop icons.'"
    )
]

for title, description in cultural:
    achievement_item(title, description)


# =========================================================
# SOLO ACHIEVEMENTS
# =========================================================

st.divider()

st.header("🌟 Solo Achievements")

st.write(
    "BTS's achievements did not stop with the group. Each member "
    "also created individual milestones through solo albums, songs, "
    "charts, records and international recognition."
)


# =========================================================
# RM
# =========================================================

with st.expander("💜 RM — Solo Achievements"):

    rm_items = [
        (
            "mono.",
            "RM's mono. became a major global streaming and chart success."
        ),
        (
            "Indigo",
            "Indigo expanded RM's identity as a solo artist and songwriter."
        ),
        (
            "Come Back to Me",
            "The single received significant international chart attention."
        ),
        (
            "LOST!",
            "RM continued international recognition with Right Place, Wrong Person."
        ),
        (
            "Solo artistry",
            "RM is recognized for songwriting, production, lyricism and collaborations beyond BTS."
        )
    ]

    for title, description in rm_items:
        achievement_item(title, description)


# =========================================================
# JIN
# =========================================================

with st.expander("💜 Jin — Solo Achievements"):

    jin_items = [
        (
            "The Astronaut",
            "Jin's solo single achieved major global chart and streaming attention."
        ),
        (
            "Happy",
            "Happy became another major chapter in Jin's solo discography."
        ),
        (
            "Running Wild",
            "Jin continued his solo chart presence with Running Wild."
        ),
        (
            "Yours",
            "Yours became an internationally recognized OST release."
        ),
        (
            "Solo career",
            "Jin established a distinct solo identity while continuing his BTS career."
        )
    ]

    for title, description in jin_items:
        achievement_item(title, description)


# =========================================================
# SUGA
# =========================================================

with st.expander("💜 SUGA / Agust D — Solo Achievements"):

    suga_items = [
        (
            "Agust D trilogy",
            "SUGA developed the Agust D project across multiple releases."
        ),
        (
            "D-DAY",
            "D-DAY became a major global solo album for SUGA."
        ),
        (
            "Haegeum",
            "Haegeum became one of SUGA's most internationally recognized solo tracks."
        ),
        (
            "SUGA | Agust D TOUR",
            "SUGA completed a major worldwide solo tour."
        ),
        (
            "Producer achievements",
            "SUGA has written and produced music for BTS and other artists."
        )
    ]

    for title, description in suga_items:
        achievement_item(title, description)


# =========================================================
# J-HOPE
# =========================================================

with st.expander("💜 j-hope — Solo Achievements"):

    jhope_items = [
        (
            "Hope World",
            "Hope World established j-hope's solo identity and reached international audiences."
        ),
        (
            "Jack In The Box",
            "Jack In The Box became a major solo album and expanded his artistic direction."
        ),
        (
            "MORE",
            "MORE marked a new musical chapter for j-hope."
        ),
        (
            "Arson",
            "Arson became one of his signature solo releases."
        ),
        (
            "on the street",
            "The song connected j-hope with international collaboration and global audiences."
        ),
        (
            "Solo headline performances",
            "j-hope became the first Korean artist to headline major festival stages including Lollapalooza."
        )
    ]

    for title, description in jhope_items:
        achievement_item(title, description)


# =========================================================
# JIMIN
# =========================================================

with st.expander("💜 Jimin — Solo Achievements"):

    jimin_items = [
        (
            "FACE",
            "FACE became a major global solo album and reached No. 1 on the Billboard 200."
        ),
        (
            "Like Crazy",
            "Like Crazy made Jimin the first Korean solo artist to reach No. 1 on the Billboard Hot 100."
        ),
        (
            "Set Me Free Pt.2",
            "The song achieved major global chart success."
        ),
        (
            "Who",
            "Who became one of Jimin's major international solo hits."
        ),
        (
            "Solo chart milestones",
            "Jimin achieved major milestones across Billboard and international charts."
        )
    ]

    for title, description in jimin_items:
        achievement_item(title, description)


# =========================================================
# V
# =========================================================

with st.expander("💜 V — Solo Achievements"):

    v_items = [
        (
            "Layover",
            "Layover became V's first solo album and achieved major global chart success."
        ),
        (
            "Love Me Again",
            "Love Me Again became one of V's major solo singles."
        ),
        (
            "Slow Dancing",
            "Slow Dancing became a major international solo release."
        ),
        (
            "FRI(END)S",
            "FRI(END)S continued V's international solo chart presence."
        ),
        (
            "Christmas Tree",
            "Christmas Tree became a widely recognized Korean OST and solo release."
        )
    ]

    for title, description in v_items:
        achievement_item(title, description)


# =========================================================
# JUNGKOOK
# =========================================================

with st.expander("💜 Jungkook — Solo Achievements"):

    jk_items = [
        (
            "Seven",
            "Seven became a major global hit and achieved No. 1 positions on major worldwide charts."
        ),
        (
            "Standing Next to You",
            "Standing Next to You became one of Jungkook's signature solo songs."
        ),
        (
            "GOLDEN",
            "GOLDEN became Jungkook's major solo album and achieved significant global chart success."
        ),
        (
            "3D",
            "3D became another major international solo hit."
        ),
        (
            "Solo Spotify records",
            "Jungkook established major streaming milestones as a solo artist."
        ),
        (
            "Global solo recognition",
            "Jungkook became one of the most commercially successful Korean solo artists internationally."
        )
    ]

    for title, description in jk_items:
        achievement_item(title, description)


# =========================================================
# SEVEN MEMBERS
# =========================================================

st.divider()

st.header("💜 Seven Members. Seven Stories.")

st.write(
    "BTS's story is not only about trophies. It is also about seven "
    "artists growing individually while continuing to be connected "
    "by the journey they started together."
)

st.success(
    "RM • Jin • SUGA • j-hope • Jimin • V • Jungkook"
)


# =========================================================
# OFFICIAL SOURCES
# =========================================================

st.divider()

st.header("🔗 Achievement Sources")

col1, col2 = st.columns(2)

with col1:

    st.link_button(
        "🏆 Guinness World Records",
        "https://www.guinnessworldrecords.com/",
        use_container_width=True
    )

with col2:

    st.link_button(
        "🎤 GRAMMY — BTS",
        "https://www.grammy.com/artists/bts/287749",
        use_container_width=True
    )


# =========================================================
# NAVIGATION
# =========================================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "← Back to Home",
        key="back_home",
        use_container_width=True
    ):
        st.switch_page("pages/02_Home.py")


with col2:

    if st.button(
        "Next: Timeline →",
        key="next_timeline",
        use_container_width=True
    ):
        st.switch_page("pages/14_timeline.py")


# =========================================================
# FOOTER
# =========================================================

st.write("")

st.caption(
    "💜 BTS: The Journey • From seven dreams to a worldwide legacy."
)