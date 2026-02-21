playlist = list(map(int,input("enter duration of playlist:").split()))
invalid_data= False
for duration in playlist:
    if duration <= 0:
        invalid_data= True
        break
if invalid_data:
   print("invalid playlist ")
else:
     total_time=0
     for duration in playlist:
        total_time += duration
     total_song = len(playlist)
     repeated = False
for duration in playlist:
    if playlist.count(duration) > 1:
        repeated= True
        break
smallest = min(playlist)
largest = max(playlist)
var = largest-smallest
if total_song ==1:
    category= "irregular playlist"
    recom="add more songs"
elif total_time <  300:
     category = "very short playlist"
     recom="add more songs"
elif total_time > 3600:
     category = "very long playlist"
     recom="reduce some songs"
elif repeated :
     category ="repeated  playlist"
     recom="add variety"
elif var <= 120:
     category ="balanced playlist"
     recom="nice taste"
else:
     category ="irregular playlist"
     recom="organise songs"
print("total duration:", total_time,"seconds")
print("songs:", total_song)
print("category:", category)
print("recommendation:", recom)


