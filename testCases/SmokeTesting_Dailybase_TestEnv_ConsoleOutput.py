import os
import time
from telnetlib import EC
import openpyxl
import pytest
import softest
from colorama import Fore, Back, Style
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.custom_Logger import custLogger
import datetime

@pytest.mark.usefixtures("setup_and_teardown",scope="class")
class Test_verifyHomePage(softest.TestCase):
    log = custLogger().getLogs()

    def test_TitleAndLogo(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.ID, "cms-login-userId").send_keys("PDPOC_VAL")
        self.driver.find_element(By.ID, "cms-login-password").send_keys("Crowd_dev_112723")
        # self.driver.find_element(By.ID, "cms-login-userId").send_keys("POC_DEV")
        # self.driver.find_element(By.ID, "cms-login-password").send_keys("Contractor_112723")
        self.driver.find_element(By.ID, "cms-label-tc").click()
        self.driver.find_element(By.ID, "cms-login-submit").click()
        #self.wait.until(EC.element_to_be_clickable(By.ID,"cms-send-push-phone" )).click()
        # self.driver.find_element(By.ID, "cms-send-push-phone").click()

    #Click on CROWD
        self.driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']").click()
        #self.driver.find_element(By.XPATH, "//div[@id='cms-crowd-tile-selected']").click()

        element_App = self.driver.find_element(By.LINK_TEXT, "Application")
        self.driver.execute_script("arguments[0].click()", element_App)


    # using now() to get current time
        combined = datetime.datetime.now()
        #formatted_combined = combined.strftime("%m/%d/%Y %I:%M:%p")
        formatted_combined = combined.strftime("%B %d, %Y %H:%M:%S")
        print('\n')
        print(Back.LIGHTYELLOW_EX)
        print(Fore.RED+'  CROWD - SMOKE TESTING RESULTS FOR TEST ENV ON ', formatted_combined )
        print(Style.RESET_ALL)
        # workbook = openpyxl.load_workbook("..\ExcelFiles\Book2.xlsx")
        # sheet = workbook['Sheet1']
        print(Fore.BLUE +'\n******************** Verifying Title(s) & Logo(s) of CROWD Application ********************')
        print(Style.RESET_ALL)

    # Verifying  Main Logo :
        #expected_Logo = "CMS.gov| My Enterprise Portal is displayed"
        actual_Logo = self.driver.find_element(By.XPATH, "//em[@id='cms-homepage-header-logo-unauth']")
        print(actual_Logo.is_displayed())
        print(Fore.GREEN  + 'Main Logo:-', end='')
        print(Style.RESET_ALL)
        print("     'CMS.Gov|My Enterprise Portal' Logo is displayed")

    # Verifying Title CMS Enterprise Portal - My Portal"
        expected_title_main = "CMS Enterprise Portal - My Portal"
        self.soft_assert(self.assertEqual,self.driver.title,expected_title_main)
        if self.driver.title == expected_title_main:
            print(Fore.GREEN +'Title Verified:-', end='')
            print(Style.RESET_ALL)
            print("     Expected Title:- " + expected_title_main)
            print("     Actual Title:- " + self.driver.title)
            # sheet.cell(row=5, column=2).value = "Pass"
            # workbook.save("..\ExcelFiles\Book2.xlsx")
        else:
            # self.log.info("Assertion Failed")
            print("Main Title not match")

        time.sleep(10)

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//object[@id='obj_crowd_wab_application']"))

    # Verify 'CROWD' Logo// Once found NoSuchElementException
        image = self.driver.find_element(By.XPATH,"//div[@class ='cms-logo']")
        print(image.is_displayed())
        print(Fore.GREEN + 'CROWD Logo:-' , end='')
        print(Style.RESET_ALL)
        print("     'CROWD' Logo is displayed")

    # Verify Title
        expected_title = "CmsCrowdUi"
        actual_title = self.driver.execute_script('return document.title')
        self.soft_assert(self.assertEqual, actual_title, expected_title)
        if actual_title == expected_title:
           print(Fore.GREEN + ' Title Verified:-', end='')
           print(Style.RESET_ALL)
           print("     Expected Title:- " + expected_title)
           print("     Actual Title:- " + actual_title)
        else:
            # self.log.info("Assertion Failed")
            print("Title not match")

