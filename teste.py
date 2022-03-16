from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.amazon.com.br/Rajada-Turbo-Mesa-Mixtel-Preto/dp/B07N8HM6XG/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2JTPEZJNJL4Q6&keywords=7899831300044&qid=1647431419&sprefix=7899831300044%2Caps%2C203&sr=8-1&ufe=app_do%3Aamzn1.fos.db68964d-7c0e-4bb2-a95c-e5cb9e32eb12')

driver(quit)