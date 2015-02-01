# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, run, route, get, post, request, template, static_file, debug #, TEMPLATE_PATH
from html_template import WeatherParameter
import crocus

# Comment when in production
debug(True)

#TEMPLATE_PATH.insert(0, r'/home/karsten/mysite/view/')

"""
See http://stackoverflow.com/questions/11744941/bottle-multiple-template-variables
"""

@route('/')
def hello_world():
    return template('main')#, 'Dette er en test server. Spoer Karsten om hjelp!')


@route('/views/<filename>')
def server_view(filename):
    return static_file(filename, root='/views/')


@route('/media/<filename>')
def server_media(filename):
    return static_file(filename, root='/media/')

@route('/test')
def test_html():
    wp = WeatherParameter()
    wplist = [wp, wp]
    html = template('weather2', wplist=wplist)
    return html

@route('/base')
def base_html():
    html = template('base', base="Base test.")
    return html

@route('/dangerlevel')
def danger_level_html():
    """
    ToDo:

    """
    # region_list_2013 = ['Alta', 'Kaafjord', 'Tromsoe', 'Balsfjord', 'Senja', 'Lyngsalpan', 'Tamokdalen', 'Bardu', 'Harstad', 'Narvik', 'Vesteraalen', 'Lofoten', 'Trollheimen', 'Romsdal', 'Sunnmoere', 'Nordfjord', 'Fjordane', 'Sogn', 'Jotunheimen', 'Voss', 'Hallingskarvet', 'Hemsedalfjella', 'Roeldal', 'Rauland']
    region_list = ['Alta', 'Kaafjord', 'Tromsoe', 'Balsfjord', 'Senja', 'Lyngsalpan', 'Tamokdalen', 'Bardu', 'Narvik', 'Vesteraalen', 'Lofoten', 'Svartisen', 'Trollheimen', 'Romsdal', 'Sunnmoere', 'Fjordane', 'Sogn', 'Jotunheimen', 'Voss', 'Hallingdal', 'Roeldal', 'Rauland']
    html = template('dangerlevel', region_list=region_list)

    return html


@get('/crocus') # or @route('/login')
def region_form():
    station_dict = crocus.read_station_list()
    region_list = station_dict.keys()
    crocus_form = template('crocus_form', region_list=region_list)
    html = template('crocus_main', crocus_form=crocus_form, crocus_result='')
    return html


@post('/region_submit') # or @route('/login', method='POST')
def region_submit():
    region = request.forms.get('region')
    station_dict = crocus.read_station_list()
    region_list = station_dict.keys()

    crocus_form = template('crocus_form', region_list=region_list)

    crocus_result = []
    for station_id in station_dict[region]:
        url_vertprofile, url_snowgraintype, url_density, url_lwc, url_temperature = crocus.get_img_urls(station_id)
        print url_density

        crocus_result.append(template('crocus_result', station=station_id, url_vertprofile=url_vertprofile, url_snowgraintype=url_snowgraintype, url_density=url_density, url_lwc=url_lwc, url_temperature=url_temperature))

    html = template('crocus_main', crocus_form=crocus_form, crocus_result=crocus_result)

    return html
    #if check_login(name, password):
    #    return "<p>Your login was correct</p>"
    #else:
    #    return "<p>Login failed</p>"

# Uncomment when running on pythonanywhere
# application = default_app()

# Uncomment when running locally
run(host='localhost', port=8080)