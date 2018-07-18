# 1mwtt - helpers

## Table of Contents
=====================
1. [How to clone repository?](#how-to-clone-repository)
1. [How to update my local repo?](#how-to-update-my-local-repo)
1. [How to start with Python?](#how-to-start-with-python)
1. [How to run python script?](#how-to-run-python-script)
1. [How to remember my git credentials?](#remember-git-credentials)

## How to clone repository
First you need to [install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and
make a fork form [toolkitten](https://github.com/1millionwomentotech/toolkitten) .

![fork repo](https://image.ibb.co/jnFfyd/fork.png)

Go to your cloned toolkitten project `https://github.com/{username}/toolkitten`, than click clone the repo and copy git url.

![clone repo](https://image.ibb.co/dz6ndd/cone_git.png)

Next step is to open your console:
- Mac - you can open [terminal](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) or download cmd emulator [iterm2](https://www.iterm2.com/).
- Windows - search for `PowerShell` (only if you have windows 10) or `GitBash` in Start Menu or download console emulator e.g. [cmdr](http://cmder.net/).
- Linux - just type cmd in Start Menu.

You can now decide which directory you would like to dedicate to clone your local repo. When you open the console you will land in your User folder. It should be something like `C:\Users\username`. You can create there dedicated folder for you projects by typing `mkdir {put here name of your project}` for example `mkdir projects`. Than step into this folder by typing `cd {put here name of your project}` e.g. `cd projects`. Next clone your repo locally by git command `git clone {put here cloned git directory}` e.g. `git clone https://github.com/username/toolkitten.git`.

Now you have your own local instance of #1mwtt :).

> Tips: If you want to clone a repo elsewhere use [cmd cheat sheet](https://i.imgur.com/ZiCzX.png) to do it.

## How to update my local repo
 with changes form 1millionwomentotech/toolkitten
- First [set your upstream](https://help.github.com/articles/configuring-a-remote-for-a-fork/).
- Now [make upstream sync](https://help.github.com/articles/syncing-a-fork/) with your origin
- The last step is to make a push

## How to start with Python
You should install python https://www.python.org/getit/. Please install version Python 3.7.0. It will be easier to do exercises with Ilona because syntax is the same.

Remember to check `Add Python 3.7 to PATH` otherwise you will get the error `py is not recognized as an internal or external command,
operable program or batch file`

You can also click `Disable path length limit` - it allowed you to add more code into your console.

![install python](https://image.ibb.co/eV05Gy/add_python.png)

How to start python 3.7 version in console? Simply by typing `py` in terminal (commend line). It will work if you are on Windows and you installed python through the steps above.
You should also be able to change version by invoking python with exact version number by command  `py -3.7` or `py -2.7`.

- You can get more info by going to [python doc windows](https://docs.python.org/3/using/windows.html)
- If you are on macintosh and have a problem check out [python doc mac](https://docs.python.org/3/using/mac.html)

## How to run python script

Open your console, than make sure that you are in proper directory by typing `pwd` in your console. You will see in which directory you are. Check if your script is in the same directory. If your project is not in the same directory than you can go to that directory by command `cd` (change directory) for example `cd C:\Users\username\projects\toolkitten\summer-of-code\week-01`. Check if there is your python script file by typing `ls`. You will see all the files that are in this directory. If there is your `yourfile.py` you can run it by command `py yourfile.py` or `python yourfile.py` depending on your python path configuration.

## How to close python running in console
If you don’t know how to exit, just type exit and you’ll get the hint :).

![close console](https://image.ibb.co/kiUFyd/exit.png)

As you see you can type exit() or Ctrl-Z and than enter.

## How to remember my git credentials
Did you hear something about ssh key? If not you need to check it out!
https://help.github.com/articles/connecting-to-github-with-ssh/
How to run JavaScript?
