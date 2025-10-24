# los conceptos basicos del enfoque orientado a objetos
## el desarrollo procedimental es mas viejo que orientado a objeto
## orientado a objeto es util para proyecto grande donde trabajan muchos desarrolladores y facilita dividir en partes
## python es a la ves procedimental y orientado a objeto

# enfoque procedimental frente al enfoque orientado a objetos
## en el enfoque procedimental, los datos y los codigos son 2 mundos a parte y datos no usan funciones pero funciones usan datos
## en el enfoque objeto, los datos pueden usar metodos
## en el enfoque orientado a objetos, los datos y el codigo estan encapsulados juntos en el mismo mundo, divididos en clases
## cada clase es como una receta que se puede usar cuando quieres crear un objeto util. ilimitados de objetos
## cada objeto tiene un conjunto de rasgos (se denominan propriedades o atributos, usaremos ambas palabras como sinonimos)
## y es capaz de realizar un conjunto de actividades (que se denominan métodos)
## las recetas pueden modificarse si son inadecuadas para fines especificos y en efecto pueden crearse nuevas clases
## estas nuevas clases heredan propriedades y metodos de los originales, y generalmente agregan nuevos, creando nuevas herramientas mas especificas
## UpperClass
## MiddleClass
## LowerClass

# jerarquias de clase
## intentaremos senalar algunas clases que son buenos ejemplos de este concepto

r"""
            vehiculos
               |_____________________________________________________________
               |                      |                  |                   |
    vehiculos terrestres   vehiculos acuaticos   vehiculos aereos   vehiculos espaciales
                |
         ______|____________________________________
        |                    |                    |
    con ruedas       vehiculos oruga       aerodeslizadores
"""

## todos los vehiculos estan relacionados por una sola caracteristica importante: la capacidad de moverse
## clase vehiculos es una superclase
## las de mas son subclases (descendientes)
## toman en cuenta la direccion de las flechas, siempre apuntan a la superclase

# otro ejemplo de jerarquias: el reino taxonomico de los animales

r"""
            animales
     __________|____________________________
     |              |        |       |      |
    mamiferos   reptiles    aves   peces   anfibios 
        |_________________________
        |                        |
    mamiferos salvajes   mamiferos domesticados

"""


# que es un objeto?
## una encarnacion de los requisitos, rasgos y cualidades asignados a una clase especifica pero toman en cuenta le jerarquia
## esto significa que un objeto que partenece a una clase especifica partenece a todas las superclases al mismo tiempo
## tambien un objeto perteneciente a una superclasse puede no pertenecer a ninguna de sus subclases
## ten en cuenta que hemos supuesto que una clase solo puede tener una superclase, esto no siempre es cierto, pero discutiremos al respeto

# herencia
# cualquier objeto hereda todos los rasgos definidos dentro de cualquiera de sus superclases

# que contiene un objeto
## tres grupos de atributos
### nombre que lo identifica de forma exclusiva dentro de su namespace (aun que hay objetos anonimos)
### conjunto de propriedades individuales (aun que algunos objetos no tengan propriedades)
### conjunto de habilidades para realizar actividades especificas (capaz de cambiar el objeto en si, o algunos de los otros objetos)
## existe una pista (aunque esto no siempre funciona) que ayuda a identificar cualquiera de las tres esferas anteriores :
### un sustantivo : el nombre del objeto
### un adjetivo : probalemenente se esta definiendo una propriedad del objeto
### un verbo : probablemente se esta definiendo una actividad del objeto

# ejemplos
## un cadillac rosa paso rapidamente
### nombre del objeto cadillac
### clase vehiculos con ruedas
### propriedad color rosa
### actividad pasar rapidamente

# mas ejemplos
## Max es un gato grande que duerme todo el dia
### nombre max
### clase gato
### propriedad tamano grande
### actividad dormir (todo el dia)

# primer clase
class TheSimplestClass:
    pass


# primer objeto
## el nombre de la clase intenta fingir que es una funcion
## la clase recien definida se convierte en herramienta pa crear objetos
## el objeto definido contiene todo lo que trae la clase, como esta vacia, el objeto tambien
## el acto de crear un objeto de la clase seleccionada tambien se llama instanciacion (ya que el objeto se convierte en una instencia de la clase)
my_first_object = TheSimplestClass()
