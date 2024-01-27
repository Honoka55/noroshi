from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter, load_font, Options
import re
import os

blocks_file_path = 'Blocks.txt'
cjk_ideo_blocks = ['CJK Radicals Supplement', 'Kangxi Radicals', 'CJK Unified Ideographs Extension A',
                   'CJK Unified Ideographs', 'CJK Compatibility Ideographs', 'CJK Unified Ideographs Extension B',
                   'CJK Unified Ideographs Extension C', 'CJK Unified Ideographs Extension D',
                   'CJK Unified Ideographs Extension E', 'CJK Unified Ideographs Extension F',
                   'CJK Unified Ideographs Extension I', 'CJK Compatibility Ideographs Supplement',
                   'CJK Unified Ideographs Extension G', 'CJK Unified Ideographs Extension H']
cjk_symb_blocks = ['Ideographic Description Characters', 'CJK Symbols and Punctuation', 'Hiragana', 'Katakana',
                   'Bopomofo', 'Hangul Compatibility Jamo', 'Kanbun', 'Bopomofo Extended', 'CJK Strokes',
                   'Katakana Phonetic Extensions', 'Enclosed CJK Letters and Months', '3300-3370', '337B-337F',
                   '33E0-33FE', 'Hangul Jamo Extended-A', 'Hangul Syllables', 'Hangul Jamo Extended-B',
                   'Vertical Forms', 'CJK Compatibility Forms', 'Small Form Variants', 'Halfwidth and Fullwidth Forms']
ref_font_path = '../ibm/IBM-Plex-Sans-JPTCKR-width1000/IBMPlexSansJPTCKR-Regular.ttf'


def get_block_ranges():
    block_ranges = {}

    with open(blocks_file_path) as f:
        for line in f:
            match = re.match(r'^([0-9A-F]+)\.\.([0-9A-F]+); (.*)$', line)
            if match:
                start = int(match.group(1), 16)
                end = int(match.group(2), 16)
                block_name = match.group(3)
                block_ranges[block_name] = (start, end)

    return block_ranges


def get_font_unicode(font):
    cmap_table = font['cmap']
    unicode_map = cmap_table.getBestCmap()

    return [code_point for code_point, _ in unicode_map.items()]


def font_subsetter(font_path, code_points):
    font = load_font(font_path, Options())
    subsetter = Subsetter()
    subsetter.populate(unicodes=code_points)
    subsetter.subset(font)

    return font


def get_exclude_range(blocks_all, blocks_ref, reference_path):
    block_ranges = get_block_ranges()
    exclude_range = []

    for block in blocks_all:
        start, end = block_ranges[block]
        for codepoint in range(start, end + 1):
            exclude_range.append(codepoint)

    if reference_path:
        reference_glyphs = get_font_unicode(TTFont(reference_path))
        for block in blocks_ref:
            if block in block_ranges:
                start, end = block_ranges[block]
            elif '-' in block:
                start, end = block.split('-')
                start = int(start, 16)
                end = int(end, 16)
            else:
                continue
            for codepoint in range(start, end + 1):
                if codepoint in reference_glyphs:
                    exclude_range.append(codepoint)

    return exclude_range


def exclude_blocks_from_font(input_path, output_path, blocks_all, blocks_ref, reference_path):
    font = TTFont(input_path)
    unicode_range = get_font_unicode(font)
    exclude_range = get_exclude_range(blocks_all, blocks_ref, reference_path)

    for codepoint in exclude_range:
        if codepoint in unicode_range:
            unicode_range.remove(codepoint)

    subset_font = font_subsetter(input_path, unicode_range)
    subset_font.save(output_path)
    print(f'{output_path} saved.')


if __name__ == '__main__':
    input_dir = '../ibm/SarasaMonoJ'
    output_dir = '../ibm/Iosevka-subset'

    for font_name in os.listdir(input_dir):
        if font_name.endswith('.ttf'):
            input_font_path = os.path.join(input_dir, font_name)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_font_path = os.path.join(output_dir, font_name.replace('SarasaMonoJ', 'Iosevka'))
            exclude_blocks_from_font(input_font_path, output_font_path, cjk_ideo_blocks, cjk_symb_blocks, ref_font_path)
