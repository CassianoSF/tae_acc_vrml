############################################
# Autor: Cassiano Surdi Franco
# Data: 12/12/2019
############################################
#
# Conversor Waverformat(.obj) to VRLM (.wrl)
# A conversão segue o padrao VRML 2.0 e se aproveita o recurso IndexedFaceSet
# segundo a documentação encontrada em http://www.c3.hu/cryptogram/vrmltut/part5.html#5.3indexedfacefaceset
# Essa maneira otimiza a utlização dos vértices, sem a necessidade de repeti-los no código.
# Eu já havia criado um importador Waveformat para OpenGL 3+ em um trabalho de Computação gráfica com o professor Jacson
# Esse trabalho pode ser encontrado em https://github.com/CassianoSF/pyong-hau-ki
# E o importador em https://github.com/CassianoSF/pyong-hau-ki/blob/master/Loader.py
# Muito similar, porem lá eu fazia mapeamento de textura
# No VRLM 2.0 não encontrei a documentação completa para implementar texturas com IndexedFaceSet
#
############################################

import sys

class Parser:
    def __init__(self, arquivoWRL, arquivoOBJ):
        self.arquivoWRL = arquivoWRL
        self.arquivoOBJ = arquivoOBJ
        self.faceBuff = []
        self.state = 'start'
        self.def_count = 2
        self.vert_count = 0
        self.norm_count = 0

    def processFaces(self):
        coordIndex = []
        normalIndex = []
        for line in self.faceBuff:
            coordIndexFace = []
            normalIndexFace = []
            for face in line.split(' '):
                coordIndexFace.append(str(int(face.split('/')[0]) - 1 - self.vert_count))
                normalIndexFace.append(str(int(face.split('/')[2]) - 1 - self.norm_count))
            coordIndex.append(coordIndexFace)
            normalIndex.append(normalIndexFace)

        self.arquivoWRL.write("                  ]\n")
        self.arquivoWRL.write("                }\n")
        self.arquivoWRL.write("                coordIndex [\n")

        for face in coordIndex:
            self.arquivoWRL.write("                    " + ' '.join(face) + " -1\n")

        self.arquivoWRL.write("                ]\n")
        self.arquivoWRL.write("                normalIndex [\n")

        for face in normalIndex:
            self.arquivoWRL.write("                    " + ' '.join(face) + " -1\n")

        self.arquivoWRL.write("                ]\n")
        self.arquivoWRL.write("              }\n")
        self.arquivoWRL.write("            }\n")
        self.arquivoWRL.write("          ]\n")
        self.arquivoWRL.write("        }\n")

        self.faceBuff = []

    def checkStateChange(self, next_state):
        if (self.state == 'face' and next_state != 'face'):
            self.processFaces()
        elif (self.state != 'vertex' and next_state == 'vertex'):
            self.def_count+=1
            self.arquivoWRL.write("              geometry DEF __"+ str(self.def_count) +" IndexedFaceSet {\n")
            self.arquivoWRL.write("                solid FALSE\n")
            self.arquivoWRL.write("                coord Coordinate {\n")
            self.arquivoWRL.write("                  point [\n")
        elif (self.state != 'normal' and next_state == 'normal'):
            self.arquivoWRL.write("                  ]\n")
            self.arquivoWRL.write("                }\n")
            self.arquivoWRL.write("                normal Normal {\n")
            self.arquivoWRL.write("                  vector [\n")asdnasjd
        self.state = next_stateasdnbfçiosdafbnasdfldsanbfpasdjfhbp

    def start(self):
        self.arquivoWRL.write("#VRML V2.0 utf8\n")
        self.arquivoWRL.write("DEF __1 Transform {\n")
        self.arquivoWRL.write("  children [\n")
        self.arquivoWRL.write("    DEF __2 Group {\n")
        self.arquivoWRL.write("      children [\n")

        aux_vert_count = 0
        aux_norm_count = 0

        for line in self.arquivoOBJ:
            if line[0:2] == "o ":
                self.checkStateChange('object')
                self.vert_count = aux_vert_count
                self.norm_count = aux_norm_count
                self.arquivoWRL.write("        DEF " + line[2:-1].replace(".", "_") + " Group {\n")
                self.arquivoWRL.write("          children [\n")
                self.arquivoWRL.write("            DEF " + line[2:-1].replace(".", "_") + "_Shape Shape {\n")
                self.def_count+=1
                self.arquivoWRL.write("              appearance DEF __"+ str(self.def_count) +" Appearance {\n")
                self.def_count+=1
                self.arquivoWRL.write("                material DEF __"+ str(self.def_count) +" Material {\n")
                self.arquivoWRL.write("                  ambientIntensity 1\n")
                self.arquivoWRL.write("                  shininess 0.324\n")
                self.arquivoWRL.write("                  specularColor 0.5 0.5 0.5\n")
                self.arquivoWRL.write("                }\n")
                self.arquivoWRL.write("              }\n")
            if line[0:2] == "v ":
                aux_vert_count +=1
                self.checkStateChange('vertex')
                self.arquivoWRL.write("                    " + line[2:-1] + "\n")
            if line[0:2] == "vn":
                aux_norm_count +=1
                self.checkStateChange('normal')
                self.arquivoWRL.write("                    " + line[2:-1] + "\n")
            if line[0:2] == "f ":
                self.checkStateChange('face')
                self.faceBuff.append(line[2:-1])


        self.processFaces()
        self.arquivoWRL.write("      ]\n")
        self.arquivoWRL.write("    }\n")
        self.arquivoWRL.write("  ]\n")
        self.arquivoWRL.write("}\n")


        self.arquivoOBJ.close()
        self.arquivoWRL.close()




if len(sys.argv) >= 3:
    print("Numero de argumentos passado corretamente")
else:
    print("Falta argumentos ($python obj-wrl.py file.obj file.wrl)")
    sys.exit(1)


# Abre o arquivo obj para leitura
try:
    arquivoOBJ = open(sys.argv[1],"r")
except Exception:
    print("Arquivo OBJ não encontrado")
    sys.exit(1)


# Abre arquivo wrl em modo escrita
try:
    arquivoWRL = open(sys.argv[2],"w")
except Exception:
    print("Arquivo WRL não pode ser aberto")
    sys.exit(1)

Parser(arquivoWRL, arquivoOBJ).start()