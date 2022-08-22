from datetime import date
from views import Index, Register, Contact, About, StudyPrograms, CoursesList, CreateCourse, CreateCategory, \
    CategoryList, CopyCourse
import json


"""Pattern front controller"""


def current_date_front(request):
    prog = json.load(open('fixtures/content.json', encoding='utf-8'))
    request['prog'] = prog


def other_front(request):
    request['key'] = 'key'


def date_front(request):
    request['date'] = date.today()


fronts = [current_date_front, other_front, date_front]

# routes = {
#     '/': Index(),
#     '/registration/': Register(),
#     '/contact/': Contact(),
#     '/about/': About(),
#     '/study_programs/': StudyPrograms(),
#     '/courses-list/': CoursesList(),
#     '/create-course/': CreateCourse(),
#     '/create-category/': CreateCategory(),
#     '/category-list/': CategoryList(),
#     '/copy-course/': CopyCourse()
# }
