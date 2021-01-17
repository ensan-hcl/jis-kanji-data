# このデータについて

[独立行政法人情報処理推進機構(IPA)](http://www.ipa.go.jp/)が[MJ文字情報一覧表 | 文字情報基盤整備事業](https://moji.or.jp/mojikiban/mjlist/)で提供する文字情報基盤 文字情報一覧表（MJ文字情報一覧表）を利用し、JIS第1、第2、第3、第4水準までの漢字の基本的な情報を抜き出したものです。

## データの構造

resource/kanji.txtは提供されている一覧表データをtxtファイルに書き出したものであり、resource/spliter.pyがここからデータを抽出します。

result/kanji_jis1~4.txtが抽出されたデータであり、漢字、unicodeポイント、画数、読み、の4つの情報をタブ区切りでまとめたものです。

## ライセンス

このデータは[クリエイティブ・コモンズ 表示 – 継承 2.1 日本 ライセンス](http://creativecommons.org/licenses/by-sa/2.1/jp/)を継承しています。MJ文字情報一覧表及びその派生物であるresource/kanji.txt、result/kanji_jis1~4.txtの著作権はIPAに帰属します。

