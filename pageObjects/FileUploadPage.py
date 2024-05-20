import os
import time
import softest
from selenium.common import TimeoutException, InvalidArgumentException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_Driver import BaseDriver

class FileUploadPage(BaseDriver):
    ######################################## LOCATORS ###############################
    btnFileSubmission_xpath = "//span[normalize-space()='File Submission']"
    btnfileUpload_xpath = "//a[normalize-space()='File Upload']"
    titleFileUpload_xpath = "//h1[@id='focus-main-content']"

    ### Accepted File
    fileBrowse_xpath ="//input[@type='file']"
    commentBox_xpath ="//textarea[@id='comment']"
    btnSubmit_xpath="//button[@type='submit']"
    btnfileStatus_xpath = "//a[normalize-space()='File Status']"
    acceptedMsg_xpath="//span[contains(text(),'ACCEPTED')][1]"

    #Failed Message
    btnFailed_linkText = "FAILED"
    status_failedMessage_xpath="//span[normalize-space()='Status: FAILED']"
    #status_failedMessage_xpath = "//div[@class='headerRow']/h2/span"  #'Status: FAILED'
    status_formName_xpath ="//div[@class='container']/mat-card/h3"
    status_prevalidationMessage_xpath = "//h3[@class='underline-text ng-star-inserted']"
    failed_note_xpath ="//b[contains(text(),'Note: The file failed Pre-Validation. Please corre')]"

    #Rejected Message
    btnRejected_linkText = "REJECTED"
    status_rejectedText_xpath="//span[normalize-space()='Status: REJECTED']"
    status_SeriousError_xpath="//h3[normalize-space()='SERIOUS ERROR(S)']"
    btnRequestOverride_xpath ="//button[@id='requestOverrideButton']//span[@class='mat-mdc-button-touch-target']"
    rejected_note_xpath ="//b[contains(text(),'Note: The deadline to request an override for the ')]"
    noEleigible_rejected_note_xpath = "//b[contains(text(),'Note: The file is no longer eligible for an overri')]"
    #### Search
    input_Searchbox_xpath = "//input[@id='mat-input-0']"  # Inputbox
    iconSearch_xpath = "//mat-icon[normalize-space()='search']"

    ### Override Accepted
    btnOverrideAccepted_linkText = "ACCEPTED (WITH OVERRIDE)"

    def __init__(self,
                 driver):  # creating constructor init,and driver is an argument and why we are creating when we create init it will be called whenever object of the class will be created  # and passing argument as driver so same driver can be used in test calss
        super().__init__(driver)
        self.driver = driver

    def click_OnFileUpload(self): # Clicking on Fie Submission
        time.sleep(6)
        # fileSubmission = WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btnFileSubmission_xpath)))
        # fileSubmission.click()
        self.driver.find_element(By.XPATH, self.btnFileSubmission_xpath).click()
        time.sleep(7)
        #fileStatus = self.driver.find_element(By.XPATH, self.btnfileStatus_xpath)
        self.driver.find_element(By.XPATH, self.btnfileUpload_xpath).click()
    def click_OnFileSubmission(self):
        time.sleep(7)
        return self.driver.find_element(By.XPATH, self.btnFileSubmission_xpath).click()
    # def click_OnFileUpload(self):
    #     time.sleep(6)
    #     return self.driver.find_element(By.XPATH, self.btnfileUpload_xpath).click()
    def click_OnFileStatusPage(self):
        return self.driver.find_element(By.XPATH, self.btnfileStatus_xpath).click()
    ######## Verify FileUpload Page Title  #####
    def verify_titleOfFileUploadPage(self):
        print("The status of 'File Upload' Page is:-")
        print(self.driver.find_element(By.XPATH, self.titleFileUpload_xpath).text)
        return self.driver.find_element(By.XPATH, self.titleFileUpload_xpath).text
    def fileUpload_withAcceptedStatus(self):
        time.sleep(6)
        try:
            fileBrowse = self.driver.find_element(By.XPATH, self.fileBrowse_xpath)
            os.path.abspath("r..\File_Tobe_Upload\Valid_FormS.txt")
            fileBrowse.send_keys(os.path.abspath(r"..\File_Tobe_Upload\Valid_FormS.txt"))
        except TimeoutException as e:
            print(e)
    def fileUpload_withFailedStatus(self):
        time.sleep(6)
        try:
            fileBrowse = self.driver.find_element(By.XPATH, self.fileBrowse_xpath)
            os.path.abspath("r..\File_Tobe_Upload\FORMQ_NoAccess_JuriCAA.txt")
            fileBrowse.send_keys(os.path.abspath(r"..\File_Tobe_Upload\FORMQ_NoAccess_JuriCAA.txt"))
        except InvalidArgumentException as e:
            #except TimeoutException as e:
            print(e)
    def fileUpload_withRejectedStatus(self):
        time.sleep(6)
        try:
            fileBrowse = self.driver.find_element(By.XPATH, self.fileBrowse_xpath)
            os.path.abspath("r..\File_Tobe_Upload\VALIDATION_BAD_L2_C1_FORM_Q.txt")
            fileBrowse.send_keys(os.path.abspath(r"..\File_Tobe_Upload\VALIDATION_BAD_L2_C1_FORM_Q.txt"))
        except TimeoutException as e:
            print(e)
    def enterComment(self):
        comment_Inputbox = self.driver.find_element(By.XPATH, self.commentBox_xpath)
        comment_Tobe_Entered = "Status Testing"
        comment_Inputbox.send_keys(comment_Tobe_Entered)

    def click_OnSubmitButton(self):
        click_on_Submit = self.driver.find_element(By.XPATH, self.btnSubmit_xpath)
        return self.driver.execute_script("arguments[0].click();", click_on_Submit)
    def click_OnSearchbox(self, filename):
        time.sleep(6)
        self.driver.find_element(By.XPATH,self.input_Searchbox_xpath).send_keys(filename)
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.iconSearch_xpath).click()
    def click_OnFAILED(self):
        return self.driver.find_element(By.LINK_TEXT, self.btnFailed_linkText).click()
    def click_OnREJECTED(self):
        return self.driver.find_element(By.LINK_TEXT, self.btnRejected_linkText).click()

    def click_OnAcceptedWithOverrideButton(self):
        return self.driver.find_element(By.LINK_TEXT, self.btnOverrideAccepted_linkText).click()
    def verify_AcceptedMessage(self):
        print("The status of file is 'ACCEPTED' on File Status Page.")
        print(self.driver.find_element(By.XPATH, self.acceptedMsg_xpath).text)
        return self.driver.find_element(By.XPATH, self.acceptedMsg_xpath).text
    def verify_failedMessage(self):
        print("The status of file is on 'File Status Page'.")
        print(self.driver.find_element(By.XPATH, self.status_failedMessage_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_failedMessage_xpath).text
    def verify_formName(self):
        print(self.driver.find_element(By.XPATH, self.status_formName_xpath).text)
        formName =self.driver.find_element(By.XPATH, self.status_formName_xpath).text
        a,b,c,d,e = formName.split()
        #print(a) print(b) print(c) print(d) print(e)
        return a


    def verify_preValidationMessage(self):
        print(self.driver.find_element(By.XPATH, self.status_prevalidationMessage_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_prevalidationMessage_xpath).text
    def verify_Note(self):
        print(self.driver.find_element(By.XPATH, self.failed_note_xpath).text)
        return self.driver.find_element(By.XPATH, self.failed_note_xpath).text
    def verify_rejectedMessage(self):
        print("The status of file is on 'File Status Page'.")
        print(self.driver.find_element(By.XPATH, self.status_rejectedText_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_rejectedText_xpath).text
    def verify_seriousErrorMessage(self):
        print(self.driver.find_element(By.XPATH, self.status_SeriousError_xpath).text)
        return self.driver.find_element(By.XPATH, self.status_SeriousError_xpath).text
    def verify_rejectedNote(self):
        print(self.driver.find_element(By.XPATH, self.rejected_note_xpath).text)
        return self.driver.find_element(By.XPATH, self.rejected_note_xpath).text
    def verify_noEleigible_rejectedNote(self):
        print(self.driver.find_element(By.XPATH, self.noEleigible_rejected_note_xpath).text)
        return self.driver.find_element(By.XPATH, self.noEleigible_rejected_note_xpath).text
    def verify_RequestOverrideEnabled(self):
        #print(self.driver.find_element(By.XPATH, self.noEleigible_rejected_note_xpath).text)
        return self.driver.find_element(By.XPATH, self.btnRequestOverride_xpath)

    def verify_AcceptedOverride(self):
        return self.driver.find_element(By.XPATH, self.btnOverrideAccepted_linkText).click()


