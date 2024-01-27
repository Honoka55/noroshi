from fontTools.ttLib import TTFont
from code_process import output_dir as reference_dir
from code_process import new_family_name as ref_family_name
from code_process import new_version_number as ref_version_number
from code_process import update_name, update_os2_and_head, generate_font_files
import os

original_dir = '../ibm/Iosevka-JPTCKR'
output_dir = '../fonts/NoroshiMono/ttf/unhinted'
ori_filename_prefix = 'IosevkaJPTCKR'
new_xAvgCharWidth = 500
new_family_name = 'Noroshi Mono'
new_version_number = '0.001'


def publish_noroshi_mono():
    for filename in os.listdir(original_dir):
        if filename.endswith('.ttf'):
            font_path = os.path.join(original_dir, filename)

            font = TTFont(font_path)

            font = update_os2_and_head(font, new_xAvgCharWidth, new_version_number)

            ref_filename = filename.replace(ori_filename_prefix, ref_family_name.replace(' ', ''))
            ref_name_table = TTFont(os.path.join(reference_dir, ref_filename))['name']
            font['name'] = ref_name_table
            name_table = font['name']
            for name_record in name_table.names:
                if ref_family_name in name_record.toUnicode():
                    update_name(name_record, new_family_name, ref_family_name)
                if ref_family_name.replace(' ', '') in name_record.toUnicode():
                    update_name(name_record, new_family_name.replace(' ', ''), ref_family_name.replace(' ', ''))
                if ref_version_number in name_record.toUnicode():
                    update_name(name_record, new_version_number, ref_version_number)
                if name_record.nameID == 0:
                    update_name(name_record, 'Copyright (c) 2024 Honoka55. Portions Copyright (c) 2015-2024, Renzhi Li (aka. Belleve Invis, belleve@typeof.net). Portions Copyright 2017-2018 IBM Corp. Portions Copyright (c) 2014, 2015 Adobe Systems Incorporated (http://www.adobe.com/). Portions Copyright (c) 2012 Google Inc.')
                if name_record.nameID == 9:
                    update_name(name_record, 'Belleve Invis; ' + name_record.toUnicode())

            new_names = [record for record in name_table.names if record.nameID < 20 and record.nameID != 12]
            name_table.names = new_names

            generate_font_files(font, output_dir, filename, ori_filename_prefix, new_family_name.replace(' ', ''))


if __name__ == '__main__':
    publish_noroshi_mono()
