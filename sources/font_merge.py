import os
import subprocess

tools_directory = 'D:/MiniPrograms/字体合并补全工具-简体中文-1.1.0-windows-x64'
base_font_directory = '../ibm/IBM-Plex-Mono'
ext_font_directory = '../ibm/IBM-Plex-Sans-JPTCKR-width1200'
output_directory = '../ibm/IBM-Plex-Mono-JPTCKR'

base_fonts = [f for f in os.listdir(base_font_directory) if f.endswith('.ttf')]
ext_fonts = [f for f in os.listdir(ext_font_directory) if f.endswith('.ttf')]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for ext_font in ext_fonts:
    base_font = ext_font.replace('SansJPTCKR', 'Mono')
    base_font_path = os.path.join(base_font_directory, base_font)
    if base_font not in base_fonts:
        continue
    ext_font_path = os.path.join(ext_font_directory, ext_font)
    print(f'Merging font: {base_font} with {ext_font}')

    output_font_path = os.path.join(output_directory, f'IBMPlexMonoJPTCKR-{base_font.split("-")[1].split(".")[0]}')

    subprocess.run([os.path.join(tools_directory, 'otfccdump.exe'), '--ignore-hints', '-o', f'{output_font_path}.otd', base_font_path])
    subprocess.run([os.path.join(tools_directory, 'otfccdump.exe'), '--ignore-hints', '-o', 'ext.otd', ext_font_path])
    subprocess.run([os.path.join(tools_directory, 'merge-otd.exe'), f'{output_font_path}.otd', 'ext.otd'])
    subprocess.run([os.path.join(tools_directory, 'otfccbuild.exe'), '-q', '-O3', '-o', f'{output_font_path}.ttf', f'{output_font_path}.otd'])

    os.remove(f'{output_font_path}.otd')
    os.remove('ext.otd')

    print(f' Merged font: {output_font_path}.ttf')

print('All fonts merged successfully!')
