from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img id="photosize" src="data:image/png;base64,%s" alt="screenshot" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra



def _capture_screenshot():
    '''
    截图保存为base64，展示到html中
    :return:
    '''
    return driver.get_screenshot_as_base64()


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    driver = None
    if driver is None:
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 禁用浏览器正在被自动化程序控制的提示
        chrome_options.add_experimental_option('w3c', False)
        chrome_options.add_argument('--enable-audio-focus=true')
        # chrome_options.add_argument('headless') #无头浏览
        # chrome_options.add_argument('--window-size=1920,1080') #只能在无头浏览时使用
        # chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        # chrome_driver_path = r'C:\Python35\chromedriver.exe'
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.set_window_size(1920, 1040)
        driver.set_window_position(0, 0)

    return driver