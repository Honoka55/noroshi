# Noroshi

Noroshi(노로시)는 [IBM Plex 글꼴](https://github.com/IBM/plex)에서 派生된 CJK를 支援하는 固定幅 글꼴 패밀리입니다.

## 特徵

Noroshi Code(노로시 코드)는 IBM Plex Mono 및 IBM Plex Sans의 CJK 現地化 버전을 統合하여 西洋文字와 CJK 文字(漢字 및 한글 等)의 調和로운 1:2 比率配置를 實現합니다. 現在 테스트 中이며, 피드백은 이슈를 通해 歡迎합니다.

알려진 問題點으로는 簡體字의 支援이 不完全한 것이 包含되어 있으며, 이에 對한 업데이트는 2024年 2月에 IBM Plex Sans SC가 出市될 때 豫定되어 있으며, 該當 버전에서는 G 소스의 字形가 優先되는 버전도 出市될 豫定입니다. 또한, 元來의 글꼴이 [制限되어 있기](https://github.com/IBM/plex/issues/276) 때문에 그리스 文字(π 除外)는 一時的으로 CJK/全角幅에 따라 表示되는 問題도 있습니다.

**注意: Windows 使用者:** Windows 글꼴 뷰어에서 OTF 形式의 글꼴 미리보기가 正常이 아닐 수 있지만, 使用中인 글꼴은 普通대로 使用할 수 있으니 安心하세요.

## 빌드方法

이 글꼴은 [Warcraft Font Merger](https://github.com/nowar-fonts/Warcraft-Font-Merger) 및 Python 라이브러리인 fonttools와 foundrytools-cli를 使用하여 生成됩니다. Python 소스 코드는 [sources/](sources/) 디렉토리에 있으며, 實際使用에는 작은 修正이 必要할 수 있습니다.

## 利用約款

글꼴 파일은 [OFL 라이선스](OFL.txt) 下에 提供되며, 소스 코드는 [MIT 라이선스](MIT.txt) 下에 提供됩니다.