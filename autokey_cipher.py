# Because coding the autokey cipher seemed much more fun than solving it by hand... 


####################-- Several Helper Functions --####################

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def letter2Number(string):
	#takes a string outputs a list of letters
	result = []
	for c in string:
		result.append(alphabet.find(c) % 26)
	return result
def number2Letter(list):
	#takes list of integers and returns a string
	string = ''
	for n in list:
		string += (alphabet[n])
	return string

####################-- Encryption and Decryption --####################

def encrypt(key, message):
	#takes key and messages as lists of integers, and returns a list of integers
	#representing the autokeyed ciphertext
	result = []
	for i in range(len(message)):
		if i < len(key):
			result.append((message[i] + key [i])%26)
		else:
			result.append((message[i] + message[i - len(key)])%26)
	return result

def decrypt(key, c):
	result = []
	for i in range(len(c)):
		if i < len(key):
			result.append((c[i] - key [i])%26)
		else:
			result.append((c[i] - result[i - len(key)])%26)
	return result


def findKey(message, cipher):
	#find a place where cipher[i] = message[i] + message[k] for k < i
	result = [0]
	first = message[0]
	newhits = []
	i = 0
	hitIndex = 0
	while i < len(cipher):
		#if hitIndex > 0:
		#	if not (cipher[i] == (message[i] + message[i - hitIndex])%26):
		#		hitIndex = 0
		#		newhits = []
		#	else:
		#		hitIndex += 1

		if cipher[i] == (message[i] + first)% 26:
			newhits.append(i)
			hitIndex = int(i)
		i += 1
	print newhits

	return result




def keyText(messageString, cipherString):
	return number2Letter(findKey(letter2Number(messageString), letter2Number(cipherString)))

def encryptText(keyString, messageString):
	return number2Letter(encrypt(letter2Number(keyString), letter2Number(messageString)))

def decryptText(keyString, messageString):
	return number2Letter(decrypt(letter2Number(keyString), letter2Number(messageString)))


####################-- Tests --####################
def test():
	### Test Letter Encoding##
	assert number2Letter(letter2Number("cat")) == "cat"
	message = letter2Number("theautokeycipheriscool")
	key = letter2Number("random")
	assert number2Letter(encrypt(key, message)) == 'khrdifhriywbdripkarvsc'

	###Test Message Encryption and Decryption###
	key1 = "shevek"
	message1 = "odoniansocialtheory"
	assert number2Letter(decrypt(letter2Number(key1), encrypt(letter2Number(key1), letter2Number(message1)))) == message1

	### Test encryptText and decryptText ##
	assert decryptText(key1,encryptText(key1, message1)) == message1

test()

######## Get Homework Answers #######

#gets answers to HPS 4.19
def homework():
	## A) encrypt
	print encryptText('lear', 'comenotbetweenthedragonandhiswrath')

	## B) decrypt
	print decryptText('cordelia', 'pckkmyowvzejwzkknyzvvuruxcstritgac')




keyText("theautokeycipheriscool", "khrdifhriywbdripkarvsc")
keyText('ifmusicbethefoodofloveplayon', 'azdzwqvjjfbwnqphhmptjsszfjci')

print decryptText('surfeit', 'azdzwqvjjfbwnqphhmptjsszfjci')
a = letter2Number('ifmusic')
b = letter2Number('azdzwqv')
c = [(b[i] - a[i]) %26 for i in range(len(b))]
print number2Letter(c)


homework()





