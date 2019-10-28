from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint


class olx(object):
	def __init__(self, arg):
		super(olx, self).__init__()
		self.option = arg[0]
		self.keyword = arg[1]
		self.FireFox_Path = r'C:\Users\Guilherme\Downloads\Selenium\drivers\geckodriver.exe'
		self.Chrome_Path = r'C:\Users\Guilherme\Downloads\Selenium\drivers\chromedriver.exe'
		self.default_page = "https://www3.olx.com.br/account/form_userinfo"
		if self.option == 1:
			chrome_options = Options()
			chrome_options.add_experimental_option("detach", True)
			self.driver = webdriver.Chrome(executable_path = self.Chrome_Path, chrome_options = chrome_options)
			self.driver.get(self.default_page)
			self.login()
			self.pesquisar()
		else:
			self.driver = webdriver.Firefox(executable_path = self.FireFox_Path)
			self.driver.get(self.default_page)
			pass

	def login(self):
		try:
			login_page = self.driver.find_elements_by_tag_name("input")
			for x in login_page:
				if x.get_property("type") == 'email':
					x.send_keys(user)
					pass
				else:
					x.send_keys(passwd)
				pass
			btn = self.driver.find_element_by_xpath("//button[@type = 'text']")
			btn.click()
			pass
		except Exception as e:
			pprint(e)
			self.driver.quit()
			raise
		else:
			pass
		finally:
			pass
		pass
	# def goToPage():
	# 	https://mg.olx.com.br/belo-horizonte-e-regiao/videogames?o=2&q=fliperama

	def pesquisar(self):
		paramPesquisa = self.driver.find_element_by_id("searchtext")
		paramPesquisa.send_keys(self.keyword)
		botaoPesquisa = self.driver.find_element_by_id("searchbutton")
		botaoPesquisa.click()
		pass

	def getAds(self):
		try:
			list_ads = self.driver.find_element_by_id("main-ad-list")
			ads = list_ads.find_elements_by_xpath(".//li[@class='item']")
			# links = ads.find_elements_by_tag_name("a")
			link_dict = {}
			for x in ads:
				link = x.find_element_by_xpath(".//a")
				link_dict[link.get_property("id")] = {"title": link.get_property("title"), "link": link.get_property("href"), 'price': link.find_element_by_xpath(".//p[@class = 'OLXad-list-price']").text}
				# new_path = './file/' + str(ids) + '/' + part['filename']
				# if not os.path.isdir('./attachments/' + str(ids) + '/'):
				# 	os.makedirs('./attachments/' + str(ids))
				# if not os.path.isfile(new_path):
				# 	with open(new_path, 'wb') as f:
				# 		f.write(file_data)
				pass
		except Exception as error:
			pprint(link_dict)