from moviepy.editor import *

#編集したい動画のパス
file_path = "./movie.mp4"

#切り出し開始時刻。秒で表現
start = 5 

#切り出し終了時刻。同じく秒で表現
end = 20 

#編集後のファイル保存先とパス
save_path = "sample_cut.mp4"

#ビデオのカット開始
video = VideoFileClip(file_path).subclip(start, end)

#Many options...#書き込み
video.write_videofile(save_path,fps=29) 