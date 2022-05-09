Requirements:
1. Python 3.9

How to use?

*** ONE TIME SETUP ***
1. Extract "Python Automation Scripts.zip" in any desired folder.
2. Open python Setup, Check the box given at the bottom of the installation window named as "Add to Path".
3. Start Installation of python
4. Now install following libraries just write following command in command prompt
	pip install google_trans_new requests
	
*** STEPS BEFORE TRANSLATION ***
		1. All the translations depend upon source English file, so keep your sentences and phrases in such a way that user will be able to understand english and all other translations respectively.
		2. This script will remove special characters like \n, \t, \' and \"
		
*** STEPS TO TRANSLATE ***
1. Open command prompt from Start menu and navigate to current working folder
	for example in my case [ cd G:\Nishat\Python Automation Scripts ] 
						OR
	Click on Address bar and write cmd and press Enter.
2. Copy source XML file (strings.xml) in current working directory. Source file should be in English language.
3. Write following command
    python auto_translator.py -h
4. This file requires 2 arguments. First is source xml file and Second are language codes, You can translate into multiple langugaes. Just seperate each language code with a space.
Sample commands are given below
		python auto_translator.py strings.xml ur                            [ english -> urdu]
		python auto_translator.py strings.xml ur ar fr                      [ english -> urdu, arabic, french]
4. Output file will be stored in values-"lang_code" Folder.

*** POSSIBLE ERRORS ***
1. Package Not found: if there is a package not found error, just write following command in CMD
	pip install package_name
2. If you find a JSON error, Than you have to change a few lines in google_trans_new library, step is as following.
	1. Look at the error and copy the path to google_trans_new.py file. It must be located in C drive. My address is as following
		C:\Users\User\AppData\Local\Programs\Python\Python39\Lib\site-packages\google_trans_new
	2. Open google_trans_new.py using notepad++ or any editor that shows line numbers.
	3. Go to line 151 and make following changes
		CHANGE		response = (decoded_line + ']')		TO 		response = (decoded_line)
	4. Repeat the same process on line no 233.
	