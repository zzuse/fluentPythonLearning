print('-' * 20)
s = 'café'
print("len {}".format(len(s)))
print('encode')
b = s.encode('utf8')
print(b)
print(len(b))
print('decode')
print(b.decode('utf8'))

print('-' * 20)
cafe = bytes('café', encoding='utf-8')
print('variable cafe = {}'.format(cafe))
print('cafe[0] = {}'.format(cafe[0]))
print('cafe[:1] = {}'.format(cafe[:1]))
cafe_arr = bytearray(cafe)
print('cafe_arr = {}'.format(cafe_arr))
print('cafe_arr[-1:] = {}'.format(cafe_arr[-1:]))

print('-' * 20)
a = bytes.fromhex('31 4B CE A9')
print("bytes.fromhex is {}".format(a))

print('-' * 20)
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print('array holds octets is {}'.format(octets))

print('-' * 20)
print('memory views and struct')
import struct
fmt = '<3s3sHH'
with open('CScmqnj.gif','rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print('bytes(header) is {}'.format(bytes(header)))
struct.unpack(fmt, header)
print('struct.unpack(fmt, header) is {}'.format(struct.unpack(fmt, header)))
del header
del img

print('-' * 20)
print('string encoding with different bytes sequences')
n = bytes.fromhex('C3 A3')
print("bytes.fromhex is {}".format(n))
print(n.decode('utf-8'))
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

print('-' * 20)
print('encoding and decoding success and error handling')
city = 'São Paulo'
city.encode('utf_8')
print('city.encode("utf_8") {} '.format(city.encode('utf_8')))
city.encode('utf_16')
print('city.encode("utf_16") {} '.format(city.encode('utf_16')))
city.encode('iso8859_1')
print('city.encode("iso8859_1") {} '.format(city.encode('iso8859_1')))
city.encode('cp437', errors='ignore')
print('city.encode("cp437") ignore error {} '.format(city.encode('cp437', errors='ignore')))
city.encode('cp437', errors='replace')
print('city.encode("cp437") replace error {} '.format(city.encode('cp437', errors='replace')))
city.encode('cp437', errors='xmlcharrefreplace')
print('city.encode("cp437") error xmlcharrefreplace {} '.format(city.encode('cp437', errors='xmlcharrefreplace')))

print('-' * 20)
print('decode from bytes to str success and error handling')
octets = b'Montr\xe9al'
print('octets.decode("cp1252") is {}'.format(octets.decode('cp1252')))
print('octets.decode("iso8859_7") is {}'.format(octets.decode('iso8859_7')))
print('octets.decode("koi8_r") is {}'.format(octets.decode('koi8_r')))
print('octets.decode("utf_8") is {}'.format(octets.decode('utf_8', errors='replace')))

print('-' * 20)
print('BOM - byte order mark')
u16 = 'El Niño'.encode('utf_16')
print('El Niño u16 is {}'.format(u16))
print('El Niño u16 list is {}'.format(list(u16)))
u16le = 'El Niño'.encode('utf_16le')
print('El Niño u16le list is {}'.format(list(u16le)))
u16be = 'El Niño'.encode('utf_16be')
print('El Niño u16be list is {}'.format(list(u16be)))

print('-' * 20)
print('read coding')
fp = open('cafe.txt', 'w', encoding='utf_8')
print('write cafe.txt {}'.format(fp.write('café')))
fp.close()
import os
print('cafe.txt size is {}'.format(os.stat('cafe.txt').st_size))
fp2 = open('cafe.txt')
print('fp2 encoding is {}'.format(fp2))
fp2.close()
fp3 = open('cafe.txt', encoding='utf_8')
print('fp3 encoding is {}'.format(fp3))
print('fp3 read is {}'.format(fp3.read()))
fp3.close()
fp4 = open('cafe.txt', 'rb')
print('fp4 is {}'.format(fp4))
print(('fp4 read is {}'.format(fp4.read())))
fp4.close()

print('-' * 20)
print('defaults I/O')
import sys, locale

expressions = """
    locale.getpreferredencoding()
    type(my_file)
    my_file.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdin.isatty()
    sys.stdin.encoding
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding()
"""
my_file = open('dummy', 'w')
for expressions in expressions.split():
    value = eval(expressions)
    print(expressions.rjust(30), '->', repr(value))

print('-' * 20)
print('cafe lens different')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1,s2)
print('café len is {}'.format(len(s1)), 'cafe\u0301 len is {}'.format(len(s2)))
print('café == cafe\u0301 is {}'.format(s1 == s2))

print('-' * 20)
print('cafe lens normalize')
from unicodedata import normalize
s1 = 'café'
s2 = 'cafe\u0301'
print('normalize s1 NFC len {}'.format(len(normalize('NFC', s1))))
print('normalize s2 NFC len {}'.format(len(normalize('NFC', s2))))

