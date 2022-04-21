from pyrogram import Client, filters as f
import os

token = os.getenv("STRING")

app = Client(
	token,
	"5775802", 
	"6011ffc6cec69c60ef86456db0ce4d09")


allUser = []
@app.on_message(f.command("get") & f.me)
async def _(b,m):
	await m.delete()
	await b.send_message(chat_id="me", text="**Kullanıcılar Getiriliyor!!**")

	for i in await m.chat.get_members():
		if i.user.status in ["recently", "online", "offline"]:
			if i.user.id not in allUser:
				if i.user.username == None or i.user.username == False:
					allUser.append(i.user.id)
				else:
					allUser.append(i.user.username)

	await b.send_message(chat_id="me", text="**{} Adet Kullanıcı Liselendi!!**".format(len(allUser)))

	with open("allUser.txt", "w+") as f:
		f.write(str(allUser))

	await b.send_document("me", "allUser.txt", caption="{} adet kullanıcı listelendi!!".format(len(allUser)))
	allUser.clear()

app.run()
