import numpy as np
import streamlit as st

import converter
import ui_logging
from updater import update_hardness_value, update_source_index

def main():
    scale_list = ["HRC","HV","HBW","HS"]
    ui_logging.log_info("launching application")
    st.set_page_config(
        page_title="Hardness Converter",
        page_icon=":material/calculate:",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None,
    )
    
    st.title("熱処理硬度 換算",anchor=False,)
    hardness_input = st.text_input("硬度を入力してください")
    ui_logging.log_info("hardness input field created")
    source_scale = st.selectbox("硬度の種類を選択してください",options=scale_list, index=0)
    ui_logging.log_info("source index field created")
    
    def calculate(hardness_input, source_scale):
        ui_logging.log_info("calculate button clicked" )
        result_container.empty()
        try:
            hardness_input = int(hardness_input)
            source_index = scale_list.index(source_scale)
            converted_values = converter.convert_hardness_scale(hardness_input, source_index)
            with result_container:
                if converted_values:
                    st.dataframe(converted_values)
                else:
                    st.write("No data to display")
        except Exception as e:
            ui_logging.log_exception(e)
            st.write("An error occurred while calculating. Please try again.")
    
    col1, col2, _, _, _ = st.columns(5, gap='small')
    with col1:
        st.button("Calculate", on_click=lambda: calculate(hardness_input, source_scale))
    with col2:
        st.button("Clear", on_click=lambda: st.rerun())
    result_container = st.container()
    
    ui_logging.log_info("calculate button created")
    ui_logging.log_info("result container created")
    ui_logging.log_info("application launched")
if __name__ == "__main__":
    main()