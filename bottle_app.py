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


@route('/crocus/')
@get('/crocus/model')
def region_form():
    station_dict = crocus.read_station_list()
    region_list = station_dict.keys()
    crocus_form = template('crocus_form', region_list=region_list)
    html = template('crocus_main', crocus_page=crocus_form)
    return html


@post('/crocus/model') # or @route('/login', method='POST')
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

    crocus_results = ""
    for result in crocus_result:
        crocus_results += u"<p>{0}</p>".format(result)

    crocus_page = u"<p>{0}</p>{1}".format(crocus_form, crocus_results)
    html = template('crocus_main', crocus_page=crocus_page)

    return html


@route('/crocus/help')
def crocus_help():

    crocus_page = template('crocus_help')
    html = template('crocus_main', crocus_page=crocus_page)
    return html

# Uncomment when running on pythonanywhere
# application = default_app()

# Uncomment when running locally
run(host='localhost', port=8080)