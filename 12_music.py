import streamlit as st
from urllib.parse import quote_plus

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="Music | BTS: The Journey",
    page_icon="🎵",
    layout="wide"
)

# ---------------------------------------------------------
# PURPLE THEME
# ---------------------------------------------------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #7040A8 0%, transparent 32%),
        radial-gradient(circle at bottom right, #432064 0%, transparent 38%),
        linear-gradient(135deg, #241033, #12081B, #08040C);
    color: white;
}

h1 {
    color: #FFFFFF !important;
    text-align: center !important;
    font-size: 50px !important;
    font-weight: 800 !important;
    letter-spacing: 2px !important;
}

h2, h3 {
    color: #FFFFFF !important;
}

p {
    color: #E9DDF5 !important;
}

.stButton > button,
.stLinkButton > a {
    border-radius: 12px !important;
    border: 1px solid rgba(220, 190, 255, 0.35) !important;
    background: linear-gradient(135deg, #8E52BD, #5D3480) !important;
    color: white !important;
    font-weight: 700 !important;
}

.stButton > button:hover,
.stLinkButton > a:hover {
    background: linear-gradient(135deg, #A96DD3, #75449B) !important;
    border-color: #E5CCFA !important;
}

[data-testid="stExpander"] {
    background: rgba(70, 34, 94, 0.38);
    border: 1px solid rgba(210, 175, 240, 0.25);
    border-radius: 15px;
}

[data-testid="stInfo"] {
    background: rgba(86, 45, 120, 0.35) !important;
    border: 1px solid rgba(210, 175, 240, 0.25) !important;
}

hr {
    border-color: rgba(220, 190, 255, 0.25) !important;
}

.song-box {
    padding: 10px 0;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SONG LINK FUNCTION
# ---------------------------------------------------------

def youtube_link(song):
    search = quote_plus(f"BTS {song} official")
    return f"https://www.youtube.com/results?search_query={search}"


def show_song(song, number):
    col1, col2 = st.columns([5, 1])

    with col1:
        st.write(f"**{number}. {song}**")

    with col2:
        st.link_button(
            "▶ Listen",
            youtube_link(song),
            use_container_width=True
        )


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🎵 BTS: MUSIC")

st.write(
    "Explore BTS music from their debut in 2013 to their latest releases, "
    "including Korean albums, Japanese releases, special albums, singles "
    "and major group projects."
)

st.divider()

# ---------------------------------------------------------
# ALBUM DATA
# ---------------------------------------------------------

albums = {

    "2013 — 2 COOL 4 SKOOL": {
        "type": "Single Album",
        "tracks": [
            "Intro: 2 COOL 4 SKOOL",
            "We Are Bulletproof Pt.2",
            "Skit: Circle Room Talk",
            "No More Dream",
            "Interlude",
            "Like",
            "Outro: Circle Room Cypher",
            "Hidden Track: Path"
        ]
    },

    "2013 — O!RUL8,2?": {
        "type": "1st Mini Album",
        "tracks": [
            "Intro: O!RUL8,2?",
            "N.O",
            "We On",
            "Skit: R U Happy Now?",
            "If I Ruled the World",
            "Coffee",
            "BTS Cypher Pt.1",
            "Attack on Bangtan",
            "Paldogangsan",
            "Outro: Luv in Skool"
        ]
    },

    "2014 — SKOOL LUV AFFAIR": {
        "type": "2nd Mini Album",
        "tracks": [
            "Intro: Skool Luv Affair",
            "Boy In Luv",
            "Skit: Soulmate",
            "Where You From",
            "Just One Day",
            "Tomorrow",
            "BTS Cypher Pt.2: Triptych",
            "Spine Breaker",
            "Jump",
            "Outro: Propose"
        ]
    },

    "2014 — SKOOL LUV AFFAIR SPECIAL ADDITION": {
        "type": "Special Album",
        "tracks": [
            "Miss Right",
            "Like (Slow Jam Remix)",
            "Intro: Skool Luv Affair",
            "Boy In Luv",
            "Just One Day",
            "Tomorrow",
            "Spine Breaker",
            "Jump",
            "Outro: Propose"
        ]
    },

    "2014 — DARK & WILD": {
        "type": "1st Studio Album",
        "tracks": [
            "Intro: What Am I to You?",
            "Danger",
            "War of Hormone",
            "Hip Hop Phile",
            "Let Me Know",
            "Rain",
            "BTS Cypher Pt.3: Killer",
            "Interlude: What Are You Doing Now?",
            "Could You Turn Off Your Cell Phone",
            "Embarrassed",
            "24/7=Heaven",
            "Look Here",
            "2nd Grade",
            "Outro: Does That Make Sense?"
        ]
    },

    "2015 — THE MOST BEAUTIFUL MOMENT IN LIFE Pt.1": {
        "type": "3rd Mini Album",
        "tracks": [
            "Intro: The Most Beautiful Moment in Life",
            "I NEED U",
            "Hold Me Tight",
            "Skit: Expectation!",
            "Dope",
            "Boyz with Fun",
            "Converse High",
            "Moving On",
            "Outro: Love Is Not Over"
        ]
    },

    "2015 — THE MOST BEAUTIFUL MOMENT IN LIFE Pt.2": {
        "type": "4th Mini Album",
        "tracks": [
            "Intro: Never Mind",
            "Run",
            "Butterfly",
            "Whalien 52",
            "Ma City",
            "Silver Spoon",
            "Autumn Leaves",
            "Outro: House of Cards"
        ]
    },

    "2016 — THE MOST BEAUTIFUL MOMENT IN LIFE: YOUNG FOREVER": {
        "type": "Special Album",
        "tracks": [
            "Intro: The Most Beautiful Moment in Life",
            "I NEED U",
            "Hold Me Tight",
            "Autumn Leaves",
            "Butterfly",
            "Run",
            "Ma City",
            "Silver Spoon",
            "Dope",
            "Fire",
            "Save Me",
            "Epilogue: Young Forever",
            "House of Cards",
            "Love Is Not Over",
            "Converse High",
            "Moving On",
            "Whalien 52"
        ]
    },

    "2016 — WINGS": {
        "type": "2nd Studio Album",
        "tracks": [
            "Intro: Boy Meets Evil",
            "Blood Sweat & Tears",
            "Begin",
            "Lie",
            "Stigma",
            "First Love",
            "Reflection",
            "MAMA",
            "Awake",
            "Lost",
            "BTS Cypher 4",
            "Am I Wrong",
            "21st Century Girl",
            "2! 3!",
            "Interlude: Wings"
        ]
    },

    "2017 — YOU NEVER WALK ALONE": {
        "type": "Repackage Album",
        "tracks": [
            "Intro: Boy Meets Evil",
            "Blood Sweat & Tears",
            "Begin",
            "Lie",
            "Stigma",
            "First Love",
            "Reflection",
            "MAMA",
            "Awake",
            "Lost",
            "BTS Cypher 4",
            "Am I Wrong",
            "21st Century Girl",
            "2! 3!",
            "Spring Day",
            "Not Today",
            "Outro: Wings",
            "A Supplementary Story: You Never Walk Alone"
        ]
    },

    "2017 — LOVE YOURSELF 承 'Her'": {
        "type": "5th Mini Album",
        "tracks": [
            "Intro: Serendipity",
            "DNA",
            "Best of Me",
            "Dimple",
            "Pied Piper",
            "Skit: Billboard Music Awards Speech",
            "MIC Drop",
            "Go Go",
            "Outro: Her"
        ]
    },

    "2018 — LOVE YOURSELF 轉 'Tear'": {
        "type": "3rd Studio Album",
        "tracks": [
            "Intro: Singularity",
            "FAKE LOVE",
            "The Truth Untold",
            "134340",
            "Paradise",
            "Love Maze",
            "Magic Shop",
            "Airplane pt.2",
            "Anpanman",
            "So What",
            "Outro: Tear"
        ]
    },

    "2018 — LOVE YOURSELF 結 'Answer'": {
        "type": "Repackage Album",
        "tracks": [
            "Euphoria",
            "Trivia 起: Just Dance",
            "Serendipity (Full Length Edition)",
            "DNA",
            "Dimple",
            "Trivia 承: Love",
            "Her",
            "Singularity",
            "FAKE LOVE",
            "The Truth Untold",
            "Trivia 轉: Seesaw",
            "Tear",
            "Epiphany",
            "I'm Fine",
            "IDOL",
            "Answer: Love Myself",
            "Magic Shop",
            "Best of Me",
            "Airplane pt.2",
            "Go Go",
            "Anpanman",
            "MIC Drop"
        ]
    },

    "2019 — MAP OF THE SOUL: PERSONA": {
        "type": "6th Mini Album",
        "tracks": [
            "Intro: Persona",
            "Boy With Luv",
            "Mikrokosmos",
            "Make It Right",
            "HOME",
            "Jamais Vu",
            "Dionysus"
        ]
    },

    "2020 — MAP OF THE SOUL: 7": {
        "type": "4th Studio Album",
        "tracks": [
            "Intro: Persona",
            "Boy With Luv",
            "Make It Right",
            "Jamais Vu",
            "Dionysus",
            "Interlude: Shadow",
            "Black Swan",
            "Filter",
            "My Time",
            "Louder than bombs",
            "ON",
            "UGH!",
            "00:00 (Zero O'Clock)",
            "Inner Child",
            "Friends",
            "Moon",
            "Respect",
            "We are Bulletproof: the Eternal",
            "Outro: Ego"
        ]
    },

    "2020 — BE": {
        "type": "Special Album",
        "tracks": [
            "Life Goes On",
            "Fly To My Room",
            "Blue & Grey",
            "Skit",
            "Telepathy",
            "Dis-ease",
            "Stay",
            "Dynamite"
        ]
    },

    "2022 — PROOF": {
        "type": "Anthology Album",
        "tracks": [
            "Born Singer",
            "No More Dream",
            "N.O",
            "Boy In Luv",
            "Danger",
            "I NEED U",
            "Run",
            "Fire",
            "Blood Sweat & Tears",
            "Spring Day",
            "DNA",
            "FAKE LOVE",
            "IDOL",
            "Boy With Luv",
            "ON",
            "Dynamite",
            "Life Goes On",
            "Butter",
            "Yet To Come",
            "Run BTS",
            "For Youth"
        ]
    },

    "2023 — TAKE TWO": {
        "type": "Digital Single",
        "tracks": [
            "Take Two"
        ]
    },

    "2026 — ARIRANG": {
        "type": "Studio Album",
        "tracks": [
            "Body to Body",
            "Hooligan",
            "Aliens",
            "F YA",
            "Melted",
            "Normal",
            "Walking on the Moon",
            "The Beginning",
            "Please",
            "Into the Sun",
            "Swim",
            "Like Animals",
            "Forever",
            "No. 1"
        ]
    }
}


# ---------------------------------------------------------
# ALBUM SECTION
# ---------------------------------------------------------

st.header("💿 Albums & Major Releases")

st.write(
    "Explore BTS releases chronologically. Open an album to see its "
    "tracklist and find a listening link for each song."
)

for album_name, album_info in albums.items():

    with st.expander(
        f"💿 {album_name}  •  {album_info['type']}"
    ):

        for number, song in enumerate(
            album_info["tracks"],
            start=1
        ):
            show_song(song, number)

# ---------------------------------------------------------
# MAJOR DIGITAL / SPECIAL SONGS
# ---------------------------------------------------------

st.divider()

st.header("🎧 Important Standalone & Special Releases")

special_songs = [
    "Dynamite",
    "Butter",
    "Permission to Dance",
    "My Universe",
    "Take Two",
    "The Planet",
    "Come Back to Me",
    "Closer Than This",
]

for number, song in enumerate(special_songs, start=1):
    show_song(song, number)

# ---------------------------------------------------------
# JAPANESE RELEASES
# ---------------------------------------------------------

st.divider()

st.header("🇯🇵 Japanese Discography")

st.write(
    "BTS also released Japanese-language albums, singles and "
    "Japanese versions of several Korean songs."
)

japanese_releases = {
    "2014 — WAKE UP": [
        "Wake Up",
        "The Stars",
        "Danger",
        "Boy In Luv",
        "Just One Day",
        "I Like It Pt.2",
        "いいね! Pt.2",
        "Attack on Bangtan",
        "N.O",
        "Furioso",
        "2nd Grade",
        "Jump",
        "Like",
        "No More Dream",
        "進撃の防弾"
    ],

    "2016 — YOUTH": [
        "Introduction: Youth",
        "Run",
        "Fire",
        "Dope",
        "Good Day",
        "Save Me",
        "FIRE",
        "Wings",
        "For You",
        "I Need U",
        "Boy In Luv",
        "Danger",
        "Run Japanese Ver.",
        "I Need U Japanese Ver."
    ],

    "2018 — FACE YOURSELF": [
        "Intro: Ringwanderung",
        "Best of Me",
        "Blood Sweat & Tears",
        "DNA",
        "Not Today",
        "MIC Drop",
        "Don't Leave Me",
        "Go Go",
        "Crystal Snow"
    ],

    "2020 — MAP OF THE SOUL: 7 ~ THE JOURNEY ~": [
        "Intro: Calling",
        "Stay Gold",
        "Boy With Luv",
        "Make It Right",
        "Dionysus",
        "IDOL",
        "Airplane pt.2",
        "Fake Love",
        "Black Swan",
        "ON",
        "Lights",
        "Your Eyes Tell",
        "Outro: The Journey"
    ]
}

for release_name, tracks in japanese_releases.items():

    with st.expander(f"🇯🇵 {release_name}"):

        for number, song in enumerate(tracks, start=1):
            show_song(song, number)

# ---------------------------------------------------------
# SOLO MUSIC
# ---------------------------------------------------------

st.divider()

st.header("🌟 Member Solo Music")

st.write(
    "Explore the members' individual music alongside BTS's group discography."
)

solo_music = {

    "RM": [
        "Change",
        "mono.",
        "forever rain",
        "seoul",
        "moonchild",
        "Wild Flower",
        "Come back to me",
        "LOST!"
    ],

    "Jin": [
        "Super Tuna",
        "Yours",
        "The Astronaut",
        "I'll Be There",
        "Running Wild"
    ],

    "SUGA / Agust D": [
        "Agust D",
        "Give It to Me",
        "The Last",
        "Daechwita",
        "People",
        "People Pt.2",
        "Haegeum"
    ],

    "j-hope": [
        "Daydream",
        "Hope World",
        "Chicken Noodle Soup",
        "MORE",
        "Arson",
        "on the street"
    ],

    "Jimin": [
        "Promise",
        "Filter",
        "Lie",
        "Serendipity",
        "With You",
        "Like Crazy",
        "Who"
    ],

    "V": [
        "Scenery",
        "Winter Bear",
        "Sweet Night",
        "Christmas Tree",
        "Love Me Again",
        "Rainy Days",
        "Slow Dancing",
        "FRI(END)S"
    ],

    "Jungkook": [
        "Still With You",
        "My Time",
        "Stay Alive",
        "Seven",
        "3D",
        "Standing Next to You",
        "Yes or No",
        "Hate You",
        "Please Don't Change"
    ]
}

for member, songs in solo_music.items():

    with st.expander(f"💜 {member}"):

        for number, song in enumerate(songs, start=1):
            show_song(song, number)

# ---------------------------------------------------------
# OFFICIAL SOURCES
# ---------------------------------------------------------

st.divider()

st.header("🔗 Official Music Sources")

st.write(
    "For official music videos, releases and BTS content, use the "
    "official BIGHIT MUSIC and BTS channels."
)

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "💜 BIGHIT MUSIC Discography",
        "https://ibighit.com/en/bts/discography/",
        use_container_width=True
    )

with col2:
    st.link_button(
        "▶ BTS Official YouTube",
        "https://www.youtube.com/@BTS",
        use_container_width=True
    )

# ---------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "← Back to Home",
        use_container_width=True
    ):
        st.switch_page("pages/02_Home.py")

with col2:
    if st.button(
        "Next: Achievements →",
        use_container_width=True
    ):
        st.switch_page("pages/13_achievements.py")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.write("")

st.caption(
    "💜 BTS: The Journey • Seven members • Countless songs • One extraordinary journey"
)