from urllib.request import urlopen
import warnings
import os
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
URL = 'https://www.oreilly.com/pub/sc/osconfeed'
JSON = 'osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON,encoding='utf-8') as fp:
        return json.load(fp)


feed = load()
sorted(feed['Schedule'].keys())
for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value), key))
print("feed['Shedule']['speakers'][-1]['name'] {}\n----------".format(feed['Schedule']['speakers'][-1]['name']))
print("feed['Shedule']['speakers'][-1]['serial'] {}\n----------".format(feed['Schedule']['speakers'][-1]['serial']))
print("feed['Schedule']['events'][40]['name'] {}\n----------".format(feed['Schedule']['events'][40]['name']))
print("feed['Schedule']['events'][40]['speakers'] {}\n----------".format(feed['Schedule']['events'][40]['speakers']))


from collections import abc
import keyword


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


raw_feed = load()
feed = FrozenJSON(raw_feed)
len(feed.Schedule.speakers)
sorted(feed.Schedule.keys())
for key, value in sorted(feed.Schedule.items()):
    print('{:3} {}'.format(len(value), key))

print("feed.Schedule.speakers[-1].name {}\n----------".format(feed.Schedule.speakers[-1].name))
talk = feed.Schedule.events[40]
print("type(talk) {}\n----------".format(type(talk)))
print("talk.name {}\n----------".format(talk.name))
print("talk.speakers {}\n----------".format(talk.speakers))

grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
print("getattr(grad, 'class_') {}\n----------".format(getattr(grad, 'class_')))


class FrozenJSON2:
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON2(self.__data[name])


DB_NAME = 'schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    raw_data = load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)


import shelve
db = shelve.open(DB_NAME)
if CONFERENCE not in db:
    load_db(db)


speaker = db['speaker.3471']
print("speaker {}\n----------".format(speaker))
type(speaker)
print("type(speaker) {}\n----------".format(type(speaker)))
print("speaker.name {} speaker.twitter {}\n----------".format(speaker.name, speaker.twitter))
db.close()


DB_NAME2 = 'schedule2_db'


class Record2:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record2):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class MissingDatabaseError(RuntimeError):
    """Raised"""


class DbRecord(Record2):
    __db = None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                if db is None:
                    msg = "database not set; call '{}.set_db(my_db)'"
                    raise MissingDatabaseError(msg.format(cls.__name__))
                else:
                    raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super().__repr__()


class Event(DbRecord):

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speakers']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key))
                                  for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}'.format(cls_name, self.name)
        else:
            return super().__repr__()

import inspect

def load_db2(db):
    raw_data = load()
    warnings.warn('loading ' + DB_NAME2)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)
        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)


import shelve
db2 = shelve.open(DB_NAME2)
if CONFERENCE not in db2:
    load_db2(db2)
DbRecord.set_db(db2)
event = DbRecord.fetch('event.33950')
print("event {}\n----------".format(event))
print("event.venue {}\n----------".format(event.venue))
print("event.venue.name {}\n----------".format(event.venue.name))

for spkr in event.speakers:
    print('{0.serial}:{0.name}'.format(spkr))



