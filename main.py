import numpy as np
import streamlit as st

import converter

def main():
    scale_list = ["HRC","HV","HBW","HS"]
    st.set_page_config(
        page_title="Hardness Converter",
        page_icon=":material/calculate:",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None,
    )
    
    st.title("熱処理硬度 換算",anchor=False,)
    hardness_input = st.text_input("硬度を入力してください")
    source_scale = st.selectbox("硬度の種類を選択してください",options=scale_list, index=None)   
    
    col1, col2, _, _, _, _ = st.columns(6, gap='small')
    with col1:
        st.button("換算する", on_click=lambda: calculate(hardness_input, source_scale))
    with col2:
        st.button("クリア", on_click=lambda: result_container.empty())

    result_container = st.container()
    with result_container:
        HRC, HV, HBW, HS = st.columns(4, gap="medium")
        
    def calculate(hardness_input, source_scale):
        result_container.empty()
        try:
            hardness_input = float(hardness_input)
            source_index = scale_list.index(source_scale)
            converted_values = converter.convert_hardness_scale(hardness_input, source_index)
            with result_container:
                if converted_values:
                    HRC.metric(label="HRC", value= converted_values["HRC"] if converted_values["HRC"] is not np.nan else "❌", delta_color="normal",border=True)
                    HV.metric(label="HV", value=converted_values["HV"] if converted_values["HV"] is not np.nan else "❌", delta_color="normal",border=True)
                    HBW.metric(label="HBW", value=converted_values["HBW"] if converted_values["HBW"] is not np.nan else "❌", delta_color="normal",border=True)
                    HS.metric(label="HS", value=converted_values["HS"] if converted_values["HS"] is not np.nan else "❌", delta_color="normal",border=True)
                else:
                    st.write("データがありません")
        except Exception as e:
            st.write("換算に失敗しました。もう一度お試しください。")
        
if __name__ == "__main__":
    main()