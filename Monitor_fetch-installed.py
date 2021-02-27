# import winapps

# # 
# apps=['skype','Facebook']
# for app in winapps.list_installed():
    
#     res=any(ele.casefold() in app.name.casefold() for ele in apps)
#     if res==True:
#         print(app.name)

from skpy import Skype
sk = Skype('poorna.raparti88@gmail.com', 'poorna9666') # connect to Skype
contacts = []
# sk = Skype(user, password)
source_contacts = sk.contacts
for contact in source_contacts:
    contacts.append(str(contact.id))
    print(contacts)
    for contact in contacts:
        try:
            # chat = sk.contacts[contact].
            chat = sk.contacts[contact].chat.getMsgs()
            if chat:
                print(chat, '\n')
        except Exception as exc:
            resp = exc.args[1]
            print(resp)

# print(sk.user) # you
# print(sk.contacts) # your contacts
for contact in contacts:
    # print(i)
    print(sk.contacts[contact].Name())
    print(sk.contacts[contact].Mood)
    print(sk.contacts[contact].Phone)
    # print(sk.contacts[contact])
    # print(i['Location'])
# print(len(sk.chats))
# ch=sk.chats["8:sudeesh.kumarr"]

# print(ch)
# for chat in sk.chats.recent():
    
#     ch=sk.chats[chat]
#     msg=ch.getMsgs()
#     print(msg)
#  # your conversations

# ch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
# ch = sk.contacts["joe.4"].chat # 1-to-1 conversation

# ch.sendMsg(content) # plain-text message
# ch.sendFile(open("song.mp3", "rb"), "song.mp3") # file upload
# ch.sendContact(sk.contacts["daisy.5"]) # contact sharing

# ch.getMsgs() # retrieve recent messages