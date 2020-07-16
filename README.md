
### Web Crawler with requests and beautifulsoup4(bs4) library in python ###

#### Installing for Development: ####
* IDE: 
```
- Download python (https://www.python.org/downloads/)
- Install IDE support compile Python: VSCode, Pycharm, Sublime Text, ...
```
* Extension for IDE:
```
+ For VSCode, you need install some extension to support code python:
    . HTML CSS Support
    . Python
    . Remote Development
  + For IDE different: Search more information on google
```
* To run:
```
- OPEN TERMINAL:
  + cd crawler
  + pip install requests // (pip3 install requests)
  + pip install beautifulsoup4 // (pip3 install beautifullsoup4) 
- OPEN getData.py file:
  ( * If you no need save data into database:
      . Comment some function  use to connect database: Eg. insertData..(),...
      . No need to worry about connecting and dealing with databases.
  )
  - Replace current available "url" variable in file with the one url address you want.

  - Reopen terminal and run with: python getData.py
```
