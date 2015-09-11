import ftplib
import json
import os


def read_station_list():
    fid = open(r"/home/karsten/mysite/resources/station_list.js", "r")
    station_dict = json.load(fid)
    fid.close()
    return station_dict


def get_ftp_content():

    ftp_pre = 'ftp://'
    ftp_met = 'ftp.met.no'
    xgeo_dir = '/users/dagrunvs/xgeo/'

    ftp = ftplib.FTP(ftp_met) # connect to host, default port
    ftp.login()
    ftp.cwd(xgeo_dir)
    files = ftp.nlst() # list directory contents

    print files

    for filename in files:
        print "Assessing file: ", filename,
        try:
            if filename[-4:] == ".jpg":
                print "Downloading ", filename
                local_filename = os.path.join(r'.\media\m_crocus', filename)
                fid = open(local_filename, 'wb')
                ftp.retrbinary('RETR '+ filename, fid.write)
                fid.close()
        except IndexError:
            pass

    ftp.quit()


def get_img_urls(station_id):
    """
    Split file name and retrieve station id and station name and use it as a heading
    Change web-page such that only the stations within a region are shown when chosen from drop-down menu.

    """
    # Read media folder content
    files = os.listdir(r"/home/karsten/mysite/media/m_crocus")

    # Compile main url
    base_url = r"http://karsten.pythonanywhere.com/media/m_crocus/"

    # Convert station_id to String
    station_id = str(station_id)

    # Find all file names containing the station_id
    station_files = [s for s in files if station_id in s]

    # Retrieve vertical profile plot
    # Currently (2015-01-18) there are two vertical profile files in the folder - therefore the '.'!
    img_vertprofile = [s for s in station_files if 'VERTICAL_PROFILE.' in s][0]
    url_vertprofile = "{0}{1}".format(base_url, img_vertprofile)

    # Retrieve snow grain type plot
    img_snowgraintype = [s for s in station_files if 'SNOWGRAINTYPE' in s][0]
    url_snowgraintype = "{0}{1}".format(base_url, img_snowgraintype)

    # Retrieve density plot
    img_density = [s for s in station_files if 'DENSITY' in s][0]
    url_density = "{0}{1}".format(base_url, img_density)

    # Retrieve LWC plot
    img_lwc = [s for s in station_files if 'LIQUID_WATER_CONTENT' in s][0]
    url_lwc = "{0}{1}".format(base_url, img_lwc)

    # Retrieve temperature plot
    img_temperature = [s for s in station_files if 'TEMPERATURE' in s][0]
    url_temperature = "{0}{1}".format(base_url, img_temperature)

    return url_vertprofile, url_snowgraintype, url_density, url_lwc, url_temperature


if __name__ == "__main__":
    img_files = get_ftp_content()
    #vp, sgt, den, lwc, temp = get_img_urls(61410)
    #print vp, sgt, den, lwc, temp