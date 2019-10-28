from olx import olx
from pprint import pprint
import os


def main():
	try:
		ol = olx([1,"fliperama"])
		pass
	except Exception as e:
		pprint(e)
		raise
	else:
		pass
	finally:
		pass
	# ol.pesquisar()
	ol.getAds()
	# ol.driver.close()


if __name__ == '__main__':
	main()