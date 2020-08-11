import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GoogleFormInput:
    def start_chrome():
        driver = webdriver.Chrome(
            executable_path=r'C:\Users\gouki\OneDrive\ドキュメント\chromedriver_win32\chromedriver.exe')

        driver.get(
            'https://docs.google.com/forms/d/e/1FAIpQLSf0Ovrhjdn4uXKL7zVSavVbEcbixPnDXxPlea3nWs23NRsRGA/viewform')
        return driver

    def login_google(driver):
        login_id = "適当"
        login_pw = "適当"

        # 最大待機時間（秒）
        wait_time = 40

        # IDを入力
        login_id_xpath = '//*[contains(@id, "identifierNext")]'
        # xpathの要素が見つかるまで待機します。
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, login_id_xpath)))
        driver.find_element_by_name("identifier").send_keys(login_id)
        driver.find_element_by_xpath(login_id_xpath).click()

        # パスワードを入力
        login_pw_xpath = '//*[contains(@id, "passwordNext")]'
        # xpathの要素が見つかるまで待機します。
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
        driver.find_element_by_name("password").send_keys(login_pw)  # クリックされずに処理が終わるのを防ぐために追加。
        driver.find_element_by_xpath(login_pw_xpath).click()

    def input_googleform_1(driver):
        for element in driver.find_elements_by_xpath('//div[contains(@aria-label, "に対する応答です")]'):
            if (element.get_attribute("data-value") == "いいえ"):
                element.click()

        driver.find_element_by_xpath('//div[@aria-label="検温した"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//span[text()="次へ"]').click()

    def input_googleform_2(driver, temperature):
        AVE_Temperature = 36.0
        i = int(temperature)
        f = int((temperature - i) * 10)
        driver.find_element_by_xpath("//div[@aria-label='" + str(i) + "']").click()
        driver.find_element_by_xpath("//div[@aria-label='" + str(f) + "']").click()
        if (temperature >= (AVE_Temperature + 0.5)):
            driver.find_element_by_xpath("//div[@aria-label='はい']").click()
        else:
            driver.find_element_by_xpath("//div[@aria-label='いいえ']").click()


if __name__ == '__main__':
    AI = GoogleFormInput
    # Chromeを起動
    driver = AI.start_chrome()
    # Googleにログイン
    AI.login_google(driver)
    time.sleep(4)
    AI.input_googleform_1(driver)
    time.sleep(1)
    AI.input_googleform_2(driver, 37.0)
