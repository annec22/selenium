from selenium import webdriver

print "Opening Chrome..."
driver_chrome = webdriver.Chrome()
print "Visiting Tumblr.."
driver_chrome.get("https://www.tumblr.com/")
print "Quitting Chrome browser.."
driver_chrome.quit()
print "Done."

