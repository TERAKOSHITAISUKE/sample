import streamlit as st

def convert_space_to_newline(input_text):
    return input_text.replace(' ', '\n')

def main():
    st.title("半角スペースを改行に変換するアプリ")

    # テキスト入力を取得
    input_text = st.text_area("テキストを入力してください", height=200)

    if st.button("変換"):
        # 入力されたテキストを変換
        converted_text = convert_space_to_newline(input_text)

        # 変換結果を表示
        st.write("変換結果:")
        st.text_area("", value=converted_text, height=200)

if __name__ == "__main__":
    main()
