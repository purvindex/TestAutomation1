import random
import string
import time
import softest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_Driver import BaseDriver

class FileStatusPage(BaseDriver):

    ################################# LOCATORS #####################################
    continue_Session_xpath ="//button[@id='cms-myprofile-session-xtend']"

    btnFileSubmission_xpath = "//span[normalize-space()='File Submission']"
    btnfileStatus_xpath = "//a[normalize-space()='File Status']"
    titleFileStatus_xpath = "//h1[@id='focus-main-content']"
    ##### Search Locators

    input_Searchbox_xpath = "//input[@id='mat-input-0']" # Inputbox
    iconSearch_xpath= "//mat-icon[normalize-space()='search']"
    btnRefresh_xpath ="//button[@class='refreshButton calltoAction']/mat-icon"
    tableData_xpath ="//tbody[@class='mdc-data-table__content']"

    ##### Ascending, Descending Order Locators
    sortButton_xpath = "//div[@class='tablePresentation']/table/thead/tr/th[1]/div/div/following-sibling::div"
    list_OfFilename_xpath ="//tbody[@class='mdc-data-table__content']/tr/td[3]"
    # list_afterSorting_xpath = "//tbody[@class='mdc-data-table__content']/tr/td[1]"
    # list_descSorting_xpath = "//tbody[@class='mdc-data-table__content']/tr/td[1]"
    txt_firstTimestamp_xpath ="//tbody[@class='mdc-data-table__content']/tr[1]/td[3]"

    ##### Pagination Locators
    btnPagination_xpath = "//div[@class='mat-mdc-paginator-range-actions']/button[@class='paginatorButton mat-custom-page ng-star-inserted']"
    txt_displayedRecords_xpath ="//div[@aria-label='Displaying records']"
    btn_Third_xpath ="//button[normalize - space() = '3']"
    btn_Previouspage_xpath = "//button[@aria-label='Previous page']//span[@class='mat-mdc-button-touch-target']"
    btn_Firstpage_xpath = "//button[@aria-label='First page']//span[@class='mat-mdc-button-touch-target']"
    btn_Nextpage_xpath = "//button[@aria-label='Next page']//span[@class='mat-mdc-button-touch-target']"
    btn_Lastpage_xpath = "//button[@aria-label='Last page']//span[@class='mat-mdc-button-touch-target']"


    link_AcceptedWithOverride_xpath ="//a[normalize - space() = 'ACCEPTED (WITH OVERRIDE)']"
    override_Formname_xpath ="//div[@class='cards']/div/mat-card/h3[1]"
    ####Comment ####
    btn_add_viewComments_xpath="//div[@class='comments']/a"
    btn_addFileComment_xpath="//button[normalize-space()='Add File Comment']"
    textArea_Inputbox_xapth = "//textarea[@id='comment']"
    btn_submitButton_xpath ="//span[normalize-space()='Submit']"
    #text_CommentdisplayedOnStatus_xpath = "//tbody[@class='mdc-data-table__content']/tr/td[3]"
    text_CommentAdded_xpath = "//div[contains(text(),'Your comment has been added to the file.')]"
    #status_column_xpath = "//tbody[@class='mdc-data-table__content']/tr[1]/td[4]"
    screenShot_fileComment ="//table[@title='File Comments']"



    form_Message_xpath="//(//h3[contains(text(),'FORM=E 002102 AKB')])[1]"
    #### Override Requested Messages
    status_overriderequested_xpath = "//span[normalize-space()='Status: OVERRIDE REQUESTED']"
    text_overrideSeriouserror_xpath = "//h3[normalize-space()='SERIOUS ERROR(S)']"
    #status_Note_xpath="//b[contains(text(),'Note: The file is pending an override decision by ')]"

    status_OR_xpath="//span[normalize-space()='Status: OVERRIDE REQUESTED']"
    status_rejected_xpath="//span[normalize-space()='Status: REJECTED']"
    status_seriousError_xpath= "//h3[normalize-space()='SERIOUS ERROR(S)']"
    status_ORNote_xpath = "//b[contains(text(),'Note: The file is pending an override decision by CMS')]"
    status_rejectedNote_xpath= "//b[contains(text(),'Note: The file is no longer eligible for an override request')]"

    btn_returnFileStatus_xpath="//span[@class='mdc-button__label']"

    def __init__(self, driver):  # creating constructor init,and driver is an argument and why we are creating when we create init it will be called whenever object of the class will be created  # and passing argument as driver so same driver can be used in test calss
        super().__init__(driver)
        self.driver = driver

    def click_OnFileStatus(self):
        time.sleep(6)
        # fileSubmission = WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btnFileSubmission_xpath)))
        # fileSubmission.click()

        self.driver.find_element(By.XPATH, self.btnFileSubmission_xpath).click()
        time.sleep(7)
        # fileStatus = WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btnfileStatus_xpath)))
        # fileStatus.click()
        #self.driver.execute_script("arguments[0].click();", fileStatus)
        self.driver.find_element(By.XPATH, self.btnfileStatus_xpath).click()
    ######## Verify FileStatus Page Title  #####
    def titleFileStatusPage(self):
        print("The status of File Status Page is:-")
        print(self.driver.find_element(By.XPATH, self.titleFileStatus_xpath).text)
        return self.driver.find_element(By.XPATH, self.titleFileStatus_xpath).text

    ######### Verify Search Funtionality  ######
    def click_OnSearchbox(self, status):
        return self.driver.find_element(By.XPATH,self.input_Searchbox_xpath).send_keys(status)
    def click_OnSearchIcon(self):
        return self.driver.find_element(By.XPATH,self.iconSearch_xpath).click()

    def verifyAcceptedOption(self):
        #table_xpath = self.driver.find_element(By.XPATH, "//tbody[@class='mdc-data-table__content']")
        table_xpath = self.driver.find_element(By.XPATH, self.tableData_xpath)
        table_rows = table_xpath.find_elements(By.TAG_NAME, "tr")
        i = 0
        j = 0
        for row in table_rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                status = col.text
                if "ACCEPTED" in status:
                    i += 1
                else:
                    j += 1
        # print("Total 'Accepted'status(word) in Table")
        # print(i)
        return i
    ###################### Sorting Functionalirty #############
    #def clickOnSortingButton(self):
    def original_List(self):
        list_elements_b4sort = self.driver.find_elements(By.XPATH, self.list_OfFilename_xpath)
        originalList = []
        for elements_b4 in list_elements_b4sort:
            submittedBy1 = elements_b4.text
            originalList.append(submittedBy1)
        print("Original List:-")
        print(originalList)
        return originalList

    def asce_OrderList(self):
        sortButton = self.driver.find_element(By.XPATH, self.sortButton_xpath)
        self.driver.execute_script("arguments[0].click();", sortButton)
        time.sleep(5)
        list_elements_afterSorting= self.driver.find_elements(By.XPATH, self.list_OfFilename_xpath )
        asc_Sorting_List = []
        for element in list_elements_afterSorting:
            submittedBy = element.text
            asc_Sorting_List.append(submittedBy)
        print("\n")
        print("Ascending Order List:-")
        print(asc_Sorting_List)
        return asc_Sorting_List

    def desc_OrederList(self):
        sortButton = self.driver.find_element(By.XPATH, self.sortButton_xpath)
        self.driver.execute_script("arguments[0].click();", sortButton)
        time.sleep(10)
        list_elements_desc_Sorting = self.driver.find_elements(By.XPATH, self.list_OfFilename_xpath)

        desc_Sorting_List = []
        for element in list_elements_desc_Sorting:
            submittedBy = element.text
            desc_Sorting_List.append(submittedBy)
        print("\n")
        print("Descnding Order List:-")
        print(desc_Sorting_List)
        return desc_Sorting_List

    def timeStamp_ofFistPage(self):
        return self.driver.find_element(By.XPATH, self.txt_firstTimestamp_xpath).text

    #### Clicking on last page from paginationButton and capture the time
    def click_OnLastButton(self):
        time.sleep(3)
        last_Button = self.driver.find_element(By.XPATH, "//button[@class='paginatorButton mat-custom-page ng-star-inserted'][5]")

        self.driver.execute_script("arguments[0].scrollIntoView();",  last_Button)
        time.sleep(3)
        last_Button.click()
    def timeStamp_ofLastPage(self):
        return self.driver.find_element(By.XPATH, self.txt_firstTimestamp_xpath).text


