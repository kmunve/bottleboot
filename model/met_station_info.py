__author__ = 'kmu'

import requests
import bs4


class MetStation():

    def __init__(self, station_id):
        self.station_id = station_id


    def __str__(self):

        try:
            s =  """
            Station: {0} - ID: {1}
            Lat: {2}, Lon: {3}, masl: {4} m
            Location on Google Maps: {5}

            """.format(self.name,
                       self.station_id,
                       self.lat,
                       self.lon,
                       self.masl,
                       self.google_maps_url)

        except AttributeError:
            s = """
            Station ID: {0}
            Run get_station_info() to retrieve more information about the station.
            """.format(self.station_id)

        return s


    def get_station_info(self):
        station_url = "http://eklima.met.no/met/MetService?invoke=getStationsProperties&stations={0}&username=".format(self.station_id)
        r = requests.get(station_url)

        soup = bs4.BeautifulSoup(r.text)

        self.municipality_no = soup.municipalityno.text
        self.department = soup.department.text

        self.name = soup.find("name").text
        self.stnr = soup.stnr.text
        self.wmo_no = soup.wmono.text

        self.masl = soup.amsl.text

        self.lat = soup.latdec.text
        self.lon = soup.londec.text
        self.latlonfmt = soup.latlonfmt.text

        self.utm_e = soup.utm_e.text
        self.utm_n = soup.utm_n.text
        self.utm_zone = soup.utm_zone.text

        self.from_day = soup.fromday.text
        self.from_month = soup.frommonth.text
        self.from_year = soup.fromyear.text

        self.to_day = soup.today.text
        self.to_month = soup.tomonth.text
        self.to_year = soup.toyear.text

        self._get_gmaps_loc()

    def _get_gmaps_loc(self):
        #self.google_maps_url = "http://maps.google.com/?q={0},{1}".format(self.lat, self.lon)
        self.google_maps_url = "http://www.google.com/maps/place/{0},{1}/@{0},{1},9z".format(self.lat, self.lon)



def __test_get_station_info():
    ms = MetStation(84210)
    ms.get_station_info()
    print ms


if __name__ == "__main__":
    __test_get_station_info()