from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()