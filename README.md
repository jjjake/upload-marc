# Upload MARC records to existing Internet Archive items.

1. Download this repository by clicking the following link: https://github.com/jjjake/upload-marc/zipball/master
2. Unzip the repository.
1. Generate a file named `itemlist` containing one IA identifier per line.
2. Move `itemlist` and all of the MARC records you intend to upload into the `jjjake-upload-marc-xxxxx` directory
(the same directory that upload_marc.py is locate in).
3. Visit http://www.archive.org/account/s3.php to obtain your S3 keys.
4. Upload the MARC records by executing the following on the command line (replacing
`Y6oUrAcCEs4sK8ey` with your access key, and `youRSECRETKEYzZzZ` with your secret key.
Separated by a colon):      

        ./upload_marc.py Y6oUrAcCEs4sK8ey:youRSECRETKEYzZzZ     

## Notes
* All HTTP errors and missing file errors are logged to a file named `upload_marc.log`.
