from bottle import route, run, view, static_file
import datetime
from horo import get_sentence_generator
from collections import OrderedDict

zodiacDict = {'Aries': ('Овен', 'a'),
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
              'Pisces': ('Рыбы', 'l')}

ordered_zodiac = OrderedDict(sorted(zodiacDict.items(), key=lambda z: z[1][1]))

month = {1: "января",
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
         12: "декабря"}


@route('/')
@view('view')
def index():
    return create_response()


@route('/<zodiac>')
@view('view')
def zodiac_page(zodiac):
    return create_response(zodiac)


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')


def create_response(zodiac=''):
    """
    Create response dictionary for index (zodiac = Null) and zodiac page
    :rtype: response: dict
    :type zodiac: str
    """
    now = datetime.datetime.now()
    response = {}
    if zodiac:
        response['title'] = zodiac
        response['header'] = "{}. {} {}".format(ordered_zodiac[zodiac][0], now.day, month[now.month])
        response['text'] = sentenceGen.generate_text()
        response['day'] = ordered_zodiac[zodiac][1]
    else:
        response['day'] = now.day
        response['month'] = month[now.month]
        response['header'] = "Узнай свою судьбу"
        response['zodiac'] = [(ordered_zodiac[z][0], z) for z in ordered_zodiac.keys()]
    return response

sentenceGen = get_sentence_generator('h.txt')

run(host='localhost', port=8080, debug=True)