# Verifying  Text Welcome to CROWD
        #self.log.info("Verifying 'Welcome to CROWD' text")

        #wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='homeTitleRow']/h1")))
        actual_Text= wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='homeTitleRow']/h1"))).text
        expected_Text ="Welcome to CROWD"
        #actual_Text=self.driver.find_element(By.XPATH, "//div[@id='homeTitleRow']/h1").text
        self.soft_assert(self.assertEqual, actual_Text, expected_Text)
        if actual_Text == expected_Text:
           # self.log.info("Assertion Passed")
            print(Fore.GREEN + 'Text Verified :-', end='')
            print(Style.RESET_ALL)
            print("     Expected Text:- " + expected_Text)
            print("     Actual Text:- " + actual_Text)

        else:
           #self.log.info("Assertion Faileded")
           print("Welcome To Crowd test does not match")

# Verifying CROWD Summary
        # self.log.info("Verifying 'Welcome to CROWD' text")
        expected_Summary = "The Contractor Reporting of Operational and Workload Data (CROWD) application provides CMS automated capabilities for monitoring and analyzing data relating to the Medicare contractor's on-going operational activities. The application contains workload reporting capabilities that allow the data to be used for estimating budgets, defining operating problems, comparing performance among contractors, and determining national workload trends."
        actual_Summary = self.driver.find_element(By.XPATH, "//p[@id='crowd_summary']").text
        self.soft_assert(self.assertEqual, actual_Summary, expected_Summary)
        if actual_Summary == expected_Summary:
            print(Fore.GREEN + 'Verified CROWD Summary:-', end='')
            print(Style.RESET_ALL)
            print("     Expected Summary:- " + expected_Summary)
            print("     Actual Summary:- " + actual_Summary)
        else:
             # self.log.info("Assertion Faileded")
                print("CROWD Summary does not match")
        self.driver.get_screenshot_as_file("..\Screenshots\Main Page.png")
############################## Verifying File Submission (File Upload & File Status) ######################################
        print(Fore.BLUE + "\n******************** Verifying File Submission - File Upload/ File Status Page ********************")
        print(Style.RESET_ALL)
        click_on_fileSubmissionLink = self.driver.find_element(By.XPATH,
                                                     "//span[normalize-space()='File Submission']")
        self.driver.execute_script("arguments[0].click();", click_on_fileSubmissionLink)

        self.driver.refresh()
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//object[@id='obj_crowd_wab_application']"))

        click_on_fileSubmissionLink = self.driver.find_element(By.XPATH,
                                                       "//span[normalize-space()='File Submission']")
        self.driver.execute_script("arguments[0].click();", click_on_fileSubmissionLink)

#Click on Upload link
        click_on_uploadLink = self.driver.find_element(By.XPATH,
                                                       "//span[normalize-space()='File Upload']")
        self.driver.execute_script("arguments[0].click();",click_on_uploadLink)

        click_on_iconButton = self.driver.find_element(By.XPATH,
                                                       "//mat-icon[@type='button']")
        self.driver.execute_script("arguments[0].click();", click_on_iconButton)
        time.sleep(5)
#Verifying File Selection Instructions
        expected_Heading = "File Selection Instructions"
        actual_Heading= wait.until(EC.visibility_of_element_located((By.XPATH, "//app-info-modal[@class='ng-star-inserted']/div/span/h1"))).text
        #actual_Heading = self.driver.find_element(By.XPATH, "//app-info-modal[@class='ng-star-inserted']/div/span/h1").text
        self.soft_assert(self.assertEqual, expected_Heading, actual_Heading)
        if  actual_Heading == expected_Heading:
            print(Fore.GREEN + "Verified 'File Selection Instructions':-", end='')
            print(Style.RESET_ALL)
            #print("     Expected Heading:- " + expected_Heading + " && Actual Heading:- " + actual_Heading)
        else:
            # self.log.info("Assertion Failed")
            print("Heading does not match")

        #fileSelectionInstruction1 = self.driver.find_element(By.XPATH, "//div[@id='submissionInfo']/div[2]").text # Need to change as path has changed on 12/28
        expected_FileInsturctions = "Please use the ‘Browse’ button to locate and select a text (*.txt) file for upload. The file size must be greater than 0 bytes, but not more than 500 KB, and the file name can only contain the following valid characters:"
        actual_FileInstructions = self.driver.find_element(By.XPATH, "//app-info-modal[@class='ng-star-inserted']/div/div[1]").text
        self.soft_assert(self.assertEqual, expected_FileInsturctions, actual_FileInstructions)
        if actual_FileInstructions == expected_FileInsturctions:
            print("    " + actual_FileInstructions)
        else:
            print("File Instructions does not match")

        list_items = self.driver.find_elements(By.XPATH, "//app-info-modal[@class='ng-star-inserted']/div/ul/li")

        for list_item in list_items:
            print("     "+list_item.text)

        click_on_closeButton = self.driver.find_element(By.XPATH, "//mat-icon[normalize-space()='close']")

        self.driver.execute_script("arguments[0].click();", click_on_closeButton)

        self.driver.get_screenshot_as_file("..\Screenshots\File Upload Page.png")
