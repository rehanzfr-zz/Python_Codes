import time
import sys
import random
import string
import os
import keyboard

# 3 seconds to alt-tab to correct window after running
time.sleep(3)
replace_time = random.randint(5,10)
start_time = time.time()


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Use randomString or the change_string
def change_string(chrar):
    charac={':':';',';':':','[':'{','{':'[',']':'}','}':']','.':',',',':'.','/':'?','?':'/','q':'a','a':'q','w':'s','s':'w','e':'d','d':'e','r':'f','f':'r','t':'g','g':'t','y':'h','h':'y','u':'j','j':'u','i':'k','k':'i','o':'l','l':'o','9':'0','0':'9','8':'7','7':'8','6':'5','5':'6','4':'3','3':'4','2':'1','1':'2','z':'x','x':'z','c':'v','v':'c','b':'n','n':'b','Q':'A','A':'Q','W':'S','S':'W','E':'D','D':'E','R':'F','F':'R','T':'G','G':'T','Y':'H','H':'Y','U':'J','J':'U','I':'K','K':'I','O':'L','L':'O','Z':'X','X':'Z','C':'V','V':'C','B':'N','N':'B','-':'=','=':'-','<':'>','>':'<',' ':' ','m':'M','M':'m',
    '~':'!','!':'~','@':'#','#':'@','$':'%','%':'$','^':'&','&':'^','*':'(','(':'*',')':'_','_':')','+':'+',
    'P':'p','p':'P','"':"'","'":'"','\n':'\b'}
    for chr1, chr2 in charac.items():
        if chr2 == chrar:
            return chr1

def mistake(chra):
    global replace_time
    global start_time
    if (time.time() - start_time) >= replace_time and chr !="\n":
        replace_time = random.randint(5,10)
        start_time = time.time()
        keyboard.write(change_string(chra))
        # keyboard.write(randomString(1))#
        time.sleep(1)
        keyboard.press_and_release('backspace')
        time.sleep(0.5)


def main():
    # New File read as list.
    filename= "E:\\Mega\\Github\\Scatterplot\\1_plot.r"
    with open(filename) as f:
        lines = f.readlines()
    print(lines)    

    # Pause multipliers
    use_multipliers =True
    comma_multiplier = 7
    stop_multiplier = 4 # end of random value 
    new_line= 12 # end of random value recommended 0.8-1.2
    base= 0.2 # start of random value

    characters=[]
    for line in lines:          # for each line of text (or each message)
        for character in line:          # for each character in each line
            # Is this a comma?
            if character in (',','<','(',')'):
                pause = (base * comma_multiplier) if use_multipliers else base
                characters.append((character, pause, 'comma'))
                continue

            # Is this a new line?
            if character =='\n':
                pause = (base * random.uniform(8,new_line)) if use_multipliers else base
                character=='\n+esc'
                characters.append((character, pause, 'NewLine'))
                continue

            # How about a full stop?
            if character in ('.', '!', '?','-'):
                pause = (base * random.uniform(2,stop_multiplier)) if use_multipliers else base
                characters.append((character, pause, 'stop'))
                continue

            # Just a regular character then.
            pause = random.uniform(0.07,base)
            characters.append((character, pause, 'regular'))
                

    # Final for typing
    # keyboard.press_and_release('alt+tab')
    
    time.sleep(0.5)
    for character, pause, char_type in characters:
        if char_type == 'regular':
            mistake(character)
        keyboard.write(character)
        time.sleep(pause)
        if character == '\n':
            while 1:
                if keyboard.is_pressed('f5') == 1:
                    break
                elif keyboard.is_pressed('f6') == 1:
                    sys.exit("Successfull Exit")
        if keyboard.is_pressed('f4') == 1:
            while 1:
                if keyboard.is_pressed('f5') == 1:
                    break
                elif keyboard.is_pressed('f6') == 1:
                    sys.exit("Successfull Exit")       



main()