import os, sys, zipfile

cwd = os.getcwd()

url = "https://dootnode.org/neko/builds/nightly/ReiNX-latest.zip"

if(sys.version_info > (3, 0)):
    import urllib.request
    urllib.request.urlretrieve(url, "reinx.zip")
else:
    import urllib2
    with open("reinx.zip",'wb') as f:
        f.write(urllib2.urlopen(url).read())
        f.close()

zipper = zipfile.ZipFile("reinx.zip", 'r')
zipper.extractall(cwd)
zipper.close()

os.remove("reinx.zip")
