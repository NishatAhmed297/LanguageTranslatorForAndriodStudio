# Andorid Language Helper
### Requirements:
1. Python 3.9

### How to use?

## ONE TIME SETUP
1. Download and install latest [Python](https://www.python.org/downloads/) version.
2. Open python Setup, Check the box given at the bottom of the installation window named as "Add to Path".
3. Start Installation of python
4. Now install following library just write following command in command prompt.<br/>
	>pip install requests
	
## STEPS BEFORE TRANSLATION
1. All the translations depend upon source English file, so keep your sentences and phrases in such a way that user will be able to understand english and all other translations respectively.
2. This script will remove special characters like \n, \t, \' and \"
		
## STEPS TO TRANSLATE
1. Open command prompt from Start menu and navigate to current working folder, for example in my case <br/>
	>  G:\Nishat\Python Automation Scripts **OR**<br/>
	> Click on Address bar and write cmd and press Enter.
2. Copy source XML file (strings.xml) in current working directory. Source file should be in English language.
3. Write following command<br/>
    > python auto_translator.py -h
4. This file requires 2 arguments. First is source xml file and Second are language codes, You can translate into multiple langugaes. Just seperate each language code with a space. Sample commands are given below<br/>
	> English -> Urdu -----> python auto_translator.py strings.xml ur<br/>
	> English -> Urdu, Arabic, French -----> python auto_translator.py strings.xml ur ar fr<br/>
5. Output file will be stored in values-**"Output"** Folder.
	