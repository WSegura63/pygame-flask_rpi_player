from flask import Flask, render_template, request
import pygame
##import os
pygame.init()

pygame.mixer.init()

songs = ["song_1.mp3","song_2.mp3","song_3.mp3","song_4.mp3"]
indx = 0

class Actions:
    ##corregir nextsong
    def nextsong():
        global indx
        if indx < len(songs):
            indx += 1
            pygame.mixer.music.load(songs[indx])
            pygame.mixer.music.play()
            if indx != (len(songs)-1):
                pygame.mixer.music.queue(songs[indx+1])
            else:
                pygame.mixer.music.queue(songs[0])
        else:
            indx = 0
            pygame.mixer.music.stop()
            pygame.mixer.music.load(songs[indx]) 
            pygame.mixer.music.play()
    ##
    def prevsong():
        global indx
        if indx == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(songs[0]) 
            pygame.mixer.music.play()
        else:    
            indx -= 1
            pygame.mixer.music.load(songs[indx])
            pygame.mixer.music.play()
            pygame.mixer.music.queue(songs[indx+1])

##Arranque Flask y creación del servidor
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global indx
    print(request.method)
    if request.method == 'POST': ##Botones del cliente
            if request.form.get('playsong') == 'playsong':
                pygame.mixer.music.load(songs[0])
                pygame.mixer.music.play()
                pygame.mixer.music.queue(songs[1])
                print("Playing Song")
            elif  request.form.get('stopsong') == 'stopsong':
                ##
                pygame.mixer.music.stop()
                index = 0
                print("Player Stopped")
            elif  request.form.get('prevsong') == 'prevsong':
                Actions.prevsong()
                print("Previous Song")
            elif  request.form.get('nextsong') == 'nextsong':
                Actions.nextsong()
                print("Next Song")
                print(indx)
            else:
                return render_template("index.html")
    elif request.method == 'GET':
            print("No Post Action")
    return render_template('index.html')


if __name__ == '__main__': ##Inicia servidor
    app.run(debug=True, host='0.0.0.0')