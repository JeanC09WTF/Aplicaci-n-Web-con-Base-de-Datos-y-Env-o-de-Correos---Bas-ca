from django.db import models

# Define la clase Carrera, que representa una carrera académica.
class Carrera(models.Model):
    # El atributo 'codigo' es un campo de texto con un máximo de 3 caracteres y es la clave primaria.
    codigo = models.CharField(max_length=3, primary_key=True)
    # El atributo 'nombre' es un campo de texto con un máximo de 50 caracteres.
    nombre = models.CharField(max_length=50)
    # El atributo 'duracion' es un campo de entero pequeño sin signo, con un valor por defecto de 5.
    duracion = models.PositiveSmallIntegerField(default=5)
    
    # Método para representar el objeto Carrera como una cadena de texto.
    def __str__(self):
        # Define un formato para la cadena de texto.
        txt = "{0} (Duracion: {1} año(s))"
        # Devuelve el nombre de la carrera y su duración en años.
        return txt.format(self.nombre, self.duracion)
 

# Define la clase Estudiante, que representa a un estudiante.
class Estudiante(models.Model):
    # El atributo 'dni' es un campo de texto con un máximo de 8 caracteres y es la clave primaria.
    dni = models.CharField(max_length=8, primary_key=True)
    # Atributos para los apellidos y nombres del estudiante.
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    # El atributo 'fechaNacimiento' es un campo de fecha.
    fechaNacimiento = models.DateField()
    # Define las opciones para el campo 'sexo'.
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    # El atributo 'sexo' es un campo de texto con un máximo de 1 carácter, con opciones definidas anteriormente y un valor por defecto de 'F'.
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    # El atributo 'carrera' es una clave foránea que referencia a la clase Carrera.
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    # El atributo 'vigencia' es un campo booleano con un valor por defecto de True.
    vigencia = models.BooleanField(default=True)
    
    # Método para obtener el nombre completo del estudiante.
    def nombreCompleto(self):
        # Define un formato para la cadena de texto.
        text = "{0} {1}, {2}"
        # Devuelve el nombre completo en el formato "ApellidoPaterno ApellidoMaterno, Nombres".
        return text.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
    # Método para representar el objeto Estudiante como una cadena de texto.
    def __str__(self):
        # Define un formato para la cadena de texto.
        txt = "{0} / Carrera: {1} / {2}"
        # Determina el estado del estudiante según el valor del campo 'vigencia'.
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"
        # Devuelve el nombre completo del estudiante, la carrera y el estado.
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)
    


# Define la clase Curso, que representa un curso académico.
class Curso(models.Model):
    # El atributo 'codigo' es un campo de texto con un máximo de 6 caracteres y es la clave primaria.
    codigo = models.CharField(max_length=6, primary_key=True)
    # El atributo 'nombre' es un campo de texto con un máximo de 30 caracteres.
    nombre = models.CharField(max_length=30)
    # El atributo 'creditos' es un campo de entero grande sin signo.
    creditos = models.PositiveBigIntegerField()
    # El atributo 'docente' es un campo de texto con un máximo de 100 caracteres.
    docente = models.CharField(max_length=100)
    
    # Método para representar el objeto Curso como una cadena de texto.
    def __str__(self):
        # Define un formato para la cadena de texto.
        txt = "{0} ({1}) / Docente: {2}"
        # Devuelve el nombre del curso, el código y el nombre del docente.
        return txt.format(self.nombre, self.codigo, self.docente)

# Define la clase Matricula, que representa la matrícula de un estudiante en un curso.
class Matricula(models.Model):
    # El atributo 'id' es un campo de entero automático que sirve como clave primaria.
    id = models.AutoField(primary_key=True)
    # El atributo 'estudiante' es una clave foránea que referencia a la clase Estudiante.
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    # El atributo 'curso' es una clave foránea que referencia a la clase Curso.
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    # El atributo 'fechaMatricula' es un campo de fecha y hora que se establece automáticamente en el momento de la creación del objeto.
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    # Método para representar el objeto Matricula como una cadena de texto.
    def __str__(self):
        # Define un formato para la cadena de texto.
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        # Determina la terminación del artículo según el sexo del estudiante.
        if self.estudiante.sexo == "F":
            letraSexo = "a"
        else:
            letraSexo = "o"
        # Formatea la fecha de matrícula en un formato legible.
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        # Devuelve el nombre completo del estudiante, la terminación correcta del artículo, el curso y la fecha de matrícula.
        return txt.format(self.estudiante.nombreCompleto(), letraSexo, self.curso, fecMat)

    

