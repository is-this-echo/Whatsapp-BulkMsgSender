import pywhatkit
import pyautogui as pg

# # Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")


# pywhatkit.sendwhatmsg_to_group_instantly("GofPpklPo4U05JrES5ZTsF", "Hey All!")

# file_path = "./numbers.txt" 
# with open(file_path, "r") as file:
#     content = file.read()

# phone_numbers = [number.strip() for number in content.split(",")]

phone_numbers = ["+918902642067", "+919875508251","+918902216984", "+918348026699", "+919062033536",
                 "+917063621611", "+918585043747"]

for number in phone_numbers:
    pywhatkit.sendwhatmsg_instantly(number,"""
Free BGMI Custom Rooms Daily

1 match per day

Timing :
7:30 pm - Erangle

All matches all be broadcasted on our YouTube channel : 
BGMI Custom Rooms 

ID and Password will be given in YouTube live stream and our Telegram group : 
BGMI Custom Rooms

Telegram : https://t.me/+mI3lwPrWv7E0MDU1
Youtube : https://youtube.com/@bgmicustomrooms

We don't ask for money to play but kindly support us by Liking, Sharing and Subscribing our YouTube channel. So that we can grow our YT channel and organise completely Free BGMI Tournaments in future.""")


# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("Dw673v1Ey5F5BddqTLW0TN", """Hey there dude. 😎 
#                                          Wanna play free BGMI Custom Rooms instead of paid ones?
#                                          Join this WhatsApp group: 
#                                          https://chat.whatsapp.com/GofPpklPo4U05JrES5ZTsF""")
                                    

