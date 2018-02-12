# wopiserver_django
Django implementation of WOPI server (or WOPI host) for Microsoft Office Online Server. 

A WOPI server is a host that can host Office documents and connect to Office Online Server to open Office documents in a browser. The WOPI server needs to work together with Office Online Server. Users can view and edit Office documents stored on the WOPI host in their local browser by using Office Online Server.

# Introduction
This project is a bare minimum implementation of WOPI server for viewing and editing Office documents online. 

The following WOPI interfaces are supported by running wopiserver_django:
- CheckFileInfo, via [GET /wopi/files/(file_id)](https://wopirest.readthedocs.io/en/latest/files/CheckFileInfo.html)
- GetFile, via [GET /wopi/files/(file_id)/contents](https://wopirest.readthedocs.io/en/latest/files/GetFile.html)
- PutFile, via [POST /wopi/files/(file_id)/contents](https://wopirest.readthedocs.io/en/latest/files/PutFile.html)

You can find more about WOPI protocal at https://blogs.msdn.microsoft.com/officedevdocs/2013/03/21/introducing-wopi/.


# Requirements
The project is developed and tested with Python 3.6 and Django 1.11.

WOPI server needs to work with Office Online Server.
The project is tested in an environments which have 3 servers and one user client.

                                        AD DS on Windows Server 2012 --------------------------------
                                                      |                                             |
browser on user client --------- Office Online Server on Windows Server 2012 --------- wopiserver_django(WOPI Server) on CentOS 7

# 

# Usage & Examples
