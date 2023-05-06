import lexer
import time
import pysinewave
if __name__ == "__main__":
    lexer = lexer.Lexer("main.py")
    obj = lexer.deconstructCode()
    sinewave = pysinewave.SineWave(pitch=obj[0].pitch, pitch_per_second=10)
    sinewave.play()
    obj.pop(0)
    for obje in obj:
        time.sleep(2)
        print(obje)
        sinewave.set_pitch(obje.pitch)
