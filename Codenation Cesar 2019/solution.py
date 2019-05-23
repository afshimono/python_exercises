import urllib.request, json, string, hashlib, base64, requests, binascii


def download_json():
	url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=138ded668441ab05ede31d4c672fe5128de3840f"
	with urllib.request.urlopen(url) as url:
		data = json.loads(url.read().decode())
		with open('answer.json','w') as json_file:
			json.dump(data,json_file)

def submit_answer():
	url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=138ded668441ab05ede31d4c672fe5128de3840f'
	with open('answer.json') as json_file:
		multipart_data = {'answer':('answer.json',json_file)}
		response = requests.post(url, files=multipart_data)
		print(response.status_code)

def decript(casas, encripted):
	alphabet = list(string.ascii_lowercase)
	alpha_size = len(alphabet)
	result = []
	for letter in list(encripted):
		
		if letter in alphabet:
			position = alphabet.index(letter)
			#print('Adding decripted:  '+alphabet[(position-casas)])
			result.append(alphabet[(position-casas)])
		else:
			result.append(letter)
	return ''.join(result)

def generate_hash():
	with open('answer.json') as json_file:
		data = json.load(json_file)
		m = hashlib.sha1()
		m.update(str.encode(data['decifrado']))
		data['resumo_criptografico'] = binascii.hexlify(m.digest()).decode('ascii')
	with open('answer.json','w') as json_file:
		json.dump(data,json_file)

def decript_file():
	with open('answer.json') as json_file:
		data = json.load(json_file)
		data['decifrado'] = decript(int(data['numero_casas']),data['cifrado'])
	with open('answer.json','w') as json_file:
		json.dump(data,json_file)


download_json()
decript_file()
generate_hash()
submit_answer()