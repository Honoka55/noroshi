from fontTools.ttLib import TTFont
from fontTools.ttLib.woff2 import compress
import os
import subprocess

original_dir = '../ibm/IBM-Plex-Mono-JPTCKR'
output_dir = '../fonts/NoroshiCode/ttf/unhinted'
new_xAvgCharWidth = 600
old_family_name = 'IBM Plex Mono + IBM Plex Sans JP + IBM Plex Sans TC + IBM Plex Sans KR'
old_version_number = '2.004'
new_family_name = 'Noroshi Code'
new_version_number = '0.001'


def update_name(record, new_name, old_str=None):
    if old_str:
        old_name = record.toUnicode()
        new_name = old_name.replace(old_str, new_name)
        record.string = new_name.encode(record.getEncoding())
    else:
        record.string = new_name.encode(record.getEncoding())


if __name__ == '__main__':
    for filename in os.listdir(original_dir):
        if filename.endswith('.ttf'):
            font_path = os.path.join(original_dir, filename)

            font = TTFont(font_path)

            os2_table = font['OS/2']
            os2_table.xAvgCharWidth = new_xAvgCharWidth
            os2_table.achVendID = 'HNK5'

            head_table = font['head']
            head_table.fontRevision = new_version_number

            name_table = font['name']
            for name_record in name_table.names:
                if name_record.nameID == 0:
                    update_name(name_record, 'Copyright 2024 Honoka55. Copyright 2017-2018 IBM Corp. All rights reserved.')
                if name_record.nameID in [1, 3, 4, 16]:
                    update_name(name_record, new_family_name, old_family_name)
                if name_record.nameID in [3, 5]:
                    update_name(name_record, new_version_number, old_version_number)
                if name_record.nameID == 6:
                    update_name(name_record, new_family_name.replace(' ', ''), old_family_name.replace(' ', ''))
                if name_record.nameID == 7:
                    update_name(name_record, '')
                if name_record.nameID == 8:
                    update_name(name_record, 'Honoka55')
                if name_record.nameID == 9:
                    update_name(name_record, 'Mike Abbink; Paul van der Laan; Pieter van Rosmalen; Eunyou Noh; Wujin Sim; Yejin We; Jinhee Kim; Yona Kim; Zheng Chuyang; Xue Tianmeng; Wang Yingqiao; Cai Huan; Li Jian; Hsuan Hao Chang; Sueh Li Tan; Hsin Yin Low; Yejin Wi; Boomi Park; Kichan Ma; Chorong Kim; Dohee Lee;')
                if name_record.nameID == 11:
                    update_name(name_record, 'https://honoka55.github.io')

            ttf_output_path = os.path.join(output_dir, filename.replace('IBMPlexMonoJPTCKR', new_family_name.replace(' ', '')))
            os.makedirs(os.path.dirname(ttf_output_path), exist_ok=True)
            font.save(ttf_output_path)
            print(f'{ttf_output_path} saved.')

            ttf_hinted_output_dir = output_dir.replace('unhinted', 'hinted')
            ttf_hinted_output_path = ttf_output_path.replace('unhinted', 'hinted')
            subprocess.run(['ftcli', 'ttf', 'autohint', '-out', ttf_hinted_output_dir, ttf_output_path])
            print(f'{ttf_hinted_output_path} saved.')

            otf_output_dir = output_dir.replace('ttf', 'otf')
            otf_output_path = ttf_output_path.replace('ttf', 'otf')
            subprocess.run(['ftcli', 'converter', 'ttf2otf', '-out', otf_output_dir, ttf_output_path])
            print(f'{otf_output_path} saved.')

            otf_hinted_output_dir = otf_output_dir.replace('unhinted', 'hinted')
            otf_hinted_output_path = otf_output_path.replace('unhinted', 'hinted')
            subprocess.run(['ftcli', 'otf', 'autohint', '-out', otf_hinted_output_dir, otf_output_path])
            print(f'{otf_hinted_output_path} saved.')

            woff2_output_path = otf_output_path.replace('otf', 'woff2')
            os.makedirs(os.path.dirname(woff2_output_path), exist_ok=True)
            compress(otf_output_path, woff2_output_path)
            print(f'{woff2_output_path} saved.')

            woff2_hinted_output_path = woff2_output_path.replace('unhinted', 'hinted')
            os.makedirs(os.path.dirname(woff2_hinted_output_path), exist_ok=True)
            compress(otf_hinted_output_path, woff2_hinted_output_path)
            print(f'{woff2_hinted_output_path} saved.\n')
