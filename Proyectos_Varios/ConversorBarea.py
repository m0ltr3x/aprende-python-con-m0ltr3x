from pytube import YouTube ##IMPORTAMOS LA LIBRERIA YOUTUBE LIBRERIA PARA PODER HACER DESCARGAS DE YOUTUBE
from pytube import Playlist ##LIBRERIA IMPORTADA PARA PODER DESCARGAR PLAYLIST
import os ##AÑADIMOS ESTA LIBRERÍA YA QUE ESTA LIBRERÍA NOS PROPORCIONARA QUE TENGAMOS FUNCIONES PARA INTERACTUAR CON NUESTRO SISTEMA OPERATIVO Y SISTEMA DE ARCHIVOS


# MENU PARA PODER ESCOGER NUESTRA OPCION
print("\n")
print("BIENVENIDOS A LA PRIMERA VERSION DEL CONVERSOR DE M0LTREX\n")
print("POR FAVOR, DECIDE UNA OPCION\n")
opcion = '0'
while not(opcion=='5'):
    print(' 1. DESCARGAR EN AUDIO MP3')
    print(' 2. DESCARGAR EN AUDIO WAV')
    print(' 3. DESCARGAR EN VIDEO ALTA DEFINICION MP4')
    print(' 4. OPCIONES PARA DESCARGAR EN PLAYLIST')
    print(' 5. SALIR')

    opcion=input('  --- ¿POR FAVOR, ELIGE UNA OPCION?: ')
    
    if (opcion=='1'):

                    #AQUÍ INTRODUCIMOS LA URL
                    nuestro_Video = YouTube(str(input("Por favor, Introduce el ENLACE de youtube que quieres transformar: ")))
                    
                    #AQUÍ VAMOS A EXTRAER NUESTRO AUDIO
                    video = nuestro_Video.streams.filter(only_audio=True).first()
                    
                    #AQUÍ VAMOS A REVISAR NUESTRA UBICACIÓN PARA GUARDAR NUESTRO ARCHIVO MP3 EN ESTE APARTADO
                    print("introduce el destino donde quieres guardar tu video transformado a MP3: ")
                    destination = str(input(">> ")) or '.'
                    
                    #AQUÍ VAMOS A REVISAR NUESTRA UBICACIÓN PARA GUARDAR NUESTRO ARCHIVO MP3 EN ESTE APARTADO
                    out_file = video.download(output_path=destination)
                    
                    #AQUÍ ESTAMOS NOMBRANDO EL DESTINO DE UBICACIÓN Y ESTE COMANDO HACE QUE REALICE ESE PROCESO
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    
                    #HEMOS GUARDADO CORRECTAMENTE LA CONNVERSIÓN A MP3
                    print(nuestro_Video.title + " NUESTRA CONVERSIÓN A SIDO REALIZADA CON EXITO")
                            
                                
    elif (opcion=='2'):
      
                  #AQUÍ INTRODUCIMOS LA URL
                    nuestro_Video = YouTube(str(input("Por favor, Introduce el ENLACE de youtube que quieres transformar: ")))
                    
                  #AQUÍ VAMOS A EXTRAER NUESTRO AUDIO
                    video = nuestro_Video.streams.filter(only_audio=True).first()
                  
                  #AQUÍ VAMOS A REVISAR NUESTRA UBICACIÓN PARA GUARDAR NUESTRO ARCHIVO WAV EN ESTE APARTADO
                    print("introduce el destino donde quieres guardar tu video transformado a WAV: ")
                    destino = str(input(">> ")) or '.'
                    
                  #AQUÍ ESTAMOS NOMBRANDO EL DESTINO DE UBICACIÓN Y ESTE COMANDO HACE QUE REALICE ESE PROCESO
                    out_file = video.download(output_path=destino)
                    
                  #GUARDAMOS NUESTRO ARCHIVO WAV
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.WAV'
                    os.rename(out_file, new_file)
                    
                  #HEMOS GUARDADO CORRECTAMENTE LA CONNVERSIÓN A wav
                    print()
                    print("A SIDO GUARDADO CON EXITO EN: ", destino)
    
    
    elif (opcion=='3'):
      
                  #AQUÍ INTRODUCIMOS LA URL
                    url_vid = input("Por favor, Introduce el ENLACE de youtube que quieres transformar: ")
                    
                    #AQUÍ VAMOS A EXTRAER NUESTRO AUDIO
                    yt = YouTube(url_vid)
                    print(yt.title)
                    print("introduce el destino donde quieres guardar tu video en alta definición MP4: ")
                    destino = str(input(">> ")) or '.'
                    
                  #AQUÍ VAMOS A EXTRAER NUESTRO VIDEO EN ALTA DEFINICIÓN
                    yt.streams.get_highest_resolution().download(output_path=destino)   
                    print()
                    print("A SIDO GUARDADO CON EXITO EN: ", destino)
                    
    elif (opcion=='4'):
      
      ##OPCION PARA PODER ESCOGER DESCARGAR LA LISTA DE REPRODUCCION DE YOUTUBE
                    url_de_la_pl = input("Por favor, Introduce el ENLACE de youtube que quieres transformar: ")
                    p = Playlist(url_de_la_pl)
                    print()   
                    lista_repro = int(input("Por favor escoja [1] si quieres descargar la lista en Videos | De lo contrario escoja [2] si deseas descargarla en Audio: "))
            
            
                    if lista_repro == 1:
                      
                      ##PRIMERA OPCION PARA TRANSFORMAR A VIDEO TODA LA LISTA DE REPRODUCCIÓN  
                            ubic = input("Por favor, escoge la ubicación donde guardar tu lista escogida: ")
                            ubic = str(input(">> ")) or '.'
                            print()
                            print("La ubicacion que has escogido para guardarlo es: ", ubic)
                            for video in p.videos:
                                video.streams.get_highest_resolution().download(output_path=ubic)
                                print("NUESTRA CONVERSIÓN A SIDO REALIZADA CON EXITO")
                            print()
                            print("A SIDO GUARDADO CON EXITO EN: ", destino)
                                                
                                                
                    if lista_repro == 2:
                      
                      ##SEGUNDA OPCION PARA TRANSFORMAR A AUDIO TODA LA LISTA DE REPRODUCCIÓN   
                            ubic = input("Por favor, escoge la ubicación donde guardar tu lista escogida: ")
                            ubic = str(input(">> ")) or '.'
                            print()
                            print("La ubicacion que has escogido para guardarlo es: ", ubic)
                                            
                            for video in p.videos:
                                video.streams.get_audio_only().download(output_path=ubic)
                            print()
                            print("A SIDO GUARDADO CON EXITO EN: ", destino)
                     
    
    elif (opcion=='5'):
      ##CON ESTA OPCIÓN AUTOMATICAMENTE SALDREMOS DEL MENU 
         print("SALIR DEL MENU")
       
    else:
      ##CON ESTE ELSE LO QUE VAMOS A REALIZAR ES QUE SI NO LE DAMOS A LA OPCIÓN DEL MENU CORRECTA TE PEDIRA QUE INTRODUZCAS BIEN EL NUMERO DEL MENU QUE TENEMOS PROPORCIONADO  
        print('No existe esta opcion')
        
        

#                .-"""-.
#               / .===. \
#               \/ 6 6 \/
#               ( \___/ )
#  ______________\_____/______________
# /                                   \
#| Bienvenidos al conversor de m0ltr3x |
# \___________________________________/
#                |  |  |
#                |_ | _|
#                |  |  |
#                |__|__|  
#                /-'Y'-\
#               (__/ \__)
