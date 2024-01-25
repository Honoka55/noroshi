# Noroshi

Noroshi is a monospaced font family designed to support CJK (Chinese, Japanese and Korean) characters, derived from the [IBM Plex typeface](https://github.com/IBM/plex).

## Features

Noroshi Code incorporates characters from IBM Plex Mono and IBM Plex Sans CJK localized versions, achieving a harmonious 1:2 ratio alignment between Western and CJK characters. It is currently undergoing testing and feedback is welcome through issue submissions.

Known issues include incomplete support for simplified Chinese characters, with an upcoming update scheduled for February 2024, coinciding with the publication of IBM Plex Sans SC. A G-source glyph prioritized version will also be released at that time. Another issue is that the Greek alphabets, excluding π, temporarily follow CJK/full-width width due to [limited support](https://github.com/IBM/plex/issues/276) in the original font.

**Note for Windows Users:** The preview of OTF format fonts in the Windows Font Viewer may appear abnormal. Please rest assured that this does not affect the normal usage of the font.

## To build

Noroshi is created using the [Warcraft Font Merger](https://github.com/nowar-fonts/Warcraft-Font-Merger) in conjunction with the fonttools and foundrytools-cli Python libraries. Python scripts can be found in the [sources/](sources/) directory, and may require slight modifications for actual use.

## License

The font files are licensed under the [OFL license](OFL.txt), while the source codes are under the [MIT license](MIT.txt).