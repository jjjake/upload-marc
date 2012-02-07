#!/usr/bin/env python

import urllib2
from urllib2 import HTTPError
import sys
import logging


logger = logging.getLogger('upload_marc')
hdlr = logging.FileHandler('./upload_marc.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)


def upload_marc(item):
    item = item.strip()
    marc = '%s_marc.xml' % item

    # Check to see if the MARC record exists locally.
    try:
        marc_data = open(marc).read()
    except IOError:
        logger.warning('Could not find the file, "%s"' % marc)
        return 'ERROR: Could not find the file, "%s"' % marc

    # Create IAS3 request.
    request = urllib2.Request('http://s3.us.archive.org/%s/%s' % 
                              (item, marc), data=marc_data)
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request.add_header('authorization', 'LOW %s' % sys.argv[1])
    request.add_header('Content-Type', 'text/xml')
    request.get_method = lambda: 'PUT' 

    # Attempt to upload the file, report errors if upload is not succesfull. 
    try:
        url = opener.open(request)
        status = url.getcode()
        if status == 200:
            return ('\n\n"%s" has been successfully uploaded to '
                    '"http://archive.org/details/%s"\n\n' % (marc,item))
    except HTTPError, e:
        logger.warning('Failed to upload "%s" to "%s". Returned HTTP status code: %s' % (marc,item,e.code))
        return ('\n\nERROR: Failed to upload "%s" to "%s". ' 
                'Returned HTTP status code: %s\n\n' % (marc,item,e.code))
    
def main():
    
    # Upload all of the MARC records from "itemlist" in current directory.
    for item in open('itemlist'):
        print upload_marc(item)
        
if __name__ == "__main__":
    main()
