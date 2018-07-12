import os, sys, zipfile

cwd = os.getcwd()

if(sys.version_info > (3, 0)):
    import urllib.request
    urllib.request.urlretrieve("https://gist.githubusercontent.com/GarnetSunset/f8713eed6efd548fb4aded28c13b428f/raw", "latest.txt")
else:
    import urllib2
    with open("latest.txt",'wb') as f:
        f.write(urllib2.urlopen("https://gist.githubusercontent.com/GarnetSunset/f8713eed6efd548fb4aded28c13b428f/raw").read())
        f.close()

with open("latest.txt", 'r') as myfile:
    url=myfile.read().replace('\n', '')

if(sys.version_info > (3, 0)):
    urllib.request.urlretrieve(url, "chromeweb.zip")
else:
    with open("chromeweb.zip",'wb') as f:
        f.write(urllib2.urlopen(url).read())
        f.close()

zipper = zipfile.ZipFile("chromeweb.zip", 'r')
zipper.extractall(cwd)
zipper.close()

os.remove("chromeweb.zip")
os.remove("latest.txt")
