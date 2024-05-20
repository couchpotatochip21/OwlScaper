from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import webbrowser
import time

import os
import glob

#!/////////////////////////////////////////////////////////////!
# DO NOT MODIFY ANYTHING ABOVE THIS LINE
#!/////////////////////////////////////////////////////////////!

#What Season to start on?
season = "01"

#What Episode to start on?
episode = "01"

# Do you want episodes to be reformatted (Jellyfin Compatible)? Ex: [theowlclub.net] s01e17 Wing It Like Witches (English) 1080p --> The Owl House S01E17
reformat = True

#!/////////////////////////////////////////////////////////////!
# DO NOT MODIFY ANYTHING BELOW THIS LINE
#!/////////////////////////////////////////////////////////////!

#list of known broken urls from the owlclub
blacklisturls = [r"https://193fffb1-toc-froppy.front.tmtnw.net/s/dl/IiudhOGRAl1b8yyNHQVc3Q/1716078900/%5Btheowlclub.net%5D%20s01e16%20Wing%20It%20Like%20Witches%20%28English%29%201080p.mp4",r"https://193fffb1-toc-froppy.front.tmtnw.net/s/dl/DjlKHDnyi7aPiZzPx3YqnQ/1716077400/%5Btheowlclub.net%5D%20s01e16%20Wing%20It%20Like%20Witches%20%28English%29%201080p.mp4", r"https://193fffb1-toc-froppy.front.tmtnw.net/s/dl/LL1C4kOlkEAizYFy9oThTA/1716077700/%5Btheowlclub.net%5D%20s01e16%20Wing%20It%20Like%20Witches%20%28English%29%201080p.mp4", r"https://193fffb1-toc-froppy.front.tmtnw.net/s/dl/AWnLN3tCBUN9jo-lJsGQJA/1716078600/%5Btheowlclub.net%5D%20s01e16%20Wing%20It%20Like%20Witches%20%28English%29%201080p.mp4"]

# Print instructions
print("--------------------------------------")

print("𓅓 OwlScraper V1.0 𓅓")

print("--------------------------------------")

print ("Follow the instructions here: LINKGOESHERE")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

print("WARNING: make sure you have created a folder in your Downloads titled: owlscraper")

print("WARNING: OwlScraper requires FireFox to be installed, if you have not installed it then please do so. (All users are shown this warning)")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

confirmvar = input("Once you have read the above hit ENTER")

# confirm that user understands what to do if they get ip banned

print("This program uses a proccess commonly known as web scraping. This can cause the site you are scraping to temporarily (rarely permanetly) ip ban you. This is characterized by an error saying something along the lines of: You are forbidden; or: access denied.")

confirmvar = input("Once you have read the above hit ENTER")

print("This script modifies files in the Downloads/owlscraper directory. You use this script at your own risk and it is always important to back up your files. The developers take no liability before, during, or after use.")

confirmvar = input("Once you have read the above hit ENTER")

print("owlscraper is under the Creative Commons Attribution NonCommercial 4.0 Liscence (CC BY-NC 4.0 Deed). To learn more about this liscence and what it means, click here: https://creativecommons.org/licenses/by-nc/4.0/ (this is simply a notice, you do not have to click here to continue the script).")

#   create webdriver object

# get the owlscraper directory
home = os.path.expanduser('~')
path = os.path.join(home, 'Downloads\owlscraper')

print("the following is the download path: " + path)

# set the default download directory

firefox_options = Options()
firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.dir", path)
firefox_options.set_preference("browser.download.useDownloadDir", True)
firefox_options.set_preference("pdfjs.disabled", True)
driver = webdriver.Firefox(options=firefox_options)


