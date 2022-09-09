import streamlit as st
import makelist_app, trans_anker_app, trans_pc_app, opt_table_app


PAGES = {
    "リスト作成アプリ": makelist_app,
    "アンカー・英語翻訳アプリ": trans_anker_app,
    '画像・英語翻訳アプリ': trans_pc_app,
    '表最適化アプリ':opt_table_app
}
st.sidebar.title('アプリケーションの選択！')
selection = st.sidebar.radio("使いたいアプリを選択してね！", list(PAGES.keys()))
page = PAGES[selection]
page.app()
