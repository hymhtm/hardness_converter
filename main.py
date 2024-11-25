import flet as ft
import numpy as np
from updater import update_hardness_value, update_source_index
import converter
import ui_logging

def main(page: ft.Page):
    ui_logging.log_info("アプリケーションが起動しました")
    page.title = "Hardness Converter"
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.CALCULATE),
        title=ft.Text("熱処理硬度 換算",size=20, weight="bold"),
        bgcolor=ft.colors.BLUE_GREY_50,
        actions=[
            ft.IconButton(ft.icons.TABLE_CHART, on_click=lambda e: page.launch_url("https://www.iwata-fa.jp/html/technicaldata/tec_other_19.pdf"))
        ]
    )
    ui_logging.log_info("アプリケーションのバーが設定されました")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.border = True
    page.window.width = 500
    page.window.height = 700
    ui_logging.log_info("アプリケーションのウィンドウが設定されました")
    # ミュータブルな変数をリストで定義
    hardness_value = [0.0]
    source_index = [0]
    ui_logging.log_info("ミュータブルな変数が設定されました")
    # 硬度値入力フィールド
    page.add(ft.Text("硬度を入力してください"))
    hardness_input = ft.TextField(
        label="硬度",
        width=150,
        on_change=lambda e: update_hardness_value(e, hardness_value)
    )
    page.add(hardness_input)
    ui_logging.log_info("硬度値入力フィールドが設定されました")
    # スケール選択ボタン
    slidebutton = ft.CupertinoSlidingSegmentedButton(
        selected_index=0, 
        on_change=lambda e: update_source_index(e, source_index),
        padding=ft.Padding(left=10, top=10, right=10, bottom=10), 
        controls=[
            ft.Text("HRC"), 
            ft.Text("HV"), 
            ft.Text("HBW"), 
            ft.Text("HS")
        ]
    )
    page.add(slidebutton)
    ui_logging.log_info("スケール選択ボタンが設定されました")
    # 換算ボタン
    button = ft.FilledButton(
        text="換算", 
        on_click=lambda e: update_converted_values()
    )
    page.add(button)
    ui_logging.log_info("換算ボタンが設定されました")
    # 結果表示用コンテナ
    result_container = ft.Container(width=400, height=200)
    page.add(result_container)
    ui_logging.log_info("結果表示用コンテナが設定されました")
    def update_converted_values():
        ui_logging.log_info("換算ボタンがクリックされました")
        try:
            # 現在の硬度値とスケールインデックスを取得
            value = hardness_value[0]
            index = source_index[0]
            
            # 換算を実行
            converted = converter.convert_hardness_scale(value, index)
            
            # 結果を表示
            display_results(converted, result_container)
        except Exception as ex:
            # エラーが発生した場合、コンソールに表示
            print(f"エラー: {ex}")
            # UI上にエラーメッセージを表示
            result_container.content = ft.Text(f"エラー: {str(ex)}", color="red")
            page.update()

    def display_results(converted, container):
        ui_logging.log_info("換算結果を表示します")
        # DataRow のリストを作成
        data_rows = []
        for unit, value in converted.items():
            if isinstance(value, float) and np.isnan(value):
                # 範囲外の場合はエラーアイコンを表示
                data_rows.append(
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text(unit)),
                        ft.DataCell(ft.Icon(ft.icons.ERROR, color="red"))
                    ])
                )
            else:
                # 有効な換算値を表示
                data_rows.append(
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text(unit)),
                        ft.DataCell(ft.Text(f"{value:.2f}"))
                    ])
                )
        
        # DataTable を作成
        data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("硬度")), 
                ft.DataColumn(ft.Text("換算値"))
            ],
            rows=data_rows
        )
        
        # コンテナに DataTable を設定
        container.content = data_table
        page.update()
        ui_logging.log_info("換算結果が表示されました")
    # ページを更新
    page.update()

# Fletアプリケーションのエントリーポイント
if __name__ == "__main__":
    ui_logging.log_info("アプリケーションのエントリーポイントが実行されました")
    ft.app(target=main)