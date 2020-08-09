import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def start_chrome():
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\gouki\OneDrive\ドキュメント\chromedriver_win32\chromedriver.exe')
    driver.maximize_window()

    driver.get(
        'https://docs.google.com/forms/d/e/1FAIpQLSf0Ovrhjdn4uXKL7zVSavVbEcbixPnDXxPlea3nWs23NRsRGA/viewform')
    return driver


def login_google(driver):
    login_id = "m18013@g.metro-cit.ac.jp"
    login_pw = "GoukiRuby0209"

    # 最大待機時間（秒）
    wait_time = 30

    # IDを入力
    login_id_xpath = '//*[@id="identifierNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_name("identifier").send_keys(login_id)
    driver.find_element_by_xpath(login_id_xpath).click()

    # パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, login_pw_xpath)))
    driver.find_element_by_name("password").send_keys(login_pw)
    time.sleep(2)  # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath(login_pw_xpath).click()


def input_googleform(driver):
    time.sleep(4)
    for element in driver.find_elements_by_xpath('//div[contains(@aria-label, "に対する応答です")]'):
        if (element.get_attribute("data-value") == "いいえ"):
            element.click()

    driver.find_element_by_xpath('//div[@aria-label="検温した"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//span[text()="次へ"]').click()


if __name__ == '__main__':
    # Chromeを起動
    driver = start_chrome()

    # Googleにログイン
    login_google(driver)

    input_googleform(driver)
