class Televisao():
    def __init__(self,modeloTV):
        self.modeloTV=modeloTV
        self.canal = 0
        self.volume = 0
        self.estado = 'desligado'

    def ligar(self):
        self.canal=1
        self.volume=10
        self.estado='ligado'

    def desligar(self):
        self.estado = 'desligado'

    def aumentarVolume(self,volume):
        if volume is None:
            self.volume += 1
            if self.volume > 100:
                self.volume = 100
            return
        if volume.isdigit() and int(volume) < 100:
            self.volume = int(volume)
        else:
            print(f'volume {volume} indevido')

    def estadoTv(self):
        print(f'{self.modeloTV}\n'
            f'{self.estado}\n'
            f'canal {self.canal} Volume {self.volume}')


tv1=Televisao('LG 55"')
tv1.estadoTv()
tv1.ligar()
tv1.aumentarVolume(None)
tv1.estadoTv()
tv1.aumentarVolume('70')
tv1.estadoTv()