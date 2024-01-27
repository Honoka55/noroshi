# Noroshi

Noroshi(노로시)는 [IBM Plex 글꼴](https://github.com/IBM/plex)에서 派生된 CJK 文字를 支援하는 固定幅 글꼴입니다.

## 特徵

Noroshi는 Noroshi Code(노로시코드)와 Noroshi Mono(노로시모노)의 2個의 글꼴 集合을 包含하고 있습니다. 모두 西洋 文字와 CJK 文字(漢字 및 한글 等)의 調和로운 1:2 比率 配置를 維持하고 있습니다. 現在 테스트 中이며, 이슈를 通해 피드백을 歡迎하고 있습니다.

Noroshi Code는 IBM Plex Mono 및 IBM Plex Sans의 CJK 現地化 버전을 統合하여 600유닛의 IBM Plex Mono의 西洋 文字에 맞추기 爲해 CJK 文字의 幅을 1200으로 調整하고 있습니다. IBM Plex에서 8個의 加重値를 갖추고 있습니다. 元來의 글꼴이 [制限되어 있다](https://github.com/IBM/plex/issues/276) 때문에 그리스 文字(π 除外)는 一時的으로 CJK/全角幅을 따르고 있습니다.

Noroshi Mono는 幅 500의 [Iosevka](https://github.com/be5invis/Iosevka)를 導入하여 보다 콤팩트한 表示를 實現하고 있습니다. 西洋 文字와 CJK 文字 間에 視覺的 一貫性을 維持하기 爲해 5個의 加重値를 維持하고 있습니다.

두 글꼴 集合 모두 現時點에서는 簡體字의 支援이 不完全합니다. IBM Plex Sans SC가 出市되는 대로 업데이트가 豫定되어 있습니다. OTF 버전은 一部 소프트웨어에서 올바르게 表示되지 않을 수 있습니다.그 境遇는 TTF 버전을 使用해 주세요.

## 빌드方法

이 글꼴은 [Warcraft Font Merger](https://github.com/nowar-fonts/Warcraft-Font-Merger) 및 Python 라이브러리인 fonttools와 foundrytools-cli를 使用하여 生成됩니다. Python 소스 코드는 [sources/](sources/) 디렉토리에 있으며, 實際使用에는 작은 修正이 必要할 수 있습니다.

## 利用約款

글꼴 파일은 [OFL 라이선스](OFL.txt) 下에 提供되며, 소스 코드는 [MIT 라이선스](MIT.txt) 下에 提供됩니다.