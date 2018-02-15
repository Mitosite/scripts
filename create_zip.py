import zipfile, os

#here put the path to your file, repeat the line for multiple files
f = "Homo_sapiens.GRCh37.dna.primary_assembly.fa"
#create the name of your zip file
f_zip = "test.zip"

zip = zipfile.ZipFile (f_zip, "w", zipfile.ZIP_DEFLATED)
zip.write(f)
zip.close()