######################## Verify Status column Functionality #######################
    # 1. Override Request 2. Rejected
    def click_OnOverrideRequested(self):
        override_RequestedBtn = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[4]/a[1]")))
        #override_RequestedBtn.click()
        self.driver.execute_script("arguments[0].click();", override_RequestedBtn)

    def click_OnRejected(self):
        override_RejectedBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[4]/a[1]")))
        # override_RequestedBtn.click()
        self.driver.execute_script("arguments[0].click();", override_RejectedBtn)

    def verify_OR_Status(self):
        #print(self.driver.find_element(By.XPATH, self.status_OR_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_OR_xpath).text

        # return self.driver.find_element(By.CSS_SELECTOR, self.status_cssSelector).text
    def verify_Rejected_Status(self):
        #print(self.driver.find_element(By.XPATH, self.status_rejected_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_rejected_xpath).text

    def verify_SeriousError(self):
        #print(self.driver.find_element(By.XPATH, self.status_seriousError_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_seriousError_xpath).text

    def verify_statusORNote(self):
        #print(self.driver.find_element(By.XPATH, self.status_ORNote_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_ORNote_xpath).text

    def verify_rejectedORNote(self):
        #print(self.driver.find_element(By.XPATH, self.status_rejectedNote_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_rejectedNote_xpath).text

