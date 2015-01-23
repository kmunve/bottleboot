# -*- coding: utf-8 -*-
__author__ = 'kmu'

from bottle import SimpleTemplate

class WeatherParameter():
    def __init__(self):
        self.name = "Nysnø (24 t)"
        self.avg = 15
        self.min = 2
        self.max = 30
        self.unit = "cm"



def _weather_parameter_stats(self, wp):
    """
    Input is a weather parameter structure.
    """

    tpl = SimpleTemplate('''
    <tr>
        <td>{{ p.name }}</td>
        <td>{{ p.avg }}</td>
        <td>{{ p.min }}</td>
        <td>{{ p.max }}</td>
        <td>{{ p.unit }}</td>
    </tr>
    ''')
    html = tpl.render(p=wp)
    return html

def _hello(self):
    return "hello world"



def region_weather_stats(self, wplist):
    """
    Template that presents a summary of relevant weather data.

    Input a weather parameter list.

    Region              Kåfjord
    New snow (last 24-hours)	15 cm
    New snow (last 72-hours)    25 cm
    Total snowpack depth	50 cm
    Temperature	+1 C
    Wind	W - 5m/s

    Forecast
    New snow (next 24 h)
    Temperature (1500 moh)
    Temperature (0 moh)
    Wind
    """

    tpl = SimpleTemplate('''
    <table style="width:300px">
    <tr>
        <th>Parameter</th>
        <th>gjsn.</th>
        <th>min.</th>
        <th>maks</th>
        <th>enhet</th>
    </tr>

    % include('weather', p=wplist[0])

    </table>
    ''')
    html = tpl.render(wplist=wplist)
    print html



class htmlPage():

    def __init__(self):
        self.content = ""

    def gen_body(self):
        self.html_body = """<!DOCTYPE html>
    <html lang="no-nb">

    <head>
    <LINK href="http://karsten.pythonanywhere.com/view/css/bootstrap.css" rel="stylesheet" type="text/css">

    </head>

    <body>

    {0}

    </body>
    </html>""".format(self.content)

    def insert_img(self, img=""):
        #html_img = """<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">"""
        html_img = """<img src="{0}">""".format(img)
        self.content += html_img

    def insert_dwnld_img(self, img_base=""):
        html_img="""
        <div>
        <h2>Utvikling av faregraden i {0}</h2>
        <img src="http://karsten.pythonanywhere.com/media/{0}_thumb.png" height="400" class="img-responsive">
        <br>
        <p align=left>Last ned som <a href="http://karsten.pythonanywhere.com/media/{0}.pdf">PDF</a> eller <a href="http://karsten.pythonanywhere.com/media/{0}.png">bildefil</a>.</p>
        </div>
        """.format(img_base)
        self.content += html_img



if __name__ == "__main__":
    hp = htmlPage()
    hp.content = """<h1>My First Heading</h1><p>My first paragraph.</p>"""
    hp.gen_body()
    wp = WeatherParameter()
    wplist = [wp, wp]
    hp.region_weather_stats(wplist)
    print hp.html_body