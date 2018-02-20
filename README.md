# Python Fb Library

<h1>Usage:</h1><br />

You can use this python library to log in to your Facebook account.<br />
It is easy,safe and it works.


<h1>How to set up</h1><br />
     1)Download the Zip file.<br />
     2)Unzip the Zip file.<br />
     
There is 2 ways to import the library.<br />
     1)Run the install.py(it will move the Fb.py to the python Library path).<br />
     OR
     2)Make a Folder and then paste the Fb.py library to the Folder.<br />
     If you use this method you must have the Fb.py library to the same folder with your project.

<h1>Example:</h1><br />
       
        
        import Fb
        
        email = "someemail@hotmail.com"
        password = "somepass"
        
        Fb.Login(email,password)
        
        if Fb.Login == True:
              print('[*]Logged in succesfully')
              print(Fb.Cookies)
        elif Fb.Login == False:
              print('[*]Failed to logged in')
              print(Fb.Cookies)
        
