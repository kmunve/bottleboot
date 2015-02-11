__author__ = 'kmu'

import requests
import bs4


class MetStation():

    def __init__(self, station_id):
        self.station_id = station_id


    def __str__(self):
        return """
        Station: {0} - ID: {1}
        Lat: {2}, Lon: {3}, masl: {4} m

        """.format(self.name,
                   self.station_id,
                   self.lat,
                   self.lon,
                   self.masl)


    def get_station_info(self):
        station_url = "http://eklima.met.no/met/MetService?invoke=getStationsProperties&stations={0}&username=".format(self.station_id)
        r = requests.get(station_url)

        soup = bs4.BeautifulSoup(r.text)

        print soup.prettify()

        self.municipality_no = soup.municipalityno.text
        self.department = soup.department.text

        self.name = soup.name.text
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





        """
                <item xsi:type="ns3:no_met_metdata_StationProperties">
                <amsl xsi:type="xsd:int">740</amsl>
                <department xsi:type="xsd:string">NORDLAND</department>
            <fromDay xsi:type="xsd:int">1</fromDay>
            <fromMonth xsi:type="xsd:int">10</fromMonth>
            <fromYear xsi:type="xsd:int">2014</fromYear>
            <latDec xsi:type="xsd:double">68.1905</latDec>
            <latLonFmt xsi:type="xsd:string">decimal_degrees</latLonFmt>
            <lonDec xsi:type="xsd:double">17.7892</lonDec>
            <municipalityNo xsi:type="xsd:int">1805</municipalityNo>
            <name xsi:type="xsd:string">LOSISTUA</name>
            <stnr xsi:type="xsd:int">84210</stnr>
            <toDay xsi:type="xsd:int">0</toDay>
            <toMonth xsi:type="xsd:int">0</toMonth>
            <toYear xsi:type="xsd:int">0</toYear>
            <utm_e xsi:type="xsd:int">615610</utm_e>
            <utm_n xsi:type="xsd:int">7566717</utm_n>
            <utm_zone xsi:type="xsd:int">33</utm_zone>
            <wmoNo xsi:type="xsd:int">1091</wmoNo>
        """

    def get_gmaps_loc(self):
        google_maps_url = "http://maps.google.com/?q={0},{1}".format(self.lat, self.lon)


def __test_get_station_info():
    ms = MetStation(84210)
    ms.get_station_info()
    print ms

if __name__ == "__main__":
    __test_get_station_info()