# Clicking on Browse button
        browse_Button = self.driver.find_element(By.XPATH,
                                               "//span[normalize-space()='Browse']")
        self.driver.execute_script("arguments[0].click();", browse_Button)
# Loading a file
        file = self.driver.find_element(By.XPATH, "//input[@type='file']")

        #For file upload from local drive
        #file.send_keys("C:\Data_Automation\Form_Q\CONTRACTOR_MAPPING_VALIDATION_BAD_WORKLOAD_FORM_Q.txt")

        #for file upload from project directory
        #os.path.abspath("..\File_Tobe_Uploaded\CONTRACTOR_MAPPING_VALIDATION_BAD_BSI_FORM_Q.txt")
        file.send_keys(os.path.abspath(r"..\File_Tobe_Uploaded\CONTRACTOR_MAPPING_VALIDATION_BAD_BSI_FORM_Q.txt"))

#Entering a comment
        comment_Inputbox = self.driver.find_element(By.XPATH, "//textarea[@id='comment']")
        comment_Tobe_Entered = "BAD_WORKLOAD"
        comment_Inputbox.send_keys(comment_Tobe_Entered)

# Click on Submit button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

#Fetch uploaded file name
        uploadedFile =self.driver.find_element(By.XPATH, "//div[@class ='submissionSubText']/div/b").text
        a, b = uploadedFile.split(' ', 1)

        uploadedFilename = a
        uploaded_Filename = uploadedFilename.replace("'", "")
        print(Style.RESET_ALL)
# Click on Status
        click_on_Status = self.driver.find_element(By.XPATH,
                                                   "//a[normalize-space()='Status']")
        self.driver.execute_script("arguments[0].click();", click_on_Status)
        time.sleep(7)
#Click on Refresh button on Status page
        click_on_Refresh =wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='refreshButton calltoAction']/mat-icon")))
        #click_on_Refresh = self.driver.find_element(By.XPATH,
                                                  # "//button[@class='refreshButton calltoAction']/mat-icon")
        self.driver.execute_script("arguments[0].click();", click_on_Refresh)

        self.driver.execute_script("arguments[0].click();", click_on_Refresh)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@title='File status Table']/tbody /tr/td")))

        filename_displayed_onStatus = self.driver.find_element(By.XPATH, "//table[@title='File status Table']/tbody /tr/td").text
        self.soft_assert(self.assertEqual, filename_displayed_onStatus, uploaded_Filename)
        if uploaded_Filename == filename_displayed_onStatus:
            print(Fore.GREEN +'Verified Uploaded File:-',end='' )
            print(Style.RESET_ALL)
            print("     Uploaded Filename:- " + uploaded_Filename )
            print("     Uploaded Filename Displayed On Status:- " + filename_displayed_onStatus)
        else:
            print("false")
#Verify Comment on status page
        # click_on_Refresh = self.driver.find_element(By.XPATH,
        #                                             "//button[@class='refreshButton calltoAction']/mat-icon")
        # self.driver.execute_script("arguments[0].click();", click_on_Refresh)
        comment_DisplayedOnStatus = self.driver.find_element(By.XPATH, "//span[@class='viewComment']").text
        self.soft_assert(self.assertEqual, comment_Tobe_Entered, comment_DisplayedOnStatus)
        if comment_Tobe_Entered == comment_DisplayedOnStatus:

            print(Fore.GREEN +'Verified Comment:-', end='')
            print(Style.RESET_ALL)
            print("     Entered Comment:- " + comment_Tobe_Entered )
            print("     Comment Displayed On Status:- " + comment_DisplayedOnStatus )
        else:
            # self.log.info("Assertion Failed")
            print("Comment does not match")
