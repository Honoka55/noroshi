# Noroshi

Noroshi是一款支持CJK字符的等宽字体家族，衍生自[IBM Plex字体](https://github.com/IBM/plex)。

## 特性

Noroshi Code合并了IBM Plex Mono及IBM Plex Sans的CJK本地化版本，实现了西文与CJK字符之间和谐的1:2比例对齐。目前正在测试中，欢迎通过issue提供反馈。

已知问题包括对简化字支持不完善，计划于IBM Plex Sans SC发布时进行更新，届时也会发布G源字形优先的版本。由于IBM Plex Mono原始字体[对希腊字母支持不完善](https://github.com/IBM/plex/issues/276)，除π以外的希腊字母目前显示为CJK/全角宽度。

**Windows用户注意：**Windows字体查看器对OTF格式字体的预览可能不正常。请放心，这并不影响字体的使用。

## 构建

字体创建过程中使用了[魔兽世界字体合并工具](https://github.com/nowar-fonts/Warcraft-Font-Merger)及Python的fonttools和foundrytools-cli库。Python源代码在[sources/](sources/)目录中，您可能需要稍作修改才能实际运行。

## 授权

字体以[OFL协议](OFL.txt)授权，源代码以[MIT协议](MIT.txt)授权。