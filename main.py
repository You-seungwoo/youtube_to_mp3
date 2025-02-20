from pytubefix import YouTube
from pydub import AudioSegment
from tkinter import filedialog, Tk, BooleanVar, Label, TOP, Entry, Checkbutton, Button
import tkinter.messagebox as msgbox
import tkinter.font
import tkinter
import os

window = Tk()
window.title("YOUTUBE CONVERTER")
window.geometry("400x200")
window.resizable(width=False, height=False)

chk_state = BooleanVar()
chk_state.set(False)

## ================================================

def on_button_click():
    try:
        YouTube(input_text.get())
    except:
        msgbox.showwarning("오류", "올바른 링크를 입력해주세요.")
        return

    yt = YouTube(input_text.get())
    dir_path = filedialog.askdirectory(parent=window,initialdir="/",title='저장할 폴더를 선택해주세요.')


    original_path = yt.streams.filter(only_audio=True).first().download(output_path=dir_path, filename=f"{yt.title}.mp3")

    if chk_state.get() == True:
        silence = AudioSegment.silent(duration=30000)
        original_audio = AudioSegment.from_file(original_path)
        result = silence + original_audio 
        try:
            result.export(original_path, format="mp3")
        except:
            msgbox.showerror("저장 실패", "ffmpeg 를 찾을 수 없습니다. https://stackoverflow.com/questions/65836756/python-ffmpeg-wont-accept-path-why 를 참조하세요.")
            os.remove(original_path)
            return

    msgbox.showinfo("완료", "성공적으로 저장했습니다.")

## ================================================

font=tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
label = Label(window, text='YOUTUBE CONVERTER', font=font)
label.pack(side=TOP)

font=tkinter.font.Font(family="맑은 고딕", size=10)
label = Label(window, text='YOUTUBE TO MP3 / Enter a YouTube URL', font=font)
label.pack(side=TOP)

input_text = Entry(window, width=30)
input_text.pack(side=TOP, pady=1)

## pydub 실험용
chk = Checkbutton(window, text='Add space (30s)', var=chk_state)
chk.pack(side=TOP, pady=5)

button = Button(window,  text="Convert", width=15, command=on_button_click)
button.pack(side=TOP, pady=5)

font=tkinter.font.Font(family="맑은 고딕", size=10)
label = Label(window, text='Made by Yoo Seung woo', font=font)
label.pack(side=TOP, pady=2)

window.mainloop()

## =================================







