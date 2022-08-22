from datetime import date
import json


def current_date_front(request):
    prog = json.load(open('fixtures/content.json', encoding='utf-8'))
    request['prog'] = prog


def other_front(request):
    request['key'] = 'key'


def date_front(request):
    request['date'] = date.today()


fronts = [current_date_front, other_front, date_front]
