# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, run, route, get, post, request, template, static_file, debug #, TEMPLATE_PATH
from html_template import WeatherParameter
import crocus

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

@route('/crocus')
def crocus_html():
    """
    ToDo:

    """
    station_list = [89920, 86070]
    region_list = crocus.station_dict.keys()


    img_files = crocus.get_ftp_content()
    url_vertprofile, url_snowgraintype, url_density = crocus.get_img_urls(img_files, crocus.station_dict['Romsdal'][0])
    # print url_vertprofile, url_snowgraintype, url_density

    html = template('crocus', region_list=region_list, url_vertprofile=url_vertprofile, url_snowgraintype=url_snowgraintype, url_density=url_density)

    return html

@get('/form_test') # or @route('/login')
def region_form():
    region_list = crocus.station_dict.keys()
    crocus_form = template('crocus_form', region_list=region_list)
    html = template('crocus_main', crocus_form=crocus_form, crocus_result='')
    return html


@post('/region_submit') # or @route('/login', method='POST')
def region_submit():
    region = request.forms.get('region')
    print region
    print crocus.station_dict.values()
    station_list = crocus.station_dict[region]
    print station_list, "after"
    region_list = crocus.station_dict.keys()

    crocus_form = template('crocus_form', region_list=region_list)

    img_files = crocus.get_ftp_content()
    url_vertprofile, url_snowgraintype, url_density = crocus.get_img_urls(img_files, crocus.station_dict[region][0])

    crocus_result = template('crocus_result', station_list=station_list, url_vertprofile=url_vertprofile, url_snowgraintype=url_snowgraintype, url_density=url_density)

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