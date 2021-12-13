import pyvisa
rm = pyvisa.ResourceManager()
resource_list=rm.list_resources()
print(resource_list)


inst = rm.open_resource('GPIB0::28::INSTR')
print(inst.query("*IDN?"))



class Freq:
    def __init__(self, instr):
        self.instr = instr
    #set SA centFreq
    def set_freq(self, Freq, unit=" M"):
        responce = self.instr.write("FREQ " + Freq + unit+'Hz')
        print("FREQ " + Freq + unit+'Hz')
        return responce

    def get_freq(self):
        responce = self.instr.query("FREQ?")
        return responce

class Level:
    def __init__(self, instr):
        self.instr = instr
    #set SA centFreq
    def set_power(self,power):
        responce = self.instr.write("POW " + power)
        return responce

    def get_power(self):
        responce = self.instr.query("POW?")
        return responce

class RfOutPut:
    def __init__(self, instr):
        self.instr = instr
    #set SA centFreq
    def set_rf_power(self,turn):
        #open    ON   or 1
        #close   OFF  or 0
        responce = self.instr.write("OUTP " + turn)
        return responce


class SingalGenerator(Freq,Level,RfOutPut):
    def __init__(self, instr):
        self.instr = instr


def main():
    new_instr = SingalGenerator(inst)
    print(new_instr.get_power())
    print(new_instr.get_freq())
    new_instr.set_freq('5180')
    new_instr.set_power('0')
    print(new_instr.get_power())
    print(new_instr.get_freq())
    new_instr.set_rf_power('0')



if __name__ == '__main__':
    main()
