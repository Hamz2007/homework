video_games={
    "action" : "sekiro" ,
    "sport" : "fifa",
    "adventure":"uncharted"

}

video_games1={
    "chooter": "call of duty",
    "horror":"aesldent evil"
}
video_games.pop("sport")
video_games.setdefault("fighting",None)
video_games.update(video_games1)
video_games1=list(video_games.keys())
video_games1=list(video_games.values())
video_games1=list(video_games.items())

print(video_games)