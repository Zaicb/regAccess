#      _   _        __   __
#     /_\ | |__ _ _ \ \ / /_ _ _ _ __ _ ___
#    / _ \| / _` | ' \ V / _` | '_/ _` / _ \
#   /_/ \_\_\__,_|_||_\_/\__,_|_| \__, \___/
#                                 |___/
# access to reg by _winreg
import _winreg

myREG = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',0,_winreg.KEY_ALL_ACCESS)
fullPATH = '"C:\Windows\System32\calc.exe" -autorun'
_winreg.SetValueEx(myREG, 'NEW', 0, _winreg.REG_SZ, fullPATH)