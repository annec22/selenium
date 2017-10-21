from selenium import webdriver

print "Opening Chrome..."
driver_chrome = webdriver.Chrome()
print "Visiting Tumblr.."
driver_chrome.get("https://www.tumblr.com/")
print "Quitting Chrome browser.."
driver_chrome.quit()
print "Done."

print "Opening Firefox..."
driver_firefox = webdriver.Firefox()
print "Visiting Tumblr.."
driver_firefox.get("https://www.tumblr.com/")
print "Quitting Firefox browser.."
driver_firefox.quit()
print "Done."

print "Opening IE..."
dirver_ie = webdriver.Ie()
print "Visiting Tumblr.."
dirver_ie.get("https://www.tumblr.com/")
print "Quitting IE browser.."
dirver_ie.quit()
print "Done."

print "Opening Opera..."
driver_opera = webdriver.Opera()
print "Visiting Tumblr.."
driver_opera.get("https://www.tumblr.com/")
print "Quitting Opera browser.."
driver_opera.quit()
print "Done."
