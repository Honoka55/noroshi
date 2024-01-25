from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform
from math import radians
import os

new_width = 1200
italic_slant_degree = 9
tables_to_drop = ['GSUB', 'GPOS', 'BASE']


def adjust_width(font):
    hmtx_table = font['hmtx']

    for glyph in font.getGlyphOrder():
        width, lsb = hmtx_table[glyph]
        offset = (new_width - width) // 2
        hmtx_table[glyph] = (new_width, lsb + offset)
    print(f'\tAll glyphs adjusted to width {new_width}.')

    return font


def drop_tables(font):
    for table in tables_to_drop:
        if table in font:
            del font[table]
            print(f'\tTable {table} dropped.')

    return font


def remove_glyphs(font):
    glyphs_to_remove = [glyph for glyph in set(font.getGlyphOrder()) if glyph.startswith('glyph')]

    if glyphs_to_remove:
        for glyph in glyphs_to_remove:
            del font['glyf'][glyph]
            # print(f'\tGlyph {glyph} removed.')
        print('\tUnused glyphs removed.')
    else:
        print('\tNo glyphs found with prefix "glyph".')

    return font


def modify_font(input_font, output_font):
    print(f'Modifying font: {input_font}')
    font = TTFont(input_font)

    font = adjust_width(font)
    font = drop_tables(font)
    font = remove_glyphs(font)

    font.save(output_font)
    print(f'\tFont successfully modified and saved to {output_font}.')
    italicize_font(output_font)


def italicize_font(upright_font_path):
    font = TTFont(upright_font_path)

    head_table = font['head']
    head_table.macStyle |= 0x0002

    post_table = font['post']
    post_table.italicAngle = -italic_slant_degree

    os2_table = font['OS/2']
    os2_table.fsSelection &= ~0x0040
    os2_table.fsSelection |= 0x0001

    name_table = font['name']
    for name_record in name_table.names:
        name_id = name_record.nameID
        name = name_record.toUnicode()

        if name_id in [2, 3, 4, 6]:
            if name.endswith("Regular"):
                new_name = name.replace("Regular", "Italic")
            else:
                new_name = f"{name} Italic" if name_id % 3 else f"{name}Italic"

            name_record.string = new_name.encode(name_record.getEncoding())

    hmtx_table = font['hmtx']
    for glyph_name in font.getGlyphOrder():
        half_width = hmtx_table[glyph_name][0] // 2
        width, lsb = hmtx_table[glyph_name]
        hmtx_table[glyph_name] = (width, lsb - half_width)

        glyph_pen = TTGlyphPen(font.getGlyphSet())
        glyph = font.getGlyphSet().get(glyph_name)
        glyph.draw(TransformPen(glyph_pen, Transform().skew(radians(italic_slant_degree))))

        hmtx_table[glyph_name] = (width, lsb)

        transformed_glyph = glyph_pen.glyph()
        font['glyf'][glyph_name] = transformed_glyph

    directory, filename = os.path.split(upright_font_path)
    filename, extension = os.path.splitext(filename)
    filename = filename.replace('Regular', '') + 'Italic'
    italic_font_path = os.path.join(directory, filename + extension)

    font.save(italic_font_path)
    print(f'\tFont successfully italicized and saved to {italic_font_path}.\n')


if __name__ == "__main__":
    input_dir = '../ibm/IBM-Plex-Sans-JPTCKR'

    for font_name in os.listdir(input_dir):
        if font_name.endswith('.ttf'):
            input_font_path = os.path.join(input_dir, font_name)
            output_dir = input_dir + '-mod'
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_font_path = os.path.join(output_dir, font_name)
            modify_font(input_font_path, output_font_path)
