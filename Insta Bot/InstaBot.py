from asyncio import exceptions
from time import sleep
import pyautogui as pg
import pyperclip as pc

sleep(2)

last_message,last_response  ='',''

def move_to_text_input(message):
    global last_response
    try:
        position = pg.locateOnScreen('images/image.png',confidence=0.9)
        pg.moveTo(position[0:2],duration=0.2)
        pg.moveRel(-120,20,duration=0.2)
        pg.click(interval=0.3)
        pg.typewrite(f'Message Received : {message}',interval=0.08)
        last_response = f'Message Received : {message}'
        pg.typewrite('\n')
    except exceptions :
        pass


#Message Retival Handle

def get_messages():
    try:

        position = pg.locateOnScreen('images/smily.png',confidence=0.9)
        pg.moveTo(position[0:2],duration=0.1)
        pg.moveRel(50,-50,duration=0.1)


        position = pg.locateOnScreen('images/dots.png',confidence=0.9)
        pg.moveTo(position[0:2],duration=0.1)
        pg.click(interval=0.1)


        position = pg.locateOnScreen('images/copy.png',confidence=0.8)
        pg.moveTo(position[0] + 10 ,position[1] + 15,duration=0.5)
        pg.click(interval=0.1)
        return pc.paste()
    except exceptions:
        pass





def Process_Message():
    try:
        global last_message , last_response 


        curr_message  = get_messages()
        if curr_message!=last_message and curr_message!=last_response:
            last_message = curr_message

            print(f'Last Copied Message {curr_message}')

            move_to_text_input(curr_message)
        else:
            print('No New Message !! ... Waiting For Message ...')
    except exceptions :
        pass


if __name__ == '__main__':
    while True:
        try: 
         Process_Message()
         sleep(10)
        except exceptions:
            pass