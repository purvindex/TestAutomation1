import random
import time
from sys import exception
from xmlrpc.client import boolean

import softest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Base.base_Driver import BaseDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


#class FormPage(BaseDriver,softest.TestCase):
class FormPage(BaseDriver):
    btn_formPage_xpath = "//a[@aria-label='Forms navigates to forms page']"
    link_firstForm_xpath = "//tbody/tr[1]/td[3]/a[1]"
    contractorType_xpath ="//td[@class='mstrPromptTOCListItemTitle']//span[contains(text(),'Contractor Type(s)')]"
    arrow_xpath ="//div[@id='id_mstr138']//img[@title='Add']"
    # Form name & Serious Error
    status_formName_xpath = "//div[@class='container']/mat-card/h3"
    first_seriousError_xpath= "(//li[@class='ng-star-inserted'])[1]"

    #### Form Table
    formTable_totalRows_xpath = "//table[@title='Forms']/tbody/tr"
    formTable_totalCols_xpath = "//table[@title='Forms']/thead/tr/th"
    firstColumn_xpath ="//table[@title='Forms']/thead/tr/th[1]"

    calendar_Year_xpath="//div[@title='CALENDAR YEAR']"
    all_Years_xpath ="//div[@class='mstrBGIcon_ae mstrTreeViewNodeShortDisplay']"

    btn_rejected_xpath="//a[normalize-space()='REJECTED']"

    # FORM Microstrategye page
    icon_2023_xpath= "//div[contains(@title,'2023')]//img[contains(@class,'mstrTreeViewNodeConnector')]"
    icon_Year_Quarter_xpath= "//*[contains(text(),'YEAR-')]/preceding-sibling::img"
    year_Quarter_xpath="//*[contains(text(),'2023-')]"
    add_Arrow_xpath="//div[@id='id_mstr106']//img[@title='Add']"
    add_Arrow_FormF_xpath ="//div[@id='id_mstr95']//img[@title='Add']"
    run_Document_xpath= "//input[@id='id_mstr249']"
    run_Document_F_xpath ="//input[@id='id_mstr234']"
    bottom_Formname_xpath="//div[@class='mstrTextBoxInput']/input"

    icon_2022_xpath="//div[contains(text(),'2022')]"

    ##### MSTR Microstrategey page 2
    total_text = "//div[@class='mstrmojo-tabcontainer-tabs']/div/div/div/span"
    frm_version_xpath= "(//div[@class='mstrmojo-DocTextfield-valueNode'][normalize-space()='CROWD (2024.1.0)'])[1]" # CROWD (2024.1.0)
    form_Name_xpath= "//*[contains(text(), 'FORM')]"
    all_FormHeadings= "//div[@class='mstrmojo-DocTextfield-valueNode']"
    all_FormHeadingsNationalTotals ="//div[@class='mstrmojo-DocTextfield-valueNode']"

    national_Total_xpath="//div[@class='c']/div/span[2]"


    workload_dropdwn_xpath= "//select[@id='mstr91_select']"
    bsi_dropdwn_xpath= "//select[@id='mstr92_select']"

    ########## Export Functionality
    export_icon_xpath="//div[@class='mstrHamburger path']"
    export_option_xpath ="//span[normalize-space()='Export']"
    exportPDFOption_xpath="//div[@id='mstrExportPopup']/div/div/div/a[2]"

    ############### Form Loading Issue dialoguebox ###################
    error_xpath="//div[@class='mstrmojo-Editor-title']"
    btn_Continue_xpath="//div[@role='button']/div"
    #Title = Home. MicroStrategy

    def __init__(self,
                 driver):  # creating constructor init,and driver is an argument and why we are creating when we create init it will be called whenever object of the class will be created  # and passing argument as driver so same driver can be used in test calss
        super().__init__(driver)
        self.driver = driver
