# MORE_JUAN_MANUEL_43865
Acceder a Administración y ver foto de perfil cambiada.
Usuario = admin 
Contraseña = 12345678

El proyecto es Mouca.
Mouca busca la conexión estre desarrolladores y aquellos que soliciten su servicio (ej: PyMEs).
Brinda un espacio donde se realizan propuestas laborales especializadas a proyectos de desarrollo así como posteos relacionados a lo mismo y da un espacio donde los desarrolladores suben sus perfiles para ser contactados.
Buscando agilizar procesos de contacto en el rubro.

En cuanto al codigo en sí, consta de cuatro modelos (Además del avatar), clientes, desarrolladores, propuestas y posteos.
En la página existe un apartado para cada modelo. Los últimos dos tienen la funcionalidad CRUD brindando la posibilidad de editar, visualizar y eliminar dichas propuestas y posteos para los usuarios logueados y los apartados clientes y desarrolladores muestran la lista de aquellos previamente cargados, así como dan la posibilidad de agregar un desarrollador o un cliente a la lista (y por ende a la base de datos).
Existe la posibilidad de buscar propuestas concretas en su apartado correspondiente "Busqueda".
Para acceder a estas funciones es necesario estar registrado y logueado en la página, una vez logueados tambien podremos ponernos una foto de perfil y editar nuestros datos en los apartados "Cargar Avatar" y "Editar perfil".
Estos apartados, desde "cargar avatar" hasta el "Agregar un posteo" heredan de una base.html utilizada como template.

De no estar logueado solo se vizualizaran los apartados Inicio, Acerca de, Registro, Login, Contacto y Administración.
En la Landing page también se incluye un link a mi linkedin en "Acerca de mí".

Se añade también un archivo de excel con los casos de usos donde se anotaron diferenteas pruebas unitarias.
