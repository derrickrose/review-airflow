# caracteres y cadena
## las compu almacenan los caracteres como numeros (cada caracter equivalente a un numero y vice versea)
## algunos de estos caracteres se llaman espacios en blanco, otros caracteres de contro (controlar dispositivo de entrada y salida)
## ejemplo de caracteres invisibles (salto de linea)
## para lidiar con todo caracteres, hay una implementacion universal denominado ASCII
## American Standard Code for Information Interchange (casi todos los dispositivos modernos usan este codigo, phone, ordi, ...)
## El codigo proporciona espacion para 256 caracteres pero solo nos interesan 128

# internacionalizacion I18N
## alfabeto latino no es suficiente, por eso existe algo mas flexible y mas capaz que el ascii
## el codigo ascii utiliza (emplea) ocho bits para cada signo. ocho bits significa 256 caracteres diferentes.
## los primeros 128 se usan para el alfabeto latino estandares, y los ultimos 128 no pueden almacenar los otros caracteres de alfabetos en el mundo

# punto de codigo y paginas de codigos
## 32 es el codigo que caracteriza el espacio en codigo ascii, podemos decir que el codigo ascii ocupan los primeros 128 del codigo ascii
## solo puedes usar los 128 restantes
## asi que no es suficiente para todos los indiomas posibles, pero para grupo de indioma similares si
## se puede establecer la mitad superior de los puntos de codigo de manear diferente para diferentes idiomas ?
## => si por supuesto a tal concepto se le denomina una pagina de codigos
## una pagina de codigo es un estandar para usar los 128 puntos de codigo superiores para almacenar caracteres especificos
## ejemplo, hay diferentes paginas de codigo para europa occidental, europa del este, alfabetos crilicos y griegos, idiomas arabe y hebreo
## esto significa que el mismo punto de codigo puede formar diferentes caracteres cuando se usa en diferentes paginas de codigos
## ejemplo el punto de codigo 200 forma una c con acento (lengua eslavas) ISO/IEC 8859-2,
## pero forma un !_!_! (una letra crilica) cuando es usado por la pagina de codigos ISO/IEC 8859-5
## en consecuencia, para determinar el significado de un punto de codigo especifico, debes conocer la pagina de codigo de destino
## en otros palabras, los puntos de codigo derivados del codigo de paginas son ambiguoso

# unicode
## las paginas de codigos ayudaron a la industria de la informatica a resolver problemas de i18n durante algun tiempo,
## pero pronto resulto que no serian una solucion permanente
## el concepto para resolver el problema en largo plazo fue unicode
## unicode asigna caracteres unicos (letras, guiones, ideogramas, etc.) a mas de un million de puntos de codigo
## los primeros 128 puntos de codigo unicode son identicos a ascii,
## y los primeros 256 puntos de codigo unicode son identicos a la pagina de codigo ISO/IEC 8859-1 (para europa occidental)

# ucs-4
## el estandar unicode no dice nada sobre como codificar y almacenar los caracteres en la memoria y los archivos
## solo se nombra todos los caracteres disponibles y los asigna a planos (un grupo de caracteres de origen, aplicacion o naturaleza similares)
## existe mas de un estandar que escribe las tecnincas utilizadas para implementar unicode en computadoras y sistemas
## de almacenamiento informaticos reales. El mas general de ellos es UCS-4
## el nombre es universal character set (conjuto de caracteres universales)
## ucs-4 emplea 32 bits (cuatro bytes) para almacenar cada caracter, y el codigo es solo el numero unico de los puntos de codigo
## un archivo que contiene texto codificado ucs-4 puede comenzar con un bom (byte order mark - marca de orden de bytes)
## una combinacion no imprimible de bits que anuncia la naturaleza del contenido del archivo. algunanas utilidades pueden requerirlo
## como puedes ver, ucs-4 es un estandar bastante derrochador, aumenta el tamano de un texto cuatro veces en comparacion con el ascii
## afortunadamente hay otra forma las inteligentes de codificar textso unicode

# utf-8
## el mas utilizado unicode transformation format
## utf-8 emplea tantos bits para cada uno de los puntos de codigo como realmente necesita para representarlos
## los caracteres latinos (y todos los de ascii estandar) ocupan 8 bits
## los caracteres no latinos (16 bits)
##  los ideografos CJK (china-japon-corea) ocupan 24 bits
## no es necesario el BOM , pero algunas herramientas lo buscan al leer, y muchos editores lo configuran durante el guardado
## python3 es totalmente compatible con utf-8
## puedes usar caracteres codificados unicode utf-8 para nombrar variables y otras entidades
## puedes usarlos durante todas las entradas y salidas
## python3 es internacionalizado
