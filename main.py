genero = input("¿De que genero es tu personaje?")
if genero=="hombre":
    raza = input("¿De que raza es tu personaje?")
    if raza =="bioandroide":
        print ("Tu personaje es Cell")
    if raza =="demonio":
        print ("Tu personaje es Super Boo")
    if raza =="Shinjin":
        print ("Tu personaje es Kaio-sama")

    if raza =="humano":
        edad = input("¿De que edad es tu personaje?")
        if edad=="adulto":
            color_cabello = input("¿De que color tiene el cabello tu personaje?")
            if color_cabello=="n/a":
                color_ropa = input("¿De que color tiene la ropa tu personaje?")
                if color_ropa=="naranja":
                    bello_facial = input("¿tu personaje tiene barba o bigote?")
                    if bello_facial=="n/a":
                        print ("Tu personaje es Krilin")
                    if bello_facial=="barba":
                        print ("Tu personaje es el Maestro Roshi")
            if color_cabello=="negro":
                color_ropa = input("¿De que color tiene la ropa tu personaje?")
                if color_ropa=="naranja":
                    print ("Tu personaje es Yamcha")
                if color_ropa=="cafe":
                    print ("Tu personaje es Mr.Satan")

    if raza =="namekusei":
        edad = input("¿De que edad es tu personaje?")
        if edad=="adulto":
            color_cabello = input("¿De que color tiene el cabello tu personaje?")
            if color_cabello=="n/a":
                color_ropa = input("¿De que color tiene la ropa tu personaje?")
                if color_ropa=="blanco":
                    print ("Tu personaje es Kami-Sama")
                if color_ropa=="morado":
                    print ("Tu personaje es Piccolo")

    if raza =="sayajin":
        edad = input("¿De que edad es tu personaje?")
        if edad=="adulto":
            color_cabello = input("¿De que color tiene el cabello tu personaje?")
            if color_cabello=="azul":
                print ("Tu personaje es Trunks")
            if color_cabello=="verde":
                print ("Tu personaje es Broly")
            if color_cabello=="rubio":
                color_ropa = input("¿De que color tiene la ropa tu personaje?")
                if color_ropa=="azul":
                    print ("Tu personaje es Vegetto SSJ")
                if color_ropa=="naranja":
                    print ("Tu personaje es Goku SSJ")    
            if color_cabello=="negro":
                color_ropa = input("¿De que color tiene la ropa tu personaje?")
                if color_ropa=="naranja":
                    print ("Tu personaje es Goku") 
                if color_ropa=="azul":
                    bello_facial = input("¿tu personaje tiene barba o bigote?")
                    if bello_facial=="n/a":
                        rastreador = input("¿tu personaje tiene usa rastreador?")
                        if rastreador=="no":
                            print ("Tu personaje es Gogeta")
                        if rastreador=="si":
                            print ("Tu personaje es Vegeta")
                if color_ropa=="negro":
                    bello_facial = input("¿tu personaje tiene barba o bigote?")
                    if bello_facial=="n/a":
                        rastreador = input("¿tu personaje tiene usa rastreador?")
                        if rastreador=="no":
                            print ("Tu personaje es Gohan")
                        if rastreador=="si":
                            cabello_largo = input("¿tu personaje tiene el cabello largo?")
                            if cabello_largo=="si":
                                print ("Tu personaje es Raditz")
                            if cabello_largo=="no":
                                print ("Tu personaje es Bardok")

        if edad=="niño":
            color_cabello = input("¿De que color tiene el cabello tu personaje?")
            if color_cabello=="rubio":
                print ("Tu personaje es Gotenks SSJ")
            if color_cabello=="negro":
                color_ropa = input("¿De que color tiene la ropa tu personaje?")
                if color_ropa=="blanco":
                    print ("Tu personaje es Gotenks")
                if color_ropa=="azul":
                    print ("Tu personaje es Goku niño")

elif genero=="mujer":
    raza = input("¿De que raza es tu personaje?")
    if raza =="humano":
        edad = input("¿De que edad es tu personaje?")
        if edad=="adulto":
            color_cabello = input("¿De que color tiene el cabello tu personaje?")
            if color_cabello=="negro":
                print ("Tu personaje es Milk")
            if color_cabello=="azul":
                print ("Tu personaje es Bulma")