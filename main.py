import pruebas

genero = input("¿De que genero es tu personaje? ")
if genero=="hombre":
    raza = input("¿De que raza es tu personaje? ")
    if raza =="bioandroide":
        print ("Tu personaje es Cell")
        pruebas.imprimir_image("Imagen/cell.png",100)
    if raza =="demonio":
        print ("Tu personaje es Super Boo")
        pruebas.imprimir_image("Imagen/super-boo.png",100)
    if raza =="Shinjin":
        print ("Tu personaje es Kaio-sama")
        pruebas.imprimir_image("Imagen/kaio-sama.png",100)
    if raza =="humano":
        edad = input("¿De que edad es tu personaje? ")
        if edad=="adulto":
            color_cabello = input("¿De que color tiene el cabello tu personaje? ")
            if color_cabello=="no":
                color_ropa = input("¿De que color tiene la ropa tu personaje? ")
                if color_ropa=="naranja":
                    bello_facial = input("¿tu personaje tiene barba o bigote? ")
                    if bello_facial=="no":
                        print ("Tu personaje es Krilin")
                        pruebas.imprimir_image("Imagen/krilin.png",100)
                    if bello_facial=="barba":
                        print ("Tu personaje es el Maestro Roshi")
                        pruebas.imprimir_image("Imagen/maestro-roshi.png",100)
            if color_cabello=="negro":
                color_ropa = input("¿De que color tiene la ropa tu personaje?")
                if color_ropa=="naranja":
                    print ("Tu personaje es Yamcha")
                    pruebas.imprimir_image("Imagen/yamcha.png",100)
                if color_ropa=="cafe":
                    print ("Tu personaje es Mr.Satan")
                    pruebas.imprimir_image("Imagen/mr-satam.png",100)

    if raza =="namekusei":
        edad = input("¿De que edad es tu personaje? ")
        if edad=="adulto":
            color_cabello = input("¿De que color tiene el cabello tu personaje? ")
            if color_cabello=="no":
                color_ropa = input("¿De que color tiene la ropa tu personaje? ")
                if color_ropa=="blanco":
                    print ("Tu personaje es Kami-Sama")
                    pruebas.imprimir_image("Imagen/kami-sama.png",100)
                if color_ropa=="morado":
                    print ("Tu personaje es Piccolo")
                    pruebas.imprimir_image("Imagen/piccolo.png",100)

    if raza =="sayajin":
        edad = input("¿De que edad es tu personaje? ")
        if edad=="adulto":
            color_cabello = input("¿De que color tiene el cabello tu personaje?" )
            if color_cabello=="azul":
                print ("Tu personaje es Trunks")
                pruebas.imprimir_image("Imagen/trunks.png",100)
            if color_cabello=="verde":
                print ("Tu personaje es Broly")
                pruebas.imprimir_image("Imagen/broly.png",100)
            if color_cabello=="rubio":
                color_ropa = input("¿De que color tiene la ropa tu personaje? ")
                if color_ropa=="azul":
                    print ("Tu personaje es Vegetto SSJ")
                    pruebas.imprimir_image("Imagen/vegetto-ssj.png",100)
                if color_ropa=="naranja":
                    print ("Tu personaje es Goku SSJ")    
                    pruebas.imprimir_image("Imagen/goku-ssj.png",100)
            if color_cabello=="negro":
                color_ropa = input("¿De que color tiene la ropa tu personaje? ")
                if color_ropa=="naranja":
                    print ("Tu personaje es Goku") 
                    pruebas.imprimir_image("Imagen/goku.png",100)
                if color_ropa=="azul":
                    bello_facial = input("¿tu personaje tiene barba o bigote? ")
                    if bello_facial=="no":
                        rastreador = input("¿tu personaje tiene usa rastreador? ")
                        if rastreador=="no":
                            print ("Tu personaje es Gogeta")
                            pruebas.imprimir_image("Imagen/gogeta.png",100)
                        if rastreador=="si":
                            print ("Tu personaje es Vegeta")
                            pruebas.imprimir_image("Imagen/vegeta.png",100)
                if color_ropa=="negro":
                    bello_facial = input("¿tu personaje tiene barba o bigote? ")
                    if bello_facial=="no":
                        rastreador = input("¿tu personaje tiene usa rastreador? ")
                        if rastreador=="no":
                            print ("Tu personaje es Gohan")
                            pruebas.imprimir_image("Imagen/gohan.png",100)
                        if rastreador=="si":
                            cabello_largo = input("¿tu personaje tiene el cabello largo? ")
                            if cabello_largo=="si":
                                print ("Tu personaje es Raditz")
                                pruebas.imprimir_image("Imagen/raditz.png",100)
                            if cabello_largo=="no":
                                print ("Tu personaje es Bardok")
                                pruebas.imprimir_image("Imagen/bardock.png",100)

        if edad=="niño":
            color_cabello = input("¿De que color tiene el cabello tu personaje? ")
            if color_cabello=="rubio":
                print ("Tu personaje es Gotenks SSJ")
                pruebas.imprimir_image("Imagen/gotenks-ssj.png",100)
            if color_cabello=="negro":
                color_ropa = input("¿De que color tiene la ropa tu personaje? ")
                if color_ropa=="blanco":
                    print ("Tu personaje es Gotenks")
                    pruebas.imprimir_image("Imagen/gotenks.png",100)
                if color_ropa=="azul":
                    print ("Tu personaje es Goku niño")
                    pruebas.imprimir_image("Imagen/goku-nino.png",100)

elif genero=="mujer":
    raza = input("¿De que raza es tu personaje? ")
    if raza =="humano":
        edad = input("¿De que edad es tu personaje? ")
        if edad=="adulto":
            color_cabello = input("¿De que color tiene el cabello tu personaje? ")
            if color_cabello=="negro":
                print ("Tu personaje es Milk")
                pruebas.imprimir_image("Imagen/milk.png",100)
            if color_cabello=="azul":
                print ("Tu personaje es Bulma")
                pruebas.imprimir_image("Imagen/bulma.png",100)

