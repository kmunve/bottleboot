# -*- coding: utf-8 -*-
__author__ = 'kmu'

"""
See http://docs.python-requests.org/en/latest/user/quickstart/
"""

import requests
import datetime
import numpy as np

from dl_bar_plot import bar_plot

def dl_request(region_id, start_date, end_date):
    """
    requests regional avalanche danger levels per region from api.nve.no.
    Plots the data.
    """
    url = "http://api01.nve.no/hydrology/forecast/avalanche/v2.0.2/api/AvalancheWarningByRegion/Simple/{0}/1/{1}/{2}".format(region_id, start_date, end_date)
    print url
    p = requests.get(url)
    data = p.json()

    region_name = data[0]["RegionName"]
    if u'å' in region_name:
        region_name = region_name.replace(u'å', 'aa').encode('ascii', 'ignore')
    elif u'ø' in region_name:
        region_name = region_name.replace(u'ø', 'oe').encode('ascii', 'ignore')
    elif u'æ' in region_name:
        region_name = region_name.replace(u'æ', 'ae').encode('ascii', 'ignore')
    else:
        region_name = region_name.encode('ascii', 'ignore')

    #region_name = unicode(data[0]["RegionName"]).encode('utf-8')
    print region_name, type(region_name)
    #region_name = data[0]["RegionName"].encode('ascii', 'ignore') # removes Norwegian letters
    #print data[0].keys()
    title = "Avalanche Danger for {0} during the period {1} - {2}".format(region_name, data[0]["ValidFrom"], data[-1]["ValidFrom"])
    dates = []
    values = []
    for i in data:
        dates.append(datetime.datetime.strptime(i["ValidFrom"], "%Y-%m-%dT%H:%M:%S"))

        values.append(i["DangerLevel"])
        #print "{0}: {1}".format(i["ValidFrom"], i["DangerLevel"])
    #print p.json()[0]["DangerLevel"]

    d = dates
    v = np.asarray(values, int)


    bar_plot(d, v, title=title, filename=region_name)
    """
    Trouble when RegionName contains norwegian letters.
    """

def __daily_update():
    start_date = "2014-12-02"
    today = datetime.datetime.now()
    td = datetime.timedelta(days=1)
    tmrw = today+td
    end_date = "{0}-{1}-{2}".format(tmrw.year, tmrw.month, tmrw.day)

    for i in range(6, 34):
        dl_request(i, start_date, end_date)


def specific_period(start_date, end_date):
    for i in range(6, 34):
        dl_request(i, start_date, end_date)

if __name__ == "__main__":
    #specific_period("2014-12-02", "2015-05-31")
    __daily_update()
