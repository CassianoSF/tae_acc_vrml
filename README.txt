############################################
# Autor: Cassiano Surdi Franco
# Data: 12/12/2019
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
############################################

para usar o conversor é necessário ter python3 instalado e usar o seguinte comando no terminal:


python3 caminho/para/obj-wrl.py caminho/para/arquivo.obj caminho/para/arquivo.wrl

ou com o terminal na pasta do projeto:

python3 obj-wrl.py arena.obj arena.wrl

