import basc_py4chan
import random
import os
import sys
import urllib.request
import time
import os.path
path = os.getcwd()


def pullfunc():
    print("▄█ █▀▄▀█ ██     ▄▀  ▄███▄          ▄▄▄▄▄      ▄▄▄▄▀ ▄███▄   ██   █     ▄███▄   █▄▄▄▄ ")
    print("██ █ █ █ █ █  ▄▀    █▀   ▀        █     ▀▄ ▀▀▀ █    █▀   ▀  █ █  █     █▀   ▀  █  ▄▀ ")
    print("██ █ ▄ █ █▄▄█ █ ▀▄  ██▄▄        ▄  ▀▀▀▀▄       █    ██▄▄    █▄▄█ █     ██▄▄    █▀▀▌  ")
    print("▐█ █   █ █  █ █   █ █▄   ▄▀      ▀▄▄▄▄▀       █     █▄   ▄▀ █  █ ███▄  █▄   ▄▀ █  █  ")
    print(" ▐    █     █  ███  ▀███▀                    ▀      ▀███▀      █     ▀ ▀███▀     █   ")
    print("     ▀     █                                                  █                 ▀    ")
    print("          ▀                                                  ▀     By Sen :)         ")
    print("To start please type a board, thread ID, and a folder to save it to")
    boardInput = input("Board: ")
    threadInput = input("Thread ID: ")
    makefolder = input("Folder Name: ")
    board = basc_py4chan.Board(boardInput, https=False, session=None)
    numberofposts = 0
    thread = board.get_thread(threadInput)
    os.mkdir(makefolder)
    madefolder = os.path.join(path, makefolder)

    for post in thread.all_posts:
        if post.has_file==True:
            numberofposts = numberofposts + 1
    answer = None
    while answer not in ("yes", "no"):
        answer = input("pull? y/n: ")
        if answer == "y":

            for post in thread.posts:
                if post.has_file==True:
                    anim="\|/-\|/-"
                    for l in anim:
                        sys.stdout.write(l)
                        sys.stdout.flush()
                        sys.stdout.write('\b')
                        time.sleep(0.2)
                    try:
                        saveto = os.path.join(madefolder, post.filename)
                        urllib.request.urlretrieve(post.file_url, saveto)
                        
                    except Exception:
                        pass 
            print("Done!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            pullfunc()
        elif answer == "n":
            print("aw ok bye")
            time.sleep(3)
            sys.exit(0)
        else:
            print("Please enter y/n.")
pullfunc()

