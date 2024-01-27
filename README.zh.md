# Noroshi

Noroshi是一款支持CJK字符的等宽字体，衍生自[IBM Plex字体](https://github.com/IBM/plex)。

## 特性

Noroshi包含两个字体家族：Noroshi Code和Noroshi Mono，均保持西文和CJK字符之间和谐的1:2比例对齐。目前正在测试中，欢迎通过issue提供反馈。

Noroshi Code合并了IBM Plex Mono及IBM Plex Sans的CJK本地化版本，将CJK字符宽度调整为1200，以匹配IBM Plex Mono西文字符的宽度600。Noroshi Code包括原版IBM Plex的全八个字重。由于IBM Plex Mono原始字体的[希腊字母支持不完善](https://github.com/IBM/plex/issues/276)，除π以外的希腊字母目前显示为CJK/全角宽度。

Noroshi Mono的西文部分来自宽度为500的[Iosevka](https://github.com/be5invis/Iosevka)，显示更加紧凑。Noroshi Mono仅保留五个字重，以确保西文和CJK之间的视觉统一。

Noroshi的汉字字形全部来自IBM Plex Sans已发布的CJK本地化版本，故目前对简化字的支持不完善，计划在IBM Plex Sans SC发布后进行更新。Windows字体查看器对OTF格式字体的预览可能不正常，不过请放心这并不影响字体的使用。

## 构建

字体创建过程中使用了[魔兽世界字体合并工具](https://github.com/nowar-fonts/Warcraft-Font-Merger)及Python的fonttools和foundrytools-cli库。Python源代码在[sources/](sources/)目录中，可能需要稍作修改才能实际运行。

## 授权

字体以[OFL协议](OFL.txt)授权，源代码以[MIT协议](MIT.txt)授权。