import ftplib

ftp_pre = 'ftp://'
ftp_met = 'ftp.met.no'
xgeo_dir = '/users/dagrunvs/xgeo/'

def get_ftp_content():

    ftp = ftplib.FTP(ftp_met) # connect to host, default port
    ftp.login()
    ftp.cwd(xgeo_dir)
    files = ftp.nlst() # list directory contents
    ftp.quit()

    return files

def get_img_urls(files):
    """
    Split file name and retrieve stationd id and station name and use it as a heading
    Change web-page such that only the sations within a region are shown when chosen from drop-down menu.

    """


    base_url = "{0}{1}{2}".format(ftp_pre, ftp_met, xgeo_dir)
    station_id = '61410'

    matching = [s for s in files if station_id in s]

    # Verticale profile
    img_vertprofile = [s for s in matching if 'VERTICAL_PROFILE' in s][0]
    url_vertprofile = "{0}{1}".format(base_url, img_vertprofile)

    # Snow grain type
    img_snowgraintype = [s for s in matching if 'SNOWGRAINTYPE' in s][0]
    url_snowgraintype = "{0}{1}".format(base_url, img_snowgraintype)

    # Density
    img_density = [s for s in matching if 'DENSITY' in s][0]
    url_density = "{0}{1}".format(base_url, img_density)


    return url_vertprofile, url_snowgraintype, url_density