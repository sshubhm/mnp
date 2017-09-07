# mnp

download and install opencv
	
	For Ubuntu: sudo apt-get install python-opencv

	For windows: http://docs.opencv.org/3.2.0/d5/de5/tutorial_py_setup_in_windows.html

Download and install Selenium

https://pypi.python.org/pypi/sel

Download geckodriver

	For LINUX: https://github.com/mozilla/geckodriver/releases
	
	Extract the folder and copy the 'geckodriver' file into '/usr/local/bin'
	Use 'sudo chmod +x /usr/local/bin/geckodriver' to permit execute.

	For Windows:
	
	Add lines in the code.
 
	from selenium import webdriver
	driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
	driver.get('http://inventwithpython.com')
