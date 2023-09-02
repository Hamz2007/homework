from colorama import Back , Fore , Style
while True:
    from pytube import YouTube
    strams1=input(Fore.LIGHTBLACK_EX+"VIDEO = 1 OR AUDIO = 2 ? : ")
    link=input(Fore.LIGHTBLACK_EX+"LINK :")
    
    
    
    if strams1 == "1":
        
        y=YouTube(link)
        s=y.streams.get_highest_resolution()
        print(Fore.RED+s.default_filename)
        print("DOWNLOAD START . . .")
        s.download(":\DOWNLOAD PYTUBE")
        print(Fore.GREEN+"DONE VIDEO !")
        


    elif strams1 == "2" :
        y=YouTube(link)
        f=y.streams.get_audio_only()
        print(Fore.RED+f.default_filename)
        print("DOWNLOAD START . . .")
        f.download("D:\DOWNLOAD PYTUBE")
        print(Fore.GREEN+"DONE AUDIO !")