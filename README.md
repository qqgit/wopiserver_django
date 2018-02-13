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

In our test environment, Office Online Server 2016 is run on a Windows Server 2012 R2 with IP address 192.168.141.131. Office Online Server provides a discovery url: http://192.168.141.131/hosting/discovery. If Office Online Server is OK, you can visit the discovery address http://192.168.141.131/hosting/discovery in a browser of user client and see some returned xml contents like following:
![hosting/discovery contents from Office Online Server](https://github.com/qqgit/wopiserver_django/blob/master/wopiserver/images/discovery.png)