#################### View Comment Functionality #####################
    def click_OnFileComment(self):
        fileComment = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btn_add_viewComments_xpath)))
        self.driver.execute_script("arguments[0].click();", fileComment)
        #self.driver.find_element(By.XPATH, self.btn_viewComment_xpath).click()
    # def click_OnAddFileComment(self):
    #     addFileComment= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btn_addFileComment_xpath)))
    #     self.driver.execute_script("arguments[0].click();", addFileComment)
    def enter_singleLineLongComment(self):
        comment_Inputbox = self.driver.find_element(By.XPATH, self.textArea_Inputbox_xapth)
        comment_Tobe_Entered = "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567891234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
        comment_Inputbox.send_keys(comment_Tobe_Entered)

    def enter_RandomComment(self):
        i=1
        while i<5:
            addFileComment = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btn_addFileComment_xpath)))
            self.driver.execute_script("arguments[0].click();", addFileComment)
            comment_Inputbox = self.driver.find_element(By.XPATH, self.textArea_Inputbox_xapth)
            min_length = 2030
            max_length = 2050
            length = random.randint(min_length, max_length)

            str_characters = string.ascii_letters + string.digits + "!@#$%^&*"
            generated_string = ''.join(random.choice(str_characters) for _ in range(length))
            comment_Inputbox.send_keys(generated_string)
            #self.driver.find_element(By.XPATH, self.btn_returnFileStatus_xpath).click()
            #def click_OnSubmitButton(self):
            self.driver.find_element(By.XPATH, self.btn_submitButton_xpath).click()
            print(self.driver.find_element(By.XPATH, self.text_CommentAdded_xpath).text)
            i += 1
    def verify_comment(self):
        # FileComment_Section = self.driver.find_element(By.XPATH,self. screenShot_fileComment)
        # return FileComment_Section.screenshot("secotion.png")
        return self.driver.find_element(By.XPATH, self.text_CommentAdded_xpath).text


    ################### Verifying Sorting Functionality ##########################
    def paginationFunctionality(self):
        output_list = []
        path = "//div[@class='mat-mdc-paginator-range-actions']/button[@class='paginatorButton mat-custom-page ng-star-inserted']"
        i = 1
        while i < 5:
            time.sleep(3)
            element_path = path + str([i]) # Its a string
            element_path_xpath = self.driver.find_element(By.XPATH,element_path) # Converting into WebElement
            time.sleep(3)
            self.driver.execute_script("arguments[0].scrollIntoView();", element_path_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", element_path_xpath)
            time.sleep(3)
            displayed_Records = self.driver.find_element(By.XPATH, self.txt_displayedRecords_xpath).text
            print(displayed_Records)
            i += 1
            output_list.append(displayed_Records)
        print("\n")
        print("The Pagination buttons output:-")
        print(output_list) # ['1 – 10 of 1801', '11 – 20 of 1801', '21 – 30 of 1801', '31 – 40 of 1801']
        print("\n")
        #Sorting list         assert all([output_list[j] <= output_list[j + 1] for j in range(len(output_list) - 1)])

        actual_output_list =[]
        prev = '1'
        for ele in output_list:
            #print (ele)
            if prev not in ele:
                raise AssertionError("Element has not been clicked")
            prev = int(prev)+10
            prev = str(prev)
            actual_output_list.append(prev)


        # print("Verify Output list")  # These 2 lines verify the list
        # print(actual_output_list)  # it will print['11', '21', '31', '41']
        return actual_output_list

    def click_OnArrows(self):  # verification for assertion is pending
        actual_output_arrowsList = []
        previousPage = self.driver.find_element(By.XPATH,"//button[@aria-label='Previous page']//span[@class='mat-mdc-button-touch-target']")
        self.driver.execute_script("arguments[0].click();", previousPage)
        time.sleep(3)
        displayed_PrePage_Record = self.driver.find_element(By.XPATH, self.txt_displayedRecords_xpath).text
        print(displayed_PrePage_Record)
        actual_output_arrowsList.append(displayed_PrePage_Record)
        time.sleep(5)
        firstPage = self.driver.find_element(By.XPATH,
                                             "//button[@aria-label='First page']//span[@class='mat-mdc-button-touch-target']")
        self.driver.execute_script("arguments[0].click();", firstPage)
        time.sleep(5)
        displayed_FstPage_Record = self.driver.find_element(By.XPATH, self.txt_displayedRecords_xpath).text
        print(displayed_FstPage_Record)
        actual_output_arrowsList.append(displayed_FstPage_Record)

        time.sleep(5)
        nextPage=self.driver.find_element(By.XPATH,
                                 "//button[@aria-label='Next page']//span[@class='mat-mdc-button-touch-target']")
        self.driver.execute_script("arguments[0].click();", nextPage)
        time.sleep(5)
        displayed_NxtPage_Record = self.driver.find_element(By.XPATH, self.txt_displayedRecords_xpath).text
        print(displayed_NxtPage_Record)
        actual_output_arrowsList.append(displayed_NxtPage_Record)
        time.sleep(5)
        lastPage=self.driver.find_element(By.XPATH, "//button[@aria-label='Last page']//span[@class='mat-mdc-button-touch-target']")
        self.driver.execute_script("arguments[0].click();", lastPage)
        time.sleep(5)
        displayed_LastPage_Record = self.driver.find_element(By.XPATH, self.txt_displayedRecords_xpath).text
        print(displayed_LastPage_Record)
        actual_output_arrowsList.append(displayed_LastPage_Record)
        print("\n")
        print("The Pagination accordion buttons output:-")
        print(actual_output_arrowsList)
        return actual_output_arrowsList


    def click_OnRefreshButton(self):
        self.driver.find_element(By.XPATH, self.btnRefresh_xpath).click()
        self.driver.find_element(By.XPATH, self.btnRefresh_xpath).click()
        self.driver.find_element(By.XPATH, self.btnRefresh_xpath).click()












