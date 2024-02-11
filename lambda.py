from selenium import webdriver
from tempfile import mkdtemp

def get_driver():
    service = webdriver.ChromeService("/opt/chromedriver")
    
    options = webdriver.ChromeOptions()
    options.binary_location = "/opt/chrome/chrome"
    options.add_argument("--single-process")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1900x1200")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")

    chrome = webdriver.Chrome(options=options, service=service)

    return chrome

def handler(event=None, context=None):
    print(f"Request ID: {context.aws_request_id}")
    print(f"Event: {event}")
    driver = get_driver()
    
    driver.get("https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json")

    print(driver.page_source)
    
    return 'success'


