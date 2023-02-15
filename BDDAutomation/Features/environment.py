from selenium.webdriver import Chrome

def before_all(context):
    path = 'C:\\Users\\rajesh.bajaj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)

def after_all(context):
    context.driver.close()

#before_feature(context,feature),after_feature(context,feature)
#before_scenario(context,scenario),after_scenario(context,scenario)
#before_scenario(context,tag),after_scenario(context,tag)
#before_scenario(context,step),after_scenario(context,step)

#behave -f allure_behave.formatter:AllureFormatter -o C:\Users\rajesh.bajaj\Desktop\BDDAutomation
#allure serve C:\Users\rajesh.bajaj\Desktop\BDDAutomation on command prompt to generate the report in HTML format

# Push ENdToEndAutomation code to Github
# After installing Jenkins , configure jenkins with GIT,PYthon and JAVA home path in Global tool configuration
# configure python bin and scripts path in envinronment variables
#
# Select Free Style project and select windows batch cmd prompt_toolkit
# set path=%PYTHON_HOME%;%PATH%
# rmdir /s /q Reports
# rmdir /s /q allure-reports
# Library/lib.bat
#
# select windows batch cmd command
#pytest --alluredir=./Reports TestCases
#

# post build actions
# under Allure reports .... give as Reports
