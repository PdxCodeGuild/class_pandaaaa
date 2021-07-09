from pytube import YouTube

video_url = YouTube('Paste video url here: ')

print('\n')
print('Video Title')
print(video_url.title) # getting the video title

print('\n')
print('Video Image')
print(video_url.thumbnail_url) # getting the video image

print('\n')
print('Download Video') 

video = video_url.streams.all()
video_url.download() # downloading video