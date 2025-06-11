import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFC0CB;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("プロフィール帳")
st.caption("フォームで情報を入力し、プロフィール帳を完成させよう！")


with st.form("基本情報"):
    st.write("★★**基本情報**★★")
    name = st.text_input("お名前")
    st.caption("名前を入力してね。")
    birthday = st.text_input("誕生日:何月", placeholder="例: 1")
    birthday2 = st.text_input("誕生日:何日", placeholder="例: 20")
    st.caption("誕生日を入力してね。")
    blood_type = st.selectbox("血液型", ["A型", "B型", "O型", "AB型", "不明"])
    zodiac_sign = st.selectbox("星座", [
        "牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", 
        "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"
    ])
    year = st.selectbox("学年", ["1年", "2年", "3年", "4年"])
    club = st.text_input("所属している部活・サークル")
    st.caption("所属している部活・サークルを入力してね。所属していなければ「なし」で大丈夫だよ。")
    hobbies = st.text_input("趣味")
    st.caption("趣味を一つ入力してね。")
    skill = st.text_input("特技")
    st.caption("特技を一つ入力してね。")
    favorite0 = st.text_input("今一番はまっているもの")
    favorite0_5 = st.file_uploader("今一番はまっているものの画像", type=["jpg", "jpeg", "png"])
    st.caption("現在はまっているものを入力して、画像を挿入してね。")

    st.markdown("---")

    st.write("★★**好きなもの**★★")
    st.caption("それぞれの項目の好きな度合いと、特に好きなものを教えてね！")
    favorite1 = st.slider("音楽", 1, 10, 5)
    favorite1_5 = st.multiselect("特に好きな音楽", ["J-POP", "K-POP", "洋楽", "クラシック", "アニメソング"])
    favorite2 = st.slider("映画", 1, 10, 5)
    favorite2_5 = st.multiselect("特に好きな映画", ["アクション", "コメディ", "ドラマ", "ホラー", "アニメ"])
    favorite3 = st.slider("スポーツ", 1, 10, 5)
    favorite3_5 = st.multiselect("特に好きなスポーツ", ["サッカー", "野球", "バスケットボール", "テニス", "水泳"])
    favorite4 = st.slider("読書", 1, 10, 5)
    favorite4_5 = st.multiselect("特に好きな本のジャンル", ["小説", "漫画", "ビジネス書", "自己啓発書", "歴史書"])

    st.markdown("---")
    st.write("入力が完了したら、下のボタンを押して情報を送信しよう！")
    submit_button = st.form_submit_button("★★ 送信 ★★")
if submit_button:
    st.success("情報が送信されました！")
    st.markdown("")
    st.markdown("")
    st.markdown(
        f"""
        <div style="background-color: #ADD8E6; padding: 15px; border-radius: 10px;">
            <h3>プロフィール</h3>
            <hr>
            <p>私の名前は <b>{name}</b> だよ！</p>
            <p>誕生日は <b>{birthday}月{birthday2}日</b> で、</p>
            <p>血液型は <b>{blood_type}</b>、星座は <b>{zodiac_sign}</b> だよ★</p>
            <p>学年は <b>{year}</b> で、所属している部活・サークルは <b>{club}</b> なんだ！</p>
            <p>趣味は <b>{hobbies}</b> で、 <b>{skill}</b> が得意！</p>
            <p>今一番はまっているものは <b>{favorite0}</b> なんだ！おすすめだよ～！</p>
            <p>音楽を好きな度合いは <b>{favorite1}</b> くらいかな。特に好きな音楽は <b>{', '.join(favorite1_5)}</b> だよ。</p>
            <p>映画を好きな度合いは <b>{favorite2}</b> くらいだと思う。特に好きな映画は <b>{', '.join(favorite2_5)}</b> かな。</p>
            <p>スポーツを好きな度合いは <b>{favorite3}</b> 。特に好きなスポーツは <b>{', '.join(favorite3_5)}</b> だよ。</p>
            <p>読書を好きな度合いは <b>{favorite4}</b> くらい！特に好きな本のジャンルは <b>{', '.join(favorite4_5)}</b> なんだ～！</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if favorite0_5:
        st.image(favorite0_5, caption=f"{favorite0}の画像", use_column_width=True)
    else:
        st.write("画像はありません。")
    st.balloons()
