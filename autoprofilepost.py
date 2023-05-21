import requests,base64,itertools,time

# PUT YOUR DETAILS HERE
accountID = "69420000" # Get this via gdbrowser.com's User Search
password = "StopHackingMeDummy"
botName = "Dashcoin"



def xor_cipher(string: str, key: str) -> str:
    result = ""
    for string_char, key_char in zip(string, itertools.cycle(key)):
        result += chr(ord(string_char) ^ ord(key_char))
    return result

def base64_encode(string: str) -> str:
    return base64.urlsafe_b64encode(string.encode()).decode()

def generate_gjp(password: str):
    gjp = xor_cipher(password, "37526")
    gjp = base64_encode(gjp)
    return gjp

def gjpost(post):
  data = {
      "accountID": accoundID,
      "gjp": generate_gjp(password),
      "comment": base64_encode(post),
      "secret": "Wmfd2893gb7",
  }
  r = requests.post('http://www.boomlings.com/database/uploadGJAccComment20.php', data=data, headers={"User-Agent":""})
  print(r.text)

while True:
  gjpost("$0.50 - Hug")
  time.sleep(0.2)
  gjpost("=== Shop ===")
  time.sleep(0.2)
  gjpost("Welcome to {botName} Shop! (Message = Buy) https://github.com/SevenworksDev/Dashcoin")
  print("\n\nYou can exit this script now...")
  time.sleep(999999)

