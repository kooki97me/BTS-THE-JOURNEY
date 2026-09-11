import streamlit as st

st.set_page_config(
    page_title="Unknown Stories | BTS: The Journey",
    page_icon="💜",
    layout="wide"
)

# =========================================================
# PURPLE THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, #7546A8 0%, transparent 35%),
        radial-gradient(circle at bottom right, #421D63 0%, transparent 40%),
        linear-gradient(135deg, #241039, #12071C, #08040D);
    color: white;
}

h1 {
    color: white !important;
    text-align: center !important;
    font-size: 50px !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: white !important;
}

p {
    color: #E9DCF5 !important;
    line-height: 1.75 !important;
}

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(220, 190, 255, 0.45);
    background: linear-gradient(135deg, #9559C7, #5E3287);
    color: white;
    font-size: 15px;
    font-weight: 700;
    padding: 11px 20px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #B47BE0, #7745A5);
    border-color: #E5D1FF;
    color: white;
}

.stLinkButton > a {
    border-radius: 12px !important;
    border: 1px solid rgba(220, 190, 255, 0.45) !important;
    background: linear-gradient(135deg, #74439D, #4C276C) !important;
    color: white !important;
    font-weight: 600 !important;
}

[data-testid="stExpander"] {
    background-color: rgba(65, 31, 92, 0.38);
    border: 1px solid rgba(210, 175, 245, 0.28);
    border-radius: 14px;
}

[data-testid="stInfo"] {
    background-color: rgba(82, 43, 112, 0.35) !important;
    border: 1px solid rgba(210, 180, 255, 0.25) !important;
}

[data-testid="stSuccess"] {
    background-color: rgba(67, 104, 82, 0.25) !important;
}

[data-testid="stWarning"] {
    background-color: rgba(110, 82, 38, 0.25) !important;
}

hr {
    border-color: rgba(220, 190, 255, 0.25) !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.title("🔮 UNKNOWN STORIES")

st.write(
    "Before the stadiums, world tours and millions of fans, "
    "BTS were seven young people sharing small spaces, practicing "
    "for hours, missing home and trying to make their dream come true."
)

st.write(
    "These are the little stories behind that journey — stories of "
    "friendship, sacrifice, arguments, laughter, kindness and the "
    "moments that slowly turned seven trainees into a family."
)

st.info(
    "💜 The stories on this page are based on BTS interviews, "
    "official BTS content, member recollections and documented "
    "accounts from people connected to their trainee years."
)

st.divider()


# =========================================================
# STORY 1 — J-HOPE ALMOST LEFT BTS
# =========================================================

st.header("💔 The Day BTS Almost Lost J-Hope")

with st.expander("🌧️ J-Hope decided to leave before debut"):

    st.subheader("One decision could have changed BTS forever.")

    st.write(
        "During BTS's trainee period, the pressure became extremely "
        "difficult for J-Hope. He had given up a lot of things he loved, "
        "including spending time with his family, going out and enjoying "
        "a normal young life."
    )

    st.write(
        "At one point, he decided that he wanted to leave the company. "
        "He even bought a one-way ticket to Gwangju."
    )

    st.write(
        "The news devastated Jungkook."
    )

    st.write(
        "Jungkook became emotional and cried while asking J-Hope not to "
        "leave. He desperately wanted his hyung to stay with them."
    )

    st.write(
        "RM also went directly to Big Hit and told the company that "
        "they needed Jung Hoseok. He believed BTS could not debut "
        "without J-Hope."
    )

    st.write(
        "Eventually, J-Hope changed his mind."
    )

    st.write(
        "He later explained that he returned because he trusted the "
        "other members. Their relationship and the bond they had built "
        "together gave him a reason to stay."
    )

    st.success(
        "Six members did not simply accept losing their seventh. "
        "They fought to keep him with them."
    )

    st.caption(
        "Source basis: BTS: Burn the Stage / You Quiz on the Block "
        "recollections and later interviews."
    )


# =========================================================
# STORY 2 — J-HOPE'S FIRST FAN LETTER
# =========================================================

st.header("💌 The Letters J-Hope Was Waiting For")

with st.expander("🥺 Jimin became the letter deliverer"):

    st.subheader("A small moment that meant much more than it looked.")

    st.write(
        "In BTS's early days, J-Hope sometimes received fewer fan "
        "messages than the other members."
    )

    st.write(
        "There is an early BANGTAN BOMB in which Jimin acts as the "
        "person delivering fan letters to the members."
    )

    st.write(
        "When the letters reach J-Hope, his reaction is especially "
        "touching. He looks genuinely surprised and happy to receive "
        "them."
    )

    st.write(
        "For someone who had spent years dreaming about standing on "
        "stage and hearing people cheer for him, a simple letter from "
        "one fan could mean an enormous amount."
    )

    st.write(
        "Years later, J-Hope also explained that messages from ARMY "
        "gave him strength and hope. He said that reading fan letters "
        "helped him understand what fans were thinking and feeling."
    )

    st.success(
        "For J-Hope, those letters were never 'just letters'. "
        "They were proof that someone was listening."
    )

    st.link_button(
        "Watch the official BANGTAN BOMB",
        "https://www.youtube.com/watch?v=CitzoKwUxNk"
    )


# =========================================================
# STORY 3 — JIMIN'S LETTER TO J-HOPE
# =========================================================

st.header("💜 The Old Letter Jimin Wrote to J-Hope")

with st.expander("✉️ A letter from the younger Jimin to his hyung"):

    st.subheader("J-Hope kept this memory for years.")

    st.write(
        "Years after receiving it, J-Hope shared an old handwritten "
        "birthday letter that Jimin had given him."
    )

    st.write(
        "Jimin explained that it was the first time he had written "
        "a letter to one of the members, which made him feel shy and "
        "embarrassed."
    )

    st.write(
        "But behind the playful beginning was a sincere message."
    )

    st.write(
        "Jimin thanked J-Hope for guiding the members, working hard "
        "without showing how difficult things could be, and taking "
        "care of the group."
    )

    st.write(
        "He also wished J-Hope good health and happiness."
    )

    st.success(
        "A small handwritten letter survived for years because the "
        "memory behind it mattered."
    )

    st.caption(
        "J-Hope shared the old letter publicly in 2022."
    )


# =========================================================
# STORY 4 — SUGA'S EXAM LUNCHBOX
# =========================================================

st.header("🍱 The Lunchbox BTS Made for SUGA")

with st.expander("🌙 They didn't have much — but they still tried"):

    st.subheader("The night before SUGA's important exam")

    st.write(
        "During their trainee years, SUGA was preparing for the "
        "university entrance exam."
    )

    st.write(
        "Former Big Hit trainee Jihoon recalled that RM decided to "
        "prepare a special lunch for SUGA."
    )

    st.write(
        "The trainees quietly prepared the food while Jungkook and V "
        "kept an eye on SUGA so he would not wake up."
    )

    st.write(
        "They also prepared letters for him."
    )

    st.write(
        "SUGA eventually woke up because of the noise, realized what "
        "they were doing and pretended to remain asleep."
    )

    st.write(
        "The lunchbox was simple — chicken breast, rice, Vienna "
        "sausages and rolled omelet."
    )

    st.write(
        "They were trainees with very little money. They simply used "
        "what they had."
    )

    st.success(
        "They couldn't give SUGA an expensive gift. "
        "So they made him something with their own hands."
    )


# =========================================================
# STORY 5 — SUGA HELPING JIHOON
# =========================================================

st.header("🏥 When SUGA Stayed Beside Someone Who Needed Help")

with st.expander("🌙 SUGA's kindness during the trainee years"):

    st.subheader("He didn't have much money himself.")

    st.write(
        "Former Big Hit trainee Jihoon also recalled becoming seriously "
        "unwell during the trainee period."
    )

    st.write(
        "SUGA noticed that Jihoon was sick and went with him to the "
        "hospital during the night."
    )

    st.write(
        "According to Jihoon's recollection, SUGA stayed with him and "
        "helped with the hospital expenses even though SUGA himself "
        "was struggling financially at the time."
    )

    st.success(
        "Sometimes the people who understand your difficult days best "
        "are the ones who are struggling too."
    )


# =========================================================
# STORY 6 — JUNGKOOK'S HOMESICKNESS
# =========================================================

st.header("🏠 The Youngest Member Who Missed Home")

with st.expander("🥺 Jungkook's early days in Seoul"):

    st.subheader("He was only a very young trainee.")

    st.write(
        "Jungkook left Busan while he was still very young to pursue "
        "his dream of becoming a singer."
    )

    st.write(
        "Moving to Seoul meant being away from his parents and "
        "everything familiar."
    )

    st.write(
        "Jungkook later talked about how scared he was when he first "
        "came to Seoul. He missed his parents and cried."
    )

    st.write(
        "His early trainee life was also very different from the "
        "comfortable life people associate with BTS today."
    )

    st.write(
        "He was the youngest in the dorm and often waited for the "
        "older members to fall asleep before showering because he was "
        "too shy to disturb them."
    )

    st.success(
        "Before Jungkook became BTS's confident maknae, "
        "he was a shy teenager trying to find his place."
    )


# =========================================================
# STORY 7 — V WAITED FOR JUNGKOOK
# =========================================================

st.header("🐻 The Quiet Beginning of V and Jungkook")

with st.expander("🌙 V waited for the shy new trainee"):

    st.subheader("Their friendship started very quietly.")

    st.write(
        "V recalled meeting Jungkook when Jungkook was taking vocal "
        "lessons."
    )

    st.write(
        "Later that day, V waited for Jungkook at the dorm."
    )

    st.write(
        "But Jungkook was extremely shy around people at that time."
    )

    st.write(
        "V eventually fell asleep while waiting, and Jungkook arrived "
        "around the same time."
    )

    st.write(
        "The quiet, shy Jungkook V first met eventually became the "
        "playful youngest member everyone knows."
    )

    st.info(
        "Sometimes the beginning of a friendship is not dramatic. "
        "Sometimes it is simply waiting for someone to come home."
    )


# =========================================================
# STORY 8 — J-HOPE AND SUGA
# =========================================================

st.header("🍗 When SUGA Became J-Hope's First Friend")

with st.expander("🌙 J-Hope was alone in the dorm"):

    st.subheader("SUGA didn't leave him alone.")

    st.write(
        "J-Hope once recalled how unfamiliar and lonely dorm life felt "
        "when he first became a trainee."
    )

    st.write(
        "SUGA was one of the first members to make him feel comfortable."
    )

    st.write(
        "When J-Hope had to stay alone in the dorm while the other "
        "members went home for a holiday, SUGA called him."
    )

    st.write(
        "Instead of simply talking on the phone, SUGA came back to the "
        "dorm and brought fried chicken."
    )

    st.success(
        "J-Hope was alone. SUGA could have stayed home. "
        "Instead, he came back with chicken."
    )


# =========================================================
# STORY 9 — J-HOPE AND SUGA FIRST MEETING
# =========================================================

st.header("😂 J-Hope's First Impression of SUGA")

with st.expander("🚿 His trainee fantasy disappeared immediately"):

    st.write(
        "When J-Hope first arrived at the dorm, he saw SUGA coming "
        "out of the shower wearing only his underwear."
    )

    st.write(
        "J-Hope later joked that his fantasy of what trainee life "
        "would look like was completely destroyed."
    )

    st.write(
        "Ironically, J-Hope later had a similarly embarrassing "
        "first encounter with Jin."
    )

    st.info(
        "BTS's trainee life was apparently much less glamorous "
        "than J-Hope had imagined. 😂"
    )


# =========================================================
# STORY 10 — JIMIN AND JIN
# =========================================================

st.header("🎤 Jimin's First Meeting With Jin")

with st.expander("😳 Jin immediately asked the new trainee to sing"):

    st.subheader("Jimin thought Jin was scary.")

    st.write(
        "When Jimin first arrived as a trainee, Jin asked him to sing."
    )

    st.write(
        "Jimin initially interpreted Jin's serious attitude as "
        "something intimidating."
    )

    st.write(
        "Later, Jimin understood that Jin was simply being cautious "
        "with a new trainee because many trainees had come and gone "
        "before."
    )

    st.write(
        "That serious first impression eventually became a very "
        "different relationship between the two."
    )


# =========================================================
# STORY 11 — RM AND V FIRST MEETING
# =========================================================

st.header("🐨 The First Time RM Met V")

with st.expander("2011 — seven people had not yet become BTS"):

    st.subheader("There were many trainees before the seven.")

    st.write(
        "RM recalled meeting V in September 2011 when they were living "
        "in a small two-room apartment in Nonhyeon-dong."
    )

    st.write(
        "At that time, there were many trainees coming through the dorm."
    )

    st.write(
        "RM remembered that around thirty trainees passed through that "
        "dorm at different points."
    )

    st.write(
        "Only seven of those trainees eventually became BTS."
    )

    st.info(
        "The seven we know today were not an obvious certainty at the time."
    )


# =========================================================
# STORY 12 — JUNGKOOK'S MELTED CHEESE
# =========================================================

st.header("🧀 Jungkook and the Melted Cheese")

with st.expander("😂 A tiny convenience-store disaster"):

    st.write(
        "Former Big Hit trainee Jihoon recalled that the trainees often "
        "went to convenience stores because they did not have much money."
    )

    st.write(
        "One day Jungkook bought string cheese."
    )

    st.write(
        "The cashier suggested microwaving it for around ten seconds."
    )

    st.write(
        "Jungkook wondered whether he could heat it for longer."
    )

    st.write(
        "Jihoon warned him not to."
    )

    st.write(
        "Jungkook apparently ignored the warning."
    )

    st.write(
        "The cheese melted completely, leaving Jungkook panicking over "
        "his ruined snack."
    )

    st.info(
        "According to Jihoon's story, Jungkook never microwaved "
        "his string cheese for that long again."
    )


# =========================================================
# STORY 13 — JUNGKOOK AND J-HOPE BANANA FIGHT
# =========================================================

st.header("🍌 The Banana Fight")

with st.expander("😂 One fruit basket caused an actual argument"):

    st.subheader("The gift was precious because gifts were rare.")

    st.write(
        "During BTS's early debut period, Jungkook received a fruit "
        "basket from a fan."
    )

    st.write(
        "At that time, fan gifts were still rare and extremely precious "
        "to the members."
    )

    st.write(
        "But the fruit disappeared very quickly because the other "
        "members were eating it."
    )

    st.write(
        "Jungkook eventually told everyone to stop because the fruit "
        "had been given to him."
    )

    st.write(
        "J-Hope was eating a banana when the argument happened."
    )

    st.write(
        "J-Hope later admitted that he threw the banana toward Jungkook."
    )

    st.write(
        "Years later, the two could laugh about the incident."
    )

    st.success(
        "They were fighting over a banana — but the reason it mattered "
        "was because a fan's gift meant so much to them at the time."
    )


# =========================================================
# STORY 14 — JIMIN AND V BUNK BED
# =========================================================

st.header("🛏️ Jimin and V's Bunk-Bed Fight")

with st.expander("😂 Six months of being nice... then the fight"):

    st.subheader("A tiny dorm problem became a huge argument.")

    st.write(
        "Jimin, V and J-Hope once shared a room."
    )

    st.write(
        "J-Hope was older, so he used the regular bed while Jimin and "
        "V shared a bunk bed."
    )

    st.write(
        "Jimin initially let V take the bottom bunk because he thought "
        "it was better."
    )

    st.write(
        "After about six months, Jimin asked V if they could switch."
    )

    st.write(
        "V's response was essentially that Jimin had chosen the top "
        "bunk himself."
    )

    st.write(
        "The two ended up having a surprisingly serious argument "
        "over the bunk bed."
    )

    st.info(
        "Even the strongest friendships have arguments over completely "
        "ridiculous things. 😂"
    )


# =========================================================
# STORY 15 — RM AND HOPE
# =========================================================

st.header("🌌 RM and J-Hope Looking at the Sky")

with st.expander("☁️ 'The sky is murky, just like our future'"):

    st.subheader("Before the world knew BTS.")

    st.write(
        "RM once recalled sitting outside a convenience store with "
        "J-Hope during their trainee years."
    )

    st.write(
        "They looked up at the sky and talked about their uncertain future."
    )

    st.write(
        "At that time, nothing was guaranteed."
    )

    st.write(
        "They were trainees from a small company, working hard without "
        "knowing whether they would actually debut."
    )

    st.write(
        "Years later, that uncertain sky became the beginning of one "
        "of the biggest journeys in music."
    )

    st.success(
        "They once looked at the sky wondering about their future. "
        "Today, that future is the story of BTS."
    )


# =========================================================
# STORY 16 — TRAINEE CHRISTMAS
# =========================================================

st.header("🎄 Their First Christmases Were Very Different")

with st.expander("🍗 Christmas with chicken breast"):

    st.write(
        "SUGA once recalled that during their trainee days, the members "
        "spent Christmas Eve eating chicken breast."
    )

    st.write(
        "There was no huge celebration or expensive meal."
    )

    st.write(
        "After BTS debuted and won their first rookie award in 2013, "
        "their company treated them to meat."
    )

    st.write(
        "The difference between those two Christmas memories shows "
        "just how dramatically their circumstances changed."
    )

    st.success(
        "From chicken breast on Christmas Eve to celebrating their "
        "first major award together — the journey really changed."
    )


# =========================================================
# STORY 17 — YOOGEONGSIKDANG
# =========================================================

st.header("🍚 The Restaurant That Knew BTS Before Fame")

with st.expander("🏠 Yoojung Sikdang and the seven trainees"):

    st.subheader("They were regular customers before anyone knew their name.")

    st.write(
        "Yoojung Sikdang, a restaurant near BTS's old practice area, "
        "became part of their trainee memories."
    )

    st.write(
        "The restaurant owner remembered the members from before they "
        "became famous."
    )

    st.write(
        "The members reportedly ate there very regularly during their "
        "trainee period."
    )

    st.write(
        "The owner remembered them as polite, bright and friendly "
        "young men."
    )

    st.write(
        "Today the restaurant is remembered by ARMY as one of the "
        "places connected to BTS's difficult early years."
    )

    st.info(
        "A place that knew BTS before the world knew their name."
    )


# =========================================================
# STORY 18 — SHARED DORM
# =========================================================

st.header("🛏️ Seven People, One Small Dorm")

with st.expander("🌙 Their trainee life was far from glamorous"):

    st.write(
        "The members have talked openly about living together in a "
        "small dorm during their trainee period."
    )

    st.write(
        "There were so many trainees at one point that shoes could be "
        "seen all the way into the kitchen."
    )

    st.write(
        "J-Hope remembered how difficult it was for all of them to "
        "share a single room."
    )

    st.write(
        "Jungkook, being the youngest, waited until the others were "
        "asleep before showering so that he would not disturb them."
    )

    st.write(
        "They were balancing school, training, very little sleep and "
        "the uncertainty of whether they would actually debut."
    )

    st.success(
        "The BTS dorm was small. Their dream was not."
    )


# =========================================================
# STORY 19 — JIMIN'S TRAINEE STRUGGLE
# =========================================================

st.header("🥺 Jimin Thought About Giving Up Too")

with st.expander("⏰ Two hours of sleep"):

    st.subheader("The pressure of being the last trainee to join")

    st.write(
        "Jimin was the last of the seven members to join as a trainee."
    )

    st.write(
        "He felt that he had to catch up with the others."
    )

    st.write(
        "He described sleeping around 4 a.m. and waking at 6 a.m. "
        "during one period of intense training."
    )

    st.write(
        "He practiced constantly because he was afraid of falling behind."
    )

    st.write(
        "Jimin also said that the other members helped fill the areas "
        "where he felt he was lacking."
    )

    st.success(
        "He wasn't trying to become perfect alone. "
        "The members helped him become better."
    )


# =========================================================
# STORY 20 — V AND HIS FATHER
# =========================================================

st.header("🐻 When V Called His Father Crying")

with st.expander("📞 'If it's too hard, you can quit'"):

    st.subheader("The answer that made V rethink everything")

    st.write(
        "V once recalled how overwhelming trainee life became."
    )

    st.write(
        "At one point, he called his father while crying and said "
        "that he wanted to give up."
    )

    st.write(
        "Instead of forcing him to continue, his father told him that "
        "if it was truly too hard, he could quit and they would find "
        "another path."
    )

    st.write(
        "V said that hearing those words made him feel embarrassed "
        "about wanting to give up."
    )

    st.write(
        "His father's response helped him understand that his family "
        "would support him whether he became a singer or chose another "
        "path."
    )

    st.success(
        "Sometimes knowing that you are allowed to leave is what gives "
        "you the strength to stay."
    )


# =========================================================
# FINAL MESSAGE
# =========================================================

st.divider()

st.header("💜 Before BTS Became BTS")

st.write(
    "There were no stadiums yet."
)

st.write(
    "There were no world tours, millions of fans or countless awards."
)

st.write(
    "There were small dorm rooms."
)

st.write(
    "There were cheap meals, practice rooms, homesickness, arguments, "
    "letters, laughter and nights when the future looked uncertain."
)

st.write(
    "There was a young Jungkook who missed home."
)

st.write(
    "There was a Jimin who worked until he barely slept."
)

st.write(
    "There was a V who once called his father crying."
)

st.write(
    "There was a SUGA who helped someone even when he had little himself."
)

st.write(
    "There was a J-Hope who almost left — and six members who refused "
    "to imagine BTS without him."
)

st.write(
    "And there was RM, who believed they needed all seven."
)

st.write(
    "Maybe that is what makes their story so special."
)

st.write(
    "They didn't start with everything."
)

st.write(
    "They started with each other."
)

st.info(
    "💜 Seven members. Small beginnings. Countless memories. "
    "One extraordinary journey."
)


# =========================================================
# NAVIGATION
# =========================================================

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "← Back to Timeline",
        key="timeline_button",
        use_container_width=True
    ):
        st.switch_page("pages/14_timeline.py")

with col2:
    if st.button(
        "Go to ARMY Space →",
        key="army_button",
        use_container_width=True
    ):
        st.switch_page("pages/16_army_space.py")