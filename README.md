# Upload MARC records to the Internet Archive.

1. Generate a file named `itemlist` containing one IA identifier per line.
2. Move `itemlist`, `upload_marc.py`, and all of the MARC records you intend
to upload into the same directory.
3. Visit (http://www.archive.org/account/s3.php)[http://www.archive.org/account/s3.php]
to obtain your S3 keys.
4. Upload the MARC records by executing the following on the command line (replacing
`Y6oUrAcCEs4sK8ey` with your access key, and `youRSECRETKEYzZzZ` with your secret key.
Separated by a colon):

    ./upload_marc.py Y6oUrAcCEs4sK8ey:youRSECRETKEYzZzZ     

## Notes
* All HTTP errors and missing file errors are logged to a file called `upload_marc.log`.