print('normalize s1 NFD len {}'.format(len(normalize('NFD', s1))))
print('normalize s2 NFD len {}'.format(len(normalize('NFD', s2))))

print('normalize s1 == s2 NFC is {}'.format(normalize('NFC', s1) == normalize('NFC', s2)) )
print('normalize s1 == s2 NFD is {}'.format(normalize('NFD', s1) == normalize('NFD', s2)) )

print('-' * 20)
print('omega normalization')
from unicodedata import name
ohm = '\u2126'
print('name of \u2126 is {}'.format(name(ohm)) )
ohm_c = normalize('NFC',ohm)
print('name of \u2126 after normailize is {}'.format(name(ohm_c)) )
print('if \u2126 == \u2126 after normailize is {}'.format(ohm == ohm_c))
print('if \u2126 normalize == \u2126 after normailize is {}'.format(normalize('NFC',ohm) == normalize('NFC',ohm_c)))

print('-' * 20)
print(' ½ NFKC normalization')
half = '½'
print('½ after NFKC is {}'.format(normalize('NFKC', half)))
four_squared = '4²'
print('4² after NFKC is {}'.format(normalize('NFKC', four_squared)))
micro = 'µ'
micro_kc = normalize('NFKC', micro)
print('µ and μ after normalization {} {}'.format(micro, micro_kc) )
print('µ and μ after ord {} -- {}'.format(ord(micro), ord(micro_kc) ) )
print('µ and μ after name {} -- {}'.format(name(micro), name(micro_kc) ) )
micro_cf = micro.casefold()
print('µ casefold is {} '.format(name(micro_cf)) )
print(micro,micro_cf)
eszett = 'ß'
print('name of ß is {}'.format(name(eszett)))
eszett_cf = eszett.casefold()
print('eszett = {} eszett_cf = {}'.format(eszett,eszett_cf))

print('-' * 20)
print('nfc_equal and case_fold')

s3 = 'Straße'
s4 = 'strasse'
print('Straße == strasse is {}'.format(s3 == s4))
print('Straße strasse normalize equal is {}'.format(normalize('NFC', s3) == normalize('NFC', s4)))
print('A a normalize equal is {}'.format(normalize('NFC', 'A') == normalize('NFC', 'a')))
print('Straße strasse casefold equal is {}'.format((normalize('NFC', s3).casefold()) == (normalize('NFC', s4).casefold())))
print('A a casefold equal is {}'.format((normalize('NFC', 'A').casefold()) == (normalize('NFC', 'a').casefold())))

print('-' * 20)
print('sanitize string')

import unicodedata
import string

def shave_marks(txt):
    """remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

def shave_marks_latin(txt):
    """remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print("order: {}".format(order))
print("order shave_marks: {}".format(shave_marks(order)))
print("order shave_marks_latin: {}".format(shave_marks_latin(order)))

greek = 'Ζέφυρος, Zéfiro'
print(greek)
print(shave_marks(greek))
print(shave_marks_latin(greek))


print('-' * 20)
print('single map')

single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # <1>
                           """'f"*^<''""---~>""")

multimap = str.maketrans({  # <2>
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multimap.update(single_map)

def dewinize(txt):
    return txt.translate(multimap)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)

print("order dewinze: {}".format(dewinize(order)))
print("order asciize: {}".format(asciize(order)))

print('-' * 20)
print('sort by locale')
import locale
locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
fruits = ['caju', 'atemoia', 'caja', 'açaí', 'acerola']
#locale.strxfrm in macosx never did its job use pyUCA instead
sorted_fruits = sorted(fruits)
print(sorted_fruits)
sorted_fruits = sorted(fruits, key = locale.strxfrm)
print(sorted_fruits)

print('-' * 20)
print('sort by pyuca')
import pyuca
coll = pyuca.Collator()
sorted_fruits = sorted(fruits, key =coll.sort_key)
print("sorted_fruits in pyuca {}".format(sorted_fruits))

print('-' * 20)
print('unicodedata metadata')

import re
re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),                       # <1>
          char.center(6),                             # <2>
          're_dig' if re_digit.match(char) else '-',  # <3>
          'isdig' if char.isdigit() else '-',         # <4>
          'isnum' if char.isnumeric() else '-',       # <5>
          format(unicodedata.numeric(char), '5.2f'),  # <6>
          unicodedata.name(char),                     # <7>
          sep='\t')
# END NUMERICS_DEMO

print('-' * 20)
print('str versus bytes in re')

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n   ')
print('Numbers')
print('   str  :', re_numbers_str.findall(text_str))
print('   bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print('   str  :', re_words_str.findall(text_str))
print('   bytes:', re_words_bytes.findall(text_bytes))

print('-' * 20)
print('filename in os')

print("listdir . {}".format(os.listdir('.')))
print("listdir b. {}".format(os.listdir(b'.')))
pi_name_bytes = os.listdir(b'.')[1]
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
print(pi_name_str)
print(pi_name_str.encode('ascii', 'surrogateescape'))