################   Accepted (With Override) ##################
    def formName_WN_Year_BSI(self):
        formName_WN_Year = self.driver.find_element(By.XPATH, self.status_formName_xpath).text
        print("FORM:- " + formName_WN_Year)
        return formName_WN_Year
    def seriousError(self):
        first_Seriouserror = self.driver.find_element(By.XPATH, self.first_seriousError_xpath).text
        # L8, C1(5)  MUST  BE <= L7, C1(3)
        print("First Serious Error is:- " + first_Seriouserror)
        return first_Seriouserror

        #### Accepted_override functionality and verifying in Forms
    def click_OnAcceptedOverrideForm(self,formName_WN_Year):

        self.driver.find_element(By.XPATH, self.btn_formPage_xpath).click()
        time.sleep(3)
        #fName_bsi_WNO = self.formName_WN_Year_BSI()
        form, wload, bsi, year, mq = formName_WN_Year.split()
        formname = form.replace("=", " ")
        rows = len(self.driver.find_elements(By.XPATH, self.formTable_totalRows_xpath))
        cols = len(self.driver.find_elements(By.XPATH, self.formTable_totalCols_xpath))
        # search_form = formname
        form_col = len(self.driver.find_elements(By.XPATH, self.firstColumn_xpath))
        for r in range(1, rows + 1):
            for c in range(1, form_col + 1):
                record = self.driver.find_element(By.XPATH,
                                                  "//table[@title='Forms']/tbody/tr[" + str(r) + "]/td[" + str(
                                                      form_col) + "]").text  # Typecasting, Searching particular Form
                if record == formname:
                    #print(formname)
                    time.sleep(2)
                    if r >= 7:
                        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)  # This will scroll down
                    time.sleep(2)
                    self.driver.find_element(By.XPATH,
                                             "//table[@title='Forms']/tbody/tr[" + str(r) + "]/td[" + str(
                                                 form_col + 2) + "]").click()
                    break
    def switch_ToWindow(self):
        windows = self.driver.window_handles
        for w in windows:
            self.driver.switch_to.window(w)
            time.sleep(3)

    def select_YearMonth(self,formName_WN_Year):
        form, wload, bsi, year, mq = formName_WN_Year.split()
        #print(year)   #print(mq)
        mon_quar=mq.replace('0', '') # Removing preceding zero from month/quarter

        windows = self.driver.window_handles
        for w in windows:
            self.driver.switch_to.window(w)
            time.sleep(2)

        year_list=self.driver.find_elements(By.XPATH, "//div[@class='mstrBGIcon_ae mstrTreeViewNodeShortDisplay']")

        for year_ in year_list:
            year1_=year_.text
            if year1_ == year:
                year_.click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//span[contains(@class,'Selected')]/preceding-sibling::img").click()
                self.driver.find_element(By.XPATH, "//*[contains(text(),'YEAR-')]/preceding-sibling::img").click()
                time.sleep(2)
                break
        add_Button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.add_Arrow_xpath)))
        add_Button.click()

        self.driver.find_element(By.XPATH, self.run_Document_xpath).click()
        time.sleep(2)

        ####### Select value from dropdown ################
        ddbsi = self.driver.find_element(By.XPATH, "//div[@class='mstrmojo-DocGroupBy ']/div/span[6]/select")
        dd_bsi = Select(ddbsi)
        dd_bsi.select_by_visible_text(bsi)
        time.sleep(1)

        ddYearQM = self.driver.find_element(By.XPATH, "//div[@class='mstrmojo-DocGroupBy ']/div/span[1]/select")
        dd_YearQM = Select(ddYearQM)
        dd_YearQM.select_by_index(mon_quar)
        time.sleep(1)

        ddwloadNo = self.driver.find_element(By.XPATH, "//div[@class='mstrmojo-DocGroupBy ']/div/span[5]/select")
        dd_wloadNo = Select(ddwloadNo)
        dd_wloadNo.select_by_visible_text(wload)
        time.sleep(1)
    def verify_LineColumnValue(self,first_Seriouserror):
        line=first_Seriouserror[:9]
        #print(line) # L8,C1 (5, printed 9 characters
        # To get the value between L and ',', to get value 8
        sub1 = "L"
        sub2 = ","
        # getting elements in between using split() and join()
        col1 = ''.join(line.split(sub1)[1].split(sub2)[0])

        #To get the value between ( ), will give the value 5
        sub3 = "("
        sub4 = ")"
        # getting elements in between using split() and join()
        col2 = ''.join(line.split(sub3)[1].split(sub4)[0])

        table_column1 = self.driver.find_elements(By.XPATH,
                                               "//div[@class='mstrmojo-XtabZone ']/table[@role='grid']/tbody/tr/td[1]")
        for row in table_column1:
                data = row.text
                spl_char = '.'
                res1 = data.partition(spl_char)[0]  # seprate value before '.', say 1,2,3,4
                if (res1 == col1):
                    print("Line No:-" + res1)
                    break

        table_column2 = self.driver.find_elements(By.XPATH,
                                               "//div[@class='mstrmojo-XtabZone ']/table[@role='grid']/tbody/tr/td[2]")
        for row1 in table_column2:
            res2 = row1.text
            #print(data1)
            if (res2 == col2):
                print("Value:-" + res2)
                break
    #################### All above method is verifying 'Accepted Override' Funcionality #####################

    def click_OnEachForm(self):   # Working fine, its randomly clicking on 5 forms out of 24
        self.driver.find_element(By.XPATH, self.btn_formPage_xpath).click()
        time.sleep(2)
        # total_FormLinks = self.driver.find_elements(By.XPATH, "//tbody[@class='mdc-data-table__content']/tr/td[3]")
        # print(len(total_FormLinks))

        for x in range(1,5):
            min_length = 1
            max_length = 24
            i = random.randint(min_length, max_length)
            time.sleep(5)
            print(x)
            if i >= 9:
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END) ## For scroll down

            frmLink = self.driver.find_element(By.XPATH,"//tbody[@class='mdc-data-table__content']/tr[" + str(i) + "]/td[3]/a")
            #frmLink.click()

            maxAttempts =3
            attempt=1
            #elementClickable = False
            while(attempt <= maxAttempts):
                try:
                   frmLink.click()
                   break
                except Exception as e:
                    print(e)
            time.sleep(2)
            parent_window_id = self.driver.current_window_handle
            windows = self.driver.window_handles
            for w in windows:
                self.driver.switch_to.window(w)
                time.sleep(2)

            if i==9: #To run  the document --- for FORM F if logic as this form is yearly
                self.driver.find_element(By.XPATH,self.icon_2022_xpath).click()
                add_Button_F = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.add_Arrow_FormF_xpath)))
                add_Button_F.click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.run_Document_F_xpath).click()

            else:
                icon_2023 = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.icon_2023_xpath)))
                icon_2023.click()
                #self.driver.find_element(By.XPATH, self.icon_2023_xpath).click()

                icon_Year_Quarter = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.icon_Year_Quarter_xpath)))
                icon_Year_Quarter.click()
                #self.driver.find_element(By.XPATH, self.icon_Year_Quarter_xpath).click()

                year_Quarter = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.year_Quarter_xpath)))
                year_Quarter.click()
                #self.driver.find_element(By.XPATH, self.year_Quarter_xpath).click()
                #time.sleep(2)
                add_Button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.add_Arrow_xpath)))
                add_Button.click()
            #self.driver.find_element(By.XPATH, self.add_Arrow_xpath).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.run_Document_xpath).click()

            total_msg = self.driver.find_element(By.XPATH, self.total_text).text
            print(total_msg)
            print(self.driver.title)

            heading_List= self.driver.find_elements(By.XPATH, self.all_FormHeadings)

            #To pull all Totals heading
            i=1
            for each_Heading in heading_List:
                time.sleep(3)
                data = each_Heading.text
                print(data)
                i += 1
                if (i == 3):
                    break
            print("\n")
            time.sleep(2)
            ## National Total
            self.driver.find_element(By.XPATH, self.national_Total_xpath).click()
            print(self.driver.find_element(By.XPATH, self.national_Total_xpath).text)
            print(self.driver.title)

            self.driver.close()
            self.driver.switch_to.window(parent_window_id)
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//object[@id='obj_crowd_wab_application']"))

    def verify_ExportFunctionality(self):
        try:
            global result
            # formPage = WebDriverWait(self.driver, 30).until(
            #     EC.presence_of_element_located(self.driver.find_element(By.XPATH, self.btn_formPage_xpath)))
            # formPage.click()
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.btn_formPage_xpath).click()
            time.sleep(2)
            # total_FormLinks = self.driver.find_elements(By.XPATH, "//tbody[@class='mdc-data-table__content']/tr/td[3]")
            # print(len(total_FormLinks))

            for x in range(1,2):
                min_length = 1
                max_length = 24
                i = random.randint(min_length, max_length)
                time.sleep(5)

                if i >= 9:
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)  ## For scroll down

                frmLink = self.driver.find_element(By.XPATH, "//tbody[@class='mdc-data-table__content']/tr[" + str(
                    i) + "]/td[3]/a")
                # frmLink.click()
                formName =self.driver.find_element(By.XPATH, "//tbody[@class='mdc-data-table__content']/tr[" + str(
                    i) + "]/td[3]/a").text
                print(" Form Name:- " + formName)

                maxAttempts = 3
                attempt = 1
                # elementClickable = False
                while (attempt <= maxAttempts):
                    try:
                        frmLink.click()
                        break
                    except Exception as e:
                        print(e)
                time.sleep(2)

                parent_window_id = self.driver.current_window_handle

                windows = self.driver.window_handles
                for w in windows:
                    self.driver.switch_to.window(w)
                    time.sleep(2)

                if i == 9:  # To run  the document --- for FORM F if logic as this form is yearly
                    self.driver.find_element(By.XPATH, self.icon_2022_xpath).click()
                    add_ButtonF = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.add_Arrow_FormF_xpath)))
                    add_ButtonF.click()
                    self.driver.find_element(By.XPATH, self.run_Document_F_xpath).click()

                else:
                    icon_2023 = WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.icon_2023_xpath)))
                    icon_2023.click()
                    # self.driver.find_element(By.XPATH, self.icon_2023_xpath).click()

                    icon_Year_Quarter = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.icon_Year_Quarter_xpath)))
                    icon_Year_Quarter.click()
                    # self.driver.find_element(By.XPATH, self.icon_Year_Quarter_xpath).click()

                    year_Quarter = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.year_Quarter_xpath)))
                    year_Quarter.click()
                    # self.driver.find_element(By.XPATH, self.year_Quarter_xpath).click()
                    # time.sleep(2)
                    add_Button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.add_Arrow_xpath)))
                    add_Button.click()
                    # self.driver.find_element(By.XPATH, self.add_Arrow_xpath).click()
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, self.run_Document_xpath).click()

                    export_Icon=self.driver.find_element(By.XPATH, self.export_icon_xpath)

                    if(export_Icon.is_displayed):
                        self.driver.find_element(By.XPATH, self.export_icon_xpath).click()
                        time.sleep(1)
                        self.driver.find_element(By.XPATH, self.export_option_xpath).click()
                        time.sleep(1)
                        self.driver.find_element(By.XPATH, self.exportPDFOption_xpath).click()
                        time.sleep(1)

                        child_windowTitle =self.driver.title
                        print("PDF Page's MicroStrategyPage Title:- " + child_windowTitle)

                        if formName in child_windowTitle:
                            result="Pass"
                        else:
                            result="Fail"

                    ### For PDF download
                    # win_id=self.driver.current_window_handle
                    # shadow_root1 = self.driver.find_element(By.CSS_SELECTOR, '[id="downloads"]').shadow_root
                    # shadow_button=shadow_root1.find_element(By.CSS_SELECTOR, '[id="download"]').shadow_root
                    # shadow_icon = shadow_button.find_element(By.CSS_SELECTOR, '[id="icon"]').shadow_root
                    # shadow_icon.click()

                    # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.driver.execute_script(
                    # "return document.querySelector('viewer-download-controls').shadowRoot.querySelector('cr-icon-button').shadowRoot.querySelector('iron-icon').shadowRoot.querySelector('svg')")))).click()


                    self.driver.close()
                    self.driver.switch_to.window(parent_window_id)
                    self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//object[@id='obj_crowd_wab_application']"))
                return result
            else:
                print("Form is not loaded")
        except NoSuchElementException as e:
            print(e)











