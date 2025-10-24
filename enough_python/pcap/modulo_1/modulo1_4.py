# modulo 1 4 ecosistema de paquetes de python y como usarlo
# dos entidades basicas :
## un repositorio centralizado de todos los paquetes de software disponibles
## una herramienta que permite a los usuarios acceder al repositorio
## Python Working Group parte del python software foundation es el groupo que mantiene los paquetes de pypi y en cargo de diseminacion (publier)
### https://wiki.python.org/psf/PackagingWG.
## el sitio de pypi
### https://pypi.org/

## en julio 2021 PyPi albergaba 315000 proyectos, 4500000 archivos administrados por 520000 usuarios
## hoy en dia 675781 proyectos , 15390307 archivos y 954485 usuarios
## Pypi no es el unico repo de Python disponible, pero si es el mas importante
## Ye International Python Software Emporium viene del Cheese Shop en la peli Monty Python que ni siquiera vende queso

## para hacer uso de la tienda PyPi shop, tendra que tener la herramienta pip
### pip se refiere a Pip installs Packages (or Pip Installs Python)

## pip a veces viene con Python pero en otras ocasiones tendra que instalarlo
### en windows, pip viene con Python pero si la variable PATH esta mal configurada, podria ser que no esté disponible
#### pip --version # para ver la version de pip
#### la forma mas facil de bien configurar la variable PATH es reinstalar Python indicando al instalador que lo configure por ti
### pip en linux
### depende de la distribucion, por ejemplo Gentoo ya viene instalado pip
### una distribucion de Linux puede utilizar 2 versiones de Python (Python2 y Python3) en mismo tiempo y pueden iniciar la version 2 como predeterminada
### esto significa que podria ser necesario especificar explicitamente el nombre del programa como python3
### en este caso puede haber 2 pip tambien, pip2 y pip3
### si no viene pip preinstalado,
#### instalar pip como paquete (usando el administrador de paquete de la distribucion) (mejor opcion)
#### instalar pip unsando mecanismos internos de python
#### instalarlo con apt (ubuntu), pacman (Arch linux), yum (distribucion de Redhat)
#### instalar pip va instalar tambien otros paquetes necesarios para el buen funcionamiento de pip
### en mac ya viene con python

# dependencias
## un paquete que haces depende de otros (tendras que instalarlos manualmente?) seria horible
## eso es lo que se llama infierno de dependencias
## afortunadamente, pip lo hace, pip puede descubrir, identificar y resolver todas las dependencias de manera inteligente
## evitando descargas y reinstalaciones innecesarias
## pip help para ver que puede hacer por nosotros
### para mas detalle sobre un comando usar pip help comando ==> pip help install
### pip list , para ver que paquetes son instalados
#### esto no se puede predecir, pero al menos va tener 2 pip y setuptools
## para mostrar mas detalles sobre un paquete, usar pip show
### pip show pip
## recuerda que pip no va almacenar todos los paquetes en PyPi en local (innecesaria y no economico)
## pip usa internert para descargar los paquetes
## busqueda con pip
### pip search anything
### la cadena sera buscada en en
#### los nombres de todos los paquetes
#### las cadenas de resumen de todos los paquetes
### la busqueda no es case sensitive pero podria producir una avalancha de informacion
#### ejemplo pip search pip podria mostrar mas de 100 lineas
### si no quieres usar el terminal, se puede usar el navegador en https://pypi.org/search

# suponiendo que la busqueda esta exitoso o quieres descargar un paquete con nombre ya conocido, puedes usar pip
## puedes usar esto para ti solo si no puedes elevar como administrador
## para todo el sistema, se requiere usuario admin
## para lidiar con esto, pip usa el comando --user (solo para el usuario no necesita cuenta admin)
## nosotros vamos descargar pygame desarrollado desde el 2000 https://www.pygame.org
## pip install pygame o pip install --user pygame
# import pygame
#
# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Bienvenido a pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False

# actualizacion de los paquetes y especificar la version
## pip install -U pygame
## pip install pygame==2.6.0

# desinstalar
## pip uninstall pygame
## te va pregungar si estas seguro
# redo exam modulo 1 https://edube.org/quiz/python-essentials-2-esp/module-1-test-9
