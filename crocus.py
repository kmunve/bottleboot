import ftplib

ftp_pre = 'ftp://'
ftp_met = 'ftp.met.no'
xgeo_dir = '/users/dagrunvs/xgeo/'

# Dictionary containing station_id per region
station_dict = {'Romsdal': [89920, 86070], 'Hallingdal': [54710, 25630, 25830]}


def get_ftp_content():

    ftp = ftplib.FTP(ftp_met) # connect to host, default port
    ftp.login()
    ftp.cwd(xgeo_dir)
    files = ftp.nlst() # list directory contents
    ftp.quit()

    return files

def get_img_urls(files, station_id):
    """
    Split file name and retrieve stationd id and station name and use it as a heading
    Change web-page such that only the sations within a region are shown when chosen from drop-down menu.

    """
    # Compile main url
    base_url = "{0}{1}{2}".format(ftp_pre, ftp_met, xgeo_dir)

    # Convert station_id to String
    station_id = str(station_id)

    # Find all filenames containing the station_id
    station_files = [s for s in files if station_id in s]

    # Retrieve verticale profile plot
    # Currently (2015-01-18) there are two vert profile files in the folder - therefore the '.'!
    img_vertprofile = [s for s in station_files if 'VERTICAL_PROFILE.' in s][0]
    url_vertprofile = "{0}{1}".format(base_url, img_vertprofile)

    # Retrieve snow grain type plot
    img_snowgraintype = [s for s in station_files if 'SNOWGRAINTYPE' in s][0]
    url_snowgraintype = "{0}{1}".format(base_url, img_snowgraintype)

    # Retrieve density plot
    img_density = [s for s in station_files if 'DENSITY' in s][0]
    url_density = "{0}{1}".format(base_url, img_density)


    return url_vertprofile, url_snowgraintype, url_density


if __name__ == "__main__":
    img_files = get_ftp_content()
    vp, sgt, den = get_img_urls(img_files, 61410)
    print vp, sgt, den