#Verify Timestamp
        timeStamp_DisplayedOnStatus = self.driver.find_element(By.XPATH, "//table[@title='File status Table']/tbody/tr/td[3]").text
        #print(timeStamp_DisplayedOnStatus)
        now =datetime.datetime.now()
        currentTime = now.strftime("%m/%d/%Y %I:%M %p")
        self.soft_assert(self.assertEqual, timeStamp_DisplayedOnStatus, currentTime)
        if timeStamp_DisplayedOnStatus == currentTime:
            print(Fore.GREEN + 'Verified Uploaded File Timing:-', end='')
            print(Style.RESET_ALL)
            print("     File Uploaded On:- " + currentTime)
            print("     Timestamp on File Status Page:- " + timeStamp_DisplayedOnStatus)
        else:
            print("false")

        self.driver.get_screenshot_as_file("..\Screenshots\File Status Page.png")
############################################# Verifying Dashboard ###################################################
        print(Fore.BLUE +"\n************************* Verifying Dashboard Page *************************")
        print(Style.RESET_ALL)
        dashboardLink = self.driver.find_element(By.XPATH,
                                                "//span[normalize-space()='Dashboards']")
        self.driver.execute_script("arguments[0].click();", dashboardLink)

        # dash_Text = self.driver.find_element(By.XPATH, "//span[@class='anchor-format grey-text ng-star-inserted']").text
        # print("Displayed text on Dashboards page:- " + dash_Text)
        dashboardID = self.driver.find_element(By.XPATH, "//table[@title='Dashboard Table']/tbody/tr/td[1]").text
        dashboardName = self.driver.find_element(By.XPATH, "//table[@title='Dashboard Table']/tbody/tr/td[2]").text
        dashboardDescription = self.driver.find_element(By.XPATH, "//table[@title='Dashboard Table']/tbody/tr/td[3]").text
        print(Fore.GREEN + "THE FIRST RECORD DISPLAYED ON  'DASHBOARD' TABLE IS:- ", end='')
        print(Style.RESET_ALL)
        print("     Dashboard ID:- " + dashboardID + "   Dashboard Name:- " + dashboardName + "   Dashboard Description:- " + dashboardDescription)
        #time.sleep(5)
        parent_window_id= self.driver.current_window_handle

        click_on_firstLink_Dashboard  = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@title='Dashboard Table']/tbody/tr/td[2]/a")))
        self.driver.execute_script("arguments[0].click();", click_on_firstLink_Dashboard)

        windows= self.driver.window_handles

        for w in windows:
            self.driver.switch_to.window(w)
            time.sleep(6)
            expected_Title = "B01. MicroStrategy"
            actual_Title = self.driver.title
            if actual_Title==expected_Title:
                print(Fore.GREEN+'Verified MicroStrategy Page Title:-', end='')
                print(Style.RESET_ALL)
                print("     Expected Title:- " + expected_Title)
                print("     Actual Title:- " + actual_Title)
            # if self.driver.title.__eq__("B01. MicroStrategy"):
            #     print(self.driver.title)
                #print(self.driver.current_window_handle)
                self.driver.close()
                break

        self.driver.switch_to.window(parent_window_id)
############################## Verifying Form Page #####################################
        print(Fore.BLUE + "\n************************* Verifying Form Page *************************")
        print(Style.RESET_ALL)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//object[@id='obj_crowd_wab_application']"))
        time.sleep(5)
        #forms_Link = self.driver.find_element(By.XPATH,"//span[normalize-space()='Forms']")
        forms_Link = self.driver.find_element(By.XPATH, "//span[@class='list-item-label'][normalize-space()='Forms']")
        self.driver.execute_script("arguments[0].click();", forms_Link)
        time.sleep(15)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//main[@id='main-forms']/table/tbody/tr[1]/td[1]")))
        # Need to be change 2/2/24
        # form= self.driver.find_element(By.XPATH, "//table[@title='Forms Table']/tbody/tr[1]/td[1]").text
        # formType = self.driver.find_element(By.XPATH, "//table[@title='Forms Table']/tbody[1]/tr/td[2]").text
        # formName=  self.driver.find_element(By.XPATH, "//table[@title='Forms Table']/tbody/tr[1]/td[3]").text

        form = self.driver.find_element(By.XPATH, "//main[@id='main-forms']/table/tbody/tr[1]/td[1]").text
        formType = self.driver.find_element(By.XPATH, "//main[@id='main-forms']/table/tbody/tr[1]/td[2]").text
        formName = self.driver.find_element(By.XPATH, "//main[@id='main-forms']/table/tbody/tr[1]/td[3]").text

        print(Fore.GREEN + "THE FIRST RECORD DISPLAYED ON  'FORM' TABLE IS:- ", end='')
        print(Style.RESET_ALL)
        print("     Form:- " + form + "  Form Type:- " + formType + "  Form Name:- " + formName)
        #time.sleep(7)
        parent_window_id = self.driver.current_window_handle

        #click_on_firstLink_Forms = self.driver.find_element(By.XPATH,
                                           #  "//main[@id='main-forms']/table[@title='Forms Table']/tbody/tr[2]/td[3]/a")
        click_on_firstLink_Forms = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//main[@id='main-forms']/table/tbody/tr[2]/td[3]/a")))
        self.driver.execute_script("arguments[0].click();", click_on_firstLink_Forms)

        windows = self.driver.window_handles

        for w in windows:
            self.driver.switch_to.window(w)
            time.sleep(15)
            expected_Title = "(FORM 7 - PART A) APPEALS ACTIVITY (CMS-2592). MicroStrategy"
            actual_Title = self.driver.title
            if actual_Title==expected_Title:
                print(Fore.GREEN + 'Verified MicroStrategy Page Title:- ', end='')
                print(Style.RESET_ALL)
                print("     Expected Title:- "+ expected_Title)
                print("     Actual Title:- " + actual_Title )
                #print(self.driver.current_window_handle)
                self.driver.close()
                break
        self.driver.switch_to.window(parent_window_id)
        #print(self.driver.current_window_handle)

