import datetime
from os.path import abspath, dirname, join

from bottle import route, run, static_file, view

from horo import get_sentence_generator

zodiac_signs = {
    # en name : (ru name, icon char)
    'Aries': ('Овен', 'a'),
    'Taurus': ('Телец', 'b'),
    'Gemini': ('Близнецы', 'c'),
    'Cancer': ('Рак', 'd'),
    'Leo': ('Лев', 'e'),
    'Virgo': ('Дева', 'f'),
    'Libra': ('Весы', 'g'),
    'Scorpio': ('Скорпион', 'h'),
    'Sagittarius': ('Стрелец', 'i'),
    'Capricorn': ('Козерог', 'j'),
    'Aquarius': ('Водолей', 'k'),
    'Pisces': ('Рыбы', 'l'),
}

zodiac_choices = [(ru_name, en_name) for (en_name, (ru_name, _)) in sorted(zodiac_signs.items(), key=lambda z: z[1][1])]

month = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}

ROOT = dirname(abspath(__file__))

sentenceGen = get_sentence_generator(join(ROOT, 'data', 'prophecy.txt'))


@route('/')
@view('index')
def index():
    now = datetime.datetime.now()
    response = {
        'title': 'Генератор гороскопа',
        'now_day': now.day,
        'now_month': month[now.month],
        'topic': "Узнай свою судьбу",
        'zodiac_choices': zodiac_choices
    }
    return response


@route('/<zodiac>')
@view('zodiac')
def zodiac_page(zodiac: str):
    now = datetime.datetime.now()
    ru_name, icon_char = zodiac_signs[zodiac]
    response = {
        'title': zodiac,
        'topic': f'{ru_name}. {now.day} {month[now.month]}',
        'text': sentenceGen.generate_text(),
        'icon': icon_char,
    }
    return response


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=join(ROOT, 'static'))


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
