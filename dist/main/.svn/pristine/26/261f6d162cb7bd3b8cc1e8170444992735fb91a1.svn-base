import pafy

video = pafy.new("https://www.youtube.com/watch?v=EQja4bK1k6c")

print video.title
print video.duration
# print video.description
print video.streams
# video.download(filepath="temp")
print video.audiostreams
print video.streams[-1].get_filesize()
print video.getbestaudio()
