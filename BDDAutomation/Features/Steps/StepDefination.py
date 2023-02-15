from behave import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@given(u'User is on Registration page')
def step_impl(context):
    context.driver.get("http://www.theTestingWorld.com/testings")


@when(u'user enters username')
def step_impl(context):
    context.driver.find_element(By.NAME,"fld_username").send_keys("test")


@when(u'user enters password')
def step_impl(context):
    context.driver.find_element(By.NAME,"fld_password").send_keys("test")


@when(u'user clicks on Signup button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//input[@type="submit" and @value="Sign up"]').click()

@then(u'validate user logged in successfully')
def step_impl(context):
    print("Registered")
