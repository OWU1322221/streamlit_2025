import streamlit as st

st.title("第7回 Streamlit フォーム演習 - テンプレート")
st.caption("st.form を使ってサークル入会申し込みフォームを作成しましょう。")

st.markdown("---")
st.subheader("演習: サークル入会申し込みフォーム")
st.write("**課題**: フォームを使って、サークル入会の申し込み情報をまとめて処理するアプリを作成する。")

# ここに演習のコードを記述してください
# ヒント: with st.form("フォーム名"): でフォームを作成し、st.form_submit_button() で送信ボタンを設置
with st.form("circle_form"):
    st.write("サークル入会申し込みフォーム")
    
    name = st.text_input("名前：")
    grade = st.selectbox("学年：",["1年", "2年", "3年", "4年"])
    email = st.text_input("メールアドレス：")
    phone = st.text_input("電話番号：")
    reason = st.text_area("入会理由：")
    
    # 送信ボタン
    submit_button = st.form_submit_button("申し込む")
    
    if submit_button:
        if name and email and phone and reason:
            st.success(f"{name}さんの申し込みを受け付けました！")
            st.write(f"学年: {grade}")
            st.write(f"メール: {email}")
            st.write(f"電話: {phone}")
            st.write(f"理由: {reason}")
        else:
            st.error("全ての項目を入力してください。")

st.markdown("---")
st.info("💡 全ての項目を入力してから「申し込む」ボタンを押すと、まとめて処理されることを確認してください。") 
