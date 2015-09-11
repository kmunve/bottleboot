# A very simple Bottle Hello World app for you to get started with...
import platform
from bottle import default_app, route, template, static_file, debug, run #, TEMPLATE_PATH
from html_template import WeatherParameter
import crocus
from model.met_station_info import MetStation

# Comment when in production
debug(True)

#TEMPLATE_PATH.insert(0, r'/home/karsten/mysite/view/')

"""
See http://stackoverflow.com/questions/11744941/bottle-multiple-template-variables
"""

@route('/')
def hello_world():
    return template('main')#, 'Dette er en test server. Spoer Karsten om hjelp!')

@route('/plotly')
def plotly_test():
    html = """<!doctype html>
<html>
  <head>
  	<meta charset="utf-8">
    <title>Plotly demo plot</title>
  </head>
  <body>
    <h2>Plotly demo plot</h2>
    <div>
      <iframe width="800" height="600" frameborder="0" seamless="seamless" scrolling="no" src="https://plot.ly/~kmunve/28.embed?width=600&height=400"></iframe>
    </div>
  </body>
</html>

    """
    return html


@route('/views/<filename>')
def server_view(filename):
    return static_file(filename, root='/views/')


@route('/media/<filename>')
def server_media(filename):
    return static_file(filename, root='/media/')


@route('/resources/:path#.+#', name='static')
def server_resources(path):
    return static_file(path, root='resources')

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

@route('/jqplot')
def jqplot_html():
    html = template('jqplot')
    return html

@route('/eaws')
def eaws_html():
    html = """<!doctype html>
<html>
  <head>
  	<meta charset="utf-8">
    <title>EAWS documents</title>
  </head>
  <body>
    <h1>Open access to the EAWS documents</h1>
    <p>By clicking on the EAWS documents button you get read access to the OneDrive folders.</p>

    <div>
      <iframe src="https://onedrive.live.com/embed?cid=C807C4B4B34B642F&resid=C807C4B4B34B642F%21163&authkey=AODw-m5jc4P2HSc" width="165" height="128" frameborder="0" scrolling="no"></iframe>
    </div>

  </body>
</html>

    """
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
@route('/crocus/model')
@route('/crocus/model/<region>')
def region_via_url(region=None):

    station_dict = crocus.read_station_list()
    region_list = station_dict.keys()

    crocus_form = template('crocus_form', region_list=region_list)

    try:
        crocus_result = []
        crocus_result.append(template("""<div class="page-header"><h1>{{region}}</h1></div>""", region=region))
        for station_id in station_dict[region]:
            url_vertprofile, url_snowgraintype, url_density, url_lwc, url_temperature = crocus.get_img_urls(station_id)
            ms = MetStation(station_id)
            ms.get_station_info()

            crocus_result.append(template('crocus_result',
                                          station_name=ms.name,
                                          station_id=station_id,
                                          station_elev=ms.masl,
                                          url_gmap=ms.google_maps_url,
                                          url_vertprofile=url_vertprofile,
                                          url_snowgraintype=url_snowgraintype,
                                          url_density=url_density,
                                          url_lwc=url_lwc,
                                          url_temperature=url_temperature))

        crocus_results = ""
        for result in crocus_result:
            crocus_results += u"<p>{0}</p>".format(result)

        crocus_page = u"<p>{0}</p>{1}".format(crocus_form, crocus_results)
        html = template('crocus_main', crocus_page=crocus_page)

    except KeyError:
        html = template('crocus_main', crocus_page=crocus_form)

    return html


@route('/crocus/help')
def crocus_help():

    crocus_page = template('crocus_help')
    html = template('crocus_main', crocus_page=crocus_page)
    return html


########################
### Start the server ###
########################

if platform.system() == 'Windows':
    # Uncomment when running locally
    print 'Running locally on Windows'
    run(host='localhost', port=8080)
else:
    # Uncomment when running on server, e.g. pythonanywhere
    application = default_app()
