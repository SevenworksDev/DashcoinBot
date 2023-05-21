# I removed some stuff I used for testing in here which is the /delay commands and also the startup message is replaced to give you privacy.
# Change the "lvl" value at the bottom of the script to lvl="Level ID Here"

# DO NOT CLAIM THIS AS YOUR OWN AND BE NICE! PLEASE CREDIT ME!


from distutils.command.upload import upload
from bettercomm import uploadGJComment
import time,requests,random,decimal,pickle,fuckit
from json import loads
from threading import Thread

un = "username"
pw = "password"

def add_coin(username, coin):
    if username in dashcoin:
        dashcoin[username] += coin
    else:
        dashcoin[username] = coin
    with open('dashcoin.sw', 'wb') as file:
      pickle.dump(dashcoin, file)


def get_coin(username):
    if username in dashcoin:
        return dashcoin[username]
    else:
        return 0

def give_coin(username, usernameTo, coin):
    if coin >= decimal.Decimal("0.000000"):
      if username == usernameTo:
        uploadGJComment(un,pw,f"Cannot give coins to yourself.",0,lvl)
      elif username in dashcoin and usernameTo in dashcoin:
          if dashcoin[username] >= coin:
              dashcoin[username] -= coin
              dashcoin[usernameTo] += coin
              uploadGJComment(un,pw,f"You gave {coin} Dashcoin to {usernameTo}.",0,lvl)
          else:
              uploadGJComment(un,pw,f"You dont have {coin} Dashcoin to give.",0,lvl)
      else:
          uploadGJComment(un,pw,f"{usernameTo} has no wallet, Tell the user to start chatting!",0,lvl)
      with open('dashcoin.sw', 'wb') as file:
        pickle.dump(dashcoin, file)
    elif coin <= decimal.Decimal("0.000000"):
      uploadGJComment(un,pw,f"Cannot give negative coins.",0,lvl)

dashcoin={}
with open('dashcoin.sw', 'rb') as file:
    dashcoin = pickle.load(file)
    print("Started")

def commands(level):
    url=f"http://gdbrowser.com/api/comments/{level}?count=1"
    r=loads(requests.get(url).text)[0]
    u=r['username']
    com=r['content']
    perc=random.randint(1,100)
    add_coin(u, decimal.Decimal(random.randrange(1, 3))/1000000)

    if(com.startswith("/bal")):
      coin=get_coin(u)
      try:
          uploadGJComment(un,pw,f"Hello, {u}! You have {coin} Dashcoin! ($1 - 0.000500)",perc,level)
          print(f"{u} executed /bal")
      except:
          return
    if(com.startswith("/getbal")):
      x=com.split("/getbal ")
      c=x[1]
      coin=get_coin(c)
      try:
          uploadGJComment(un,pw,f"{c}s Wallet: {coin} ($1 - 0.000500)",perc,level)
          print(f"{u} executed /getbal on {c}")
      except:
          return
    if(com.startswith("/gift")):
      c=com.split(" ")
      try:
          with open("gift.log", "a") as f:
            print(c, file=f)
          give_coin(u, c[1], decimal.Decimal(c[2]))
          print(f"{u} executed /gift: {c}")
      except:
          uploadGJComment(un,pw,f"@{u} Unknown Error, Make sure the amount is a decimal number.",perc,level)
          return
    elif(com.startswith("/help")):
        time.sleep(25)
        coin=get_coin(u)
        try:
            uploadGJComment(un,pw,f"@{u}, Dashcoin Help | /bal | /getbal [user] | /gift [user] [amount]",perc,level)
            print(f"{u} executed /redeem")
        except:
            return
    elif(com.startswith("hello" or "hi" or "hey" or "Hello" or "Hi" or "Hey")):
        try:
            uploadGJComment(un,pw,f"Hey @{u}! (Check Dashcoin Balance - /bal)",perc,level)
        except:
            return
    elif(com.startswith("kys" or "Kys" or "KYS" or "kill" or "Kill" or "shut" or "Shut" or "SHUT" or "die" or "Die" or "DIE")):
        try:
            uploadGJComment(un,pw,f"Hey @{u}, Thats not nice!",perc,level)
        except:
            return

lvl='levelID'
uploadGJComment(un,pw,f"[SevenworksSys]: This is running off of https://github.com/Sevenworks/Dashcoin! Please support me!",0,lvl)
while 1:
    with fuckit:
        t=Thread(target=commands,args=(lvl,))
        t.start()
        time.sleep(2)
