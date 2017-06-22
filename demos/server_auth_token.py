import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print "Error\n"
	print "Usage: $>python server_auth_token.py YOUR_API_TOKEN YOUR_PRIVATE_KEY \n"
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]

ziggeo = Ziggeo(api_token, private_key)

print ziggeo.authtokens().create()