while True:
    # there is a glitch in the site that causes s1e12 to be labeled in the url as s1e11
    if "s{}e{}".format(season, episode) == "s01e12":
        driver.get("https://www.theowlclub.net/2020/07/s01e11-adventures-in-the-elements/")
    elif "s{}e{}".format(season, episode) == "s01e11":
        driver.get("https://www.theowlclub.net/2020/07/s01e11-sense-and-insensitivity/")
    elif "s{}e{}".format(season, episode) == "s04e01":
        print("OwlScaper has hit the end of the current number of seasons")
        exit()
    else:
        driver.get("https://www.theowlclub.net/s{}e{}/".format(season, episode))
        print("going to: " + driver.current_url + " for Season {} Episode{}".format(season, episode))
    
    if "No se ha encontrado la página que estás buscando. Debe haber sido eliminada, renombrada, o tal vez nunca existió. Puedes volver a la página de inicio a través del enlace." in driver.page_source:
            print("site has 404'd moving on to next season automatically")
            season = str(int(season)+1).zfill(2)
            onevar = str(1)
            episode = str(onevar.zfill(2))
            continue
    
    
    
    elements2 = driver.find_elements("tag name", "a")

    #print("test9")

    for e in elements2:
        if "toh-s{}e{}".format(season, episode) in str(e.get_attribute("onclick")):
            print(e.get_attribute('href'), e.get_attribute("onclick"))
            print("opening downloads menu")
            e.click()
            time.sleep(5)

    # get elements
    elements = driver.find_elements("tag name", "a")

    for e in elements:
        href = e.get_attribute('href')
        if "English" in href and not "PreRelease" in href and href not in blacklisturls:
            if "1080p" in href:
                #print("test")
                #print(href)

                hrefvar = href

                #open the download link
                #print("test2")
                driver.execute_script("window.open('');")   
                time.sleep(1)
                #print("test3")  
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)
                #print("test4")
                #driver.get(href)
                driver.execute_script(f"location.href='{href}';")
                time.sleep(5)
                #print("test5")
                #driver.switch_to.window(driver.window_handles[0])

                #driver.get(href)

                # Check for IP ban
                if driver.title != "":
                    if "This object does not exist or is not publicly accessible at this" in driver.page_source:
                        print("Failed to get S{}E{} at current link. Checking the site for other matching links and/or moving on.".format(season, episode))
                        #inputvar = input("Hit enter once you believe the ip ban to be gone")
                        time.sleep(1)
                        driver.close
                        time.sleep(1)
                        driver.switch_to.window(driver.window_handles[0])
                        continue
                        #driver.get(href)
                    if "This object does not exist or is not publicly accessible at this" in driver.page_source:
                        print("IP Ban still in effect. Please restart the script completely, after setting it to the next undownloaded episode.")
                        exit(1)
                
                #webbrowser.open_new(href)

                driver.switch_to.window(driver.window_handles[0])

                #get path to download
                home = os.path.expanduser('~')
                path = os.path.join(home, 'Downloads/owlscraper')

                # reset loading icon
                loadingindex = 0

                # declare dlfound
                dlfound = False

                #declare nautseconds
                nautseconds = 0

                # await download
                print("Waiting for download to start")
                while True and nautseconds < 200:

                    # set second counter
                    nautseconds += 1
                    time.sleep(0.1)

                    loadingindex += 1
                    loadingicons = r"|/-\\"
                    if loadingindex > 3:
                        loadingindex = 0
                    print(loadingicons[loadingindex], end='\r')
                    for fname in os.listdir(path):
                            if fname.endswith('.part'):
                                print("Download has started")
                                dlfound = True
                    if dlfound == True:
                        break

                #check if download is finished
                print("downloading, will proceed when download finishes....")
                
                # define the download wait function
                def dl_wait():
                    #tell the program to wait for the download to finish
                    dl_wait = True

                    #reset loading icon
                    loadingindex = 0

                    while dl_wait:
                        loadingindex += 1
                        loadingicons = r"|/-\\"
                        if loadingindex > 3:
                            loadingindex = 0
                        print(loadingicons[loadingindex], end='\r')
                        partfound = False
                        time.sleep(0.1)
                        #print("dir:" + ' '.join(os.listdir(path)))
                        for fname in os.listdir(path):
                            if fname.endswith('.part'):
                                partfound = True
                        if partfound == False:
                            dl_wait = False
                            break
                
                # call said function
                dl_wait()

                #double check and rerun the function if needed
                for filename in os.listdir(path):
                    if filename.endswith('.part'):
                        dl_wait()
                
                #Rename the file if specified in the params

                if reformat:            
                    print("finished downloading, now renaming")
                    time.sleep(2)
                    driver.close
                    #rename any files that start with [theowlclub.net]

                    home = os.path.expanduser('~')
                    path = os.path.join(home, 'Downloads/owlscraper')

                    path_a = path + "/*theowlclub.net*" # * means (match all), if specific format required then *.csv This will get all the files ending with .csv
                    list_of_files = glob.glob(path_a) 
                    latest_file = max(list_of_files, key=os.path.getctime)

                    new_file_name = str("The Owl House " + latest_file[53:59].upper() + ".mp4")
                    new_file = os.path.join(path, new_file_name)
                    print("renaming ", latest_file[53:59], "file: ", latest_file)
                    #prints a.txt which was latest file i created
                    os.rename(latest_file, new_file)
                else:
                    print("File was not renamed.")

                

    # print complete elements list
    #print(elements[120].get_attribute('href'))
    episode = str(int(episode)+1).zfill(2)


