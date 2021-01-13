=============================================
Ta3refa
Django Web app
=============================================
1.Required Running environment
	I.while in the same directory run the following in your shell:
		pip install -r requirements.txt

	II.You have to Download and install postgresql v13.0: https://www.postgresql.org/download/
  	provide password :1234

	III.You have to Download and install pgAdmin 4:https://www.pgadmin.org/download/
	
	IV.Open pgAdmin , click on postgresql type password :1234 ,right click on databases and click "Create-Database"
	V.Fill the form with the following : 
	   [Database:Ecommerce
	    Owner : postgres
	   ]
	
======================================
2.To configure the Webapp
............*Note: these changes are mandatory.................
	I.type the follwing in your shell:
		python manage.py makemigrations
		python manage.py migrate
		python manage.py createsuperuser
	II.then type any credentials you want for the super user
		python manage.py runserver
	III.then go to : "http://127.0.0.1:8000/admin" in your browser
	    Under the "SOCIAL ACCOUNTS" tab ,Click on "social applications" ,then fill the form using the following values:
	       [Provider :Google
		Name:demo google
		Client id:984219763261-8d7pjer1hjugcr25ecipdcfdoch22uqg.apps.googleusercontent.com
		Secret Key:9Vw6rin8hngnQ1ME4JMMIo2O
		Sites: Double click on 'example.com' to be shown in "Chosen sites" tab.
		]
	IV.After you click save go to "Site" from the left side panel
	   Click on 'example.com'
		fill the form using:
		[Domain name:ta3refa.com
		 Display name:ta3refa
		]
	V.Click "SAVE" ,then navigate to "Home" at the top left side ,and then click "LOG OUT".
===========================================================
3.You can now navigate to "http://127.0.0.1:8000" to start browsing the webapp
===========================================================
4. TESTING

	I.To test one app (ex:checkout) type: python manage.py test checkout
	II.To run all tests in all apps (including integration test) type: python manage.py test
	III.To test stress and respond time set directory of the project in cmd then write (python system_stress_respond.py)
	     NOTE: You should change the domain name in "system_stress_respond.py" to your server ip (you can use free ngrock tunneling)
	



