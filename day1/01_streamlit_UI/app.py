import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
st.set_page_config(
    page_title="Streamlit デモ",
    layout="wide",
    initial_sidebar_state="expanded"
)
i = 0
# ============================================
# タイトルと説明
# ============================================
# st.title("Streamlit 初心者向けデモ")
# st.markdown("### コメントを解除しながらStreamlitの機能を学びましょう")
# st.markdown("このデモコードでは、コメントアウトされた部分を順番に解除しながらUIの変化を確認できます。")

# ============================================
# サイドバー 
# ============================================
st.sidebar.header("デモのガイド")
st.sidebar.info("コードのコメントを解除して、Streamlitのさまざまな機能を確認しましょう。")



# エクスパンダー
with st.expander("入力"):
    tab1, tab2, tab3, tab4 = st.tabs(["名前", "年齢","性別","progress"])
    with tab1:
        st.subheader("テキスト入力")
        name = st.text_input("あなたの名前", "ゲスト")
    with tab2:
        age = st.slider("年齢", 0, 100, 25)
    with tab3:
        sex= st.selectbox(
    "性別",
    ["男", "女", "その他"]
)
    with tab4:
        if st.checkbox("progress"):
            st.info("これは隠れたコンテンツです！")
            i += 50
# ============================================
# 基本的なUI要素
# ============================================
st.header("your data")

# テキスト入力
st.write(f"こんにちは、{name}さん！")
st.write(f"あなたの年齢: {age}")
st.write(f"あなたの性別: {sex}")

# ボタン
# st.subheader("ボタン")
# if st.button("クリックしてください"):
#     st.success("ボタンがクリックされました！")



# チェックボックス
st.subheader("確認")
if st.checkbox("私はロボットではありません"):
    i += 50

# スライダー
# st.subheader("スライダー")
# age = st.slider("年齢", 0, 100, 25)
# st.write(f"あなたの年齢: {age}")

# セレクトボックス
# st.subheader("セレクトボックス")
# option = st.selectbox(
#     "好きなプログラミング言語は?",
#     ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
# )
# st.write(f"あなたは{option}を選びました")

# ============================================
# レイアウト
# ============================================
# st.header("レイアウト")

# カラム
# st.subheader("カラムレイアウト")
# col1, col2 = st.columns(2)
# with col1:
#     st.write("これは左カラムです")
#     st.number_input("数値を入力", value=10)
# with col2:
#     st.write("これは右カラムです")
#     st.metric("メトリクス", "42", "2%")

# タブ
# st.subheader("タブ")
# tab1, tab2 = st.tabs(["第1タブ", "第2タブ"])
# with tab1:
#     st.write("これは第1タブの内容です")
# with tab2:
#     st.write("これは第2タブの内容です")

# エクスパンダー
# st.subheader("エクスパンダー")
# with st.expander("詳細を表示"):
#     st.write("これはエクスパンダー内の隠れたコンテンツです")
#     st.code("print('Hello, Streamlit！')")

# ============================================
# データ表示
# ============================================
st.header("データの表示")

# サンプルデータフレームを作成
df = pd.DataFrame({
    '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤',name],
    '年齢': [25, 30, 22, 28, 33,age],
    '性別': ['男', '女', '男', '男', '女', sex]
})

# データフレーム表示
# st.subheader("データフレーム")
# st.dataframe(df, use_container_width=True)

# テーブル表示
st.subheader("テーブル")
st.table(df)

# メトリクス表示
st.subheader("メトリクス")
col1, col2, col3 = st.columns(3)
col1.metric("温度", "23°C", "1.5°C")
col2.metric("湿度", "45%", "-5%")
col3.metric("気圧", "1013hPa", "0.1hPa")

# ============================================
# グラフ表示
# ============================================
# st.header("グラフの表示")

# # ラインチャート
st.subheader("ラインチャート")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C'])
st.line_chart(chart_data)

# バーチャート
st.subheader("バーチャート")
chart_data = pd.DataFrame({
    'カテゴリ': ['A', 'B', 'C', 'D'],
    '値': [10, 25, 15, 30]
}).set_index('カテゴリ')
st.bar_chart(chart_data)

# ============================================
# インタラクティブ機能
# ============================================
st.header("インタラクティブ機能")

# プログレスバー
st.write("progress : " + str(i) + " / 100")
st.subheader("プログレスバー")
progress = st.progress(0)
if st.button("進捗をシミュレート"):
    # for i in range(101):
    #     time.sleep(0.01)
    progress.progress(i / 100)
    if i >= 100:
        st.balloons()

# ファイルアップロード
# st.subheader("ファイルアップロード")
# uploaded_file = st.file_uploader("ファイルをアップロード", type=["csv", "txt"])
# if uploaded_file is not None:
#     # ファイルのデータを表示
#     bytes_data = uploaded_file.getvalue()
#     st.write(f"ファイルサイズ: {len(bytes_data)} bytes")
    
#     # CSVの場合はデータフレームとして読み込む
#     if uploaded_file.name.endswith('.csv'):
#         df = pd.read_csv(uploaded_file)
#         st.write("CSVデータのプレビュー:")
#         st.dataframe(df.head())

# ============================================
# カスタマイズ
# ============================================
st.header("スタイルのカスタマイズ")

# カスタムCSS
st.markdown("""
<style>
.big-font {
    font-size:20px ！important;
    font-weight: bold;
    color: #0066cc;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">これはカスタムCSSでスタイリングされたテキストです！</p>', unsafe_allow_html=True)

# ============================================
# デモの使用方法
# ============================================
# st.divider()
# st.subheader("このデモの使い方")
# st.markdown("""
# 1. コードエディタでコメントアウトされた部分を見つけます（#で始まる行）
# 2. 確認したい機能のコメントを解除します（先頭の#を削除）
# 3. 変更を保存して、ブラウザで結果を確認します
# 4. 様々な組み合わせを試して、UIがどのように変化するか確認しましょう
# """)

# st.code("""
# # コメントアウトされた例:
# # if st.button("クリックしてください"):
# #     st.success("ボタンがクリックされました！")

# # コメントを解除した例:
# if st.button("クリックしてください"):
#     st.success("ボタンがクリックされました！")
# """)