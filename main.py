import lexer
import time
import pysinewave
import musicalbeeps

player = musicalbeeps.Player(volume=1,
                             mute_output=False)
if __name__ == "__main__":
    lexer = lexer.Lexer("main.py")
    obj = lexer.deconstructCode()
    #sinewave = pysinewave.SineWave(pitch=obj[0].pitch, pitch_per_second=10)
    #sinewave.play()
    obj.pop(0)
    for obje in obj:
        time.sleep(0.8)
        player.play_note(obje.note, 0.8)
        print(obje)
        #sinewave.set_pitch(obje.pitch)
