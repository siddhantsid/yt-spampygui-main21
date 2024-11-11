import pyautogui
import time
from os import system
#__---_--_--__-__-________________________________________________________
mozilac="Point(x=205, y=33)"
urlBox="Point(x=423, y=82)"
url="https://www.youtube.com/watch?v=uUMf2JptRe4"
#____________________________________________________________________________
def main():
    pyautogui.hotkey("ctrlleft","altleft","d")
    pyautogui.click(205,33,duration=1)
    pyautogui.hotkey("ctrlleft","t") 
    pyautogui.PAUSE=3
    pyautogui.click(423,82,duration=2)
    pyautogui.typewrite(url)
    pyautogui.click(717,126)
    time.sleep(22)
    pyautogui.scroll(-15)
    pyautogui.click('reply-1.png')
    pyautogui.typewrite("I am a Bot")
    pyautogui.PAUSE=3
    pyautogui.click("final.png")
    time.sleep(2)
    print("We have replied successfully")

#__-------------------------------------------------------------------
if __name__=="__main__":
    main()