# ############################## Verifying Reports Page #####################################
        print(Fore.BLUE + "\n************************* Verifying Reports Page *************************")
        print(Style.RESET_ALL)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//object[@id='obj_crowd_wab_application']"))
        #time.sleep(3)

        report_Link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Reports']")))
        self.driver.execute_script("arguments[0].click();", report_Link)

        # reports_Link = self.driver.find_element(By.XPATH,
        #                                          "//span[normalize-space()='Reports']")
        # self.driver.execute_script("arguments[0].click();", reports_Link)
        time.sleep(5)

        reportID = self.driver.find_element(By.XPATH, "//table[@title='Reports Table']/tbody/tr/td[1]").text # WebDriver Exception
        reportName = self.driver.find_element(By.XPATH, "//table[@title='Reports Table']/tbody/tr/td[2]").text
        reportDescription = self.driver.find_element(By.XPATH, "//table[@title='Reports Table']/tbody/tr/td[3]").text

        print(Fore.GREEN + "THE FIRST RECORD DISPLAYED ON  'REPORT' TABLE IS:- ", end='')
        print(Style.RESET_ALL)
        print("     Report ID:- " + reportID + "   Report Name:- " + reportName + "   Report Description:- " + reportDescription)

############################## Verifying News Page #####################################
        print(Fore.BLUE + "\n************************* Verifying News Page *************************")
        print(Style.RESET_ALL)

        #Path changed found on 5th Jan news_Link = self.driver.find_element(By.XPATH,
                                                 #"//span[@class='mat-list-item-content'][normalize-space()='News']")
        #self.driver.execute_script("arguments[0].click();", news_Link)

        news_Link = self.driver.find_element(By.XPATH,
                                                 "//span[normalize-space()='News']")
        self.driver.execute_script("arguments[0].click();", news_Link)
        #time.sleep
        print(Fore.GREEN + "NEWS for Year 2020:-")
        print(Style.RESET_ALL)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='2020']")))

        year2020 = self.driver.find_element(By.XPATH,
                                             "//h2[normalize-space()='2020']")
        self.driver.execute_script("arguments[0].click();", year2020)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='blue'][normalize-space()='Attn: Medicare Contractors'])[1]")))
        #time.sleep(6)

       # self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//object[@id='obj_crowd_wab_application']"))
        line1 =self.driver.find_element(By.XPATH, " (//span[@class='blue'][normalize-space()='Attn: Medicare Contractors'])[1]").text

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[normalize-space()='| February 12, 2020']")))
        #time.sleep(6)

        line2 = self.driver.find_element(By.XPATH,
                                         "//span[normalize-space()='| February 12, 2020']").text

        print(line1 + ' ' + line2)

        #line3 =self.driver.find_element(By.XPATH, "//span[normalize-space()='| December 23rd, 2021']").text

        line3 = self.driver.find_element(By.XPATH, "//p[contains(text(),'Although CR 11353 (Supplier Specialty Code D5) for')]").text
        print(line3)
        # line2 = self.driver.find_element(By.XPATH,
        #                                  " //span[@class='ng-star-inserted'][normalize-space()='| February 12, 2020'])[1]").text
        self.assert_all()
















