# RJLibrary
Django Library Web App

django version: 2.0.1

Steps to run server.

Install MySQL:

	version: 5.5

	$ sudo apt-get update
	$ sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
	
MySQL Database Setup:

	Create Database:
		> create database rjlibrary character set utf8;	
	Create User:
		> create user rjuser@localhost identified by 'rjpassword';
	User Access:
		> grant all privileges on rjlibrary.* to rjuser@localhost;
		> flush privileges;
		
	*Make sure you update the same db credentials in RJProj/settings.py

Migrations:

	$ python manage.py migrate
	
Runserver:

	$ python manage.py runserver localhost:<favourite-port>
	or
	$ python manage.py runserver 0.0.0.0:<favourite-port>



