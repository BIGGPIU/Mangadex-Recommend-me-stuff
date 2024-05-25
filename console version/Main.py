import curses
from curses import wrapper
from collections import Counter
from time import sleep
from mainbackend import searchformanga
import webbrowser



#from mainbackend import maincall
#hey me make sure to get rid of the hashtags when you're ready to release. I only added them so it doesnt take forever to test. also you may want to change the genre list into a string to make counting easier.

#by the way curses uses y x for coords.
def main(stdscr):
    stdscr.clear()
    maxx = 60
    maxy = 30
    x=0
    y=1
    xone = 60
    xtwo = 0
    while True:
        if x != (maxx+1):
            stdscr.addstr(0,x,"█")
            sleep(0.01)
            x+=1
            stdscr.refresh()
        if x == (maxx+1):
            if y != (maxy+1):
                stdscr.addstr(y,0,"█")
                stdscr.addstr(y,60,"█")
                sleep(0.01)
                y+=1
                stdscr.refresh()
            if y == (maxy+1):
                stdscr.addstr(30,xone,"█")
                stdscr.addstr(30,xtwo,"█")
                xtwo += 1
                xone -= 1
                sleep(0.01)
                stdscr.refresh()
                if xtwo == 31:
                    break

    stdscr.addstr(5,17,"MANGADEX RECOMMENDATIONS",curses.A_BOLD) #23 is the center for X I have no clue why but I think its just like that 
    stdscr.refresh()
    sleep(0.5)
    stdscr.addstr(6,23,"Made by BIGG")
    stdscr.refresh()
    sleep(0.5)
    stdscr.addstr(15,18,"Get your recommendations")
    stdscr.addstr(17,19,"Input your information")
    stdscr.addstr(27,2,"Use up and down to navigate. Hit A to select")
    stdscr.addstr(28,2,"MOTD: gacha addiction is fake keep gambling")
    stdscr.refresh()

    x=0
    y=0
    while True:
        key = stdscr.getkey()
        if key == ("KEY_DOWN"):
            x+=1
            if y == 0:
                y+=1

        if key == ("KEY_UP"):
            x-=1
            if y == 0:
                stdscr.addstr(15,18,"Get your recommendations",curses.A_STANDOUT)
                y+=1
                x = 0
        

        if x == 1:
            stdscr.addstr(17,19,"Input your information",curses.A_STANDOUT)
            stdscr.addstr(15,18,"Get your recommendations")

        if x == 0:
            stdscr.addstr(15,18,"Get your recommendations",curses.A_STANDOUT)
            stdscr.addstr(17,19,"Input your information")

        if x == -1:
            x = 0

        if x == 2:
            x = 1
        
        if key == ("a"):
            if y == 1:
                if x == 0:
                    stdscr.clear()
                    break
                if x == 1:
                    stdscr.clear()
                    stdscr.addstr(17,19,"Please input your information in settings.txt I have not finished this yet.")
                    stdscr.refresh()
                    sleep(5)
                    webbrowser.open("https://media.tenor.com/JwDQsf0cKyMAAAAi/arknights-u-official-uofficial-eureka-arknights-gif.gif",1)

        stdscr.refresh()

    maxx = 60 # I know this is a nooby thing to do but idc
    maxy = 30
    x=0
    y=1
    xone = 60
    xtwo = 0
    while True:
        if x != (maxx+1):
            stdscr.addstr(0,x,"█")
            x+=1
            stdscr.refresh()
        if x == (maxx+1):
            if y != (maxy+1):
                stdscr.addstr(y,0,"█")
                stdscr.addstr(y,60,"█")
                y+=1
                stdscr.refresh()
            if y == (maxy+1):
                stdscr.addstr(30,xone,"█")
                stdscr.addstr(30,xtwo,"█")
                xtwo += 1
                xone -= 1
                stdscr.refresh()
                if xtwo == 31:
                    break
    
    stdscr.addstr(25,2,"LOADING") #this is a fake loading screen I'm adding this to be funny
    stdscr.addstr(27,2,"10% █")
    sleep(0.01)
    stdscr.refresh()
    stdscr.addstr(27,2,"20% ██")
    sleep(0.20)
    stdscr.refresh()
    stdscr.addstr(27,2,"30% ████")
    sleep(0.40)
    stdscr.refresh()
    stdscr.addstr(27,2,"40% ██████")
    sleep(0.80)
    stdscr.refresh()
    stdscr.addstr(27,2,"50% ████████")
    sleep(0.30)
    stdscr.refresh()
    stdscr.addstr(27,2,"60% ██████████")
    sleep(0.30)
    stdscr.refresh()
    stdscr.addstr(27,2,"70% ████████████")
    sleep(0.100)
    stdscr.refresh()
    stdscr.addstr(27,2,"80% ██████████████")
    sleep(0.10)
    stdscr.refresh()
    stdscr.addstr(27,2,"90% ████████████████")
    sleep(0.50)
    stdscr.refresh()
    stdscr.addstr(27,2,"99% █████████████████")
    sleep(1)
    stdscr.refresh()
    identify,name,favorite = searchformanga()
    sleep(5)
    
    stdscr.clear()

    
    stdscr.addstr(20,2,f"your favorite genres are:")
    stdscr.addstr(21,1,f"{favorite[0]}")
    stdscr.addstr(22,1,f"{favorite[1]}")
    stdscr.addstr(23,1,f"{favorite[2]}")
    stdscr.addstr(24,1,f"{favorite[3]}")
    stdscr.addstr(25,1,f"{favorite[4]}")

    
    stdscr.addstr(3,2,"Use the arrow keys to navigate. hit A to open a manga in your browser")
    stdscr.addstr(4,2,"Use E to end the program.")
    stdscr.addstr(5,2,"your recommendations are:")
    l = 6
    m = 0
    while m != len(identify):
        stdscr.addstr(l,1,f"{name[m]}")
        m+=1
        l+=1
    


    m = 0
    l = 6
    select = 0
    while True:
        key = stdscr.getkey()
        if key == ("KEY_DOWN"):
            l+=1
            m+=1
            try:
                stdscr.addstr(l,1,f"{name[m]}",curses.A_STANDOUT)
                stdscr.addstr(l-1,1,f"{name[m-1]}")
            except:
                l-=1
                m-=1
        if key == ("KEY_UP"):
            l-=1
            m-=1
            if l == 5:
                l=6
                m+=1
            else:
                try:
                    stdscr.addstr(l,1,f"{name[m]}",curses.A_STANDOUT)
                    stdscr.addstr(l+1,1,f"{name[m+1]}")
                except:
                    l+=1
                    m-=1
        if key == ("a"):
            webbrowser.open(f"https://mangadex.org/title/{identify[m]}",new=2) 
        if key == ("e"):
            break

        stdscr.refresh()



   
    #print(mostpopular)
    # note to self I think I can move this to mainbackend.py but im not going to do it for now since I need this info right now so im not going to take a decade for bug testing. Just remember to do this later
    #permgenre,permmanga = maincall()
    #print (permgenre,permmanga) 



def link(uri, label=None):
    if label is None: 
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)


def getfave():
    f = open("dev.txt","r")
    permgenre = f.readline()
    permgenre = permgenre.replace("[","")
    permgenre = permgenre.replace("]","")
    permgenre = permgenre.replace("'","")
    permgenre = permgenre.replace('"',"")
    permgenre = permgenre.replace("\n","")
    permgenrelist = permgenre.split(",")
    genredict = Counter(permgenrelist)
    mostpopular = sorted(genredict, key=genredict.get, reverse=True)[:5]
    return mostpopular


if __name__ == "__main__":
    wrapper(main)