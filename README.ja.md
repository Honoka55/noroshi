# Noroshi

Noroshi（ノロシ）は、[IBM Plexタイプフェイス](https://github.com/IBM/plex)から派生したCJK文字に対応した等幅フォントです。

## 特徴

Noroshiは、Noroshi Code（ノロシコード）とNoroshi Mono（ノロシモノ）の2つのフォントファミリーを含んでいます。どちらも西洋文字とCJK文字（漢字・ハングルなど）の調和のとれた1:2の比率の配置を維持しています。現在、テスト中であり、イシューを通じてフィードバックを歓迎しています。

Noroshi Codeは、IBM Plex MonoおよびIBM Plex SansのCJK現地化バージョンを統合し、幅600ユニットのIBM Plex Monoの西洋文字に合わせるため、CJK文字の幅を1200に調整しています。IBM Plexから8つの太さを備えています。元のフォントが[制限されている](https://github.com/IBM/plex/issues/276)ため、ギリシャ文字（πを除く）は一時的にCJK/全角幅に従っています。

Noroshi Monoは、幅500の[Iosevka](https://github.com/be5invis/Iosevka)を導入し、よりコンパクトな表示を実現しています。西洋文字とCJK文字間で視覚的な一貫性を保つために5つの太さを維持しています。

両ファミリーとも、現時点では簡体字のサポートが不完全です。IBM Plex Sans SCがリリースされ次第、アップデートが予定されています。OTFバージョンは一部のソフトで正しく表示されない場合があります。その場合はTTFバージョンを使用してください。

## ビルド方法

Noroshiは、[Warcraft Font Merger](https://github.com/nowar-fonts/Warcraft-Font-Merger)およびPythonライブラリのfonttoolsとfoundrytools-cliを利用して作成されます。Pythonソースコードは[sources/](sources/)ディレクトリにあり、実際の使用には僅かな修正が必要かもしれません。

## 利用規約

フォントファイルは[OFLライセンス](OFL.txt)のもとで提供されており、ソースコードは[MITライセンス](MIT.txt)のもとで提供されています。