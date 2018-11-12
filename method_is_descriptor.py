import collections


class Text(collections.UserString):
    def __repr__(self):
        return 'Text({!r})'.format(self.data)
    def reverse(self):
        return self[::-1]


word = Text('forward')
print("word {}\n----------".format(word))

print("word.reverse() {}\n----------".format(word.reverse()))
print("Text.reverse(Text('backward')) {}\n----------".format(Text.reverse(Text('backward'))))
print("type(Text.reverse) {}\n----------".format(type(Text.reverse)))
print("type(word.reverse) {}\n----------".format(type(word.reverse)))
print("list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')])) {}\n----------".format(list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')]))))

print("Text.reverse.__get__(word) {}\n----------".format(Text.reverse.__get__(word)))
print("Text.reverse.__get__(None, Text) {}\n----------".format(Text.reverse.__get__(None, Text)))
print("word.reverse {}\n----------".format(word.reverse))
print("word.reverse.__self__ {}\n----------".format(word.reverse.__self__))
print("word.reverse.__func__ is Text.reverse {}\n----------".format(word.reverse.__func__ is Text.reverse))


