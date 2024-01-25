# Noroshi

Noroshi（ノロシ）は、[IBM Plexタイプフェイス](https://github.com/IBM/plex)から派生したCJKに対応した等幅フォントファミリーです。

## 特徴

Noroshi Code（ノロシコード）は、IBM Plex MonoおよびIBM Plex SansのCJK現地化バージョンを統合し、西洋文字とCJK文字（漢字・ハングルなど）の調和のとれた1:2の比率の配置を実現しています。現在、テスト中であり、イシューを通じてフィードバックを歓迎しています。

既知の問題には、簡体字のサポートが不完全であることが含まれており、これに対するアップデートは2024年2月にIBM Plex Sans SCが公開される際に予定されており、その際にはGソースの字形が優先されるバージョンもリリースされる予定です。また、元のフォントが[制限されている](https://github.com/IBM/plex/issues/276)ため、ギリシャ文字（πを除く）は一時的にCJK/全角幅に従って表示されるという問題もあります。

**Windowsユーザーの方へのお知らせ：**Windows フォント ビューアーでOTF形式のフォントのプレビューが正常でない場合がありますが、お使いのフォントは通常通りご利用いただけますので、ご安心ください。

## ビルド方法

このフォントは、[Warcraft Font Merger](https://github.com/nowar-fonts/Warcraft-Font-Merger)およびPythonライブラリのfonttoolsとfoundrytools-cliを利用して作成されます。Pythonソースコードは[sources/](sources/)ディレクトリにあり、実際の使用には僅かな修正が必要かもしれません。

## 利用規約

フォントファイルは[OFLライセンス](OFL.txt)のもとで提供されており、ソースコードは[MITライセンス](MIT.txt)のもとで提供されています。