# 熱処理硬度換算ツール

硬度スケール間での熱処理硬度の換算を行うためのツールです。ユーザーは硬度値を入力し、選択したスケールに基づいて換算結果を得ることができます。
Streamlitを使用して、簡単なインターフェースを作成しています。

## 特徴

- 硬度スケールの選択: HRC、HV、HBW、HSの中から選択可能
- 入力された硬度値に基づいて、選択されたスケールに換算

## 必要条件

以下のPythonパッケージが必要です。

- numpy
- pandas
- scipy
- streamlit

これらは、`requirements.txt`ファイルに記載されています。以下のコマンドでインストールできます。

```
pip install -r requirements.txt
```

## 使用方法

1. リポジトリをクローンします。

```
git clone https://github.com/yourusername/hardness_converter.git
cd hardness_converter
```

```

2. 必要なパッケージをインストールします。

```
pip install -r requirements.txt
```

3. アプリケーションを起動します。

```
streamlit run main.py
```

4. ブラウザで表示されたURLにアクセスし、硬度値を入力して換算を行います。


このツールを使用して、熱処理硬度の換算を簡単に行ってください！
