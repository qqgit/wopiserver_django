# wopiserver_django
Django implementation of WOPI server (or WOPI host) for Microsoft Office Online Server. 

A WOPI server is a host that can host Office documents and connect to Office Online Server to open Office documents in a browser. The WOPI server needs to work together with Office Online Server. Users can view and edit Office documents stored on the WOPI host in their local browser by using Office Online Server.

# Introduction
This project is a bare minimum implementation of WOPI server for viewing and editing Office documents online. 

The following WOPI interfaces are supported by running wopiserver_django:
- CheckFileInfo, via [GET /wopi/files/(fileid)](https://wopirest.readthedocs.io/en/latest/files/CheckFileInfo.html)
- GetFile, via [GET /wopi/files/(fileid)/contents](https://wopirest.readthedocs.io/en/latest/files/GetFile.html)
- PutFile, via [POST /wopi/files/(fileid)/contents](https://wopirest.readthedocs.io/en/latest/files/PutFile.html)

You can find more about WOPI protocol at https://blogs.msdn.microsoft.com/officedevdocs/2013/03/21/introducing-wopi/.


# Requirements
The project is developed and tested with Python 3.6 and Django 1.11.

WOPI server needs to work with Office Online Server.

The project is tested in an environment which have 3 servers and one user client:

                                        ![Test Environment for wopiserver_django](https://github.com/qqgit/wopiserver_django/blob/master/wopiserver/images/Test%20Environment.png)

# 

# Usage & Examples
## Check Office Online Server in a browser
You should make sure Office Online Server is doing its job OK.

In our test environment, Office Online Server 2016 is run on a Windows Server 2012 R2 with IP address 192.168.141.131. Office Online Server provides a discovery url: http://192.168.141.131/hosting/discovery. If Office Online Server works well, you can visit the discovery address http://192.168.141.131/hosting/discovery in a browser of user client and see some returned xml contents like following:
![hosting/discovery contents from Office Online Server](https://github.com/qqgit/wopiserver_django/blob/master/wopiserver/images/discovery.png)
## Download, run and test WOPI Server
First you should make sure python 3.6 and django 1.11 is installed correctly on your system.
```
$ python -V
Python 3.6...
$ python -c "import django;print(django.\__version\__)"
1.11.3
```
Then download wopiserver_django and run server
```
$ git clone https://github.com/qqgit/wopiserver_django.git
$ cd wopiserver_django/
$ python manage.py runserver 0.0.0.0:8000$ 
```
You can change the value of WOPI_FILE_DIR in wopiserver_django/settings.py to your directory for office documents storation. If you wish to following the following instruction, please keep WOPI_FILE_DIR unchanged now.

Now you can test the server in another terminal (the test step can be skipped). Open another terminal and change to xxxx/wopiserver_django/ directory and run
```
$ python manage.py test
```
If everything goes well, congratulations! You have a WOPI server running now.
## Check your WOPI Server in a browser
For the CheckFileInfo interface, you can visit http://192.168.141.132:8000/wopi/files/test.docx and it should returns some json string like 
```
{"BaseFileName": "test.docx", "OwnerId": "qi", "Size": 13918, "SHA256": "zaDaG/7D0CZ2Rp4oB69h8GWIte70KLgZGg6fEHPPZvs=", "Version": "1", "SupportsUpdate": true, "UserCanWrite": true, "SupportsLocks": true}
```
For the GetFile interface, you can visit http://192.168.141.132:8000/wopi/files/test.docx/contents and it should prompt to download the file test.docx.
## View Office documents online in a browser
Word View

http://192.168.141.131/wv/wordviewerframe.aspx?WOPISrc=http://192.168.141.132:8000/wopi/files/test.docx&access_token=123

PowerPoint View

http://192.168.141.131/p/PowerPointFrame.aspx?PowerPointView=ReadingView&WOPISrc=http://192.168.141.132:8000/wopi/files/test.pptx&access_token=123

Excel View

http://192.168.141.131/x/_layouts/xlviewerinternal.aspx?ui=zh-CN&rs=zh-CN&WOPISrc=http://192.168.141.132:8000/wopi/files/test.xlsx&access_token=123

## Edit Office documents online in a browser
Word Edit

http://192.168.141.131/we/wordeditorframe.aspx?WOPISrc=http://192.168.141.132:8000/wopi/files/test.docx&access_token=123

PowerPoint Edit

http://192.168.141.131/p/PowerPointFrame.aspx?PowerPointView=EditView&WOPISrc=http://192.168.141.13:8000/wopi/files/test.pptx&access_token=123

Excel Edit

http://192.168.141.131/x/_layouts/xlviewerinternal.aspx?edit=1&WOPISrc=http://192.168.141.132:8000/wopi/files/test.xlsx&access_token=123
