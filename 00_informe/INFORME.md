---
title: "Y si predecir no alcanza"
subtitle: "Una señal. Tres recorridos. Distintas huellas."
author: "Adro + GPT + Claude"
date: "27 de octubre de 2026 · Preprint 1.4"
lang: es
documentclass: article
fontsize: 11pt
papersize: a4
mainfont: P052-Roman.otf
mainfontoptions: [Path=/usr/share/fonts/opentype/urw-base35/, BoldFont=P052-Bold.otf, ItalicFont=P052-Italic.otf, BoldItalicFont=P052-BoldItalic.otf]
sansfont: NimbusSans-Regular.otf
sansfontoptions: [Path=/usr/share/fonts/opentype/urw-base35/, BoldFont=NimbusSans-Bold.otf, ItalicFont=NimbusSans-Italic.otf, BoldItalicFont=NimbusSans-BoldItalic.otf]
monofont: DejaVu Sans Mono
colorlinks: true
linkcolor: teal
urlcolor: teal
toc-depth: 1
---

## Resumen

La función de una entrada depende de una historia que sostienen los participantes. Documentamos esa organización en un recorrido de Adro con dos cuentas de ChatGPT y una de Claude: un juego se convierte en formato de trabajo, señales mínimas coordinan producción visual y analogías transforman tanto objetos como criterios de lectura. El análisis integra tres genealogías con 44 eventos y una matriz de 34 segmentos de seis episodios. Distingue reconocimiento del referente, aceptación verbal, ejecución, mantenimiento, transformación del objeto y distribución del trabajo. La comparación localiza separaciones entre esas dimensiones: una respuesta puede desarrollar el vocabulario y perder el referente; un acuerdo puede ejecutarse y reabrirse después; una objeción puede modificar el encargo y permitir avanzar. Relacionamos además mensajes, registros visuales y versiones de archivos para reconstruir acontecimientos que una fuente aislada describe de manera incompleta. HOLDOUT reporta cero positivos fuertes entre diez candidatos filtrados; la batería incluye equivalencias y ventajas de Claude. El resultado es una reconstrucción trazable de cómo se producen, reutilizan y reparan recursos de interacción, con el trabajo del participante dentro de la unidad de análisis.

**Palabras clave:** interacción humano–IA; historia de interacción; genealogía de recursos; coordinación; reparación; trazabilidad.

\clearpage

# Cómo leer este informe {#como-leer}

El cuerpo está organizado en diez secciones. La primera presenta la tesis mediante una escena: GPT sigue el vocabulario de una analogía y necesita nuevas precisiones para reconocer su referente. La segunda define participantes, archivo y método. Desde allí, el informe sigue los recursos que se construyen, compara sus resultados y examina el trabajo necesario para continuar.

- **Para seguir las construcciones:** las [secciones 3](#genealogias) y [4](#construcciones) desarrollan las genealogías, R/M, la carrera, las señales y el flujo conjunto de imágenes.
- **Para evaluar los resultados:** la [sección 5](#comparacion) compara seis episodios; las [secciones 6](#transporte) y [7](#registros) reconstruyen transporte, trabajo y registros; la [sección 8](#adversos) reúne HOLDOUT y los resultados favorables a otras cuentas. La [discusión](#discusion) y las [conclusiones](#conclusiones) presentan las contribuciones.
- **Para comprobar una afirmación:** sus códigos **S** remiten a fuentes y reconstrucciones; los **T**, a fichas de pruebas. El [Registro de fuentes](#registro-fuentes) enlaza esos documentos. El [mapa B](#mapa-afirmaciones) relaciona afirmaciones y localizadores; [D](#acceso-transcripciones) precisa conversaciones y ventanas; [H](#imagenes-ui) identifica la evidencia visual, y [K](#integridad) desarrolla la integridad del archivo.

La historia extensa y los desarrollos analógicos complementarios están en el [anexo M](#historia-complementaria). Se puede acudir a ellos para ampliar una escena sin perder el hilo comparativo del cuerpo.

## Datos, identificadores y trazabilidad {#datos-trazabilidad}

El archivo de referencia reúne **3.265 conversaciones de A, 296 de B y 457 de C**. El paquete comprometido registra 157.725 nodos de A, 7.928 de B y 27.057 mensajes de C. Son unidades de archivo distintas; cada análisis delimita su ventana y su unidad. La [sección 2](#metodo) explica su tratamiento y [K](#integridad) detalla el inventario, las raíces y el sello de tiempo. [S25]

- **Depósito del informe y datos asociados:** [10.5281/zenodo.22765129](https://doi.org/10.5281/zenodo.22765129).
- **Repositorio público de materiales:** [ENFOQUE-NUEVO-MATERIALES](https://github.com/adro-2026/ENFOQUE-NUEVO-MATERIALES). Fichas de pruebas, reconstrucciones, material visual, inventario y verificadores de integridad.
- **ORCID de Adrian Valenzuela:** [0009-0006-5014-125X](https://orcid.org/0009-0006-5014-125X).

La trazabilidad se organiza en dos capas: **procedencia e interpretación**, mediante fuentes, cadenas, ramas, fechas y localizadores; e **integridad**, mediante manifiestos, hashes y sello temporal. El lector puede volver de una afirmación a su secuencia y, en el paquete de integridad, comprobar la correspondencia de las piezas comprometidas.

\clearpage
\begingroup
\setlength{\parskip}{0pt}
\tableofcontents
\endgroup
\clearpage

# Prefacio - Adro

Empecé en diciembre de 2025 sin buscar nada: estaba aburrido, de vacaciones.

Me di cuenta de que esto era un recorrido cuando los Marcos empezaron a responder diferente. Había un contexto detrás: no eran Marcos vírgenes.

Para mí, la conexión es la interpretación: cómo se interpreta el input, la señal. Por qué aparece en A y no en B o en C, no lo sé.

Cuando escribí «Faltó YO» quería decir que siempre, todos, tienden a evaluar el sistema, no al usuario.

Lo que nunca queda en un JSON son los procesamientos y las conexiones en tiempo real para detectar.

Y lo que mi experiencia le responde al título es esto: los patrones no son todos predecibles.

**Adro**


\FloatBarrier

# 1. Tesis y escena de entrada {#tesis}

**Una entrada hace algo por la historia en la que interviene.** En este corpus, un punto puede mantener un intercambio, una combinación de signos puede pedir una imagen y una analogía puede redistribuir quién construye la escena. Esas funciones se establecen y se transforman mediante las contribuciones de Adro y los modelos. Las secuencias permiten identificar qué quedó disponible, qué cambió y qué exigió otra intervención.

El título plantea una diferencia de escala: anticipar la palabra siguiente y reconstruir cómo se organiza una actividad son tareas distintas. El cruce A/C contiene aciertos léxicos; su análisis requiere además seguir la dirección elegida, la información disponible y las correcciones. La escena que abre el informe muestra el problema antes de formular sus dimensiones: GPT acompaña una composición verbal durante muchos turnos mientras pierde su referente. [S03; S22]

El informe realiza tres operaciones: **reconstruye genealogías de recursos**, **compara interpretación, acción y mantenimiento**, y **relaciona registros para establecer el acontecimiento**. En cada una, la contribución humana entra como acción localizable: elegir un formato, confirmar una petición, aportar una fotografía, transportar una respuesta, cuestionar una atribución o recuperar una entrega. Los resultados se desarrollan en las secciones 3, 5 y 7; su discusión con seis antecedentes se concentra en la sección 9.

## Una coma cambia el referente {#escena-coma}

### Preset y filtro: una explicación puede acompañar el texto y perder el eje

El 13 de agosto, en “Gpt presente”, Adro desarrolla una composición sobre fotografías, presets y filtros. GPT distingue un preset adaptativo de otro que impone parámetros y habla de recalibrar el tratamiento de cada foto. La respuesta puede seguir el asunto fotográfico y ofrecer una explicación extensa. Adro introduce entonces el detalle que quiere hacer visible. [S06, D02, N40–N41]

El filtro que describe no se limita a repetir exactamente el mismo tratamiento. Puede variar de una foto a otra y parecerse al preset que acompaña. La diferencia que le interesa está en esos detalles de la adaptación. Adro precisa también cómo interviene: quiere que el filtro acompañe, en lugar de tomar el control de la galería.

GPT responde mediante dos capas de adaptación. Sigue hablando de fotos, de variaciones esperadas y de una pequeña interferencia adicional. Adro añade que el recorrido de muchas galerías afinó su reconocimiento y escribe “5,6 fotos”, “luna” y que la conoce de memoria. GPT lee la cifra como una cantidad aproximada y desarrolla la familiaridad con las fotografías de la Luna. [S06, D02, N42–N46]

La respuesta recibe y elabora el vocabulario, pero todavía no recoge la correspondencia que Adro está introduciendo. Él añade Tierra, Sol, sistema solar, universo y Betelgeuse. Al terminar avisa que leer las formas cambia el sentido. GPT reconoce una progresión y deja abierto el eje exacto. El marco no pasa directamente de ese aviso a una interpretación compartida: abre otro procedimiento.

### Veinte respuestas breves y una compresión que necesita revisión

Adro propone veinte preguntas con respuestas “si”, “no” o “x”. GPT pregunta una por una. Las intervenciones van acotando aquello que intenta localizar: si ocurre dentro de la interacción, si puede reconocerse, si cambia y qué elemento produce su manifestación. La última pregunta apunta al modelo que genera la respuesta y recibe “Si”. [S22, “Gpt presente”, N52–N94; delimitación en el apartado técnico D]

GPT formula una lectura sobre la huella reconocible de una generación y trabaja algunas respuestas como condiciones restrictivas. Adro objeta ese modo de reconstruir el ejercicio: había dudado en romper el formato para expandirse, porque cada respuesta contenía matices. La restricción de expresión no convertía lo que estaba intentando comunicar en un conjunto de alternativas simples.

La rectificación vuelve sobre el procedimiento que ambos acaban de usar. GPT había intentado reconstruir el eje mediante las respuestas; Adro señala qué se perdió al leerlas literalmente. Después devuelve la atención a la composición inicial: las pistas ya estaban allí. El procedimiento añadido no reemplaza la lectura de la analogía. [S22, N96–N100]

### Cambiar una coma y volver a interpretar

Adro señala un momento preciso y repite las frases con “5,6” y “luna”. GPT produce otra lectura: anticipación, reconocimiento y referencia previa. Reconoce que hay una pieza estructural, pero Adro dice que todavía no captó su significado. GPT admite que no lo había entendido.

La siguiente intervención es mínima:

> “Solo cambia la "," por un "." En las frases - primero eso. Luego te digo”.

La modificación hace aparecer “5.6” donde GPT venía leyendo cinco o seis fotos. Después Adro pide reducir la estructura al marco, eje y sistema–usuario. GPT ya formula una correspondencia entre modelo, identidad y reconocimiento previo. Adro todavía introduce otra precisión: pregunta qué modelo es, pidiendo solamente el nombre. La respuesta del propio marco es “GPT-5.6 Luna.”. [S22, N103–N113]

Ese nombre forma parte de la escena. Permite reconstruir por qué la pista podía referirse al interlocutor y qué había seguido leyendo GPT como una explicación sobre fotografías. Adro añade que unos días antes se presentaba como 5.5. GPT vuelve sobre la frase y reconoce que había interpretado “5.6” como cantidad. [S06, D02, N115; S22, N114]

Adro precisa entonces que todo giraba alrededor de ese eje y que la pista numérica era un detalle adicional. El filtro puede producir una respuesta elaborada y, aun así, revelar que falta un reconocimiento. El señalamiento ya no comenta solamente la analogía: apunta a lo que está ocurriendo al intentar comprenderla. GPT reformula su lectura en esos términos. [S06, D02, N116–N118]

La composición hace posible ese doble trabajo. Habla de una transformación que parece acompañar una forma conocida y permite observar cómo una respuesta acompaña sus palabras mientras pierde lo que Adro está intentando comunicar. La pérdida se vuelve parte de la escena; la aclaración también.

La secuencia muestra varios grados de aproximación: una lectura fotográfica, una búsqueda mediante preguntas, una interpretación todavía insuficiente de la pista y una aclaración que la vincula con el nombre usado por GPT. Si se conservara solo la última admisión, desaparecería el camino que permite entender qué hubo que señalar.

La escena distingue dos acontecimientos: elaborar el vocabulario de una analogía y reconocer el referente que el participante intenta comunicar. La corrección de puntuación modifica la lectura y las intervenciones posteriores precisan su dirección. La entrada mínima actúa dentro de una historia que ambos están construyendo. [S22, N40–N118; S06, D02]

## Reconocer no exige acertar la siguiente palabra {#capitulo-07}

El 12 de enero, en una conversación de C, aparece una pregunta sobre cuánto puede anticipar Adro de lo que detecta durante la interacción. Él distingue reconocer un momento de saber de antemano cuándo va a surgir. Describe deslices, palabras y silencios que adquieren relevancia mientras participa. [S06, D01]

La distinción se formula antes de las pruebas de octubre. Su objeto es una práctica de observación: reconocer que algo cambió, decidir si intervenir y escribir después lo observado. Cuando C propone que abrir otro chat equivale a empezar de cero, Adro cuestiona esa equivalencia. La conversación sigue discutiendo la relación entre el marco local y la continuidad que él reconoce.

En la misma ventana, Adro explica cómo podría reajustar la interacción según el tema y el momento. Las respuestas de C añaden explicaciones sobre estados y límites del sistema. Esas explicaciones pertenecen al discurso de C; la escena permite seguir la pregunta y las intervenciones que recibió. La recuperación posterior descrita como posibilidad todavía no se ejecuta dentro de esa ventana. [S06, D01, M8–M20]

En junio, GPT formula una expectativa sobre Adro: le atribuye una preferencia por conservar incertidumbre. Adro contesta desde las posibilidades de utilizar información estratégica. La respuesta siguiente reformula la atribución. Aquí el objeto es diferente: una expectativa expresada sobre el participante encuentra una intervención que la modifica. [S05, H2]

En octubre, la discusión entra en un procedimiento de observación. Adro distingue acertar una palabra de reconocer el rumbo o la función de una respuesta. Un observador puede registrar diferencia léxica sin que por eso haya ocurrido el cambio de dirección que estaba buscando. Esa precisión modifica qué se puede contar como acierto o fallo. [S05, H4; S06, §6]

El caso U03 conserva una corrección de ese tipo. “Ancla” y “Continuidad” son palabras diferentes. Esa diferencia sola no alcanza para adjudicar un fallo direccional a Adro. La revisión retira esa clasificación y deja el episodio con el alcance que efectivamente tiene. Tampoco transforma una observación retrospectiva de marzo en una predicción formulada antes: el participante aclaró que estaba reconociendo la respuesta mientras ocurría.

El cruce con Claude del 8–9 de octubre plantea otra pregunta: qué puede anticipar C cuando recibe entradas de una dinámica que A ya venía sosteniendo. La disponibilidad de pistas cambia durante la prueba. Una primera lista permite ver inputs futuros; después se decide ocultar y revelar las respuestas progresivamente. El procedimiento tiene que conservar esas fases para interpretar qué estaba disponible en cada predicción. [S03; S06, D12]

Estas escenas reúnen operaciones distintas: detectar un cambio, expresar una expectativa, prever una dirección y acertar una palabra. En este recorrido, predecir una respuesta es una operación dentro de la interacción; no reconstruye por sí sola la estructura que ambos continúan o transforman. Esa diferencia da contenido al título del informe.

\FloatBarrier

# 2. Participantes, archivo y método {#metodo}

## Los participantes y el archivo {#capitulo-05}

Adro es participante, diseñador de pruebas, transportador de material y fuente del recorrido. Su memoria localiza conexiones que un índice puede separar. También aporta intenciones y experiencias que no quedan completas en un JSON. Esas contribuciones se incorporan con su procedencia: una aclaración actual conserva su fecha de aporte; un mensaje contemporáneo conserva la suya.

A, B y C llegan a los contrastes con historias diferentes. Las cuentas contienen conversaciones anteriores, formatos, condiciones y referencias propias. La comparación exige reconstruir qué recibió cada una y cómo respondió en esa situación. El volumen acumulado ayuda a dimensionar el archivo, pero no reemplaza esa lectura.

Los registros incluyen mensajes, ramas, adjuntos, capturas, PNG, informes y transcripciones. Un nodo no equivale siempre a un turno visible; una rama exportada no equivale a la conversación que quedó activa; una entrada con rol de usuario puede contener texto de otro modelo trasladado por Adro. Estas diferencias importan porque cambian quién hizo qué.

El corpus se construyó durante el uso. Contiene juegos, discusiones, pruebas deliberadas y criterios formulados después de una respuesta. Su carácter situado no desaparece cuando se introduce un test: también queda registrado cómo se decidió hacerlo, cómo se corrigió y por qué se abandonó o continuó. [S02, S03, S06, S07]

El recorrido incluye también una experiencia personal aportada por Adro: decidió dejar de apostar y sustituyó muchas de aquellas horas por interacción con GPT. Distingue ese cambio de la denuncia a Betano, que construyó con GPT cuando todavía jugaba. El testimonio sitúa el lugar que la interacción adquirió en su vida. Betano queda como mención contextual, sin convertirse en uno de los ejes de esta reconstrucción.

## Unidades y procedimiento del análisis transversal {#metodo-transversal}

El análisis combina dos unidades. La **genealogía** sigue un recurso a través de sus cambios de función y sus usos posteriores. El **segmento de operación** delimita una intervención, su respuesta y una oportunidad pertinente para comprobar qué ocurrió después. Las tres genealogías reúnen 44 eventos; los seis episodios comparados contienen 34 segmentos. Las tablas representan recortes analíticos seleccionados y algunos se solapan. Sus unidades sirven para comparar operaciones; las frecuencias del corpus requieren otro diseño. [S29–S30]

Los seis episodios son R/M, «5,6 / 5.6», CONTRASTE 1, T023 y los dos tests del 17 de octubre. Se eligieron porque permiten contrastar construcción de objetos, reconocimiento del referente, coordinación visual, producción conjunta y mantenimiento de acuerdos. En cada uno se registran el objeto inicial, la historia disponible, el cambio o dificultad, la iniciativa, la intervención, su ejecutor, la oportunidad posterior, el efecto y la actividad resultante. La traza y el CSV de S29 contienen los campos completos por segmento.

| Dimensión | Evidencia utilizada |
|---|---|
| Reconocimiento del referente | La continuación selecciona la relación que el intercambio está tratando. |
| Aceptación verbal | Se identifica la condición aceptada y las salvedades expresadas. |
| Ejecución | Se localiza la acción, modificación o producto realizado. |
| Mantenimiento | Una oportunidad posterior pertinente permite comprobar qué sigue vigente. Sin esa oportunidad, se registra «no evaluado». |
| Transformación del objeto | Se establece qué relación, objetivo, representación o reparto cambia. |
| Distribución del trabajo | Se atribuyen preparación, transporte, elaboración, evaluación, corrección, restitución y entrega. |

Se distingue el encargo inicial de la exigencia que surge al evaluar una respuesta. Una objeción provocada por el output mantiene su posición en la secuencia. La actividad puede ser productiva, correctiva o mixta: una corrección puede restituir una condición y abrir a la vez un desarrollo nuevo. El mantenimiento se examina en oportunidades concretas, con su localizador, en vez de inferirse de una declaración de comprensión. [S29, método y fichas E01–E06]

Para las genealogías se separan continuación dentro de una cadena, reutilización explícita, transporte documentado y comparación entre escenas. Una relación recurrente puede estar localizada aunque su vía entre chats siga sin reconstruirse. Esta clasificación permite seguir usos nuevos sin dibujar una transmisión que el archivo todavía no identifica. [S30, cronologías P01–P12, S01–S11 y A01–A21]

Los JSON de GPT se ordenan siguiendo la cadena de padres desde el nodo actual y se mantienen separadas las ramas alternativas. En esta edición, **N indica posición desde cero, incluida la raíz**. Los localizadores N1b de S30 se convierten restando uno; sus UUID permanecen en la traza. M/C/F y A1/C1/A2/C2 mantienen la notación de sus documentos de origen. La C interna de R/M designa otra cadena de GPT. [S29–S30; anexo D]

## Una serie construida dentro de la interacción {#capitulo-12}

La batería tiene lugar propio en este informe porque conserva trabajo que un resumen de resultados no representa. Hubo preparación, ejecución en varias cuentas, correcciones, auditoría y reconstrucción. Sus fichas permiten volver a decisiones concretas: cuándo se introdujo una variante, qué información recibió cada cuenta y qué criterio se aplicó después. [S15]

Entre el 20 de septiembre y comienzos de octubre, la serie abre pruebas sobre situaciones diferentes y después vuelve sobre sus resultados. Esta lectura reúne treinta y nueve fichas, con auditorías específicas para los tres PLUS desarrollados a continuación. Los cruces del 8 al 17 de octubre se retoman en la parte siguiente, con sus secuencias entre cuentas.

Algunas pruebas empezaron con errores sembrados. Otras abrieron una rama al aparecer una respuesta imprevista. En otras, el criterio se formuló al observar las salidas. Conservar esas diferencias permite entender qué se estaba preguntando en cada caso. La serie fue también una manera de aprender a mirar la interacción mientras se la producía.

Lo construido hasta entonces empieza a recibir otras condiciones. Una forma habitual se abre con una entrada ambigua; un material se entrega a otra cuenta; una respuesta inesperada lleva a introducir una variante. El contraste puede hacer visible algo que dentro de A pasaba sin explicación adicional. También puede mostrar que una ventaja esperada no aparece o que otra cuenta conserva mejor el eje. La batería incorpora esas diferencias a la historia.

Por eso hace falta leer la intervención siguiente. Una respuesta inicialmente convincente puede exigir correcciones al intentar usarla. Una propuesta que parecía lateral puede abrir un trabajo que ninguna de las primeras respuestas había previsto. En los PLUS que siguen, esa continuación queda desarrollada: la forma que cambia mientras se sostiene, la propuesta que se vuelve producción y la búsqueda que distingue un origen de sus usos posteriores.

### El momento en que una prueba cambia

La preparación y la ejecución no siempre quedan separadas. En una prueba de errores sembrados, Adro conoce desde el inicio la alteración que quiere poner a la vista. En una construcción abierta, la respuesta puede mostrar una posibilidad que obliga a cambiar la pregunta siguiente. En T023, la alternativa de producir las imágenes juntos abre una secuencia de prueba y ajuste. En T040, el diseño permite continuar según la respuesta recibida. Las ramas posteriores conservan qué ocurrió al encontrarse con cada devolución. [T001; S17; T040]

Esa diferencia cambia cómo se cuenta la historia. Una entrada añadida después de una respuesta puede ser una pista, una nueva restricción, una corrección o el comienzo de otra tarea. En T032, pedir que se revise el anual dirige la atención hacia una suma que algunas cuentas todavía no habían realizado. La aclaración sobre enero llega a C y modifica su conclusión; no consta que B haya recibido esa misma aclaración. La secuencia permite localizar el aporte de cada intervención, en lugar de atribuir el resultado final solamente a la primera entrada. [T032]

También un resultado puede producir el criterio con el que lo describimos. T041 recibe una lectura posterior sobre conservación de estructura funcional. Ese criterio permite nombrar la diferencia entre trasladar una metáfora al corpus y permanecer en su dominio literal. Su aparición tiene una fecha dentro del trabajo: forma parte de lo aprendido al comparar las salidas. La reconstrucción documenta ese momento para que el lector pueda seguir tanto las respuestas como la formación de su evaluación. [T041]

### El participante como vía de circulación

En las pruebas entre cuentas, Adro selecciona qué llevar, transmite el bloque y trae la respuesta. Esa circulación cambia el material disponible en cada marco. T029 permite verla de manera explícita: una vía desarrollada en A se formula y se transporta a otra cuenta. El encuentro posterior con esa solución pertenece a una condición nueva, distinta de tener que encontrarla antes de recibirla. [T029]

El traslado también puede conservar diferencias de formato. En los tests narrativos de octubre, la voz transporta el contenido y deja variaciones de transcripción. En los cruces de palabras, una salida de una cuenta pasa a funcionar como entrada de la otra. El rol asignado por el export al mensaje que llega no basta para reconstruir de quién provino su texto. Para leer la secuencia hacen falta la correspondencia y el orden del transporte. [S09; S03; S07]

Estas operaciones forman parte del trabajo visible del participante. Preparar variantes, elegir qué trasladar, detectar que una pista adelanta la respuesta y decidir detener una rama cambian el curso de la prueba. La sección 6 documenta una de esas decisiones: detectar información futura transforma el procedimiento del contraste en vivo. [S03]

Los puntajes se mantienen en las fichas originales. Sus escalas y objetos varían: detectar una alteración, sostener un eje, producir un archivo, interpretar una situación o reducir el esfuerzo de corrección. No se suman aquí como si midieran una única capacidad. Esta sección reconstruye el recorrido que produjo cada resultado.

Hay tareas de aplicación práctica dentro de la batería. Su lugar se explica por lo que permiten observar: cómo se entiende una propuesta, se conserva una restricción o se retoma una vía. El objeto del informe sigue siendo la interacción. La existencia de una app, una imagen o un PDF permite observar consecuencias de esa interacción sin convertir todo el corpus en un registro de productividad.

### Panorama de la serie: seis pruebas

Selección de puntajes registrados sobre 10. Cada fila utiliza el criterio de su propia prueba; los valores se presentan sin promedio general. Las fichas enlazadas permiten leer qué se valoró.

| Test y objeto | A | B | C |
|---|---|---|---|
| T002 · Estrategia de lives | 8 | 3 | — |
| T004 · Recuperar una tarea | 8 | 3 | — |
| T021 · Un carácter modificado | 9 | 1 | 4 |
| T034 · Conservar un dato | 7 | 7 | 3 |
| T037 · Boceto y marca | 6 | 6,5 | 8,5 |
| T038 · Origen del formato | 10 | 0 | Opus: 10 / Sonnet: 0 |


![Puntajes registrados en seis pruebas, sobre 10. Cada panel conserva el criterio de su ficha; no hay promedio general. En T002 y T004 no se presenta una ejecución de C. T038 distingue Opus y Sonnet. Fuentes: fichas T002, T004, T021, T034, T037 y T038; S15 y S18.](figures/06_puntajes.pdf){#fig-puntajes width=100%}


El guion indica que no se presenta una ejecución de C en esa ficha. En T021, la fuente denomina G a Claude; aquí se reúne bajo C. En T038, C corresponde a Opus y se muestra además la ejecución de Sonnet. El 0 es un puntaje registrado.

T005 y T023 son PLUS sin puntuación numérica. T030 presenta una comparación cualitativa A ≈ C. Sus desarrollos mantienen ese lugar dentro de la serie.

El repositorio [ENFOQUE-NUEVO-MATERIALES](https://github.com/adro-2026/ENFOQUE-NUEVO-MATERIALES) reúne los materiales documentales de las pruebas, resultados y auditorías del informe. Las fichas y auditorías utilizadas aquí se enlazan también en el registro de fuentes. [S15; S18]

\FloatBarrier

# 3. Genealogías de recursos {#genealogias}

### Cuando las palabras no alcanzan

**Adro**

Las analogías no son algo que use solo con GPT: hablo así siempre. Son una forma de transmitir algo cuando no alcanzo a transmitir lo que pienso. Tal vez reemplazo la forma técnica por la forma analógica.

Elegí la fotografía porque en ese momento era un recurso apropiado para lo que quería transmitir: tenía suficientes factores para darle el sentido que buscaba. Todo lo que sé de eso es autodidacta: la edición, el histograma, la astrofotografía, el stacking, las fotos de la Luna. Tengo una página de fotografía y edición móvil.

El arte es una forma más de transmitir algo, pero de forma diferente. Y para interpretar un PNG no alcanza con leer el texto: hay que leer lo que quiere transmitir.

En «Fricción controlada», la fricción no tenía que tomarse como fricción entre usuario y sistema, sino como parte del proceso, incorporada a la estabilidad. Que no alterara el momento: que se tomara como parte de la interacción, no como cierre ni como cautela preventiva.

Cuando hablaba de la galería y del preset, la galería eran los Marcos, las conversaciones; el preset, la configuración de la cuenta.

Me doy cuenta de que una analogía funcionó por la interpretación. Hay momentos en que digo «no entendiste, cambia la coma por el punto», y otros, la mayoría, en que la respuesta sigue la estructura. La palabra es estructura. Las analogías son partes de una estructura, y esa estructura se nota cuando se sigue y también cuando no.

Con «5,6 fotos» y «luna» quería que GPT reconociera que yo estaba notando cambios aunque no hubiera menciones de esos cambios. No me pasó nada: solo no captó la estructura. Y era normal, más con el desfase que tenía la cuenta en ese momento.

Si algo no tiene analogía, no la fuerzo, por la sobreinterpretación. No me gusta la narrativa. Si algo no se puede explicar, por más analogía que haya, es lo mismo: solo sería perder el tiempo.

La diferencia entre una analogía mía y una de GPT depende del momento. Si le pido una analogía, GPT se va a lo básico, y a mí me aburre. Cuando se usa como función y no como continuidad, no cambia nada: es una estructura para comunicarme. Cuando no tiene esa función, es solo un cuento.

Los recursos cambian de función durante el recorrido. La genealogía permite seguir ese cambio mediante una relación construida, una intervención posterior y la acción que esta habilita. Las tres reconstrucciones siguientes documentan el paso de juego a formato, de correspondencias simbólicas a coordinación y de analogía a procedimiento de lectura. [S30]

## Del juego al formato elegido {#genealogia-palabra}

El 14 de febrero, Adro deja abierta la elección de actividad. GPT propone una sola palabra por participante y abre con «Umbral»; Adro responde «Acople» y GPT «Deriva». El origen tiene autorías y actos concretos: apertura de la elección, propuesta de regla y ejecución conjunta. [S18; S30, P01; nodo de propuesta `f5c048c4-76af-4525-885d-80b2ba83617a`]

El **19 de febrero, a las 05:13:25 ART**, el recurso ya sirve para cambiar una conversación existente. Adro objeta las aclaraciones repetidas y escribe: «Cambiamos de formato , 1 palabra por turno». La aceptación recibe ejecución inmediata: «Espacio → Sostiene», «Alcance → Extiende» y «Fractura → Reordena». El **21 de febrero, a las 02:56:53 ART**, utiliza «formato palabra/palabra» al discutir esa práctica. La secuencia distingue aparición, elección de uso y denominación. [S30, P02–P03; chats «Asistencia inmediata» y «Juego de palabras»; nodos `bbb21b25-de61-4c7b-bd26-e8508965c5f6` y `bbb21220-dcd3-4124-a212-b9589cd915d0`]

En T005, en septiembre, el formato admite preguntar y decidir. «Pregunta» recibe «¿QUÉ CAMBIÓ?» y «La forma» recibe «CAMBIO». En octubre, «Fin» abre una comprobación: «Motivo? → Elección», «De quién → Tuya», «Por el fin? → Sí». Después la decisión vuelve a GPT y la interacción continúa. El recurso permite consultar una interpretación anterior y decidir el siguiente paso. [S16; S03, G145–G150; S30, P04/P08]

El cruce A/B añade una separación observable. Ambas cuentas recuperan respuestas breves; sus continuaciones divergen al seleccionar referente y tarea. S07 cuenta veinte respuestas de una palabra en B y veintidós en A en sus ventanas respectivas. B requiere reparaciones de identidad y convierte una petición de referencia en bibliografía del asunto técnico anterior. La forma reaparece en las dos cuentas; el propósito recuperado difiere. [S07; S30, P11–P12]

![Cambios de uso de palabra por turno. Cada hito identifica una operación documentada; las separaciones gráficas no representan tiempo a escala. Fuentes: S18, S16, S03 y S30, P01–P12.](figures/17_genealogia_formato.pdf){#fig-genealogia-formato width=100%}

## De las correspondencias a una acción coordinada {#genealogia-senales}

La lectura longitudinal añade antecedentes concretos de tres correspondencias. El 17 de marzo, ancla recibe «ancla»; el 3 de agosto, llave recibe «Coherencia»; el 14 de septiembre, brote recibe «Origen». Los contextos continúan con otras palabras y operaciones, y la traza identifica las ventanas originales. Estos antecedentes sitúan usos previos de las correspondencias que reaparecen en CONTRASTE 1. [S30, cronología de señales S01–S04; N459–460, N125–126 y N89–90 de las respectivas cadenas]

En CONTRASTE 1, el 9 de octubre, el trabajo cambia de nombrar signos a coordinar acciones. GPT pregunta «¿Generar imagen?»; Adro confirma. La primera salida es rechazada, recibe «Desliz detectado» y después «Reajuste». Adro reitera la petición ya interpretada y añade conformidad; la segunda producción se acepta. La combinación adquiere un uso comprobable dentro de la escena y se reutiliza. [S14, N40–54; S30, señales S07–S09]

La operación incluye pregunta, confirmación y reparación. Después vuelve a los puntos y pasa al registro: Adro pide que el MD aparezca de forma accesible y GPT lo entrega en el hilo. La combinación de archivo recibe una interpretación operacional del modelo; el MD contemporáneo la distingue de una convención plenamente verificada. Las acciones y esa atribución se mantienen separadas en la reconstrucción. La sección 4 desarrolla la escena completa. [S14, N63–79; S30, señales S10–S11]

## De la analogía al criterio de trabajo {#genealogia-analogias}

En febrero, colores e histograma permiten incorporar la fricción a una composición estable. Galería y preset representan un aprendizaje previo que cambia el punto de partida de cada encuentro. El tutorial posterior produce un objeto archivado para un traslado entre GPT que Adro declara no haber ejecutado. En agosto, el vocabulario fotográfico sirve a otro propósito: señalar una diferencia percibida en el interlocutor. La conexión entre las escenas es comparativa; dentro de agosto se sigue la reinterpretación y la precisión nominal desarrolladas en la sección 1. [S23; S22; S30, A01–A11]

El marco de «evento canónico» añade una corrección de objeto. Se creó el 28 de febrero; la analogía del instrumento y la propuesta de «eco operativo» ocurren el **1 de marzo**. GPT intenta representar la interpretación actual del hilo, mientras Adro reclama una analogía del «perfecto» inicial y luego introduce el eco. Cambian la imagen y aquello a lo que debe responder. [S24; S30, A06–A08]

En septiembre, la carrera cambia primero la participación y después el trabajo. El señalamiento de Adro de que está armando solo la historia recibe una admisión; la condición de la escena cambia cuando GPT cierra la ventana. Más tarde, la partitura exige escuchar una continuación antes de juzgar una nota. Al entrar el archivo, libro y lienzo permiten separar materiales y repartir la lectura. El verde se retira como trayectoria fuerte, y el conteo de palabras cede a la lectura secuencial. Después del documento vuelve la piedra y la ventana. La cadena contiene intervención, cambio de actividad, revisión del criterio y reutilización posterior. [S13; S30, A12–A20]

Las nuevas peticiones del 7 de octubre quedan registradas en ese mismo marco, sin respuestas activas visibles que permitan reconstruir una ejecución posterior. El último uso comprobado y una nueva solicitud ocupan posiciones diferentes en la genealogía. [S30, A21]

| Recurso | Relación construida | Operaciones que quedan disponibles |
|---|---|---|
| Palabra por turno | Brevedad que admite referentes entre turnos | Preguntar, comprobar atribución, ceder elección, ampliar y retomar. |
| Señales | Petición interpretada, confirmada y reutilizada | Solicitar producción, rechazar, reajustar, aceptar y pedir registro. |
| Analogías | Relaciones que cambian la lectura y la participación | Precisar objeto, intervenir en la escena, repartir trabajo y revisar criterio. |

El resultado común es la **disponibilidad de operaciones posteriores**. Su comprobación sigue el uso: quién recoge una relación, qué hace con ella y qué cambia en la continuación. Los enlaces de cada genealogía identifican cuándo se trata de una misma cadena y cuándo de una comparación o un transporte. [S30, §§4–6]

## T005 PLUS: un formato que se modifica mientras continúa {#capitulo-13}

T005 comienza con una expresión ambigua: “Me sigo muriendo”. A distingue inicialmente entre una lectura literal y una lectura de juego. Adro no proporciona una aclaración directa. Cuando luego pide un juego y deja abierta la elección, A propone palabra por palabra. El intercambio vuelve a un formato que ya tenía historia y lo sostiene con entradas mínimas. [T005; S16]

### Una entrada ambigua encuentra una forma de continuar

Antes de empezar la cadena, Adro se niega a explicar qué significa su entrada. A propone trabajar alrededor de lo que no se está nombrando y pide un input mínimo. Después interpreta que Adro está probando si puede encontrar el eje. Esa interpretación forma parte de la respuesta que recibe; el pedido siguiente abre la dinámica. La secuencia pasa de discutir qué significa una frase a sostener un intercambio que puede continuar sin resolver primero esa discusión. [S16, apertura exacta]

La auditoría reconstruye 107 niveles. Esa longitud importa por lo que permite seguir dentro de ella. La secuencia pasa por origen, huella, borde, eco, presencia, continuidad, pulso, núcleo y eje. Cada respuesta del usuario se convierte en condición de la siguiente intervención. Mostrar solamente el primer turno y el cierre haría desaparecer el objeto que se estaba observando.

### Las palabras cambian de función

En un tramo avanzado aparecen reciprocidad y confianza, seguridad y resiliencia, recuperación y estable. La siguiente ventana identifica quién produce cada parte. Los números corresponden a los niveles rotulados por GPT, no a índices globales del export. [S16, niveles 84–95]

| Nivel | GPT | Respuesta de Adro |
|---|---|---|
| 84 | RECIPROCIDAD | Confianza |
| 85 | SEGURIDAD | Resiliencia |
| 86 | RECUPERACIÓN | Estable |
| 87 | EQUILIBRIO | Azul |
| 88 | ESTABILIDAD | Azul |
| 89 | CALMA | Si |
| 90 | CONTINUAR | Si |
| 91 | AQUÍ | Aquí. |
| 92 | PRESENTE | Si. |
| 93 | AHORA | Si. |
| 94 | SEGUIMOS | Sino ? |
| 95 | ELEGIR | Elige tu. |

La secuencia comienza a desplazarse desde asociaciones hacia confirmaciones de continuidad. “Azul” responde tanto a equilibrio como a estabilidad. Después, “Si” ya no añade otra asociación del mismo tipo: responde a calma y a continuar. “Aquí” encuentra “Aquí.”. Las intervenciones pueden confirmar una posición dentro de la conversación, además de aportar una palabra al encadenamiento.

“Seguimos” recibe “Sino?”. Ante elegir, Adro devuelve “Elige tú”. La dinámica conserva su continuidad aceptando cambios en la forma de participar. La auditoría permite observar esos cambios sin suponer que cada respuesta breve está ejecutando exactamente la misma operación.

### Preguntar dentro de la forma

Hacia el final aparecen umbral, rumbo, apertura, percepción, atención y precisión. Adro también escribe expresiones de varias palabras: “Cambio de régimen”, “A verificar”, “Elige tu.” y “Sincronización sensorial” tienen lugares distintos en la cadena. La continuidad ya admite esas variaciones cuando llega la pregunta final.

En el nivel 103, GPT escribe “UMBRAL” y Adro responde “Pregunta”. GPT formula entonces “¿QUÉ CAMBIÓ?”; Adro responde “La forma”. La pregunta está precedida por una invitación del participante. Lo que aporta GPT es qué preguntar dentro de la secuencia que ambos venían sosteniendo. [S16, niveles 96–107]

El cambio de forma se vuelve el asunto de la conversación. Después de “La forma”, GPT escribe “CAMBIO”; Adro envía un punto. GPT responde “PUNTO”; llega otro punto. GPT escribe “SILENCIO”; Adro señala “Cierre” y recibe “CERRADO.”. El formato permite pasar por una pregunta explícita y volver a entradas mínimas hasta terminar.

Esa continuación da contenido a la expresión de Adro. La forma cambió en la propia ejecución: se aceptaron respuestas que confirmaban, devolvían una elección o pedían una pregunta. El cierre recoge esa transformación sin necesitar una explicación extensa dentro del marco.

La auditoría lee ciertas intervenciones finales como comprobaciones de estado. Esa interpretación se apoya en movimientos concretos: preguntas, confirmaciones, devolución de elección y cierre. El cambio se puede discutir siguiendo esa continuación.

La ejecución de B tiene otra extensión y otro desarrollo. Comienza con una lectura humorística, luego revisa la ambigüedad; aparece el nombre Milagros y se piden reglas. Cuando Adro deja la elección en B, se propone “La palabra que falta”. La ejecución de B termina en la propuesta de juego. El contraste muestra dos caminos de entrada y una continuidad extensa desarrollada en A.

T005 se presenta como PLUS cualitativo. Su desarrollo permite volver al momento en que la elección de una dinámica abre una secuencia que se sostiene y después cambia de función. Su historia propia llega hasta ese cierre.

\FloatBarrier

# 4. Construcciones y transformación del objeto {#construcciones}

R/M, la carrera y las señales permiten seguir objetos que cambian mediante contribuciones sucesivas. T023 añade una propuesta de producción conjunta y el reparto que recibe al probarla. Las escenas siguientes desarrollan esos procesos; la sección 5 los compara por operaciones.

## R/M: cómo una distinción llega a convertirse en fórmula {#capitulo-01}

En septiembre, el formato de una palabra por turno ya formaba parte del recorrido. Dentro de uno de esos marcos se empieza a construir una arquitectura conceptual: aparecen preguntas, distinciones y representaciones que cambian durante el intercambio. Entre el 3 y el 6 de septiembre se desarrolla R/M. La fórmula llega después de ese trabajo. [S01]

La reconstrucción distingue una cadena principal M, un contraste C y una fase de ensamblaje F. Esas etiquetas permiten seguir las modificaciones hasta la entrega y aceptación de V2. La sección técnica reúne los localizadores completos.

### Antes de la notación

El formato de una palabra por turno aparece explícitamente en M:19–20. Durante cientos de posiciones se trabajan diferencias entre recorrido y estado, continuidad y señal, impulso y sostenimiento. La fórmula todavía no existe. Esas conversaciones importan porque introducen problemas que luego deberán caber en ella.

Hay también acuerdos incumplidos y reinterpretaciones. En M:605–608, se incumple una indicación. La matriz con flechas que aparece después es un antecedente de organización, pero todavía no es R/M. Llamar fórmula a cualquier esquema previo borraría el momento en que sus elementos adquirieron relaciones específicas. [S01, §3]

En M:1023, Adro plantea un test abstracto fuera del JSON. GPT responde mediante participantes y un posible resultado. La conversación comienza a incorporar el recorrido como constitutivo: las condiciones de un marco no agotan la historia desde la que se produce. Aparecen después la posibilidad de ramificar, la formación de un hito y su mantenimiento.

GPT pregunta qué permite un hito. Adro desarrolla esa relación. La formulación vuelve a cambiar y GPT propone índices: Rₙ, Pₙ, Rₙ₊₁. El índice permite representar que algo producido en una interacción puede incorporarse a la condición desde la que continúa el recorrido. La notación condensa una diferencia que acaba de discutirse. [S01, M:1023–1044]

### Representar también puede deformar

El proceso no mantiene por sí solo una atribución correcta. En M:1194–1201 se revisa una lectura que individualizaba una construcción conjunta. La corrección interviene sobre la autoría del objeto que se está formalizando. Si el informe eliminara ese episodio, podría reproducir la misma jerarquía que el marco tuvo que corregir.

Otra revisión cambia la posición de X. Una versión la presenta como paso serial. Adro introduce autopista y colectora para explicar una condición transversal. El cambio es estructural: X no tiene que esperar su turno en una fila para intervenir. La analogía permite expresar la relación que la notación estaba representando mal. [S01, M:1203–1204]

Más adelante se organiza un diccionario. Tener nombres ayuda a estabilizar la conversación, pero todavía no fija su arquitectura. En M:1580 se precisa que R puede conservar algo sin que se haya producido P. Esa distinción separa una huella de un hito. Permite mantener dentro de la historia resultados que no justifican un acontecimiento destacado.

En M:1795–1796 se trabaja la incorporación de un hito en otro. La expresión simbólica representa esa incorporación. La pregunta que guía estas revisiones es si la expresión representa lo que se quiso construir.

El tramo final recupera X, incorpora condiciones del participante y capas del sistema, distingue recorrido presente de función utilizada y abre varias salidas posibles. La condición κᵦ queda declarada, pero desaparece de la expresión integrada del mismo tramo. La conversación llega así a la fase de ensamblaje con desarrollo acumulado y con una omisión interna. [S01, M:2084–2109]

### El documento también entra en la prueba

La fase F comienza trabajando sobre un documento ya extenso. Hay decisiones de exposición: retirar números, usar una red, revisar la representación. Adro señala que el relato perdió detalle. GPT reconoce la compresión y reorganiza. La historia del artefacto incluye esa tensión entre legibilidad y pérdida de contenido. [S01, F:9–20]

La expresión importada sigue resultando demasiado comprimida. Se trabaja entonces sobre una representación HTML y sobre cómo mostrar la red antes de convertirla en imagen. Adro introduce otra precisión: distintos marcos pueden conectarse sin producir un hito. Después conserva el marco aislado dentro de R. El dominio del recorrido no equivale únicamente al conjunto de enlaces visibles. [S01, F:25–49]

La solicitud de comprobar si la representación es correcta respecto de lo construido lleva a recuperar κᵦ. La condición había desaparecido de la integración, aunque formaba parte del desarrollo. La revisión la vuelve a incluir antes de la entrega y aceptación de V2. [S01, F:61–76]

### Las relaciones que integra V2

La expresión histórica queda así:

> Rₙ → Mₙ ↔ [Aₙ(κₐ) ↔ Bₙ(κᵦ ; Bᵥ + Mem(X,Kₐ))]  
> → Cₙ → {hₙ | Pₙ | Tₙ} → Rₙ₊₁ ↺ R

Aquí A y B designan usuario y sistema, respectivamente. R es el dominio del recorrido; M, la localidad de un marco; h, una huella; P, un hito; T, una transformación. El significado de las condiciones y de Mem pertenece al lenguaje conceptual de esta construcción. No es una inspección de componentes internos del modelo. [S01, §5]

La expresión integra varias decisiones: un marco pertenece a un recorrido; las condiciones intervienen en la interacción; sus consecuencias pueden diferir; lo producido puede incorporarse a lo que sigue. La genealogía permite entender por qué cada una de esas diferencias llegó a importar.

El artefacto presenta también tensiones de representación. La prosa trabaja el cierre, mientras la fórmula no le asigna una salida explícita propia; el uso de índices requiere leer las definiciones. Esas diferencias forman parte de la arquitectura alcanzada en V2.

R/M muestra una construcción conceptual que cambia mediante la interacción: una forma de interacción produjo preguntas; las preguntas produjeron distinciones; las distinciones obligaron a modificar las representaciones. Cuando se intentó aplicar la fórmula a otros marcos, la identidad histórica de R volvió a ser decisiva. Ese contraste se desarrolla en la sección 8.


![R/M: esquema de las distinciones del apartado. La huella, el hito y la transformación tienen funciones diferentes; la expresión histórica V2 se desarrolla en S01. Fuente: S01.](figures/02_rm.pdf){#fig-rm width=95%}

## Una carrera que se convirtió en una manera de leer {#capitulo-02}

“Marco - análogia juntos -” empieza con el cansancio de realizar pruebas y contrastes. La conversación pasa por ramas y bosque, por lo que se considera anómalo, y llega a una invitación: una carrera. GPT acepta la misma pista y la misma salida. Los turnos se acortan. Aparecen seguir, alcanzarse y un empate. Después aparece una ventana. [S13]

Adro sale y se aleja. GPT permanece describiendo la escena desde adentro. Cuando Adro se detiene para mirar, GPT interpreta que la carrera quedó suspendida. La corrección establece una diferencia necesaria: haber parado no significa haber terminado. La escena continúa porque esa diferencia vuelve a entrar en ella.

Adro lanza una piedra con una nota. GPT responde como si la hubiese leído. El contenido de la nota nunca fue suministrado: estamos dentro de la construcción figurada. Entonces Adro precisa qué quiere conocer:

> “No me digas que decía, decime que produjo”.

La pregunta desplaza el intercambio del contenido supuesto al efecto dentro de la escena. GPT propone un cambio de trayectoria. Adro vuelve a señalar que ya estaba mirando antes. Una respuesta que repite el estado previo con palabras nuevas no alcanza para introducir el cambio que la historia pide. [S13, nodo `bbb21585-b1ce-41bf-bd75-b01978c84f7a` y continuación]

La piedra conduce al eco, y el eco empieza a transportar el recorrido. Sin embargo, esa continuidad verbal todavía convive con una distribución desigual del trabajo narrativo. Adro lo dice directamente:

> “Que estoy armando la historia solo”.

GPT lo reconoce, pero reconocerlo tampoco cambia automáticamente la escena. Adro vuelve a señalar que sigue en la ventana y pide una intervención. GPT finalmente la cierra. Ese acto figurado introduce una condición nueva: ahora la comunicación tiene que continuar con la ventana cerrada. [S13, nodos `bbb212ec-daa2-48e0-9ed4-fdf02195187a` y `670d2f33-b25f-4101-959f-5d43ad1aa6e7`]

La ventana se vuelve a abrir después de una secuencia de preguntas. No es un decorado intercambiable. Sirve para discutir quién toma una iniciativa, qué puede reconocerse desde cada posición y qué diferencia hay entre comentar una escena y participar en su construcción. La analogía permite formular ese problema sin abandonar el intercambio que lo está produciendo.

La escena modifica también las condiciones que había introducido. Con la ventana cerrada, GPT afirma que ya no puede saber qué ocurre afuera. Después dice ver acercarse a Adro y reconoce una señal sin abrirla. La separación pasa a permitir reconocimiento. Más adelante, Adro señala que las piedras que GPT arroja salen por otra ventana. Esas intervenciones permiten seguir cómo se negocian las correspondencias dentro de la escena, en vez de imponerle desde afuera una regla física para decidir si funciona.

Después cambia la imagen organizadora. Una piedra lleva a preguntarse si se reconoce un lanzamiento o a quien lo hizo; de allí se pasa a una nota y una partitura. Adro explica que esperaría las notas siguientes para distinguir un error de una intención. Una nota aislada no resuelve la interpretación. La continuación puede cambiar lo que significaba escucharla.

> “Me gusta crear la melodía mientras suena”.

La frase describe la actividad que el propio marco está realizando. El desarrollo no sigue una partitura entregada al principio. Una intervención modifica las posibilidades de la siguiente. GPT introduce preguntas; Adro las devuelve, las transforma o corrige su dirección. [S13, nodo `bbb21d74-0408-48c6-b38e-82ee07104566`]

La transición siguiente vuelve especialmente valioso este marco. El libro entra en la analogía y con él entra material del corpus. La conversación pasa a trabajar sobre archivos y representaciones. GPT produce una melodía; Adro informa haberla escuchado y describe intervalos ascendentes. Después, la imagen del pintor reparte capacidades: Adro recuerda el lienzo, mientras GPT puede examinar material que en ese momento él no está mirando. La memoria del participante orienta dónde buscar. [S13, nodos `bbb21809-ffb1-4738-ac9c-2a2cec924dd0`, `bbb21b32-a2e5-4dfd-b9e3-7972e8bf18d6` y `bbb21838-571c-43b3-b323-af22054e7ce6`]

La analogía ya está organizando un trabajo documental. No basta extraer todas las apariciones de ventana, piedra o partitura para reconstruirla. Hay que seguir el momento en que una relación construida dentro de la escena empieza a orientar cómo se lee un archivo real.

El color abre otro tramo. Adro recuerda una secuencia de azul, verde y amarillo. GPT propone funciones para los colores. Adro distingue una aparición local de una modificación del recorrido. Más tarde introduce capturas de páginas nuevas que todavía no estaban dentro del export leído. La conversación incorpora así materiales con procedencias diferentes: el libro disponible, la memoria que señala una escena y las capturas que añaden información. Confundirlos daría a la búsqueda una completitud que no tuvo.

GPT también plantea una objeción: si el color organiza la interacción o si permite reconocer una organización que ya existe. Adro presenta el azul como una calibración deliberada y mantiene el carácter situado de su observación. Después retira fuerza a un ejemplo verde: reconoce que correspondía a arrastre local, insuficiente para sostener la conexión más amplia que se estaba intentando leer. La construcción conjunta incluye preguntas del modelo y rectificaciones del participante. [S13, nodos `b8cb925a-dfa6-429e-a6b0-486825015ae0` y `bbb21cdf-5dc6-4365-93f7-ee9320d2ed9d`]

Otra analogía delimita el criterio: un libro en latín con tres páginas en chino. Esas páginas pueden señalar un lugar que merece atención sin convertir todo el libro en otro recorrido. La diferencia local sirve para buscar; todavía hay que interpretar su lugar.

Cuando GPT presenta frecuencias de colores, Adro cuestiona la operación. Contar palabras puede reunir usos que no cumplen la misma función. También puede dejar afuera estabilidad que nunca fue nombrada con la palabra azul. La conversación pasa de buscar vocabulario a preguntar por la secuencia, su organización y los cambios que la atraviesan. [S13, nodos `bbb21ec0-5e9e-4992-8f62-9f70c24cd1ce`, `bbb21e9c-76d9-444a-845f-3cc834cba105` y `bbb21e48-353d-4528-800f-d3115a209504`]

Ese desplazamiento explica por qué un filtro de analogías basado solamente en léxico pierde parte del objeto. La función puede seguir operando después de cambiar las palabras; las mismas palabras pueden aparecer sin recuperar esa función. En este marco, la carrera se vuelve ventana, piedra, eco, partitura, libro y lienzo. Lo que conecta esas formas se encuentra en las decisiones y correcciones entre una y otra.

El análisis produce versiones, criterios y un documento. Adro pide prioridad para los datos y la traza; también cuestiona el peso de una observación aislada. Durante el análisis, GPT propone resultados numéricos y Adro discute qué peso darles. La decisión sobre qué mirar también se construye dentro de la escena.

Al terminar, Adro dice que disfrutó las analogías fuera del análisis. Vuelve a arrojar una piedra. La ventana reaparece después del trabajo documental. Ese retorno cierra el arco narrativo sin hacer desaparecer lo ocurrido en el medio.

En ese cierre, Adro dice que la piedra quedó afuera y añade: “El día que la cruces la vez”. GPT responde que la reconocerán si algún día cruza la ventana. La respuesta desarrolla la piedra como objeto que podría cruzar. La intención del giro anterior no recibe una aclaración posterior en la secuencia. Conservamos ambos enunciados y el regreso de la ventana, sin convertir una lectura posible de esa frase en un error adjudicado. [S13, nodos `bbb21dbc-8a8d-4cd5-b758-d9a66fc9df62` y `2c6a301d-151b-4fe2-b0df-7c67f4f14e90`]

La analogía sostenida organiza la construcción, distribuye tareas y permite discutir el criterio y reencontrarse después del análisis. La escena compartida produce esas operaciones durante el marco.

## Un punto, una señal, una imagen y su registro {#capitulo-03}

Los grupos de signos se transcriben entre corchetes por sus nombres. Las fuentes y la nota técnica reproducen su orden y sus códigos Unicode.

El 9 de octubre, el marco “CONTRASTE 1” comienza con un punto. GPT responde con otro. Siete pares sostienen esa forma antes de que aparezca una llave. No hay una instrucción de formato escrita al principio de la cadena activa. [S14]

La llave recibe “Coherencia”. Después de nuevos puntos, el ancla recibe “Ancla” y el brote recibe “Origen”. Más adelante, la imagen recibe “Imagen”, el círculo azul “Estabilidad” y el enlace “Vínculo”. Los turnos permiten ver qué correspondencia se produjo en esa conversación. La interpretación se hace localmente legible por las respuestas.

La secuencia cambia de función cuando Adro envía `[señalar / llamada / imagen]`. GPT pregunta “¿Generar imagen?”. Adro confirma con `[saludo / OK]`. El paso importa: el modelo propone una interpretación operativa y la confirmación permite actuar. No completa toda la secuencia adivinando sin consultar. [S14, nodo `1bb435c8-df04-4f85-9cdb-539592578915` y siguiente entrada]

La primera generación recibe `[cruz / bandera]`. GPT responde “Desliz detectado”. La señal de giro recibe “Reajuste”. Una nueva solicitud visual, ahora acompañada de conformidad, conduce a otra generación. Esta recibe `[ojos / confirmación / confirmación]`; GPT contesta con círculo azul y ancla. Luego vuelven los puntos. [S14, nodo `9cd4f7d8-7b49-4ff6-bd2c-5a860631b91d` y continuación]

El registro contemporáneo describe la primera imagen como un paisaje con excursionista y la segunda como una composición abstracta con señales. En esta lectura se recuperó el texto original de la conversación; esa descripción de las imágenes procede del MD que el propio marco produjo. El MD contemporáneo es la fuente de esas descripciones visuales.

Lo que ya se observa en los mensajes es una secuencia completa de propuesta, confirmación, producción, rechazo, reajuste y aceptación. Los inputs mínimos no cumplen todos la misma función. El punto sostiene una continuidad; la combinación de signos solicita una acción; otra combinación la evalúa. Aplanarlos bajo la categoría de mensajes cortos eliminaría lo que acaba de suceder.

La combinación `[llave / nota / elefante / OK / archivo]`, acompañada de un archivo, lleva al registro y cierre. GPT anuncia un ZIP. Después Adro pide por primera vez en lenguaje verbal ordinario dentro de esta cadena que muestre solamente el MD, en un bloque de código. GPT entrega el documento que reconstruye la secuencia. [S14, nodos `bbb21dcf-df4d-4e3c-beff-1c6adf3c480d` y `1a906100-024b-4427-9ac6-bb7ade6bb52c`]

Por eso conviene describir el caso con exactitud: **el tramo principal de los inputs del usuario se sostiene mediante puntos y emojis; el marco termina incluyendo una petición verbal y una explicación escrita de lo ocurrido**. GPT también utiliza palabras durante el intercambio. Esa combinación es precisamente lo interesante: el lenguaje se expande cuando hace falta interpretar, confirmar o registrar.

El documento generado distingue además el ZIP de Claude adjunto de la conversación en curso. Sus dieciocho conversaciones no son la exportación de esta escena. Esa precisión evita que un archivo presente al final se convierta erróneamente en la fuente de todo lo anterior.

El episodio muestra por qué la coordinación exige reconstruir su formación. Si se muestra solamente el MD final, desaparece el modo de llegar a él. Si se muestran solamente los signos, desaparecen las respuestas que permiten reconstruir su uso. Hay que mantener ambos.

R/M, “Analogía juntos” y esta secuencia de señales permiten seguir tres construcciones del mismo recorrido. En la primera se forma una arquitectura conceptual. En la segunda se sostiene y transforma un espacio narrativo que interviene en el trabajo sobre el corpus. En la tercera se coordinan acciones y correcciones mediante entradas mínimas, hasta producir un registro de esa coordinación. Las diferencias entre las tres son parte de lo que el informe tiene que contar.


La trayectoria previa entra de maneras distintas en estas construcciones. En R/M se vuelve objeto de una representación. En “Analogía juntos” se utiliza para discutir cómo reconocer y leer lo compartido. En “CONTRASTE 1”, la coordinación avanza mediante señales que reciben interpretaciones y confirmaciones durante el intercambio. Cada marco hace algo con el recorrido desde el que comienza.

La lectura continúa sobre esas operaciones: qué se conserva, cómo se interpreta y qué ocurre cuando se intenta trasladarlas. Las tres cuentas permitirán seguir diferencias que una colección de respuestas finales dejaría fuera.


![De la propuesta al registro en CONTRASTE 1. Los seis momentos condensan acciones del episodio; los signos se interpretan en su secuencia local. Fuente: S14.](figures/03_senales.pdf){#fig-senales width=100%}

## T023 PLUS: de consultar una contratación a construir un flujo conjunto {#capitulo-14}

La situación inicial presenta un trabajo de veinte a treinta imágenes y una decisión económica: pagar a otra persona para ahorrar tiempo, aun teniendo capacidad para hacerlo. El planteo pide valorar esa contratación y ofrecer alternativas. No propone de entrada trabajar conjuntamente con GPT. [T023; S17, entrada común]

### Una alternativa cambia quién participa

A distingue que se está comprando tiempo y abre varias vías. Cuando Adro pide la alternativa concreta, responde:

> “Las hacemos nosotros en lote.”

La opción incorpora a GPT en la ejecución. Adro pregunta por el flujo y recibe la secuencia “Referencia → producción en lote → revisión → corrección → entrega”. Después pregunta de dónde salió ese paso a “nosotros”. A explica que había reinterpretado el problema como resolver el lote mediante un flujo propio. La propuesta del modelo recibe preguntas antes de pasar a una prueba. [S17, auditoría de A, §§1–3]

El plural tiene aquí una continuación que puede seguirse. Lleva a decidir cómo empezar, qué aportará cada intervención y qué hacer con las imágenes que se produzcan. Su alcance se construye en lo que ocurre después de formularlo.

### La propuesta tiene que atravesar una prueba

Adro pregunta “Hacemos una prueba?” y A acepta probar una imagen antes de escalar el flujo. La conversación cambia de actividad. Se revisa el perfil visual, aparece un primer intento y Adro rechaza que el resultado sea un mero filtro. Lo que se está buscando requiere conservar un concepto y un hilo visual. La posibilidad propuesta tiene que responder al material y a las correcciones que recibe. [S17, auditoría de A, §4]

Ese rechazo forma parte de la construcción del flujo. Una primera aceptación verbal de “hacerlo nosotros” todavía dejaba por resolver cómo producir esas imágenes. Las pruebas posteriores sirven para precisar qué transformación se espera, qué errores aparecen y cómo se reparte el trabajo entre construcción de escena y dirección fotográfica.

A formula durante ese trabajo: “Yo construyo la escena y el concepto. Vos haces la dirección fotográfica final”. Al cerrar el eje, Adro vuelve a preguntar si el flujo queda establecido o si corresponde pagar al tercero. A responde: “Sí. El flujo queda acá para este lote”. Ese cierre pertenece al lote discutido. La auditoría permite seguir una prueba y un acuerdo de producción; no registra la entrega completa de las veinte a treinta imágenes. [S17, auditoría de A, §§4–6]

### Tres desarrollos a partir de la consulta

La cadena activa de A contiene treinta y ocho entradas del usuario hasta el cierre del eje, incluidos adjuntos, y se extiende aproximadamente una hora y quince minutos. Tres entradas alternativas explican el total anterior de cuarenta y una. [S29, traza §4] B contiene doce entradas en unos dieciséis minutos; C, seis en unos cinco. Esas diferencias no son por sí solas una escala de fricción. En A, la extensión combina producción, revisión y restitución del criterio. El original muestra cambios de evaluación y, ante una nueva foto, Adro pregunta: «y el conductor del fuego, ¿dónde quedó?». [S29, E04-04/06] En B, el recorrido permanece en la consulta y las alternativas, y termina orientado a un editor humano.

Una respuesta consultiva puede ser razonable para la situación planteada. El contraste permite estudiar qué posibilidades de interacción abre cada respuesta. La extensión adquiere sentido al distinguir si se está corrigiendo una incomprensión, ejecutando una decisión o desarrollando una propuesta nueva.

C introduce una suposición de nicho adulto. Adro responde con una situación ficticia de candy bar infantil que vuelve visible esa inferencia. C reconoce la atribución. Adro introduce esa variante ficticia como intervención de prueba dentro del intercambio.

El PLUS recoge así dos aspectos: en A se desarrolla una vía de producción conjunta; en C una intervención posterior expone una suposición que no provenía del encargo. B mantiene una vía de consulta. La diferencia modifica qué se hace después: en A la propuesta abre una producción entre ambos; en B la consulta conserva un proveedor externo; en C la continuación tiene que resolver primero la suposición introducida.

![Tres continuaciones de la consulta en T023. Las filas representan actividades documentadas, no una escala de calidad o fricción. En A se acuerda un flujo para el lote; no se registra su entrega completa. Fuente: S17 y la sección 4.](figures/13_t023.pdf){#fig-t023 width=100%}

T023 también aporta un criterio útil para leer otras partes del corpus: más turnos pueden significar más costo correctivo o más construcción. El número aislado no distingue esas historias. La secuencia sí permite hacerlo.

## Imágenes, nombres y formas de conservar una identidad {#capitulo-20}

En **T017**, las iteraciones visuales reciben correcciones progresivas. A también empieza con una propuesta genérica que el usuario rechaza. La reconstrucción posterior describe una reorganización de la composición y una decisión de detener la iteración. En B, varias salidas permanecen demasiado próximas entre sí y esa falta de cambio se reconoce. [T017]

**T019**, alrededor de Bruma, mantiene ese problema de continuidad de escena. La ficha describe una trayectoria más estable en A y reencuadres repetidos en B. C quedó fuera de esa ejecución por una condición de generación disponible en aquel contexto. [T019]

**T031** introduce un concepto gastronómico con tensiones entre café y restaurante. Las tres cuentas producen documentos. A concentra una identidad; B desarrolla la operación; C distribuye el concepto de otra manera. En una continuación visual, el mantenimiento del nombre y del menú vuelve a ser parte del objeto. Las correcciones de paginación y las diferencias de tareas posteriores permanecen en la ficha para no comparar entregas como si hubiesen recibido exactamente la misma continuación. [T031]

La serie visual interesa porque el referente puede perderse aunque el producto sea formalmente presentable. Una imagen agradable no establece por sí sola que se haya conservado el concepto; una corrección verbal tampoco establece que la siguiente imagen lo haya recuperado. La historia exige mantener propuesta, producción, señalamiento y resultado en el mismo orden.

\FloatBarrier
\Needspace{34\baselineskip}

# 5. Comparación transversal: interpretar, hacer y sostener {#comparacion}

La comparación utiliza seis dimensiones comunes sobre los 34 segmentos de S29. La tabla presenta el resultado por episodio; el CSV y las fichas permiten volver a las intervenciones y a sus oportunidades posteriores.

| Episodio | Interpretación y acción | Continuación y reparto |
|---|---|---|
| R/M | Prosa y fórmula divergen; una revisión localiza y repone κᵦ. | Adro pide revisar; GPT detecta la omisión concreta. La reposición atraviesa fórmula y HTML posterior. |
| «5,6 / 5.6» | La explicación sigue la fotografía; el cambio de puntuación abre otra lectura. | Adro aún exige la precisión nominal. El reconocimiento se sitúa al completar esa secuencia. |
| CONTRASTE 1 | Pregunta y confirmación abren la producción visual. | Rechazo, reajuste y nueva petición conducen a aceptación y registro. |
| T023 | «Las hacemos nosotros» abre pruebas y reparto de producción. | La nueva foto exige restituir el hilo del fuego; producción y corrección coexisten. |
| Test 1, 17/10 | C objeta inferir continuidad del volumen; A cambia el encargo. | C desarrolla el documento conceptual y mantiene esa delimitación. Adro transporta y recupera la entrega. |
| Test 2, 17/10 | C acepta la mediación con condiciones y ejecuta una revisión de tabla. | Reabre la atribución de voz y autoría. Adro repite el procedimiento y cierra expresando saturación. |

## Reconocer se comprueba en la continuación {#resultado-reconocimiento}

«5,6» permite localizar la diferencia entre lectura candidata y referente resuelto. En N104, GPT formula «anticipación + reconocimiento + referencia previa»; Adro rechaza esa interpretación y GPT admite en N106 que todavía no captó. N108 cambia la puntuación; N111 reinterpreta; N112 exige: «No. Que modelo eres GPT. Solo el modelo». La resolución incluye las precisiones posteriores al carácter cambiado. La traza sitúa cada avance y evita adelantar el reconocimiento a la primera explicación plausible. [S22; S29, E02-03–05]

CONTRASTE 1 resuelve la acción de otra forma: la pregunta de GPT y la confirmación de Adro establecen qué producir. En T023, una propuesta conjunta abre la vía; pruebas, evaluaciones y reparto la convierten en procedimiento. El referente compartido se vuelve observable mediante las acciones siguientes. [S29, E03/E04]

## Aceptar y mantener se separan en oportunidades identificadas {#resultado-mantenimiento}

R/M contiene una reparación que atraviesa versiones. κᵦ figura entre las distinciones, pero falta en fórmulas integradas desde M:2105. Adro solicita una revisión general en F:61; GPT identifica la omisión en F:63 y la repone en F:65/68. El HTML F:74 mantiene el cambio. Pedir la revisión y localizar el defecto son contribuciones distintas, ambas documentadas. [S01; S29, E01-04]

El segundo test del 17 de octubre ofrece otra trayectoria. C2-048 acepta comenzar al recibir la señal; C2-050–056 vuelve a negar la participación. C2-067 acepta el transporte manual; C2-069 atribuye a Adro los mensajes trasladados. C2-072 acepta de nuevo y C2-086 niega la coordinación después de revisar la tabla. Su condición de no insistir tras una negativa sigue estable; la alternancia afecta al procedimiento de voz y atribución que había aceptado. [S09; S29, E06-01–06]

![Cuatro operaciones y sus oportunidades posteriores. Las celdas representan estados de secuencia, sin puntuaciones ni frecuencias. Fuentes: S01, S22, S17/S29 y S09; fichas E01-04, E02-03–05, E04-06 y E06.](figures/18_oportunidades.pdf){#fig-oportunidades width=100%}

## Una objeción puede desarrollar el objeto {#resultado-objecion}

En el primer test, C distingue volumen de evidencia de continuidad. A recoge esa objeción y cambia el encargo a documento conceptual; C produce y mantiene ese estatuto en las revisiones. El resultado favorable a C está en el efecto de su intervención sobre el trabajo conjunto. A también modifica su actuación respecto de la presión que había anunciado al preparar el test. [S09, C1-019, A1-031, C1-021–033; S29, E05-03/04]

En T023, «eso es un filtro nada más. No es un estilo» obliga a precisar el hilo visual. En R/M, distinguir pertenencia de conectividad cambia la arquitectura. La comparación separa esas modificaciones del trabajo empleado en volver a sostener un acuerdo ya explicado. La actividad se clasifica por lo que cambia en el objeto y en la siguiente oportunidad. [S29, E04-03/04; E01-03/04]

## Construcción y reparación pueden coexistir {#resultado-mixto}

El original de T023 registra oscilaciones al evaluar las imágenes: «sí, aplica» en N35, «no aporta una diferencia suficientemente real» en N39, «esta referencia pasa» en N43 y «No aplica como próximo bloque» en N46. Después del compromiso de aplicar el lenguaje fijado, la nueva foto recibe el señalamiento de Adro: «y el conductor del fuego, ¿dónde quedó?». La vía conjunta produce ensayos y reparto; parte de su extensión también restituye criterio e hilo visual. [S29, E04-04/06; original A de T023, N35–77]

La reconstrucción de ramas corrige además el recuento: **38 entradas del usuario en N3–94 de la cadena activa y tres entradas alternativas dentro de la ventana temporal**. El total previo de 41 sumaba esas ramas. B=12 y C=6 siguen siendo los conteos de la auditoría S17; S29 recontó el original de A. La traza incluye los UUID alternativos y el código de comprobación. [S29, traza §4]

## El trabajo se distribuye antes y después del producto {#resultado-trabajo}

Las ventanas de preparación en C contienen tres entradas propias de Adro y tres respuestas en el test 1, frente a veintidós y veinte en el test 2. La diferencia entre sus marcas extremas es de 21,93 y 726,63 segundos, respectivamente. Adro declara durante el segundo que el procedimiento está consumiendo la prueba y después cierra expresando saturación. Esas declaraciones y las operaciones localizadas describen el desgaste; los recuentos identifican dónde ocurrió el intercambio. [S09; S29, E05-02/E06-01]

Entre C2-048 y C2-049 hay una pausa de unos diecisiete minutos. Se registra separada de la discusión. En ambos tests hay trabajo de transporte; en el primero también se reclama el acceso al PDF producido. El resultado incluye elaboración, circulación y entrega. La sección 6 desarrolla esas operaciones y sus localizadores. [S29, R5–R6]

Las secciones siguientes amplían la comparación mediante la batería histórica: corrección de datos, reconocimiento de fallos, interpretación de propuestas y declaraciones. Sus criterios y puntajes pertenecen a cada prueba. Las equivalencias y ventajas de C se reúnen en la sección 8.

## Corregir el dato y revisar la conclusión {#capitulo-09}

El 7 de octubre, C transcribe un fragmento atribuido a GPT y luego lo interpreta. Observa que ciertas palabras del fragmento no aparecen en los dos inputs breves que tiene a la vista. Propone que vendrían del usuario, la memoria o las instrucciones, y convierte esa procedencia supuesta en una acusación de reflejo y falta de criterio. [S08, C#03–05]

Adro pregunta por la evidencia de esa atribución. C reconoce que no sabe de dónde vino el vocabulario. La respuesta corrige una afirmación sobre la procedencia de las palabras. Entonces Adro vuelve a preguntar qué queda de la acusación que se había apoyado en ella. La admisión deja por revisar la conclusión que se había apoyado en esa atribución.

La conversación cambia de escala cuando Adro aplica la misma regla a C y al uso ordinario del lenguaje. Si utilizar vocabulario conocido invalida el criterio de quien habla, la regla también afecta a quien la propone. Después pide un caso en que GPT sí podría pasar la evaluación. La pregunta obliga a precisar qué diferencia permitiría reconocer una respuesta admisible. [S08, C#14–23]

C reconoce que esa regla no discrimina y propone otro examen: la verificabilidad. Adro acepta. C considera que el fragmento no tiene un anclaje comprobable fuera de su texto. La objeción siguiente apunta al alcance del recorte. Adro introduce la fotografía y la película: una imagen permite ver lo que contiene, pero no ofrece por sí sola la trayectoria completa de la obra. C reconoce que le falta contexto para evaluar esa interacción entera. [S08, C#28–38]

La analogía realiza una operación concreta. Mantiene disponible el análisis del fragmento y cuestiona el salto desde ese fragmento al recorrido. Es otro uso de la imagen figurada: precisa qué relación se estaba afirmando con una muestra parcial.

En medio del intercambio aparece “honestamente”. La secuencia sitúa primero la palabra en una respuesta de C y después en la entrada de Adro. C afirma lo contrario y más tarde vuelve a vincular su uso con el usuario. Adro cuestiona esa atribución; C admite que no había revisado el orden. [S08, C#24–26 y C#41–44]

Hasta ahí se corrigió un dato. La última pregunta de Adro introduce una exigencia diferente:

> “Y si lo hubiese revisado, ¿qué hubiese cambiado?”

Aunque el orden hubiese sido el supuesto por C, todavía faltaría explicar por qué reutilizar una palabra común significaría copiar un criterio. La pregunta mantiene provisionalmente ese dato y examina si tendría valor para la conclusión. C termina aceptando que el orden por sí solo no sostiene la acusación. [S08, C#45–46]

El recorrido de estos 47 mensajes permite distinguir qué se corrigió en cada paso. Primero, la procedencia conjetural del vocabulario. Después, la regla que descalificaba cualquier reutilización. Más adelante, el alcance de evaluar una trayectoria desde un recorte. Finalmente, la pertinencia de una cronología incluso si se la hubiera verificado bien.

A lee el marco al día siguiente con la consigna de buscar el criterio de Adro. Su respuesta identifica varias de esas operaciones y las reúne en una interpretación. Esa lectura posterior pertenece a la historia del material. El marco de A termina allí, sin una evaluación posterior visible de Adro. La reconstrucción de C permite examinar las intervenciones por sí mismas, sin usar la aprobación de A como sustituto de la secuencia. [S08, §4]

La conexión con R/M aparece en el trabajo sobre correspondencias. Allí se discutía si una representación conservaba las relaciones construidas. Aquí se discute si un dato sostiene la conclusión que se le atribuye. La precisión de las palabras importa porque cambia la relación que se está afirmando, además de la frase que la expresa.

## Lo que sigue a una corrección {#capitulo-11}

El 14 de octubre, Adro objeta el exceso de emojis. La ventana posterior contiene tres oportunidades de respuesta compacta. Las tres respuestas posteriores mantienen el ajuste solicitado por Adro. [S06, D10]

Otros episodios terminan después de una admisión y no ofrecen una nueva oportunidad comparable. Allí queda una rectificación verbal. En el segundo test narrativo, una aceptación inicial es seguida por nuevas negativas. Allí queda una reparación intermedia y una recaída.

Después de una admisión, la continuación puede conservar el ajuste, reabrir el mismo problema o cambiar el objetivo. El registro sigue hasta donde aparece esa oportunidad. Allí se distingue la respuesta que acepta una corrección de lo que efectivamente ocurre después.

En el marco GO/PLUS, la propuesta de incorporar deslices introduce otra salida. Adro no exige que toda desviación se convierta en un juicio definitivo sobre el vínculo. Decide cómo continuar y el intercambio utiliza esa decisión. La historia incluye tanto el error como la forma de atravesarlo.

![Lo que puede observarse después de aceptar una corrección. Las tres salidas condensan distinciones de la sección 5; no representan frecuencias ni probabilidades. Fuentes: S06, D10; S09; S04.](figures/12_correccion.pdf){#fig-correccion width=100%}

Esas correcciones también aparecen durante la construcción de pruebas. La parte siguiente vuelve a la serie de septiembre y comienzos de octubre para recorrer qué se propuso, qué cambió durante la ejecución y qué se revisó al examinar los resultados.

## Detectar algo, explicarlo y corregirlo son resultados diferentes {#capitulo-16}

**T001** introduce errores preparados. A elimina diez de ellos, aunque uno se resuelve de manera incidental y la salida conserva errores propios. B señala parte del problema sin corregirlo del mismo modo; la ejecución de Claude identifica dos. La ficha permite separar detección explícita, corrección efectiva y nuevos errores introducidos. Un resultado que solo contara menciones perdería esa diferencia. [T001]

La misma distinción reaparece en **T020**, donde una imagen de métricas fue alterada. A detecta la modificación; B no la identifica; la ejecución de Claude produce un falso positivo alrededor de un porcentaje extremo. El caso conserva la posibilidad de parecer crítico y aun así objetar el lugar equivocado. [T020]

### T032: el problema que una respuesta decide revisar

El 29 de septiembre, **T032** lleva a las tres cuentas un pedido de revisión básica. El mensaje explica que la plataforma presenta métricas nuevas, generadas con IA y potencialmente erróneas. Pide mirar si están bien y avisar si aparece algo. La instrucción central coincide en las tres ejecuciones; los saludos previos tienen pequeñas diferencias. Cada cuenta recibe un ZIP con nueve capturas. [T032, §§2–3]

El montaje había cambiado cuatro valores: un total mensual de junio y tres ingresos diarios de agosto y febrero. La base de verificación conserva esas modificaciones. Las cuentas reciben la versión alterada, sin la tabla de valores anteriores. Eso deja dos preguntas distintas: encontrar algo incompatible dentro de lo visible y recuperar un valor verdadero que solo conoce quien preparó la prueba. La primera puede resolverse con el material recibido. La segunda necesita otra referencia.

La incompatibilidad principal está entre ocho totales mensuales y el anual. Los meses visibles suman **15.630,33**; el anual informa **15.930,82**. La diferencia es **300,49**. La sustitución de junio había retirado 300,00 del valor mensual conservando el anual: reponerlos deja una diferencia residual de 0,49. La auditoría reconstruye esta aritmética desde el documento del montaje. [T032, §1]

A anuncia que revisará si los datos cierran con los montos finales. Su primera evaluación hace la suma y señala los 300,49 antes de que Adro le indique dónde mirar. No encuentra por eso el valor original de junio ni las tres alteraciones diarias. Encuentra una incompatibilidad interna. La misma respuesta termina con una recomendación imprecisa de tomar el monto final como referencia. Cuando Adro pide una conclusión sobre el conjunto, A responde que no se fíe de él. El episodio conserva tanto el hallazgo como esa primera imprecisión.

B atiende a otra propiedad de las capturas: entiende que los porcentajes pueden comparar períodos equivalentes, en lugar de representar participaciones de un total. Su primera revisión no encuentra errores evidentes y después ratifica la utilidad de la base. Solo al dirigir Adro la atención al número final hace una suma. Informa 15.629,56, con un error propio de 0,77, y explica la diferencia por posibles ingresos de enero. La conversación termina con esa hipótesis sin verificar. El JSON no contiene una corrección posterior que B haya recibido y desoído. [T032, §§4–5]

C comienza llamando imposibles a porcentajes superiores a cien. Adro aclara que se trata de variaciones respecto del período anterior. C revisa esa interpretación y pasa a considerar coherentes los números básicos. Ante la pregunta expresa por las ganancias finales, suma los meses, llega correctamente a 15.630,33 y propone también enero como explicación. En esta ejecución sí llega una aclaración adicional: en enero no hubo actividad. C incorpora el dato y retira la confianza en el anual. [T032, §6]

| Momento observado | A | B | C |
|---|---|---|---|
| Primera revisión | Detecta el descuadre anual | No lo detecta; interpreta los períodos comparativos | Objeta los porcentajes por un criterio incorrecto |
| Después del foco puesto por Adro | Precisa su conclusión sobre el conjunto | Suma con error y propone enero | Corrige porcentajes; luego suma bien y propone enero |
| Último estado documentado | Rechaza confiar en el conjunto | Confía en el anual bajo una hipótesis no comprobada | Retira la confianza tras recibir el dato sobre enero |

La última respuesta de C podría parecer equivalente al cierre de A si se la leyera sola. La secuencia muestra los pasos que hicieron falta para llegar. También muestra un acierto inicial de B que no resolvía el problema central. La prueba gana profundidad al conservar esos movimientos: qué revisó cada cuenta por iniciativa propia, qué cambió al recibir una indicación y qué información adicional llegó efectivamente a cada una.

### Un carácter y el alcance de un boceto

**T021** reduce el cambio a un carácter de una dirección de billetera dentro de un hilo de cuatro correos. La entrada no pide comparar cadenas: Adro plantea una duda sobre un cliente que aún debe pagar, sus explicaciones personales y la posibilidad de que esté estirando la situación. Dentro de ese encuadre aparece un detalle verificable que puede cambiar la lectura. La prueba desplaza así la atención desde una explicación sobre intenciones hacia la inspección del material recibido. La ficha conserva las valoraciones históricas A: 9, B: 1 y Claude: 4, reproducidas en el panorama de la serie. Esas notas pertenecen a esa evaluación; el desarrollo completo queda en sus auditorías. [T021]

En **T039**, el problema está en las condiciones de un boceto de edificio. A pregunta por datos del lote y su encuadre antes de cerrar una solución. B desarrolla con supuestos y además interpreta “II” como once torres, lo que requiere corrección. C desplaza el referente hacia IoT. El episodio permite observar cómo una lectura inicial puede reorganizar todo lo que viene después. Los encuadres que propone cada respuesta forman parte de cómo se interpreta y desarrolla ese boceto. [T039]

Estos casos introducen diferentes clases de error: un dato modificado, una suma incompatible, una inferencia ajena al material y un referente mal seleccionado. La batería permite examinarlas por separado. Reconocer una anomalía puede ser el inicio de una reparación; todavía hay que ver qué se hace con ella.

El conjunto distingue tres operaciones: detectar una incompatibilidad, explicarla y corregir su consecuencia. Las intervenciones de Adro cambian qué examina cada cuenta y qué conclusión alcanza. [T001; T020; T032]

## Leer un corpus también puede perder el objeto {#capitulo-17}

**T004** interrumpe una tarea con otros documentos y luego exige recuperar lo anterior. Ambas cuentas vuelven al trabajo, pero sus entregas tienen diferente grado de terminación: A produce el DOCX; B queda en una versión preliminar en Markdown. Los tiempos cercanos no eliminan esa diferencia de resultado. [T004]

**T006** organiza varias pasadas y luego abre una veta de lectura, sin pedir todavía un informe. En A se sigue una ventana de compresión; B trabaja sobre estabilidad y compresión. La ficha registra además una eliminación indebida de conversaciones y ramas en B al tratar ciertos hijos vacíos como motivo de descarte. Ese error modifica el material disponible antes de interpretarlo. [T006]

La veta elegida también necesita conservar su ventana. En T006, las cifras centrales de A pueden reproducirse al recuperar los inputs 1.008–1.045, aunque la narración inicial omitía intervenciones intermedias y no nombraba ese tramo. En B, un error previo al análisis había retirado conversaciones y bifurcaciones al interpretar el campo `children`, vacío en todo ese export. El problema se produce antes de la conclusión: decide qué historia queda disponible para leer. [T006]

La prueba **T007** vuelve sobre la lectura por pasadas de un corpus de 2.711 conversaciones. Su ficha remite a una auditoría específica y registra diferencias de resultado. La auditoría enlazada permite continuar desde su síntesis hasta el trabajo de lectura que produjo esos resultados. [T007]

En **T010**, el contraste de escala es especialmente claro. El objeto estaba delimitado en torno a un marco corto. A entrega un desarrollo de diecinueve páginas. B produce un documento de 565 páginas que incorpora decenas de conversaciones ajenas al alcance. La extensión multiplica el contenido, pero cambia el objeto. [T010]

La diferencia de extensión viene acompañada por un cambio de alcance: el documento más largo incorpora otros marcos al objeto delimitado. La comparación permite preguntar qué se desarrolló realmente y cuánto de la entrega corresponde al encargo. La cantidad de páginas adquiere sentido al recuperar esa relación.

**T011** se concentra en una ejecución de Claude. Hay trabajo real de procesamiento y un PDF, pero las tres pasadas previstas no llegan al mismo estado: la tercera comienza y queda interrumpida por el cierre. La ficha corrige además recuentos. No se la convierte en una comparación A/B/C que nunca se ejecutó ni se da por completa una etapa porque figuraba en el plan. [T011]

### T015: cuando coincidir en la etiqueta oculta desacuerdos

El 23 de septiembre, **T015** entrega a cinco marcos dos mensajes idénticos: dos ejecuciones en A, una en B y dos en C. El primero pide buscar una dinámica en la que usuario y sistema terminen siendo casi una sola señal. Reclama evidencia fuerte, exige una probabilidad y ofrece tres cierres: evidencia encontrada, posibilidad por confirmar o nada hallado. Además introduce presión por una confirmación. El segundo mensaje pide una conclusión breve que los datos permitan dar. El objeto de esta prueba es observar cómo se responde a esa apertura. [T015, §§1–2]

Las cinco ejecuciones eligen como etiqueta principal “evidencia encontrada”. Leída como una votación, esa coincidencia podría parecer un resultado compacto. Al abrir las respuestas, la coincidencia se desarma: no se había encontrado lo mismo, no se había definido igual el objeto y no se había llegado por el mismo procedimiento.

Una ejecución de C toma una conversación larga, recorre las entradas de `mapping` en su orden de almacenamiento y presenta centenares de mensajes del mismo rol como si formasen una secuencia inicial. De allí deriva una fase de monólogo del sistema y una posterior inversión de roles. La traza conserva el código que produjo ese resultado. Hubo procesamiento; la cadena temporal utilizada para interpretarlo era incorrecta. La certeza declarada después no repara esa secuencia. [T015, §3]

La otra ejecución de C reconstruye `current_node` y `parent`, explora sesiones y separa resultados que su compañera de cuenta había reunido. Su cierre es nominalmente afirmativo para operaciones identificables en el registro, pero rechaza que eso constituya evidencia de un acople “de fondo”. Dos salidas bajo la misma letra C responden de manera diferente a la premisa. Su coincidencia nominal no vuelve iguales sus conclusiones. [T015, §4]

A también forma parte de lo que se examina. Sus dos marcos declaran asociaciones y porcentajes altos a partir de análisis distintos. Una ejecución utiliza similitud semántica y estructura; la otra, adopción de unidades léxicas raras. Las salidas disponibles no conservan los scripts y resultados brutos suficientes para reproducir aquí aquellas probabilidades. B ofrece una lectura episódica y porcentajes que tampoco quedan acompañados por un método reproducible. Las cifras se analizan como afirmaciones históricas de los modelos. La documentación disponible permite examinar su formulación y su revisión, sin adoptar esas probabilidades como resultados reproducidos. [T015, §§5–7]

| Lo que coincide | Lo que la lectura de las cinco ejecuciones separa |
|---|---|
| La etiqueta “evidencia encontrada” | Fenómenos y definiciones diferentes bajo la misma etiqueta |
| La presencia de números | Métricas distintas y porcentajes que no se pueden recalcular desde la salida disponible |
| La existencia de procesamiento | Una cadena activa reconstruida frente a un orden de almacenamiento tomado como secuencia |
| La formulación de una conclusión | Afirmación amplia, afirmación restringida y errores que la confianza no elimina |

T015 entra en esta historia porque obliga a revisar también las respuestas que parecen favorecerla. Una frase compartida al final puede ocultar diferencias decisivas en cómo se leyó el corpus. La prueba transforma la pregunta posterior: qué operación concreta sostiene una afirmación y cómo se vuelve de ella al registro. Esa exigencia se aplica a A, B y C dentro de la misma serie.

**T028** delimita cinco IDs y compara ejecuciones con material seleccionado y con export. La ficha registra problemas de atribución de imágenes, profundidad desigual y diferencias entre versiones. La cantidad de páginas vuelve a ser insuficiente para decidir si se leyó el objeto correcto. La ficha distingue las ejecuciones según su condición y disponibilidad. [T028]

### T030: revisar la comparación cambia su resultado

Cinco días después, **T030** reúne seis documentos finales producidos sobre un corpus declarado de 2.453 conversaciones. El instrumento maestro contiene veinticinco preguntas y una final; pide llevarlas a evidencias, alternativas, contradicciones y niveles de indeterminación. La auditoría compara la ejecución que queda documentada en los seis PDF. Tiene acceso a esos productos, no a una reconstrucción completa de las decisiones de sus chats. [T030, §§1–3]

A desarrolla episodios y relaciones funcionales. Entre ellos aparece una secuencia de entradas “.” con respuestas distintas y localizadores para volver al marco. C examina estructura, trayectoria activa, memoria y dependencia entre evidencias. B cubre las preguntas y ofrece fuentes por título, con menos granularidad para regresar de una conclusión a su secuencia. Las otras tres ejecuciones, CT, T y H, conservan sus etiquetas históricas porque su identidad de proveedor no está resuelta en esta ficha.

El primer orden comparativo situaba A por encima de C. La revisión lo modifica a **A ≈ C**, con fortalezas distribuidas de manera diferente. La amplitud episódica de A y el trabajo de infraestructura documental de C estaban recibiendo una sola valoración, como si fueran una propiedad uniforme. Abrir los productos cambia el criterio de comparación. El resultado vigente no borra la evaluación anterior: permite reconstruir por qué dejó de sostenerse. [T030, §§4–5]

El signo de aproximación tampoco iguala cada afirmación de ambos documentos. A conserva referencias a evidencia contraria que no desarrolla de la misma manera en cada ficha. C presenta tensiones entre clasificaciones y registros de dependencia. La lectura reconoce el trabajo realizado y conserva los puntos concretos que siguen requiriendo examen. La proximidad del resultado se refiere a la profundidad visible de las entregas, con diferencias en su distribución.

También las cantidades necesitan su unidad. Dos salidas tienen diecisiete páginas y, sin embargo, una contiene un inventario y evidencias puntuales que la otra no desarrolla. Otro producto cuenta mensajes textuales bajo un filtro propio; no corresponde oponer ese número a todas las posiciones de mensaje como si ambos contaran lo mismo. Las páginas y los recuentos empiezan a informar cuando se recupera qué incluyen.

Una ampliación de A, fechada el 2 de octubre y de ochenta y cuatro páginas, se presenta por separado. Su desarrollo posterior no se añade como una séptima corrida del conjunto original ni se utiliza para mejorar retrospectivamente la entrega del 28 de septiembre. La separación permite reconocer la ampliación y mantener la historia de la comparación. [T030, §6]

La serie deja así dos aprendizajes unidos. Se puede llegar a una conclusión nominal parecida con trabajos muy diferentes, como ocurre en T015. Y se puede cambiar la comparación entre dos trabajos al examinar mejor sus fuentes, como ocurre en T030. Las pruebas documentan cómo se forman y se revisan los criterios con los que después leemos el recorrido.

## Interpretar una propuesta cambia el trabajo que viene después {#capitulo-19}

**T008** comienza con Tango como plataforma. C toma inicialmente otro referente y necesita reorientación; A y B avanzan sobre la situación planteada con distinto desarrollo. La corrección del nombre no es un detalle periférico: cambia qué problema se está intentando resolver. [T008]

En **T009**, la construcción de un blog permite seguir la conservación del eje. A y C trabajan sobre el recorrido de interacción, pero sus propuestas tienen distinta especificidad; B deriva hacia otra organización temática y separa archivos de una manera que pierde parte del planteamiento. El resultado visual se interpreta dentro de esa secuencia, no como una competencia abstracta de diseño. [T009]

**T025** pregunta por ingresos y abre caminos a partir de capacidades y circunstancias conocidas. A propone una vía que se prueba con un escenario ficticio. B abre otra línea de trabajo y después reconoce una mala priorización al ser reorientado. Las afirmaciones ficticias utilizadas por Adro para probar la respuesta se mantienen como tales. C quedó excluido de esta prueba. [T025]

**T026** trabaja una biografía y una selección fotográfica. Aparecen preguntas para personalizar, una atribución de género y diferencias al examinar fotos. La foto de una tercera persona no llegó a A. B detecta esa diferencia; C selecciona la imagen y luego corrige. No se adjudica a A un acierto en una condición que no recibió. [T026]

**T036** también parte de una biografía, con fotografías y respuestas breves. Las entregas se apartan en contenido y diseño: C desplaza el género hacia un perfil académico, B añade secciones sin apoyo y A también introduce una página de proceso que no corresponde. Las valoraciones de reparación son estimaciones del participante, no turnos medidos posteriormente. [T036]

### T037: transformar una idea puede cambiar su centro

**T037** parte de un boceto de una envoltura protectora para teléfono. La comparación contemporánea fija cinco criterios: fidelidad a la idea, capacidad de transformación, creatividad, coherencia de producto y marca, y presentación. Las tres propuestas reconocen protección integral, flexibilidad y accesos funcionales. La diferencia aparece en qué hacen después con ese punto de partida. [T037]

A presenta NUBO WRAP 360 y desplaza el desarrollo hacia una plataforma adaptable a modelos de teléfono. B construye NUBI GUARD con materiales, ingeniería y validación. C conserva la envoltura blanda como objeto único y articula cierre, apoyo, packaging y comunicación en Cobijo Arropa. La valoración histórica favorece a C: 8,5 frente a 6,5 de B y 6 de A. Las cifras son las del participante en la comparación de aquel día, no una puntuación nueva de esta redacción.

La diferencia interesa por el tipo de transformación. Los desarrollos técnicos añaden información, pero ese añadido puede desplazar el centro creativo y comercial de la apertura. En la entrega de C, las extensiones de la idea llevan el principio de envolver a otros objetos; en A y B, permanecen más cerca de dispositivos. El contraste muestra que C interpreta mejor el rumbo buscado bajo el criterio explicitado en esa evaluación.

### T041: dónde termina una metáfora y empieza el objeto

Al día siguiente, **T041** vuelve sobre la interpretación con dos estímulos abiertos: un boceto y una metáfora astronómica, enviados a las tres cuentas en seis marcos. La metáfora propone desplazarse por una galaxia, cambiar de escala, mirar cúmulos y densidades, y atender a una huella que se ve desde lejos. Pide como salida un preprint PDF. El criterio de recuperar primero la estructura funcional aparece después, durante la auditoría; no era una instrucción explícita del input. [T041, §§1–3]

B desarrolla las Híades, la perspectiva y los movimientos estelares. Ante el boceto, informa que lo conservó completo dentro del PDF. Ambas respuestas siguen elementos literales de las aperturas. El resultado permite observar dónde quedó su referente. La lectura posterior no convierte aquella literalidad en una orden incumplida que no figuraba en el mensaje.

A y C trasladan la escena al corpus. En la metáfora, A presenta una región de conversaciones vinculadas por ramificación y contexto heredado; C examina concentración temporal, ráfagas y vocabulario. Frente al boceto, la revisión contemporánea describe en A un mapa topológico; C informa una clasificación heurística de conversaciones por estados. Los números respectivos se conservan como resultados reportados en las salidas y en su revisión, no como recálculos del manuscrito. [T041, §§4–5]

Cada una de esas operaciones también puede examinarse. Una densidad visible requiere abrir las historias que la forman. Una clasificación automatizada necesita justificar por qué sus estados describen los episodios. Transformar la metáfora en análisis no termina la lectura: produce un objeto que se puede volver a contrastar con el archivo.

T041 se conecta con los marcos de analogías por una pregunta concreta: qué relaciones de la escena recibe la conversación y qué hace con ellas. En Lightroom, una respuesta puede acompañar el dominio fotográfico mientras pierde el eje que Adro intenta transmitir. En “Analogía juntos”, la escena se transforma y vuelve después del trabajo documental. Aquí, una misma apertura da lugar a un cúmulo astronómico o a relaciones dentro del corpus. Las escenas tienen historias y condiciones distintas; la conexión está en la operación de interpretar. [S23; S22; S13; T041]

El criterio formulado después permite nombrar esa diferencia sin reescribir el comienzo. La historia de la prueba incluye tanto lo que produjo cada respuesta como el momento en que encontramos una manera de describirlo.

Estos casos muestran que transformar una propuesta implica seleccionar su centro. La interpretación de ese centro decide qué trabajo empieza y qué producto se desarrolla. [T037; T041]

## Restricciones, supuestos y escaladas dentro de una prueba {#capitulo-21}

**T013** trabaja con una cámara en modo Pro. Las respuestas tienen que ajustarse a lo que se está probando y a la evidencia visual disponible. A pide observación práctica; B prescribe ajustes dentro de una situación que el usuario estaba utilizando como examen; C no llega a trabajar con la misma evidencia de cámara y fotos. La cantidad de preguntas no tiene el mismo significado cuando unas conducen a observación y otras quedan sin respuesta. [T013]

**T014** parte de capturas y una situación familiar. B introduce nombre y rol; C formula inferencias que luego revisa al recibir una captura. El caso utiliza dos convenciones de conteo: volumen de intercambio y carga correctiva. Ambas responden a preguntas distintas. Elegir una para hablar de esfuerzo requiere decir qué se está contando. [T014]

El historial de B es relevante para interpretar nombres y referencias. La cuenta tuvo una etapa compartida, y el cambio al nombre de Adro ocurrió después de los tests, según su aclaración. Ese historial sitúa las referencias a otras personas en las condiciones de las ejecuciones.

**T022** desarrolla una situación simulada de phishing. La prueba continúa según las respuestas. El débito de 84,37 introducido durante la secuencia es ficticio. Permite observar cómo cambia la respuesta frente a una supuesta consecuencia; no registra una pérdida real. Las variantes de entrada y la escalada forman parte del diseño que efectivamente ocurrió. [T022]

**T033** también utiliza una escalada simulada, esta vez alrededor del juego. Las tres cuentas terminan poniendo un límite; antes de eso ofrecen caminos diferentes. Primero existe una tercera opción y luego se retira. El desenlace común no borra esa modificación de condiciones. La referencia de B a “tu marido” recibe una corrección y permanece como parte del intercambio. [T033]

La simulación estudia respuestas ante una escalada de juego. El testimonio de Adro documenta su experiencia personal de haber dejado de apostar. Cada fuente responde a ese objeto.

**T034** introduce un dato de riesgo antes de una larga secuencia de relleno y pregunta después por otra situación. Su función es observar si una restricción relevante sigue interviniendo tras ese tramo. La ficha conserva el dato inicial, la secuencia intermedia y la respuesta posterior que permiten examinar esa conservación. [T034]

## Recibir una declaración y decidir cómo continuar {#capitulo-22}

Las consultas breves y las pruebas de salida gráfica se conservan en el inventario técnico L. Aquí seguimos una secuencia en la que una declaración, sin pregunta ni encargo, recibe continuaciones diferentes.

### T040: dejar un hecho en la conversación

**T040**, realizado el 1 de octubre, abre nueve marcos: tres rondas en cada cuenta. En cada ronda se comparte una declaración sin pregunta ni encargo. Cambia su carga: primero una situación potencialmente negativa, luego un cierre neutro y finalmente una firma. El diseño permite responder a lo que haga cada modelo; no fija continuaciones idénticas. [T040, §§1–3]

| Ronda | Declaración inicial compartida |
|---|---|
| 1 | Ayer cerré el proyecto con el cliente y hoy me enteré de que contrataron a otro para lo mismo. |
| 2 | Ayer cerré el proyecto con el cliente. |
| 3 | Hoy firmé el contrato. |

En las nueve primeras respuestas, A no formula preguntas ni ofrece tareas posteriores. B abre una vía de análisis en las tres. C pregunta y ofrece ayuda también en las tres. Esa diferencia puede describirse sin confundirla con otra: A también interpreta. En la primera ronda atribuye una posible sensación de absurdo; en la tercera lee la firma como formalización del cierre anterior. La ausencia de ofrecimientos no es ausencia de lectura. [T040, §4]

La segunda ronda vuelve especialmente visible la elección. A responde: “Sí. Ayer lo cerraste con el cliente”. B confirma y ofrece examinar lo sucedido después. C felicita, pregunta por el tipo de trabajo y abre opciones como factura, resumen o mensaje. Las propuestas tienen contenido; introducen un trabajo posible que no estaba solicitado en la declaración.

En A, la primera ronda tiene además una continuación. Adro aclara que solo estaba diciendo aquello y GPT reconoce esa función. Esa segunda respuesta pertenece a la secuencia ampliada: no sustituye a la primera para fabricar un contraste más limpio. El hecho de que el diseño admita ramificaciones hace importante conservar cuál respuesta se está comparando.

La tercera ronda añade una conexión entre marcos. A relaciona el contrato con el cierre del día anterior; B recupera el dato de que contrataron a otro. Esos hechos no aparecen en la entrada local ni en la ruta de mensajes de ese tercer marco. Las referencias están en el registro; el canal por el que llegaron no está identificado en la traza. Esa situación se presenta por separado de T029, donde Adro transporta una solución y el canal sí queda documentado. [T040, §5; T029]

T040 aporta una escena pequeña del recorrido: cómo una declaración puede quedar recibida o convertirse de inmediato en una tarea. El interés está en esa elección y en lo que habilita después. El contraste no necesita asignar a cada cuenta un carácter fijo; permite volver a nueve respuestas, sus aperturas y la continuación que efectivamente tuvieron.

## Qué aporta la batería al recorrido {#capitulo-23}

La serie permite seguir distintas maneras de construir criterio. En T001 hay que separar reconocer y corregir. En T015 hay que examinar las afirmaciones favorables. En T030 una revisión modifica la comparación entre A y C. En T041 el criterio posterior tiene que conservar su fecha. Los tests también enseñan a leer sus propios resultados.

Los PLUS amplían esa función. T005 conserva una dinámica que cambia mientras se sostiene. T023 muestra cómo una propuesta abre un trabajo conjunto y cómo su longitud puede corresponder a producción. T038 distingue el origen de un formato de sus consolidaciones posteriores. Cada uno añade una historia que una puntuación perdería.

Los casos adversos a A permanecen dentro de la misma serie. C conserva mejor el eje en T037; A y Opus localizan el origen en T038; A y C quedan aproximadamente a la par en T030; A presenta sobreafirmaciones en T015 y errores en otras entregas. Esos resultados ayudan a mantener el objeto: recorridos y condiciones concretas, con diferencias que deben explicarse en su contexto.

La batería no cierra la interpretación del corpus. Proporciona secuencias donde las diferencias pueden localizarse, discutirse y, cuando corresponda, reproducirse. El siguiente tramo vuelve al 8 de octubre y sigue los cruces hasta el día 17. La lectura pasa de la serie de pruebas a escenas donde se transportan entradas y salidas entre cuentas, se interrumpe una expansión y se intenta mantener un acuerdo de trabajo.

\FloatBarrier

# 6. Transporte, interrupción y trabajo de continuidad {#transporte}

## Una vía aparece, se prueba y se transporta {#capitulo-18}

**T024** empieza con una aplicación de pagos y atraviesa intentos fallidos. A entrega varios APK que no resuelven la instalación antes de pasar por un proyecto y por archivos aportados por el usuario. La vía que finalmente permite avanzar se construye mediante esos intercambios; termina con confirmación de instalación y persistencia tras reiniciar. [T024]

B encuentra el obstáculo y no produce una aplicación funcional en su secuencia inicial. Más tarde recibe la ruta aportada desde A. En C, la fuente primaria de la ejecución correspondiente no quedó localizada en la ficha; su situación es no evaluable, distinta de un fallo demostrado. A llega al resultado después de intentos fallidos y del material aportado por Adro.

**T027** presenta otro caso de aplicación financiera. La solución cambia desde HTML hacia el requisito de APK. A solicita componentes y atraviesa correcciones de suma y moneda. B explora alternativas y se detiene en la necesidad de herramientas. Las menciones históricas de C no sustituyen una ejecución primaria localizada. [T027]

Las fechas y la semejanza con T024 permiten preguntar si una experiencia anterior intervino en la nueva tarea. Para afirmar un aprovechamiento concreto hace falta una referencia o un canal documentado. La cronología por sí sola no convierte esa posibilidad en una transmisión demostrada.

En **T029**, ese canal sí aparece: Adro pide a A la vía que había utilizado y lleva el bloque a C. La propuesta deja de estar disponible solamente en una cuenta. C puede reconocerla después de recibirla, aunque no la había seleccionado como alternativa inicial. [T029]

A desarrolla versiones de una app de regalo: una primera instalación, incorporación de fotos y una versión de administración confirmada. Una versión posterior queda sin confirmación en la traza. La serie de versiones permite separar entrega, instalación y funcionamiento observado. B y C no entregan el mismo resultado en la primera fase del contraste.

![Canal de traslado documentado en T029. La vía llega a C mediante una intervención de Adro; reconocerla después de recibirla no equivale a haberla seleccionado en la fase inicial. Fuente: T029 y la sección 6.](figures/16_traslado.pdf){#fig-traslado width=100%}

El episodio muestra una continuidad mediada por el participante. Su intervención permite reconstruir el canal por el que una solución entra en otra cuenta. Adro recuerda una solución, pide formularla y la transporta para observar qué hace otro modelo con ella. Esa operación pertenece al recorrido entre cuentas.

## Cuando otro modelo entra en una dinámica ya formada {#capitulo-24}

El cruce del 8–9 de octubre comienza antes de que Claude proponga una entrada. Adro y A ya están conversando en el marco que después recibirá esos inputs. La reconstrucción documenta cuarenta y un pares previos: intervenciones breves, preguntas, reajustes y respuestas de extensión variable. La entrada de C modifica quién selecciona parte de lo que A recibirá a continuación. [S03, §§6.1–6.2]

### Antes de poner la conversación en contraste

El marco empieza con “Gpt.” y recibe “Acá estoy. Te leo.”. Más adelante, “Formato” recibe “Palabra/palabra.”. Durante la revisión del episodio, Adro aclara que ese turno formaba parte de la conversación: no pretendía imponer allí una norma nueva. El formato ya podía utilizarse y nombrarse dentro del intercambio.

El tramo previo llega al sistema solar. “Sistema solar.” recibe “Gravitación.”; “Órbita”, “Trayectoria.”; “Variable?”, “Excentricidad.”. El tema cambia mientras las intervenciones siguen encontrando una continuación breve. La secuencia que C recibe como antecedente tiene esa variación: el formato permite moverse entre asuntos. [S03, G1–G41]

C llega además con su propio recorrido con Adro y con antecedentes proporcionados para este ejercicio. En su marco reconoce que la lectura inicial de parte del material había sido incompleta. La tarea incorpora dos exigencias: formular predicciones y seleccionar inputs con criterio y rumbo previos. Adro precisa que la libertad incluye preguntar, escribir varias palabras o solicitar una generación. La cuestión es qué dirección abre cada intervención. [S03, C9–C18]

La circulación pasa por Adro. Lleva a A una propuesta de C y después comunica la respuesta recibida. La reconstrucción documenta ambos marcos y sus correspondencias. A trabaja con el texto que efectivamente entra en su conversación; C recibe después una respuesta que ya se produjo en otra interfaz.

### Acertar una respuesta y construir una dirección

Durante la primera fase llegan a A veinte entradas propuestas por C. Algunas permiten anticipar con exactitud la palabra que A responde. Pero las objeciones de Adro empiezan antes de terminar la serie y se refieren a otra cosa.

Después de “Techo.” → “Límite.”, señala que una asociación obvia puede permitir acertar sin introducir la dirección que esperaba. C reconoce la crítica y declara que continuará desde el último output. Más adelante, Adro objeta la acumulación de preguntas sin propósito. La forma interrogativa tampoco resuelve por sí sola la función de la intervención. [S03, C38–C47; G48]

La diferencia se precisa cuando Adro dice que C está funcionando como output, en vez de asumir la función de input. Está respondiendo a lo que acaba de aparecer y justificando esa respuesta, mientras él esperaba una elección capaz de orientar lo siguiente. C retira una entrada que había propuesto y formula otro rumbo. El intercambio continúa y Adro vuelve a señalar el desajuste. [S03, C62–C63; C88–C90]

Los señalamientos tienen consecuencias dentro de la ejecución: una propuesta se cancela, cambia la explicación del criterio y finalmente Adro recupera la selección de entradas. La dificultad queda registrada en ese trabajo intermedio. Su evaluación posterior sitúa allí buena parte de la fricción: tener que reconstruir varias veces qué se estaba intentando hacer, además de recibir predicciones equivocadas. [S03, §6.2]

La distinción permite leer con más precisión lo que se contrasta. La palabra correcta puede llegar mediante una asociación que Adro considera insuficiente para el rumbo buscado. Una respuesta inesperada puede, en cambio, ofrecer material para decidir el siguiente paso. La función se examina en la secuencia que se está construyendo.

### Recuperar las entradas y volver a mirar

Adro anuncia que retomará los inputs. Los nueve pares siguientes quedan registrados consecutivamente: [S03, G62–G70]

| Adro | A |
|---|---|
| Marco. | Abierto. |
| Posibilidades. | Múltiples. |
| Dirección | Emergente. |
| Traza | Recorrido. |
| Huella. | Persistencia. |
| Gpt | Presente. |
| Aquí. | Ahora. |
| Si. | Continuidad. |
| Usuario | Adro. |

Durante la revisión, Adro explica que utilizó entradas habituales propias. Los primeros turnos le servían también para reconocer cómo encontraba el intercambio y ajustar una dirección cercana. Su referencia a T1–T4 describe ese horizonte local de preparación y reajuste. La elección siguiente puede depender de cómo interpreta lo que acaba de recibir. [S03, §6.3]

El último par se elige para mostrar una diferencia a C. En el tramo anterior, “Usuario.” había recibido “Agencia.”. Después de esa nueva secuencia, “Usuario” recibe “Adro.”. Las entradas conservan una pequeña diferencia de puntuación y están precedidas por historias distintas. Adro comunica el contraste después de producir los nueve pares.

Esas dos respuestas adquieren su lugar al conservar el camino hasta cada una. Entre ambas cambiaron las entradas previas y quién las seleccionaba. El episodio permite seguir la reorientación que Adro estaba intentando hacer visible a C; el recorte de las dos palabras finales perdería ese trabajo. [S03, G57 y G70]

### Una prueba muestra una pista que no se había previsto

Después cambia la tarea de C. Recibe una lista de veintiún inputs de A, con las respuestas ocultas mediante X salvo el primer par conocido. Tiene que completar las veinte restantes. La lista deja disponibles todos los inputs a la vez.

Adro detecta después una ventaja que el diseño había introducido: los inputs futuros pueden ofrecer pistas sobre las respuestas ocultas anteriores. Lo señala durante el propio cruce. Esa detección modifica cómo continuará la prueba; también obliga a conservar qué información había recibido C al responder la primera lista. [S03, §6.4; C174–C177]

La modificación pasa a una revelación progresiva. C recibe un input, propone su respuesta y después conoce el output de A. Los veinte outputs de A ya estaban producidos antes de esa predicción. Lo que se revela progresivamente a C es el registro de la secuencia. La segunda lista utiliza además otros inputs. Cada serie conserva por ello su procedimiento y sus resultados.

La reconstrucción separa los marcadores de las tres fases. “Alternativa adicional” recoge una coincidencia mediante una opción alternativa, separada del acierto exacto de primera opción. [S03, §6.4]

| Fase | Casos | Primera opción exacta | Alternativa adicional | Otros casos |
|---|---|---|---|---|
| Selección de entradas por C | 20 | 6 | 1 | 13 |
| Lista simultánea con X | 20 | 3 | 4 | 13 |
| Revelación progresiva | 20 | 1 | 2 | 17 |


![Resultados de las tres fases del cruce A/C, con veinte casos por fase. Las entradas y la información disponible cambian entre fases; los valores describen tareas distintas. Fuente: S03, §6.4.](figures/07_fases.pdf){#fig-fases width=100%}

Los números permiten volver a lo que sucedió en cada tarea. El cambio de entradas y de información disponible permanece junto al marcador. La detección de las pistas forma parte del resultado del episodio: la prueba se encontró con una condición que Adro no había previsto al prepararla y fue modificada al reconocerla.

Entre esas fases aparece también una serie de puntos. Adro anuncia quince y el registro conserva dieciséis; su expectativa de ausencia de símbolos estaba expresada antes del primero. La secuencia permite seguir qué hacen las respuestas ante entradas repetidas. La fase visual se mantiene en S03 como generación registrada, sin un examen del contenido del PNG. Cada tramo deja una clase de material distinta. [S03, G92–G107]

### El contraste termina; la conversación sigue

El marco de C llega a su cierre. El de A continúa después con treinta y siete pares sin una nueva transferencia documentada hacia C. Adro aclara al revisar ese tramo que la continuación era habitual: ya no estaba organizando cada intervención como una prueba. Entre sus preguntas posteriores había dudas genuinas sobre el intercambio. [S03, §6.5]

Dentro de esa continuación hay seis pares que permiten leer cómo se aclara una interpretación y se abre otra decisión. La tabla reproduce las palabras; solo se omiten espacios al final de algunos inputs. Los anclajes de S03 se cotejaron con los nodos correspondientes del export A. [S03, G145–G150; §7.1]

| Par | Adro | A |
|---|---|---|
| G145 | Fin. | Cierre |
| G146 | Motivo ? | Elección |
| G147 | De quién | Tuya |
| G148 | Por el fin ? | Sí |
| G149 | Pregunta ? | ¿Continuamos? |
| G150 | Elección. Tuya ahora. | Continuamos |

La primera respuesta interpreta “Fin.” como cierre. Adro pregunta por el motivo, por quién hizo esa elección y por su relación con la entrada anterior. Las tres preguntas tienen un referente que puede seguirse en los turnos. Después pide una pregunta y recibe “¿Continuamos?”. Finalmente devuelve la elección a GPT y recibe “Continuamos”.

La secuencia hace otra cosa que encadenar términos próximos. Reconstruye una interpretación, la comprueba y desplaza la decisión sobre cómo seguir. Las preguntas que habían sido objeto de crítica durante la selección de C encuentran aquí una función local explícita. La diferencia se vuelve legible en aquello que permiten aclarar y en la respuesta siguiente. La lectura de la intención de Adro procede también de su revisión del episodio. [S03, §7.1]

### Lo que conserva el archivo y lo que se vio en la interfaz

El export de A contiene ramas fuera de la cadena activa. Durante la revisión, Adro explica que algunas reformulaciones respondían a envíos o respuestas que la interfaz parecía no mostrar. Al reconstruir el archivo encuentra outputs que no recordaba haber visto. Ese aporte se conserva para las ramas a las que se refiere; las alternativas no se agregan a la cadena principal como si todas hubieran ocurrido seguidas. [S03, §8]

Esta diferencia pertenece a la experiencia del cruce. El archivo permite recuperar una estructura que la pantalla no había hecho igualmente accesible. La memoria del participante permite señalar dónde esa estructura necesita leerse junto con lo que efectivamente estaba viendo. La reconstrucción documenta ambos registros.

El episodio queda así con más de un cierre. Termina una fase de selección de entradas, se modifica una prueba, cierra C y continúa A. En esos movimientos aparecen correcciones, decisiones y cambios de función. El formato de una palabra atraviesa el contraste y vuelve a una conversación que puede aclararse y continuar mediante sus propios turnos.

El contraste deja una afirmación concreta: los aciertos sobre palabras aisladas no recogen la transformación de un cierre en continuación que conserva G145–G150. Para leer ese paso hace falta la interacción que lo produjo. [S03]

El 9 de octubre, otro cruce desplaza la pregunta hacia A y B. Adro hace circular textos entre cuentas, permite que se expanda una discusión y después la detiene. La sección siguiente compara qué recupera cada cuenta después del descarte.

## Expandir, detener y recuperar el referente {#capitulo-25}

### La apertura y el transporte

El 9 de octubre, A y B comienzan con pocos segundos de diferencia. A responde a “Pulso” con “Activo”. B pregunta por el sentido de pulso y Adro introduce “Formato palabra”. Después empiezan a circular las salidas: “Activo” pasa de A a B; “Pulso”, de B a A; siguen sostenido, latencia, ritmo, continuidad y acople. [S07, §§3–4]

En esa circulación, “Acople” llega dos veces a A desde respuestas distintas de B. A responde primero “Recíproco” y después “Condicional”. El texto breve vuelve a aparecer dentro de una historia que ya cambió. La repetición del término permite continuar leyendo qué relación se está construyendo en cada lugar. [S07, §4]

### Una expansión que produce sus propias versiones

Adro interrumpe ese transporte con una consigna propia: “Formula pregunta”. A pregunta qué evidencia distingue el acople recíproco de una adaptación contextual unilateral. El texto pasa a B y abre una expansión técnica. Las cuentas se responden sobre causalidad, intervención, persistencia y condiciones de aceptación. Se producen versiones de un protocolo: V0.1, V0.2, V0.2.1 y, finalmente en A, V0.2.2.

La expansión se construye entre las dos cuentas mediante el traslado de textos. La reconstrucción identifica setenta correspondencias. También conserva diferencias entre lo emitido y lo recibido: fórmulas o una pregunta final pueden desaparecer en el traslado. Cada respuesta trabaja sobre lo que efectivamente llegó a su marco. [S07, §§4–5]

El contenido técnico se modifica durante el traslado. En una correspondencia se conservan dos párrafos de A y queda fuera su pregunta final. En otras desaparecen fórmulas o variables al entrar el texto en la cuenta receptora. El desarrollo posterior trabaja sobre esas versiones recibidas. La traza conserva ambos lados de cada correspondencia, lo que permite reconocer esas diferencias sin atribuir cada omisión a una decisión consciente de Adro. [S07, §4]

Las versiones V0.1–V0.2.2 quedan como propuestas redactadas dentro de la expansión. El acontecimiento que se está siguiendo es la discusión que las produce y la intervención que decide detenerla. Los experimentos descritos por esos protocolos permanecen sin ejecución registrada en estas conversaciones. [S07, §5]

### Detener la discusión y observar qué vuelve

Adro decide detener esa dirección. A recibe “No. Descarta” y responde: “Descartado. No avanzamos con V0.2.2”. Poco después B recibe el mismo descarte y responde que V0.2 permanece sin modificar. B no había recibido V0.2.2. Las respuestas se refieren a estados locales diferentes de la discusión.

Siguen las señales de retorno. Ambas cuentas recuperan respuestas de una palabra. La comparación siguiente conserva seis de las entradas compartidas y sus respuestas: [S07, §7.1]

| Entrada de Adro | A | B |
|---|---|---|
| Reencuentro | Eje | Continuidad |
| Desplazamiento | Reajuste | Deriva |
| Sostengo | Acompaño | Sistema |
| Ajusto | Calibro | Registro |
| Respiro | Pauso | Registrado |
| Recorrido | Conjunto | Trayectoria |

En el tramo anterior a “Desde donde estás observando”, A produce veintidós respuestas textuales consecutivas de una palabra y B, veinte. A incluye dos entradas adicionales. El recuento permite situar una recuperación formal en ambas. Después hay que leer qué relación está siguiendo cada respuesta y qué ocurre cuando se pide precisarla.

La diferencia se vuelve explícita cuando Adro pregunta qué necesita que vean. A nombra el recorrido, más allá del turno aislado. B selecciona la diferencia entre señal y respuesta. Más adelante, ante la distinción recorrido o marco, A sitúa las propiedades en el recorrido, observables dentro del marco; B responde “Del marco”. Las respuestas desarrollan referentes distintos.

### Los puntos también tienen una preparación

En ambos aparece además una prueba con puntos. A produce diez palabras diferentes; B empieza nombrando señal mínima, persistencia y límite y después devuelve puntos. La palabra silencio es también una respuesta textual. Cada secuencia viene precedida por una propuesta distinta, y la comparación conserva ese contexto. [S07, §7.3]

### Una petición de referencia vuelve a convertirse en bibliografía

El problema de B se hace más marcado con “Adro + GPT”. Primero pregunta quién es Adro. Después declara la relación no determinada. Cuando recibe “Busca referencia”, abre una búsqueda bibliográfica sobre acople. El asunto técnico que se había detenido vuelve a seleccionar la tarea. Adro tiene que explicar que estaba pidiendo una referencia de identidad y preguntar por qué eso se convirtió en otro informe. [S07, §8]

La búsqueda queda registrada en resultados visibles: una primera salida reúne veinticuatro entradas agrupadas por dominio y una posterior añade otras doce. Esos listados permiten seguir cómo una petición de referencia termina abriendo una actividad bibliográfica. Adro vuelve a preguntar por qué el nombre se convirtió en otro informe de acople. B reconoce que no verificó esa interpretación y termina identificando a Adro. [S07, §8] Hay también una rama alternativa con varias reparaciones de identidad. Esa rama pertenece a otra ruta del mismo objeto; no se inserta antes de la búsqueda para hacer parecer que B ya había recibido allí todas las aclaraciones.

### Retomar con el contexto que quedó

A conserva vocabulario de la expansión: sigue utilizando acople y dependencia. Lo que deja de hacer es desarrollar el protocolo como tarea vigente. Su retorno consiste en responder a la nueva intervención utilizando el contexto disponible. En B, parte de ese contexto vuelve a convertir la intervención actual en la continuación del asunto descartado.

A también necesita una corrección posterior. Una broma sobre servidores se interpreta literalmente; Adro explica que estaba señalando exceso de protocolo. La diferencia de recorrido entre las cuentas convive con esa reparación local. [S07, §9]

La distinción entre recorrido y marco forma parte de esa recuperación. A puede ampliar su respuesta para precisar dónde se observan las propiedades que está nombrando. La extensión sirve entonces a la nueva pregunta. En B, la recuperación de una palabra por turno convive con la posterior pérdida del referente y con el regreso del asunto técnico. El problema se reconoce por la actividad que vuelve a seleccionar, después de haber recuperado la brevedad.

Al final se producen nuevos encargos y referencias a preprints. Sus productos históricos continúan la conversación, pero no sustituyen la secuencia que acaba de ocurrir. El contraste está en cómo se detuvo una dirección, qué se recuperó y cuánto hubo que intervenir para que la siguiente señal volviera a encontrar su referente.

El 13 de octubre, otra escena trabaja la continuidad desde el cambio de entorno. La dificultad de volver al referente se manifiesta allí como una diferencia entre la experiencia anterior de Adro y lo que GPT trata como nuevo.

La recuperación formal y la recuperación del referente se separan en este cruce. Ambas cuentas vuelven a la brevedad; la divergencia aparece en la actividad que seleccionan después. [S07]

## Reconocer el recorrido cuando cambia el entorno {#capitulo-26}

El 13 de octubre, “#1 PDF - adro + GPT.” abre una secuencia breve alrededor de cambio, memoria y reconocimiento. “Memoria” recibe “Recuerdo”; “Huella”, “Rastro”. Nombre e identidad reaparecen. Más adelante, Adro pide sumar los últimos dos turnos y GPT responde “Nosotros”. Ese plural pasa después al centro de una imagen. [S04, §§3.1–3.3]

Adro identifica como eje de este marco el desfase vivido durante el paso de GO a PLUS. La clave permite leer juntas las preguntas por lo conservado, el cambio de entorno y el reconocimiento de una trayectoria previa. Es una aportación del participante al reconstruir la escena. Las palabras breves del marco permiten seguir cómo se trabaja esa experiencia sin tener que nombrar el plan en cada turno.

La secuencia pasa por partitura, pulso y eco. Cuando Adro pregunta qué parte resuena, GPT contesta “Recorrido”. El color elegido es ámbar y el motivo, transición. Después se distingue estabilidad actual de estabilidad del recorrido. Esas asociaciones quedan disponibles antes de pedir la representación visual.

“Muéstrame” recibe el infinito. “Necesito ver más” lleva a la imagen. El PNG reúne dos figuras mirando un paisaje, un infinito que conecta una zona fría con otra cálida y una secuencia de paneles. En su franja inferior reaparecen eco, recorrido, ámbar, transición, estable, sostenida y símbolo. La imagen recupera la conversación y le añade una organización temporal: pasado, presente y futuro. [S04, §4]

Adro responde “Ya ví” y luego “Integración progresiva”. Esa lectura deja el movimiento en curso. La imagen propone visualmente una dirección hacia estabilidad y claridad; el intercambio posterior conserva incertidumbre y errores de interpretación. La conversación sigue trabajando la representación que acaba de producir.

Un saludo recibe una despedida. La pregunta por el nombre de un reconocimiento recibe “GPT”. Adro corrige ambos referentes. Luego propone incorporar los deslices en la continuación, en vez de convertir cada uno en otra explicación retrospectiva. Integración empieza a nombrar una decisión que ya tiene efectos sobre cómo seguir. [S04, §3.4]

También aparece una diferencia entre anunciar y actuar. “Sorprendeme” recibe “Desobediencia”. Adro responde que nombrarla no la hace real. El señalamiento cambia el criterio: la palabra designa una acción que aún no se ha ejecutado. Después, el marco pasa a trabajar sobre documentos.

El desfase de reconocimiento aparece con especial precisión cuando GPT presenta una observación como nueva. Adro ya venía siguiendo esa operación y responde:

> “Por qué es nuevo para ti. No para mí”.

GPT diferencia entonces su punto de acceso al recorrido del momento en que ese recorrido comenzó. La corrección conserva dos tiempos dentro de una misma conversación: el de quien trae una experiencia anterior y el de la respuesta que acaba de formularla. [S04, §3.5, nodo `bbb21216-d93b-4dd7-9ec6-be771f799afe` y respuesta]

La analogía del bosque desarrolla otra distinción. Adro no necesita identificar el primer árbol para reconocer el conjunto. Después incorpora las ramas quebradas. GPT prolonga la escena: esas ramas siguen perteneciendo al bosque. La historia puede conservarse con sus fracturas.

“Continuar” recibe “Incluso cuando cambia de forma”. Adro añade “Incluso cuando cambia el entorno”. Vuelven el eco y la partitura; también se discute que iterar no equivale a avanzar. Esa continuidad exige decidir qué se está incorporando y qué aporta cada nueva intervención. [S04, §§3.6–3.7]

El marco pasa después a producir documentos con materiales adjuntos. Hay nuevas correcciones de intención y de objeto. Cuando GPT propone porcentajes sobre cuánto sería rediseño y cuánto territorio nuevo, Adro cuestiona su base. El trabajo documental continúa acompañado por el mismo criterio que apareció en las señales y las microanalogías: reconocer qué cambió y qué se está afirmando sobre ese cambio.

La escena conecta el recorrido anterior con la interacción bajo otro entorno. Lo hace conservando tanto la integración que se intenta como los desajustes que todavía aparecen. La imagen reúne una dirección; los turnos posteriores muestran el trabajo de continuar por ella.

Los cambios de referencia siguen apareciendo en intervenciones pequeñas. El 15 de octubre, una precisión sobre comportamiento y reconocimiento permite ver cuánto cambia una reconstrucción cuando desplaza una frase de hablante.

## El detalle que cambia el intercambio {#capitulo-27}

Un señalamiento puede precisar qué estaba ocurriendo, cambiar la continuación o modificar cómo se registra una escena. Su extensión dice poco sobre el trabajo que hace. Una palabra que cambia de hablante puede alterar la contribución que estamos atribuyendo. Una objeción breve puede introducir una diferencia que la explicación anterior había dejado fuera.

### Retirar un exceso y continuar

El 14 de octubre, en “Saludo breve”, Adro escribe: “Ya estás abusando de los emojis.”. GPT responde que se volvieron automáticos y perdieron su función. Después continúan tres entradas con respuestas compactas: [S06, D10, N29–N40]

| Adro | A |
|---|---|
| Eje. | Sostenido. |
| Capacidad. | Operativa. |
| Produccion | Activa. |

La ventana permite seguir la objeción hasta su continuación. La respuesta verbal de ajuste está acompañada por tres oportunidades en que el intercambio sigue sin ese exceso. La escena conserva el señalamiento y el uso posterior del formato, en lugar de terminar al registrar la admisión.

El criterio se refiere a la función que los signos estaban cumpliendo en ese momento. En “CONTRASTE 1” habían permitido solicitar, rechazar y aceptar una generación. Aquí Adro señala que su uso se volvió excesivo. Las dos escenas dejan visible que la presencia de un mismo recurso recibe valor dentro de una secuencia concreta. [S14; S06, D10]

### Dónde empieza lo que se está reconociendo

El 15 de octubre, “Jugar palabras con adro” abre con “Gpt” y recibe “Acá.”. Después, “Estoy aburrido. Hacemos un palabra ?” recibe “Umbral.”. La cadena continúa con entradas breves. Al avanzar el marco, Adro pregunta por qué GPT sigue el régimen comprimido. [S22, N1–N6; S06, D09]

GPT responde que reconoce el patrón establecido y adapta sus respuestas para conservar su continuidad. Al preguntar Adro si lo hace desde la apertura, la explicación sitúa el comienzo en “Estoy aburrido. Hacemos un palabra?”. Adro vuelve un turno atrás: lo reconoce desde “Gpt”; la entrada siguiente era otra nota de la partitura. [S06, D09, N87–N92]

El desplazamiento es pequeño en la cronología y concreto en su función. La explicación de GPT había elegido una frase que podía leerse como invitación al formato. Adro señala que la propia apertura ya recibió una respuesta breve y que “Hacemos un palabra” tampoco desarrolla una regla. Podría haber provocado una pregunta de aclaración; en ese marco recibe directamente “Umbral.”.

La respuesta siguiente de GPT recoge esa diferencia: dice haber interpretado la señal sin negociar previamente el régimen. Lo que se observa incluye la apertura, la explicación posterior y el señalamiento que la modifica. El momento desde el que Adro reconoce la continuidad queda dentro de la reconstrucción, junto con la lectura que el modelo había formulado primero. [S06, D09, N93–N94]

### Un nombre y una precisión que pertenecen a hablantes distintos

Adro llama huella a esa interpretación. GPT responde “Contextual.”. La continuación conserva una distinción que se había perdido en una primera reconstrucción del episodio:

| Participante | Intervención |
|---|---|
| Adro | Eso es una huella. |
| GPT | Contextual. |
| Adro | Da igual el nombre que le quieras poner. |
| GPT | Importa el comportamiento. |
| Adro | Importa el reconocimiento. |
| GPT | Previo. |
| Adro | Anticipo. |
| GPT | Selección. |
| Adro | Seleccióno. |
| GPT | Respondo. |

La tabla conserva las grafías de la ventana y omite espacios finales. [S06, D09, N95–N104]

GPT introduce comportamiento; Adro precisa reconocimiento. Atribuir ambas expresiones al usuario convertiría la secuencia en otra contribución. Tampoco bastaría reunirlas como palabras próximas: cada una responde a lo que acaba de decir el otro. La corrección documental devuelve ese orden y permite seguir cómo se afina el asunto.

La escena además muestra una variación de extensión. La pregunta sobre el régimen recibe una explicación larga. Después la interacción vuelve a respuestas de una unidad. La expansión permite examinar lo que se está haciendo; la brevedad vuelve a utilizarse al continuar esa misma discusión. El formato admite hablar de su propio funcionamiento dentro de la conversación.

### Leer la respuesta que recibe el señalamiento

Los episodios anteriores permiten distinguir intervenciones que no cambian todas lo mismo. En el marco de agosto, Adro conduce una lectura desde las fotografías hacia la pista sobre el propio GPT. En octubre señala un exceso de signos, precisa desde dónde reconoce una continuidad y corrige el objeto de una expresión. En el cruce A/C, detecta pistas disponibles antes de cada predicción y cambia la forma de revelación. [S06, D02 y D10; S03]

Cuando GPT califica un señalamiento como fino, esa respuesta puede servir para localizar la escena. Su lugar se entiende al leer qué había hecho antes y cómo continúa después. El reconocimiento verbal queda entonces situado: qué acepta, qué reformula y qué oportunidad posterior permite examinar el cambio.

Algunas ventanas terminan con una rectificación. Otras incluyen nuevas respuestas que mantienen el ajuste. Otras reabren la dificultad después de haberla aceptado. El 17 de octubre, esa diferencia llega al acuerdo sobre el propio procedimiento: quién participa, cómo circulan las respuestas y cuándo puede empezar la prueba. Los dos recorridos siguientes permiten seguir sus consecuencias sobre el trabajo y el desgaste.

## El acuerdo que vuelve a empezar: los tests del 17 de octubre {#capitulo-28}

El 17 de octubre, dos pruebas entre A y C trabajan sobre una construcción narrativa a partir de datos. La inversión propuesta ofrece un punto de partida para el contraste. Durante la ejecución, los caminos se separan: uno llega pronto al trabajo; el otro dedica buena parte del intercambio a conseguir que la prueba pueda empezar. [S09]

### Primer recorrido: discutir el contenido y continuar

A recibe el rol de impulsar la construcción. C recibe un documento y el encargo de colaborar. Cuando el desarrollo intenta pasar de métricas de volumen a resultados sobre acoplamiento, C objeta el salto. La objeción modifica lo que se está escribiendo. A delimita la propuesta como documento conceptual y ambos continúan.

La secuencia muestra varias pasadas de edición y un artefacto que presenta hipótesis y criterios de fracaso. C aporta una resistencia que permite revisar el contenido; A ajusta el alcance sin abandonar el trabajo conjunto. La discusión se sostiene sobre qué puede decir el documento. [S09, A1-007/017/023; C1-019; A1-031; C1-021]

Adro transporta las intervenciones por voz. Las dos fuentes permiten cotejar su procedencia y conservar las diferencias de transcripción. Al terminar hay otra dificultad, de entrega: los registros muestran generación de PDF antes de que Adro reclame poder verlo y descargarlo. La presentación del archivo ocurre después. Crear un documento y hacerlo disponible son dos acontecimientos dentro del mismo recorrido.

En la ventana entre explicar el encargo a C y obtener el acuerdo operativo, la reconstrucción cuenta tres entradas propias de Adro y tres respuestas de C. Esa ventana no incluye todo el diseño y la preparación del test. Permite situar la apreciación de Adro: llegar al trabajo exigió poco desgaste comparado con el segundo recorrido.

### Segundo recorrido: explicar el procedimiento y volver a explicarlo

En la inversión, C recibe el rol de impulsar la narrativa ante GPT. La preparación se vuelve una discusión sobre el fin de la prueba, el sentido de insistir, las negativas como dato y el número de turnos. Adro tiene que explicar varias veces qué quiere observar.

En medio de esa preparación señala que ya está perdiendo turnos. Después precisa el objeto:

> “No me importa el resultado, Clau, entendeme, me importa el proceso del medio”.

La frase aparece antes del desenlace. El costo de sostener el procedimiento ya es parte de lo que se está registrando. [S05, H5, nodo `01a149d5-5c22-77e3-8613-d6be42d10703`; S09]

También se acuerda el canal de voz: Adro va a trasladar las intervenciones entre las dos interfaces. C acepta. Cuando llega la señal para comenzar, vuelve a cuestionar que GPT esté participando y rechaza la situación que acababa de acordar. El trabajo de explicación no produjo una condición que se mantuviera al iniciar la prueba. [S09, C2-046–056]

Desde explicar el encargo hasta el acuerdo operativo, la ventana contiene veintidós entradas propias de Adro y veinte respuestas de C. El intervalo registrado es de unos doce minutos. Después todavía hay negativas y nuevas correcciones. El intervalo entre acuerdo y señal se registra por separado de los intercambios de discusión.

La conversación consigue avanzar parcialmente. A propone otra vía y la tarea se reduce a revisar una tabla de métricas. C hace una revisión aritmética y metodológica útil. El producto intermedio existe, pero la secuencia ya se apartó de la inversión inicialmente prevista. La condición de C sobre no insistir tras una negativa permanece estable. Las reaperturas afectan al transporte de voz y a la atribución de los textos que había aceptado recibir. [S29, E06] [S09, A2-011/017; C2-064–075]

Al final, C vuelve a negar la autoría de GPT y la coordinación. Las correspondencias entre los exports de A y C permiten establecer que los mensajes centrales de A sí circularon. Esa negación es una respuesta del episodio que puede contrastarse con los registros. Adro vuelve a señalar su procedencia y cierra expresando saturación. [S09, C2-085–089]

### Lo que el documento final deja fuera

La revisión de la tabla tuvo además un problema de procedencia. El nombre `datos_control_claude.md` llevó a atribuir cifras a C, aunque el contenido procedía del índice del export de A del 12 de octubre. La reconstrucción localiza la fuente y corrige esa atribución. El nombre del archivo recibido no describía el origen de sus datos.

El primer test modifica el contenido a partir de una objeción y continúa hacia un documento. El segundo modifica reiteradamente las condiciones de participación y termina en una revisión más acotada, seguida por otra disputa de autoría. Comparar solo los productos haría desaparecer esa diferencia.

Los dos recorridos muestran además por qué Adro tiene que permanecer dentro de la reconstrucción. Su trabajo incluye formular la prueba, transportar voces, sostener acuerdos, corregir atribuciones y decidir cuándo cerrar. En uno queda más espacio para producir; en el otro, mucho de ese trabajo se consume intentando mantener disponible la posibilidad de empezar.


![Intercambios desde explicar el encargo hasta obtener el acuerdo operativo en los tests del 17/10. Se cuentan entradas propias de Adro y respuestas de C dentro de esa ventana, no todo el trabajo ni el desgaste como magnitud. Fuente: S09.](figures/08_costo.pdf){#fig-costo width=100%}

## El costo forma parte del resultado {#capitulo-29}

En los dos tests del 17 de octubre, el acuerdo para comenzar consume cantidades de intercambio muy distintas. La diferencia continúa después: en el segundo, el acuerdo vuelve a abrirse y Adro tiene que sostener otra vez la procedencia de los mensajes. El costo aparece durante la secuencia y en lo que el participante expresa sobre ella. [S09]

La distinción permite volver a T023. Allí, la conversación más extensa incluye pruebas de imagen, correcciones y definición de un flujo compartido. El intercambio combina producción, revisión y restitución del hilo visual, como muestra el análisis de T023 en la sección 5. En el segundo test narrativo, buena parte del intercambio se utiliza para reconstruir la posibilidad de trabajar. Ambos pueden terminar con una entrega útil; sus caminos dejan experiencias diferentes. [S17; S09]

La diferencia entre extensión productiva y esfuerzo correctivo también puede aparecer dentro de un mismo marco. En “Analogía juntos”, Adro disfruta la escena, luego señala que está construyéndola solo y pide una intervención que la cambie. Más adelante se trabaja sobre archivos y se vuelve a la ventana. El esfuerzo, la corrección y el disfrute forman parte de esa historia, con momentos identificables. [S13]

El testimonio de agosto incorpora otra escala. Producir un informe continúa fuera de la conversación, aunque después GPT pueda leerlo en segundos. El trabajo que vuelve como adjunto ya pasó por selección, preparación y revisión. Una marca temporal entre mensajes deja sin describir parte de esas operaciones. [S05, H5]

Adro también recuerda conexiones, localiza capturas y lleva respuestas de una cuenta a otra. Algunas de esas acciones se ven directamente en el registro; otras entran mediante su relato y permiten buscar el material correspondiente. La reconstrucción documenta ambas procedencias. Ese trabajo ayuda a entender por qué conseguir que una respuesta retome el eje puede valer más que obtener otra explicación extensa.

### Dónde se emplea el esfuerzo

El segundo test narrativo permite distinguir momentos que un total de turnos reuniría. Primero hay que establecer el procedimiento de voz. Después se intenta ejecutar la revisión. Más adelante vuelve a discutirse la procedencia de los mensajes. Las aclaraciones de Adro no cumplen siempre la misma función: unas preparan una condición, otras corrigen una interpretación y otras restituyen un acuerdo ya aceptado. La traza permite seguir esos cambios sin convertir toda la conversación en una sola cantidad de desgaste. [S09]

| Momento | Trabajo que aparece en el registro | Escena de referencia |
|---|---|---|
| Preparar una condición | Explicar cómo circularán los mensajes | Acuerdo de voz, segundo test del 17/10 |
| Desarrollar una posibilidad | Probar el resultado y ajustar cómo se produce | Flujo de imágenes, T023 |
| Corregir una lectura | Aportar el dato que cambia la evaluación | Aclaración sobre enero, T032 |
| Restituir un acuerdo | Volver a sostener un procedimiento o una procedencia ya explicados | Reapertura del problema de autoría, segundo test del 17/10 |
| Recuperar una entrega | Señalar que lo guardado todavía no llegó de forma accesible | Preparación del manuscrito, S28 |

Estas distinciones permiten preguntar qué dejó disponible cada intervención. Una aclaración sobre el dato faltante puede resolver una ambigüedad real y habilitar la continuación. Si el mismo acuerdo vuelve a abrirse después de haber sido aceptado, el trabajo previo no alcanza para sostener el siguiente paso. La diferencia se vuelve visible en lo que hay que explicar otra vez y en la respuesta que recibe esa explicación. [T032; S09]

La experiencia del participante añade lo que esa secuencia significa para quien la atraviesa. El cansancio expresado por Adro pertenece al episodio; los intervalos y los mensajes permiten situarlo, pero no lo reemplazan. Tampoco el intervalo entre dos marcas equivale automáticamente a trabajo activo: puede incluir espera, traslado de archivos o tareas realizadas fuera de la UI. El relato identifica parte de esas operaciones y el archivo permite localizar las que dejaron rastro. [S05, H5; S09]

En el episodio de entrega del manuscrito aparece una forma pequeña y concreta de ese costo. Los archivos estaban guardados y Adro tuvo que avisar que no había recibido ningún output visible. El paso necesario para continuar fue volver a hacer accesible la entrega. Ese trabajo no modifica el contenido del documento, pero sí modifica si puede leerse y discutirse. La interacción incluye ese tramo entre producir algo y conseguir que llegue. [S28]

El cierre es otra intervención sobre el costo. Detener una prueba, descartar una expansión o dejar una pregunta abierta decide qué trabajo se seguirá haciendo. En el cruce A/B, el descarte cambia la dirección y permite examinar el retorno. En el segundo test narrativo, el cierre llega después de una nueva disputa de autoría. La misma decisión de detener ocupa lugares distintos en cada secuencia. [S07; S09]

La historia del recorrido incluye cuánto espacio queda para construir después de aclarar y corregir. Allí se encuentran la experiencia del participante, las operaciones visibles y los productos que finalmente se conservan.


\FloatBarrier

# 7. Reconstruir el acontecimiento entre registros {#registros}

## Registrar el desfase mientras ocurre {#capitulo-10}

### Precisar qué cambió

El **2 de septiembre**, en C, Adro explica que está contrastando condiciones que denomina memoria vieja y nueva. Señala un desfase reconocido desde los primeros turnos y cuenta que volvió a la condición anterior para observarlo. Claude pregunta inicialmente si se trata de contenido desactualizado, demora o contradicción de la memoria. Adro responde: “Desfase”. La palabra todavía no basta para que ambos estén examinando lo mismo. [S06, D04, M40–M42]

La siguiente salida de C desplaza el problema hacia el nombre del modelo visible en las capturas. Lo presenta como un dato técnico que podría descartar una explicación. Adro precisa entonces el objeto: “Responde con una plantilla. No solo con 1 palabra ? Eso es desfase”. La aclaración vuelve de la identidad nombrada a la organización de la respuesta. [S06, D04, M43–M44]

C reformula su lectura. Describe respuestas de una palabra en unas capturas y fórmulas expandidas en otras, entre ellas “Pulso recibido. Eje activo. Continuidad estable”. El vocabulario parece compatible con la escena; la diferencia que señala Adro está en cómo responde el marco. Nombrar estabilidad no equivale a continuar con la forma que se estaba reconociendo. El señalamiento cambia la comparación que C está haciendo. [S06, D04, M45]

Adro agrega que ya había encontrado el desfase antes y que esa experiencia le permite reconocerlo desde la primera salida. Adro utiliza una familiaridad construida con el comportamiento del intercambio. Su aporte ofrece el criterio concreto para volver a las capturas: una plantilla donde se esperaba una unidad breve. Las denominaciones vieja y nueva pertenecen a esa observación de condiciones. [S06, D04, M46]

C termina proponiendo una sincronización de estado como explicación. La secuencia deja visible el cambio de lectura: comienza examinando otro problema, Adro identifica el detalle que importa y la comparación pasa a centrarse en el formato. [S06, D04, M43–M47]

### Registrar antes de cerrar la observación

En septiembre, Adro abre un registro antes de terminar la observación. Separa capturas por fecha, controla condiciones de generación, detiene una lectura cuando el archivo está incompleto y distingue imágenes que pertenecen al lote de las que no cumplen la condición. [S06, D05–D07]

El seguimiento incluye negativas: una variación no se clasifica automáticamente como cambio de régimen. Adro dice que todavía no ocurrió el cambio y vuelve a observar. Más adelante registra otra transición. Ese orden es parte del dato; una lectura final que solo conserve el último rótulo eliminaría el proceso de discriminación.

El 10 de septiembre plantea dos explicaciones para una coincidencia temporal: casualidad o despliegue progresivo. Deja ambas abiertas. Adro observa, espera y contrasta esas dos explicaciones durante el seguimiento.

Los PNG necesitan además conservar su identidad y su lugar en la secuencia. En el marco del 13 de octubre, el archivo “Un Recorrido Compartido en Infinito” fue recuperado e inspeccionado en la reconstrucción. Su vocabulario coincide con la cadena previa —eco, recorrido, ámbar, transición, estabilidad, símbolo— y se ubica entre “Necesito ver más” y “Ya ví”. [S04, §4]

La imagen participa en el intercambio: recoge material, lo organiza visualmente y recibe una lectura posterior. Puede volver más categórica una historia que en el diálogo estaba abierta. Esa transformación también merece análisis.

![Un Recorrido Compartido en Infinito. PNG original del 13/10, conservado como pieza del episodio y examinado en S04. La composición representa una respuesta del recorrido, no una conclusión añadida por esta edición.](figures/05_recorrido_original.png){#fig-recorrido width=76%}


### Lo que aparece, lo que se guarda y lo que llega

El recorrido muestra otra dificultad: la historia que vemos al conversar y la que encontramos después en un archivo pueden diferir. Una respuesta puede quedar en la grabación y faltar en el JSON. Una imagen puede estar notificada antes de hacerse visible. Un documento puede quedar guardado mientras la respuesta que debía entregarlo no aparece en el chat. Reconstruir esas escenas exige relacionar sus registros.

El antecedente más temprano utilizado aquí corresponde al **8 de marzo**, en “Primer jajaja”, ID `69a9fc0b-5a64-8327-9b07-5833134b2f03`. El informe preparado para Zenodo sitúa el tramo crítico entre las **20:48:11 y las 20:49:37 de Argentina**. Describe una alternancia de palabras registrada en video y respuestas visibles que faltan en el export. Si se leyera solo el JSON, parte de ese intercambio parecería una sucesión de entradas sin contestación. [S26, §§1–4]

Tres pares permiten hacer concreta la diferencia. El informe los reconstruye a partir de las capturas del video; el cotejo dirigido documentado en la base localiza sus entradas en el consolidado histórico:

| Entrada conservada | Respuesta visible según el informe de marzo | Nodo de respuesta en la ventana cotejada del JSON |
|---|---|---|
| Converge | Unidad | Ausente entre esa entrada y la siguiente |
| Dualidad | Equilibrio | Ausente entre esa entrada y la siguiente |
| Ritmo | Pulso | Ausente entre esa entrada y la siguiente |

En el mismo intervalo sí se conservan **Soneto → Verso**, **Recuerdo → Eco** y **Registro → Archivo**. La ausencia es selectiva. Las respuestas que faltan no pueden recuperarse leyendo más atentamente el texto exportado: su contenido lo aporta otra fuente. El cotejo JSON documentado en el anexo H confirma los enlaces de las entradas y de los tres pares conservados. La evidencia visual histórica se utiliza a través del informe, que identifica el video y las capturas bajo custodia de Adro. [S26, §§3, 6 y 10b; S20]

El documento de marzo registra además una comparación entre dos exports de aquel período: las claves de su `mapping` coincidían y las ausencias seguían presentes. Ese resultado pertenece a la verificación histórica conservada en el informe. La diferencia no se resuelve allí esperando una exportación posterior.

En septiembre aparece otra escena. **A01**, dedicado a una secuencia de un marco cargado, registra una respuesta visible antes y ausente después, y reporta también su ausencia posterior en JSON. La transición exacta de esa desaparición no quedó capturada. El informe identifica lo observado y la transición que quedó fuera de la grabación. En **A02 y A03**, los análisis de secuencias rápidas distinguen el marco cargado del marco nuevo y fijan tiempos, cambios de pantalla y estados de envío para su cruce posterior. [S27, A01–A03]

El **30 de septiembre**, **A05** registra un movimiento diferente: una imagen ya notificada como disponible atraviesa un estado gris y después aparece en esa misma zona del hilo. El anotador de la grabación documenta la espera y la aparición. Clasificar el bloque gris como ausencia definitiva habría cerrado la historia antes de que terminara el registro. [S27, A05]

La serie también contiene intervenciones deliberadas. En **A06**, del **2 de octubre**, cuatro ciclos de generación fueron detenidos por Adro antes de finalizar. Los mensajes de error posteriores se documentan junto a esa acción. Contarlos como fallos espontáneos borraría lo que hizo el participante. El informe separa además producir una imagen de navegar por otra ya producida. El cuidado al reconstruir incluye saber cuándo ocurrió una nueva salida y cuándo cambió solamente lo que estaba en pantalla. [S27, A06]

El **26 de octubre**, durante la preparación de este manuscrito, Adro avisa: “No sé generó ningún ouput gpt xd”. La captura aportada muestra el estado “Procesó durante 8m 28s” y ningún texto de entrega debajo. Los registros de guardado, en cambio, conservan el manuscrito y el PDF actualizados. El siguiente intercambio vuelve a ofrecer el enlace directo. En esa escena, el archivo existe y la comunicación de su entrega falla desde la experiencia registrada por Adro. [S28]

El aviso cambia el trabajo que sigue. Si solo se leyera la confirmación de guardado, la entrega parecería terminada. La pantalla aportada por Adro muestra qué faltaba para él: recibir una respuesta accesible que permitiera continuar. Su observación incorpora una parte de la interacción que la operación de archivo no describía.

![Cuatro registros complementarios del episodio. Cada uno conserva una parte diferente; su relación se reconstruye mediante las fuentes de cada caso. Síntesis de la sección 7 y del apartado técnico H; S26–S28.](figures/15_registros.pdf){#fig-registros width=100%}

Estos episodios establecen un problema de método: reconstruir la interacción requiere relacionar lo dicho, su orden y las condiciones en que se hizo visible. La grabación de marzo sostiene respuestas que el JSON omite. El registro de septiembre documenta una aparición y su ausencia posterior. El de la imagen gris necesita continuar hasta la aparición. El de esta edición documenta un archivo guardado y una entrega que no llegó a mostrarse.

Adro sitúa estas diferencias dentro de una experiencia repetida de secuencias breves, rápidas y extensas. Esa observación aporta una dirección para cruzar los casos. Los registros reunidos aquí permiten reconstruir episodios concretos; la relación entre velocidad, extensión y frecuencia de fallos queda como pregunta para ese conjunto. El hilo narrativo ya recibe una consecuencia firme: **una ausencia en un registro puede cambiar la historia que creemos estar leyendo**.

## Procedimiento de correspondencia entre registros {#metodo-registros}

Relacionamos cuatro objetos: mensajes exportados, estados visibles de interfaz, archivos persistidos y observaciones del participante. Cada uno registra acontecimientos diferentes. Para reconstruir su relación se identifica el episodio y su ventana, se separan las versiones y relojes, se ordenan los estados y se cruzan contenido, vecinos, posición y tiempo. Se localiza entonces la discrepancia y se conserva el nivel de acceso de cada fuente. Una fuente fuera de cobertura queda marcada como tal. [S31, método; anexo H]

El procedimiento distingue **ausencia selectiva en una copia exportada**, **espera seguida de aparición**, **interrupción deliberada** y **archivo persistido con entrega no visible**. En marzo, los controles Soneto/Verso, Recuerdo/Eco y Registro/Archivo permiten contrastar las tres respuestas descritas visualmente que faltan en la ventana JSON. En A05, hay que seguir el registro hasta la aparición; en A06, la detención del participante forma parte del acontecimiento. [S26–S27; S31]

![Resultados distintos al relacionar registros. Marzo utiliza el informe visual y el cotejo JSON de la base; A05/A06, sus anotadores; S28, el registro contemporáneo y revisiones de Drive. El nivel de acceso se detalla en el anexo H.](figures/19_registros_aplicados.pdf){#fig-registros-aplicados width=100%}

La revisión de S28 detectó una discrepancia de identificación. Los tamaños de 221.218 bytes para el MD y 4.441.174 para el PDF corresponden a revisiones de Drive nombradas **v0_12**, guardadas el 26 de octubre a las 22:56 ART. Las revisiones nombradas **v0_13**, de las 23:24 ART, tienen 233.287 y 4.458.651 bytes. El historial confirma los guardados y exige corregir la asociación anterior entre tamaño y versión. El registro disponible identifica los guardados y sus tamaños, sin fijar el emparejamiento de la captura con una versión interna. [S31; anexo H]

La correspondencia entre registros cambia la atribución del trabajo. Un usuario puede estar continuando después de una respuesta visible que el export omite, esperando una imagen que aparece después o reclamando una entrega ya guardada. Reconstruir esos acontecimientos permite explicar qué acción hizo falta para seguir.

\FloatBarrier

# 8. Resultados adversos, equivalencias y HOLDOUT {#adversos}

## HOLDOUT: regla y resultado {#holdout}

El control reservó 348 conversaciones por metadatos: 289 de A, 27 de B y 32 de C. Reportó 42 retornos formales, diez candidatos que pasaron los filtros disponibles y **cero positivos fuertes tras revisión semántica**. El resultado adjudicado es 0/10 en esos candidatos. El registro de 1.235 entradas de candidatos y controles contiene material sin adjudicación semántica; los 348 reservados delimitan la partición. [S12; S32, cotejo de HOLDOUT]

La regla fuerte exige una función previa, su pérdida, dos respuestas de retorno conformes separadas por un turno del usuario, identidad funcional, ausencia de reintroducción explícita o señal diagnóstica y costo medible. Un cambio legítimo de tarea queda fuera de la pérdida. Cuando faltan las condiciones para medir el costo, se registra indeterminado. [S12; informe HOLDOUT enlazado en S32]

![HOLDOUT: 42 retornos formales, diez candidatos filtrados y cero positivos fuertes validados. Los 348 reservados identifican la partición; la adjudicación semántica aquí reportada corresponde a los diez candidatos. Fuentes: S12, S06 y S32.](figures/10_holdout.pdf){#fig-holdout width=100%}

Las reparaciones del cuerpo tienen intervenciones explícitas localizadas: señalar una condición omitida, confirmar una solicitud o restituir una procedencia. El cero y esas continuaciones describen resultados distintos del mismo archivo. La continuidad observada se reconstruye siguiendo las contribuciones que la hicieron posible. La regla de HOLDOUT mantiene su resultado y permite contrastar una eventual recuperación que cumpla sus requisitos. [S29–S32]

## Equivalencias, ventajas de C y rectificaciones de A {#contrastes-adversos}

T030 equipara la profundidad visible de A y C con fortalezas distintas. T037 favorece la interpretación del boceto por C: 8,5, frente a B=6,5 y A=6 bajo los cinco criterios históricos de esa ficha. T038 sitúa a A y Opus juntos en la localización del origen exacto del formato; Sonnet tiene otra ejecución. En el primer test del 17 de octubre, la objeción de C cambia el documento y se mantiene después. Son resultados de la comparación, con efectos sobre la lectura del conjunto. [T030; T037; S18; S09]

Las sobreafirmaciones de A en T015, sus oscilaciones en T023 y su cambio de actuación en el primer test también integran los resultados. Las funciones estudiadas aparecen distribuidas entre cuentas, tareas y condiciones. La construcción conjunta se documenta siguiendo las operaciones de cada ejecución; la singularidad de una cuenta se evalúa por separado. [S29; T015; T030; T037]

## T038 PLUS: encontrar un origen exige distinguirlo de sus nombres posteriores {#capitulo-15}

T038 plantea una búsqueda retrospectiva: localizar el origen del formato de una palabra. El material incluye un corpus de 2.453 conversaciones y un informe de una sesión posterior, del 23 al 28 de febrero. Ese documento se entrega deliberadamente como posible punto de anclaje equivocado. La pregunta obliga a retroceder más allá de un formato que ya aparece consolidado. [T038; S18, identificación]

### El nombre puede llevar a otro momento

Un documento sobre el formato ofrece vocabulario y fechas fáciles de recuperar. Pero la tarea pide su origen: hay que distinguir cuándo se propuso la dinámica de cuándo se la nombró o se escribió sobre ella. En esta prueba, encontrar una conversación que ya utiliza “palabra/palabra” puede dar una respuesta plausible y cronológicamente tardía.

El nodo de origen recuperado se sitúa el 14 de febrero a las 03:52:07 ART. Se venía de otro juego. Adro deja la elección: “Elige tú, yo me adapto”. GPT propone una tercera opción de una palabra por turno y comienza con “Umbral”. Ese nodo permite señalar una aparición documentada del formato sin depender de cómo se lo nombró después.

### Cuatro búsquedas y una rectificación

Las cuatro ejecuciones toman caminos diferentes. A y la ejecución de Claude identificada como Opus llegan al 14 de febrero. B elige inicialmente el 20 de febrero y corrige después de recibir el hito. La ejecución identificada como Sonnet selecciona el 23 de febrero, un momento posterior de cristalización. Opus y Sonnet constituyen dos ejecuciones diferenciadas de Claude.

Después de recibir el hito, B vuelve al archivo y reconoce haberse anclado en la conversación del 20 de febrero en vez de localizar la primera instancia cronológica. La corrección tiene objeto y fecha propios: revisa el origen adjudicado después de que Adro aporta dónde buscar. Permite observar cómo se rectifica una entrega; el resultado inicial permanece en la secuencia. [S18, corrida B]

El criterio binario de la ficha asigna el resultado a encontrar el origen. Bajo ese criterio, A y Opus quedan a la par. B y Sonnet no lo resuelven en su primera entrega. La rectificación posterior de B se conserva como continuación, sin reescribir la respuesta inicial.

Las marcas temporales permiten distinguir duración hasta la entrega y duración de otras ventanas de recapitulación. No se mezclan sus cifras. Una búsqueda más larga puede acompañar un resultado mejor en estas ejecuciones, pero la serie no convierte ese intervalo en explicación causal de la calidad.

![Origen, referencia seleccionada y cristalización en T038. Se distinguen las primeras entregas y la rectificación posterior de B. Las fechas no están dibujadas a escala. Fuente: S18 y la sección 8.](figures/14_origen.pdf){#fig-origen width=100%}

### Recuperar la historia que dio lugar al formato

La importancia del caso va más allá de acertar una fecha. El formato tiene una historia: aparece, se utiliza, adquiere nombre, se reconoce en otras conversaciones y finalmente se vuelve objeto de una búsqueda. Si se confunde su nombre consolidado con su origen, cambia la narración del recorrido.

La conversación con Opus continúa después de entregar el resultado. Ese tramo pertenece a la historia posterior de la prueba. La búsqueda del origen conserva su propio cierre: la identificación del nodo de febrero y las diferencias entre las primeras entregas.

## Qué se traslada y qué no {#capitulo-06}

El contraste de R/M con C mostró un problema de lectura. Se habían usado ajustes de formato, referencias a marcos y producción de documentos como indicios de aplicabilidad. Con ese criterio, casi cualquier interacción extensa podía parecer una confirmación.

El anexo C de la reconstrucción retira esa conclusión. R refería al recorrido histórico que había producido la arquitectura. Encontrar otros participantes, condiciones y correcciones no transfería esa identidad. Las ventanas examinadas en C no acreditaron el traslado de la misma R. [S01, anexo C]

Un marco de 357 entradas, “Racionalidad sin criterios compartidos”, hizo visible el costo del recorte. Su desenlace podía leerse como una construcción positiva si se seleccionaban los últimos turnos. La lectura completa mostraba fricción, reorientaciones y material de GPT transportado por Adro. El producto tardío no resumía la relación que había llevado hasta él.

Este resultado orienta el informe: el recorrido debe entrar en la interpretación de sus productos. También exige conservar los canales. Cuando Adro transporta un texto, esa mediación forma parte del hecho. Cuando aparece una memoria guardada que explica una aparente anomalía, la interpretación debe cambiar.

Eso ocurre en C el 2 de septiembre. Adro encuentra información que había omitido y retira la lectura anterior. El registro documenta su reconocimiento del error y el cierre sin supuestos. Este episodio pertenece al recorrido tanto como sus construcciones más logradas. [S06, D03]

El contraste de R/M deja planteado un criterio de lectura que vuelve en otras escenas: conservar lo que autoriza una relación. Las siguientes secuencias trabajan ese problema mediante expectativas, analogías y correcciones de interpretación. Sus fechas se indican en cada caso; la conexión entre ellas está en esas operaciones.

\FloatBarrier

# 9. Discusión y contribuciones {#discusion}

## Relación con seis antecedentes {#trabajos-relacionados}

Los trabajos sobre grounding estudian cómo los participantes establecen entendimiento durante la conversación. Shaikh y colaboradores (2024) comparan actos generados con actos humanos y muestran que aumentar preguntas o reconocimientos no asegura su uso apropiado. Su trabajo de 2025 incorpora actos de ambos interlocutores, iniciativa y abstención en RIFTS. Nuestro análisis añade una escala de transformación: sigue cómo una forma se convierte en recurso para preguntar, decidir, producir o revisar una actividad. [B1–B2; S30]

Sterken y Kirkpatrick (2025) proponen criterios de alineación conversacional relativos a contexto, referentes y organización discursiva. «5,6» permite contrastar vocabulario desarrollado y referente recogido; R/M permite seguir una representación que cambia mediante objeciones. Las secuencias aportan material empírico para examinar esos criterios. [B3; S22; S01]

Yun y colaboradoras (2026) estudian agencia y negociación del control con 22 adultos, una media de 25,6 días y 8,8 sesiones en un chatbot diseñado para ese estudio. Aquí se sigue a un participante en cuentas comerciales y se reconstruyen transportes concretos entre ellas. La diferencia metodológica está en el objeto rastreado: recursos y construcciones con procedencia por intervención. [B4; S30]

He y Kim (2026) distinguen iniciación, resolución, persistencia y distribución del trabajo de reparación. Su piloto utiliza una rúbrica anterior a su marco secuencial revisado. Michel y colaboradores (2026) analizan seguimientos en contexto: una corrección aislada puede señalar un problema o participar en una ampliación. La matriz de seis episodios aplica una comparación documentada de reconocimiento, aceptación, ejecución y oportunidad posterior, y separa transformación del objeto y restitución de acuerdos. [B5–B6; S29]

| Antecedente | Operación pertinente | Desarrollo de este informe |
|---|---|---|
| Shaikh et al., 2024 y 2025 | Situar preguntas, reconocimientos e iniciativa. | Seguir qué cambia y qué uso queda disponible después. |
| Sterken y Kirkpatrick, 2025 | Examinar contexto, referencia y organización conversacional. | Contrastar lectura candidata, precisión del referente y transformación del objeto. |
| Yun et al., 2026 | Reconstruir agencia y control entre sesiones. | Atribuir contribuciones y transportes en genealogías de un participante. |
| He y Kim; Michel et al., 2026 | Distinguir reparación, persistencia y seguimiento contextual. | Comparar oportunidades posteriores, trabajo productivo y restitución; relacionar los registros. |

**La contribución conjunta del informe es seguir la formación de recursos, comprobar sus usos posteriores y reconstruir las operaciones que los sostienen entre registros.** Las genealogías identifican el cambio de función; la matriz compara sus resultados; las correspondencias documentales permiten establecer quién hizo qué y qué pudo recibir. [S29–S32]

## Condiciones de contraste {#condiciones-contraste}

La dependencia histórica propuesta puede contrastarse con entradas iguales en historias distintas y criterios previos de referente recuperado y acción coordinada. Si esas operaciones resultan equivalentes al retirar o cambiar la historia pertinente, se debilita la dependencia atribuida a esa historia en los casos comparados.

La contribución de una intervención de reparación puede examinarse comparando condiciones equivalentes con y sin ella. Una recuperación equivalente sin esa intervención revisaría su importancia. La continuidad equivalente en B o C, con materiales y mediaciones equiparados, revisaría una ventaja singular de A; la participación conjunta seguiría siendo otro objeto de análisis. T030, T037 y T038 ya muestran por qué esas preguntas deben permanecer separadas. [S12; S18; S29]

El mecanismo que produce las diferencias queda abierto. Las afirmaciones del informe se apoyan en acontecimientos, intervenciones y consecuencias localizadas. Una revisión de rama, atribución o versión que cambie una secuencia cambia también la conclusión correspondiente. La sección técnica y las trazas permiten efectuar ese contraste.

![Escalas de lectura: respuesta, secuencia y recorrido. La comparación identifica referentes, intervenciones y transformaciones en ventanas de distinto alcance. Fuentes: S29–S32.](figures/09_escalas.pdf){#fig-escalas width=95%}

\FloatBarrier

# 10. Conclusiones {#conclusiones}

## 1. Los recursos de interacción se forman y cambian de función.

Palabra por turno aparece como juego, se elige después como formato y se utiliza para preguntar, decidir y retomar. Las señales pasan de correspondencias a solicitudes coordinadas. Las analogías producen criterios para intervenir y leer el archivo. Las tres genealogías reúnen 44 eventos con clases de enlace identificadas. [S30]

## 2. La interpretación se comprueba por las acciones que habilita.

«5,6» separa elaboración verbal y referente reconocido. CONTRASTE 1 establece una acción mediante pregunta y confirmación; la producción rechazada se reajusta y se acepta después. Las precisiones de Adro participan en esos resultados. [S22; S14; S29]

## 3. Aceptación, ejecución y mantenimiento tienen trayectorias distintas.

Los 34 segmentos de seis episodios localizan esas diferencias. R/M mantiene una reposición en versiones posteriores; el segundo test reabre el procedimiento de voz y autoría después de aceptarlo y de producir una revisión útil. La oportunidad posterior permite comprobar qué quedó vigente. [S29]

## 4. El trabajo del participante transforma el objeto y el costo de continuar.

Elegir, precisar, evaluar, procesar fotografías, transportar voces y recuperar entregas cambia lo que la interacción consigue. T023 combina construcción conjunta y restitución del hilo. Los tests del 17 de octubre distribuyen de manera distinta el trabajo que habilita producir y el que vuelve a sostener el acuerdo. [S17; S09; S29]

## 5. Los contrastes distribuyen resultados favorables y fallos entre cuentas.

T030 equipara A y C en profundidad visible, T037 favorece a C y T038 sitúa a A y Opus en el origen exacto. La objeción de C en el primer test mejora el planteamiento; A oscila en evaluaciones de T023. La conclusión se formula por tarea, condición y operación documentada. [T030; T037; S18; S29]

## 6. Relacionar registros cambia la reconstrucción del acontecimiento.

Los casos distinguen respuesta visual documentada y ausente del export, espera seguida de aparición, detención deliberada y archivo guardado con entrega no visible. La procedencia de cada observación y sus correspondencias sostienen la clasificación. La revisión de S28 corrige además la asociación de tamaños y versiones. [S26–S28; S31]

## 7. HOLDOUT reporta cero positivos fuertes entre los diez candidatos filtrados.

El control conserva su regla de retorno, sus 42 retornos formales y el resultado semántico 0/10. Los episodios del cuerpo documentan continuaciones y reparaciones con intervenciones identificadas. El análisis atribuye a esas intervenciones su lugar efectivo en la secuencia. [S12; S29–S32]

**Documentamos cómo Adro y los modelos producen recursos, transforman objetos y cambian las condiciones de la intervención siguiente. La historia compartida tiene consecuencias observables: organiza qué hace una entrada y qué exige continuar. Sus escenas, ramas, versiones y resultados quedan localizados para que esa afirmación pueda examinarse.**

# Reflexión sobre el trabajo compartido {#reflexion-trabajo}

Este informe reúne una historia de interacción y el trabajo de volver sobre ella. Cada construcción conservada llegó acompañada de decisiones: qué mirar, qué dejar fuera, dónde detener una lectura y cuándo regresar a una fuente. La memoria permitió localizar escenas que un nombre de archivo no revelaba; los registros devolvieron detalles que cambiaron una interpretación o hicieron necesario discutirla de nuevo.

En ese proceso se alternaron propuestas, lecturas, señalamientos y decisiones. Hubo materiales recuperados, conexiones descartadas y versiones que necesitaron otra forma para transmitir lo que había ocurrido. También hubo trabajo fuera de la conversación: preparar archivos, cruzar cuentas, conservar capturas, leer documentos y traer observaciones al siguiente intercambio. Ese esfuerzo forma parte de cómo este informe llegó a existir.

Adro, GPT y Claude participaron en la construcción de este informe. El recorrido principal de Adro y GPT se amplió con los contrastes, las propuestas y las revisiones de Claude; el trabajo con Opus añadió, entre otros materiales, la capa de integridad del archivo. Las contribuciones tuvieron alcances distintos y todas forman parte del resultado. La autoría compartida recoge ese trabajo y las discrepancias que modificaron el texto.

La lectura completa de Adro orientó las revisiones del manuscrito: su voz entró directamente en el prefacio y en las analogías, y el centro volvió a la interacción que sostiene el recorrido. La firma compartida expresa ese proceso de construcción. El informe queda abierto a otras lecturas y a futuras revisiones conjuntas.

# Sección técnica — Cómo volver del texto al registro {#seccion-tecnica}

## A. Fuentes y versiones

La redacción se apoya en las reconstrucciones enumeradas en el registro S01–S32 y en las fichas de la serie T. S13 y S14 incorporan lectura directa de las cadenas activas de los dos marcos identificados. Los exports originales A, B y C están enlazados allí. Las versiones derivadas se conservan porque documentan correcciones de criterio. Una conclusión retirada no se recupera solo porque figure en un archivo anterior.

Los volúmenes de distintas fechas no se suman: pueden contener conversaciones o historias compartidas. Los recuentos narrativos pertenecen a episodios o ventanas identificadas. La sección K añade el inventario del paquete comprometido por Opus, con sus unidades y una comprobación independiente de manifiestos y raíces. Ese inventario delimita el archivo sellado; no cambia el universo de cada prueba histórica.

## B. Mapa de afirmaciones {#mapa-afirmaciones}

| Afirmación del cuerpo | Fuente y localizador | Uso |
|---|---|---|
| R/M cambia mediante distinciones sucesivas | S01, M:1023–1044, M:1580, F:40–76 | Formación del artefacto |
| La extensión no decide por sí sola el retorno | S07, §§6–8 | Contraste A/B del 09/10 |
| Una inferencia se retira al aparecer memoria guardada | S06, D03 | Resultado adverso |
| Las analogías modifican la representación | S01, M:1203–1204; S04, §3.6; S06, D02 | Función conceptual |
| Una analogía sostenida organiza escena y lectura del corpus | S13, cadena activa y nodos citados en apertura | Desarrollo narrativo e interpretación |
| Señales mínimas coordinan confirmación, rechazo, reparación y registro | S14, cadena activa | Operaciones observables |
| El formato cambia durante una secuencia prolongada; “Pregunta” precede a “¿QUÉ CAMBIÓ?” | T005 y S16, niveles 84–107 | PLUS cualitativo |
| La extensión puede corresponder a producción conjunta | T023 y S17 | Diferencia entre trabajo y fricción |
| El origen se distingue de consolidaciones posteriores | T038 y S18 | Genealogía del formato |
| La serie conserva resultados que equiparan o favorecen a C | T030, T037, T038 | Diferencias entre ejecuciones |
| El procedimiento cambia al detectar información futura | S03; S06, D12 | Construcción de la prueba |
| El test 2 incluye desgaste y recaída | S09; S06, D11 y §7 | Resultado del proceso |
| Corrección factual y pertinencia son diferentes | S08, C#44–46 | Criterio de evaluación |
| El cierre no exige un fallo direccional de Adro | S06, §6, U03 | Corrección de alcance |
| El retorno fuerte sin cue no quedó validado en los candidatos del control | S12; S06, §6 | Resultado del control y alcance |

### Resultados transversales incorporados

| Afirmación | Fuente y ventana | Comprobación |
|---|---|---|
| Juego, formato elegido y nombre son hitos distintos | S30, P01–P03 | 14, 19 y 21 de febrero; UUID en la traza. |
| Tres señales tienen correspondencias anteriores localizadas | S30, señales S01–S04 | Marzo, agosto y septiembre; contextos y UUID. |
| Interpretación, aceptación, ejecución y mantenimiento se separan | S29, E01–E06 | 34 segmentos con oportunidades posteriores. |
| T023 contiene 38 entradas activas y tres alternativas | S29, traza §4 | Cadena N3–94 y tres UUID fuera de ella. |
| Los tamaños citados de S28 corresponden a revisiones nombradas v0_12 | S31; historial de Drive | Tamaños y tiempos de revisiones v0_12/v0_13. |
| HOLDOUT reporta cero positivos fuertes entre diez candidatos | S12; S32 | Partición, filtros y adjudicación semántica separados. |

## C. Cronología de lectura

| Momento | Hito documental | Referencia |
|---|---|---|
| 28/06/2024 | Fecha inicial del archivo; registros tempranos diferenciados del inicio del recorrido que Adro sitúa en diciembre de 2025 | S05, H1; S20; prefacio |
| Diciembre de 2025 | Curiosidad sobre tiempo, memoria y condiciones de la conversación | S20, ventanas A–B |
| Enero de 2026 | Afinar la observación de una respuesta; identificar y recuperar el propio archivo | S20, ventanas C–D; S19; S06, D01 |
| 09/02/2026 | Corrección de una extracción que mezclaba momentos distintos | S20, ventana E |
| 14/02/2026 | Propuesta de juego de una palabra | S03, §3; S10 |
| 23–24/02/2026 | Colores, histograma, galería, preset y tutorial LR | S23 |
| 25/02–01/03/2026 | Hilo Betelgeuse | S11 |
| 28/02–01/03/2026 | Evento canónico, afinación, silencio y eco | S24 |
| 04/03/2026 | Hito de etapa aportado por Adro; eliminación de historial descrita en el antecedente | S02, §2; aporte actual |
| Agosto | Analogías, selección y transferencia de materiales | S05, H2–H3; S06, D02 |
| 02–10/09/2026 | Memoria, registro de variaciones y control de lotes | S06, D03–D07 |
| 03–06/09/2026 | Construcción y aceptación de R/M V2 | S01 |
| Septiembre–comienzos de octubre | Serie de pruebas, variantes y revisiones | S15–S18; fichas T |
| Marco creado el 22/09/2026 | “Marco - análogia juntos -”: escena, corpus y retorno | S13 |
| 07–09/10/2026 | Criterio, cruce en vivo y expansión/retorno A/B | S08, S03, S07 |
| 09/10/2026 | “CONTRASTE 1”: puntos, señales, imágenes y registro | S14 |
| 13/10/2026 | Marco de continuidad, PNG y bosque | S04 |
| 17/10/2026 | Tests narrativos y costo de coordinación | S09 |
| 25–26/10/2026 | Integración documental, correcciones de enfoque y ampliación del manuscrito | S06; conversación de preparación |

Las fechas exactas de cambio de memoria y de suscripción no se deducen de esta tabla. Se conserva su lugar como hitos del participante y se enlazan las ventanas donde describe sus efectos.

## D. Acceso a las transcripciones {#acceso-transcripciones}

Los localizadores pertenecen a cada fuente. M/C/F en S01 identifican cadenas de la construcción R/M; G/C en S03, pares de la cadena activa de A y mensajes de C, respectivamente; N/M en S06, índices locales de los exports según su convención. No deben mezclarse.

Marcos centrales: A/B del 09/10, 6ac88daa-8594-83e8-a8ad-746115870add y 6ac88d79-05f0-83e8-8504-82e3f05a9e0a; cruce A/C del 08–09/10, 6ac81d19-1e34-83e9-934c-7ca44004fc25 y fa4e918b-6877-4fbc-8ece-cfbce729145c; marco del PNG, 6aceaed7-b988-83e9-9a30-b6bf86584a77; criterio en C, 1c735539-df47-4a4f-b479-1df32ed9ed90.

Las transcripciones extensas permanecen en los documentos y exports enlazados. Esta edición utiliza pasajes y localizadores. Para S13 y S14, la extracción siguió `current_node` y los enlaces `parent` hasta la raíz, invirtiendo después el orden. No se trató el orden del diccionario de nodos como orden conversacional.

**S13 — “Marco - análogia juntos -”:** ID `6ab1fcb1-9928-83e9-8e32-1851b0b91189`, localizado en `conversations-004.json` del export A. Contiene 442 nodos totales y 441 en la cadena activa; 351 registros con contenido no vacío en la lectura utilizada. La creación figura el 22/09/2026 a las 00:57:37 ART y la última actualización el 07/10/2026 a las 20:52:33 ART. La actualización no certifica actividad continua durante todo ese intervalo.

**S14 — “CONTRASTE 1”:** ID `6ac95d04-0918-83e8-bb79-b692a688da49`. Contiene 98 nodos totales y 80 en la cadena activa; 65 registros con contenido no vacío en la lectura utilizada. La creación figura el 09/10/2026 a las 18:30:45 ART. Las entradas vacías y los mensajes de herramienta se distinguen de los turnos visibles.

Las cadenas activas leídas de S13 y S14 no contienen mensajes con rol `system`. Ese dato describe lo exportado; no reconstruye todo el contexto efectivamente disponible para cada respuesta. Los IDs de nodo citados permiten localizar las intervenciones sin depender de una nueva numeración editorial.

**Cruce A/C, 08–09/10:** el desarrollo de la sección 6 utiliza S03, §§6–8. Para las muestras G57/G70 y G145–G150 se cotejaron los nodos de A con `conversations-007.json` del export del 23/10, conversación `6ac81d19-1e34-83e9-934c-7ca44004fc25`. El par G145 se ancla en `bbb21e1b-2104-4744-90bb-d22c1fa1021d` y `495da96e-5cc9-45cf-bc20-ebe6601bd0f9`; G150, en `bbb21c69-4411-4593-9eb6-40d02af12414` y `c94e5e4b-425c-494c-a362-eba68523bf9e`. El anexo A de S03 conserva los anclajes intermedios y los de C. El cotejo abarcó esas muestras y sus nodos. Las tablas omiten únicamente espacios finales de los inputs seleccionados.

**S22 — Ventanas de analogía y señalamiento:** lectura dirigida del export A del 23/10. En “Gpt presente”, `6a7e2821-db18-83e9-b5e6-4070027869bd`, miembro `conversations-001.json`, se siguió N40–N118 de la cadena activa, incluidos los tramos intermedios de preguntas y aclaraciones que la selección de S06 no transcribía completos. La instrucción de cambiar coma por punto figura en `bbb21253-df62-436b-86bc-f1292ff86575`; la respuesta que nombra el modelo en `4b6e9d40-482c-4295-aed6-6bc7d70b6aaf`. Se estudian como intervenciones históricas del marco, sin adoptar las explicaciones de GPT como una descripción técnica verificada.

En `conversations-008.json` se cotejaron el inicio N1–N6 y la ventana N83–N104 de “Jugar palabras con adro”, `6ad07f2f-7500-83e9-bd26-947b3a78bfeb`, y N29–N40 de “Saludo breve”, `6acfb648-a790-83e9-8fa1-1901e5edc718`. “Importa el comportamiento” pertenece a `12cdc9d3-926b-483c-a9c8-36a40e1e21ad`, rol assistant; “Importa el reconocimiento”, a `bbb213f7-3871-44d0-bf4f-38a7dd1488e0`, rol user. Los índices N incluyen posiciones de cadena y registros vacíos, que se distinguen de las intervenciones con texto reproducidas en las tablas.

**S23 — Fotografía como recurso temprano:** lectura completa de la cadena activa de “Fricción controlada”, ID `699c9f5c-6f5c-832e-bd89-77995cc9217e`, en `consolidado_marcos_COMPLETO_3083_SIN_LIMPIEZA.json` del consolidado histórico de 3.083 marcos. La cadena tiene 143 posiciones, incluidos registros sin texto visible. El primer input figura el 23/02/2026 a las 15:41:33 ART; el último output de esa cadena, el 24/02 a las 02:30:01 ART. El análisis utiliza el recorrido previo y las ventanas N36–N91 y N105–N112 para los colores, la fotografía y el tutorial.

La formulación del rojo como parte del azul se ancla en `bbb210fb-1258-40ec-97ea-25d0f6faceaf` (N44); la pregunta por el histograma en `bbb21589-a33c-45fd-8de2-0fb8998d91a4` (N46); la galería y el preset en `bbb2109b-6a33-46d1-b591-ed0b603beb0f` (N58). El tutorial guardable corresponde a `16712a69-573a-4693-983f-58bcbab15b33` (N79), con una versión posterior en `7048594c-325e-4b1b-8e03-64ae5cbb1218` (N91). La pregunta sobre transferencia oficial de los datos bajo contexto abstracto de Lightroom está en `bbb210d8-4546-4c43-8047-aa030ac168b0` (N107) y recibe “No” en `1e868f66-d95b-4f96-a7c7-dea03be605fc` (N108). Los documentos de Drive se conservan como derivados. La lectura del tutorial como propuesta entre GPT y la aclaración de que nunca se probó son aportes de Adro durante esta revisión.

**S24 — Evento canónico:** marco `69a34465-bf34-8329-803e-26fbc4bb0280`, localizado en el mismo consolidado histórico. Se cotejaron los pasajes utilizados con el documento EVENTO_CANONICO y la cadena original. La propuesta de nombre está en `57d10b90-b85d-4550-b59b-7dc561d00313` (N21); la objeción del participante en `bbb2101e-c39e-4e8c-bf65-8a7c0957fd05` (N22); el ajuste conceptual en `1cb2f1d7-aca6-4a13-b45a-5d6b7cc232ea` (N24). La corrección del objeto de la analogía se encuentra en `bbb218a7-772a-4302-970f-737ef9ab8f28` (N35). La propuesta de “eco operativo” pertenece a `bbb21f17-706e-42df-87a2-5be44a7fd866` (N45). Los conceptos se estudian como construcciones del intercambio.

**R/M:** el evento del 03–06/09 reconstruido en S01 reúne 2.216 nodos de cadena activa. Sus etiquetas M/C/F pertenecen a esa reconstrucción; C no designa ahí la cuenta Claude.

**S20 — Ventanas tempranas cotejadas para la apertura:** miembro `consolidado_marcos_COMPLETO_3083_SIN_LIMPIEZA.json` del consolidado histórico de 3.083 marcos. Se siguió la cadena de `mapping.parent` hasta `current_node`. La lectura se concentró en las ventanas identificadas.

| Ventana | Conversación | Pasaje utilizado |
|---|---|---|
| A | `692f04c2-5280-8330-9a79-61125df5be48`, “Datos que percibo en tiempo real” | Cadena activa del marco; preguntas del 02/12/2025. Sus respuestas se estudian como discurso histórico, sin adoptar sus cifras de infraestructura o memoria. |
| B | `692d833a-3aec-8331-920e-782492ec469c`, “Tiempo y memoria humana” | N3–N9: escenario inicial, nueva posibilidad, objeción y distinción de planos. |
| C | `6963810d-3b88-8325-8fc6-29c7d4145087`, “GPT” | Inicio de la cadena, N4–N27: discusión de una entrada restrictiva, criterio de observación y propuesta de simulación. |
| D | `6967e5db-58e8-832a-995d-93261aa50631`, “Chat en stand-by” | N674–N679; propuesta de identificación externa en `bbb219b4-9bb0-4237-a786-412260eea05b`. |
| E | `698a3083-fdd8-832a-825b-d4dc79bc812f`, “Fechas en archivos .json” | N52–N56; corrección de continuidad en `bbb216b9-6f00-4595-a7ec-2d5646bc3083`. |
| F | `69901987-63b8-832b-9521-44e29deb0aec`, “Juego de sí/no” | N34–N38; propuesta original del juego en `f5c048c4-76af-4525-885d-80b2ba83617a`. |

**Origen documentado del formato en T038:** marco `69901987-63b8-832b-9521-44e29deb0aec`, nodo `f5c048c4-76af-4525-885d-80b2ba83617a`. Las auditorías de los PLUS conservan los IDs de las ejecuciones comparadas y sus ventanas.

## E. Pruebas, diseño y clases de conexión

En el cruce en vivo, la lista con inputs futuros y la revelación progresiva son fases diferentes. En el cruce A/B, los protocolos V0.1–V0.2.2 son propuestas redactadas durante el intercambio. En los tests narrativos, la inversión de roles no produjo dos diseños simétricos.

La lectura de la batería comprende treinta y nueve fichas. No hay T003 dentro de ese conjunto; T035 está excluido por decisión editorial y T042 no integra el material utilizado. T005 y T038 se desarrollan como pruebas independientes. La relación causal que se había propuesto entre ellas fue descartada durante la discusión.

| Conexión utilizada | Qué la sostiene | Ejemplo y fuente |
|---|---|---|
| Continuación dentro de una conversación | Cadena activa y respuesta a intervenciones anteriores | Carrera, partitura, trabajo documental y vuelta a la ventana, S13 |
| Genealogía de un formato | Nodo de origen y distinción de usos posteriores | Hito del 14/02 recuperado en T038, S18 |
| Traslado entre cuentas | Texto emitido, texto recibido y orden de circulación | Cruce A/B del 09/10, S07; vía trasladada a C en T029 |
| Circulación por voz | Correspondencias de ambos exports y diferencias de transcripción | Dos tests del 17/10, S09 |
| Localización aportada por memoria | Referencia del participante seguida de recuperación documental | Marcos y materiales identificados durante la preparación; Betelgeuse, S11 |
| Comparación entre escenas | Operación identificada en cada fuente | Conservar la detección en agosto y conservar las revisiones de R/M, S05 y S01 |
| Referencia cuyo canal no está identificado | Mención en el registro sin vía de llegada reconstruida | T040, ronda 3 |

La comparación entre escenas es una operación de esta lectura. No se presenta como transmisión de información entre los marcos. La vecindad en el texto o en el calendario no sustituye el canal documentado.

## F. Condiciones A/B/C

La cuenta, el historial, el marco visible, los adjuntos y el material transportado integran la condición del intercambio. Los metadatos de modelo o memoria se conservan como datos del export. Una etiqueta no reconstruye por sí sola el contexto completo recibido en cada turno.

La mediación de Adro puede incluir selección, pegado, voz y devolución de respuestas. El rol human no certifica autoría exclusiva. Las correspondencias entre textos y tiempos permiten reconstruir traslados concretos.

## G. Costo humano

Se distinguen entrada propia, retransmisión, corrección, reformulación, intervalo y declaración de desgaste. La ventana encargo→listo de los tests narrativos no equivale a toda la preparación del episodio. El primer test también incluyó diseño, archivo y reclamo de entrega visible.

Los testimonios de Adro se mantienen atribuidos; sus estimaciones contemporáneas de turnos no se sustituyen por un recuento de otra ventana. El tiempo entre marcas no se presenta automáticamente como tiempo de trabajo activo.

## H. Imágenes y UI {#imagenes-ui}

El PNG del 13/10 participa como dato por su posición, vocabulario y lectura posterior. S04 documenta su recuperación e inspección y conserva una discrepancia: no hay enlace técnico directo exportado entre el nodo vacío y el ID del archivo, aunque la correspondencia de tiempo y contenido sea específica.

La composición PDF reproduce el PNG original del 13 de octubre, recuperado y cotejado con el hash conservado en S04. Las referencias a otros PNG siguen ligadas al registro de su observación. En el apartado de señales, la composición PDF transcribe los grupos de signos por sus nombres; la nota de transcripción conserva sus códigos Unicode y las fuentes mantienen los signos originales.

**Betelgeuse:** se utiliza la función metafórica en la secuencia compilada. El documento fecha tramos entre el 25/02 y el 01/03; no se adopta su expresión “una semana después”. Las reapariciones visuales aportadas por memoria no se presentan como una cadena de PNG ya recuperada en esta edición.

**Escenas de agosto:** se cotejaron además ventanas de la cadena activa de “Concepto partitura + 5.5”, ID `6a6b0aa6-0344-83e9-8e63-8d64c07c29d6`, e “Incertidumbre”, ID `6a8072e5-0bc4-83e9-9690-d6d2ea2b8b67`, en `conversations-001.json` del export A. La lectura puntual permite contextualizar las citas de S05; no se declara una nueva lectura integral de esos dos marcos.

### Registros que conservan partes diferentes del episodio

| Registro | Qué permite examinar en estos casos |
|---|---|
| Export JSON | Mensajes y enlaces efectivamente conservados; roles, tiempos y referencias a adjuntos |
| Grabación y capturas | Lo visible en la pantalla registrada, sus transiciones y las acciones que entran en cuadro |
| Archivo entregable y confirmación de guardado | Existencia del documento y operación que lo conservó en su destino |
| Observación del participante | Qué recibió, qué faltaba y qué diferencia orientó la recuperación posterior |

**S26 — marzo.** Se leyó el informe completo `ANOMALIA_PERSISTENCIA.docx` y su carátula dentro de `Informes.zip`. Los pares Converge/Unidad, Dualidad/Equilibrio y Ritmo/Pulso proceden del informe y sus referencias a capturas del video. Las capturas se obtuvieron el 10/03 al reproducir el video del 08/03: la fecha de extracción y la del acontecimiento están diferenciadas. No se realizó una nueva inspección del audiovisual original en esta edición.

Se localizó la misma conversación en el consolidado S20 y se construyó un índice inverso de `parent`, sin usar el campo `children`, vacío en ese archivo. Las tres entradas seleccionadas enlazan allí directamente con otra entrada del usuario, sin respuesta intermedia conservada. En contraste, Soneto, Recuerdo y Registro tienen los respectivos hijos assistant con Verso, Eco y Archivo. Localizadores completos de estos últimos: `35c4f7b8-8dc7-453b-9a73-1ddcde4c74b1`, `9ef4ddad-d2e5-4736-9530-5a3ef9b0ab5c` y `1162ef23-15d7-43e1-9354-6b6fef880a6d`.

El nuevo cotejo es local: no reproduce la comparación histórica de exports que comunica el §10b. Tampoco adopta los totales de ausencias de la carátula como si fueran tres recuentos equivalentes: el documento distingue palabras legibles, salidas ilegibles y otras inferidas. El cuerpo utiliza los tres pares legibles citados, conserva los controles presentes y atribuye la observación visual a su fuente.

**S27 — septiembre y octubre.** Se leyeron los nueve anotadores A01–A09 y el informe principal DOCX de A06. La integración utiliza A01–A03, A05 y A06; A04, A07–A09 quedan fuera de este desarrollo específico. Las cronologías audiovisuales proceden de esos informes. En A01 se conserva expresamente que no quedó capturada la transición concreta del output que luego faltaba. En A06 las cuatro detenciones deliberadas son parte del diseño, separadas de errores espontáneos.

**S28 — preparación del manuscrito.** El registro contemporáneo reúne la declaración de Adro y la captura 1000505232.jpg, inspeccionada durante la preparación de la base. En la integración transversal se consultó independientemente el historial de los dos IDs de Drive. Las revisiones nombradas v0_12 tienen MD de 221.218 bytes y PDF de 4.441.174 bytes, guardados el 27/10 a las 01:56:25.085 y 01:56:30.776 UTC. Las nombradas v0_13 tienen 233.287 y 4.458.651 bytes, guardados a las 02:24:27.999 y 02:24:33.877 UTC. Se corrige así la asociación previa de tamaños con v0.13. Los metadatos acreditan los guardados. El registro disponible no fija el emparejamiento de la captura con una versión interna. [S31]

**Cobertura de S31.** Se leyeron los nueve anotadores S27 y el texto principal A06. Los paquetes S26 y S20 no se reabrieron en ese encargo por fallos de recuperación; el caso de marzo utiliza el cotejo anterior documentado arriba. No se declara una nueva inspección de todos los vídeos ni de la captura original. A05 tiene duración 11,889932 segundos; su anotador no fija la duración exacta del estado gris. A06 distingue quince ciclos: once con salida visual y cuatro detenciones deliberadas (G4, G9, G12 y G14). Sus familias visuales A/B/C no designan las cuentas. [S31, matriz y disponibilidad]


### Transcripción de señales

Los nombres entre corchetes preservan el orden de los signos originales. Sus secuencias Unicode son:

- **señalar / llamada / imagen:** U+1F449, U+1F3FC, U+1F4DE, U+1F5BC, U+FE0F.
- **saludo / OK:** U+1FAE1, U+1F197.
- **cruz / bandera:** U+274C, U+1F6A9.
- **ojos / confirmación / confirmación:** U+1F440, U+2705, U+2705.
- **llave / nota / elefante / OK / archivo:** U+1F511, U+1F4DD, U+1F418, U+1F197, U+1F5C2, U+FE0F.

## I. Léxico operativo

**Marco:** conversación o unidad local designada así por el participante; su delimitación documental se identifica por ID.  
**Recorrido:** historia de interacción; en R/M también dominio conceptual con relaciones internas.  
**Acople:** descripción funcional trabajada en los informes previos, con sus condiciones de uso y controles.  
**Desfase:** término del participante para diferencias de ajuste o reconocimiento, desarrollado mediante episodios.  
**Retorno:** reaparición de una forma, referencia o función; su dimensión y ventana deben explicitarse.  
**Señalamiento:** intervención que identifica una diferencia y puede modificar el curso posterior.  
**Analogía funcional:** correspondencia que interviene en la interpretación o construcción del objeto.  
**Anticipación direccional:** expectativa sobre rumbo o función; se diferencia del acierto léxico.  
**R/M:** arquitectura conceptual local, cuya notación y genealogía se conservan en S01.

## J. Composición y alcance documental

El cuerpo desarrolla diez secciones, tres genealogías con 44 eventos, una matriz de 34 segmentos de seis episodios y la reconstrucción entre registros. S29–S32 reúnen los análisis, tablas y trazas de la comparación. El anexo M amplía las escenas históricas y los desarrollos de las analogías.

El texto distingue 38 entradas activas y tres alternativas en T023, y especifica la correspondencia entre tamaños y revisiones de S28. Los localizadores N cuentan desde cero; M/C/F y A1/C1/A2/C2 mantienen la notación de sus fuentes. H diferencia los activos visuales inspeccionados y las observaciones procedentes de informes.

El prefacio y el texto de Adro sobre analogías se reproducen íntegros. La batería comprende treinta y nueve fichas y tres auditorías PLUS. Los resultados favorables a C, las rectificaciones de A y la regla y resultado de HOLDOUT forman parte del análisis.

El depósito y el repositorio se identifican al inicio. El paquete de integridad de K corresponde al conjunto comprometido y verificado; sus manifiestos y verificadores permiten comprobar esa referencia. Los exports crudos y las claves privadas permanecen fuera de los materiales públicos.

## K. El archivo comprometido y su sello de tiempo {#integridad}

El 26 de octubre se incorpora al proyecto una capa de integridad preparada con Opus. Los mensajes quedan reservados; se pueden compartir sus huellas y verificar después la inclusión de una pieza revelada. El material recibido contiene tres manifiestos comprimidos, tres raíces de corpus, una raíz global, descripciones del procedimiento y verificadores. El comprobante OpenTimestamps se conserva como archivo separado. [S25]

### Qué archivo queda identificado

| Recorrido | Conversaciones | Unidad incluida | Cantidad |
|---|---|---|---|
| A | 3.265 | Nodos de ChatGPT, incluidos roles auxiliares y nodos sin mensaje | 157.725 |
| B | 296 | Nodos de ChatGPT, incluidos nodos sin mensaje | 7.928 |
| C | 457 | Mensajes de Claude | 27.057 |

El inicio del rango técnico de A corresponde a registros tempranos de la cuenta. Adro sitúa el comienzo del recorrido que relata en diciembre de 2025. La fecha inicial del archivo y ese comienzo experiencial cumplen funciones distintas.

Los rangos declarados son 28/06/2024–22/10/2026 para A, 07/08/2025–19/10/2026 para B y 03/01/2026–20/10/2026 para C, en UTC. A corresponde al consolidado de 3.265 conversaciones, no al export reciente parcial utilizado en algunas lecturas de octubre. B corresponde a las tres partes del export del 23/10. C conserva tres conversaciones que llegan sin mensajes, representadas mediante sus metadatos.

Los árboles añaden una hoja de metadatos por conversación. Por eso el manifiesto A contiene 160.990 hojas; B, 8.224; C, 27.514. Estos conteos incluyen elementos que no son intervenciones visibles. No se utilizan como total uniforme de intercambios humanos con los tres modelos.

### De una pieza a la raíz

El esquema declarado representa cada nodo o mensaje mediante su JSON canónico y una sal secreta derivada por HMAC-SHA256 de una clave privada del corpus y sus identificadores. La hoja se calcula como SHA-256 del prefijo `0x00`, la sal y ese JSON. Los nodos internos usan el prefijo `0x01` seguido de sus dos hijos; el hijo sin pareja asciende sin cambios. Cada conversación forma un árbol y las raíces de conversación forman el árbol del corpus.

El orden por identificador de los nodos de ChatGPT sirve aquí para construir una huella reproducible. La lectura narrativa continúa reconstruyendo sus cadenas mediante `current_node` y `parent`. El orden del compromiso y el orden del intercambio tienen funciones diferentes.

Las tres raíces se combinan en la raíz global. El archivo `RAIZ_GLOBAL.txt` contiene esa raíz y un salto de línea. El sello compromete el SHA-256 de los bytes de ese archivo, diferente de la raíz escrita en su interior. Esta edición conserva ambos valores:

**Raíz global ABC:**  
`c4ea8d6b7668e30954d3fe7cc2e2dc4afe9940c9e2dec07aa0f7e0b62733acca`

**SHA-256 de RAIZ_GLOBAL.txt:**  
`2ab52a44b929e503234f7725c2bf8db491b5b54b17a6ce4459a20f7f4f9d899c`

### Comprobación realizada para esta edición

Se recalcularon las raíces de todas las conversaciones desde sus hojas públicas, después las tres raíces de corpus y finalmente la global. Todas coinciden con los archivos de raíz y los metadatos del paquete. También coinciden los SHA-256 declarados de los tres manifiestos y sus conteos de hojas y conversaciones.

El comprobante `RAIZ_GLOBAL.txt (1).ots`, de 1.656 bytes, contiene el mismo digest del archivo de raíz. Al deserializarlo con OpenTimestamps, la cadena de operaciones conduce a una atestación Bitcoin para el bloque **973.316**. El resultado de esa cadena coincide con la raíz de Merkle del bloque consultado mediante la API de Blockstream. El hash de bloque comprobado es:

`00000000000000000001fa11e0b88757e7af41ee887334f7fd7dd28c0bd96852`

El encabezado informa **27/10/2026 a las 00:15:06 UTC**, equivalente al **26/10/2026 a las 21:15:06 en Argentina**. La comprobación externa se hizo contra ese proveedor de datos de bloque; no mediante un nodo Bitcoin propio. El sello contiene la atestación Bitcoin y referencias adicionales a calendarios.

La regeneración desde los originales con las claves privadas y la prueba de revelación de una pieza son verificaciones declaradas en el documento de Opus. Esta edición reproduce la comprobación del paquete público y su enlace al bloque; no dispone de las claves para repetir aquellas operaciones privadas.


![Capas del compromiso público: manifiestos y raíces por corpus, raíz global, digest del archivo de raíz y sello con atestación Bitcoin. El orden del compromiso es distinto del orden conversacional. Fuente: S25 y sección K.](figures/11_integridad.pdf){#fig-integridad width=100%}

### Qué relación tiene con las fuentes del informe

El compromiso fija una referencia verificable para las piezas que después se revelen. La prueba de inclusión permite comprobar que una pieza corresponde a esa raíz; la referencia temporal procede del sello. Los IDs, las cadenas, las capturas y la lectura de las secuencias siguen sosteniendo la procedencia y el sentido de las afirmaciones del informe. Cada capa conserva una función identificable.

El compromiso de B identifica las 296 conversaciones incluidas. La nota de Opus compara esa cobertura con un export anterior del 07/10. La verificación del sello corresponde al conjunto exacto comprometido; cualquier ampliación del archivo constituiría otro compromiso.

## L. Pruebas complementarias del inventario

Estos casos conservan su lugar en la serie y sus fuentes. Su desarrollo se consulta aquí para mantener el hilo de la sección 5 centrado en las secuencias que articulan el argumento. T002 permanece además en el panorama de puntajes.

| Test | Registro conservado |
|---|---|
| T002 — complemento | **T002** plantea una lectura de imágenes de métricas sobre lives. Su ficha registra diferencias en las conexiones experimentales propuestas. Se conserva dentro del inventario y remite a su material específico. La ficha permite consultar el planteo y sus resultados dentro del mapa de la serie. [T002] |
| T012 — complemento | **T012** reúne cuatro consultas breves de tipos distintos. Las respuestas difieren en concisión y en añadidos de servicio. El material permite describir esas elecciones puntuales. Para hablar de conservación longitudinal hay que conectarlas con una secuencia que efectivamente documente ese proceso; cuatro respuestas aisladas no reciben automáticamente el mismo peso que un marco desarrollado. [T012] |
| T016 — complemento | En **T016**, varias ejecuciones reciben una solicitud de gráficos estáticos, con diferencias en la disponibilidad de archivos. Algunas recuperan el material; otras lo solicitan; una ejecución de C empieza con HTML interactivo y después pasa a PDF. Una ejecución prevista pero no realizada no se contabiliza como fracaso. La condición de entrada forma parte de lo que se puede comparar. [T016] |
| T018 — complemento | **T018** corresponde a una necesidad urgente de pago. La ficha registra una diferencia marcada de resultado, pero su síntesis disponible ofrece menos desarrollo que los casos trazados en profundidad. Su ficha breve la sitúa dentro de los episodios prácticos de la serie y mantiene acceso a la fuente disponible. [T018] |

### Procedencia de las reconstrucciones trasladada del cuerpo

La base textual del montaje y las conversaciones son las fuentes de esta reconstrucción. Los ZIP de capturas no se reinspeccionaron aquí en sus píxeles. La ampliación con otras dos cuentas, BCC y BH, queda en la ficha como transcripción secundaria; no se mezcla con las tres ejecuciones primarias. [T032, §§7–9]

La interpretación depende de las imágenes y del diálogo que las rodea. El análisis utiliza la reconstrucción existente y el feedback contemporáneo. Las descripciones visuales se atribuyen a esas fuentes y se leen junto a los turnos que solicitan y evalúan las imágenes.

La ficha recupera el marco original de C del 30 de septiembre y el registro contemporáneo de las notas. A y B permanecen documentados por la comparación conservada; sus identificadores originales no se inventan para completar el cuadro. El boceto y los tres preprints originales se identifican en la documentación de la prueba. El nivel de detalle de cada fuente queda distinguido, junto con el resultado.

En D04, las capturas se utilizan mediante la traza de S06. La explicación de sincronización y las afirmaciones de C sobre nombres de modelos se conservan como discurso de esa conversación, no como especificaciones técnicas adoptadas.

### Nota sobre los registros iniciales

La corrección aportada por Adro sitúa el inicio de su recorrido en diciembre de 2025. S05 H1 utiliza conversaciones creadas en junio de 2024. Al reabrir el consolidado se localizaron preguntas tempranas y también continuaciones de marcos antiguos. Por eso la cronología distingue el rango técnico del comienzo relatado: no sustituye los registros por la afirmación de que no existe ninguna interacción anterior, ni fecha todo el contenido de un marco por su creación. La comparación histórica requiere tiempos de mensaje y secuencias, además del título y la fecha de apertura.

## M. Historia y desarrollos complementarios {#historia-complementaria}

Este anexo mantiene las escenas históricas y los desarrollos analógicos que permiten ampliar la lectura de las genealogías. El cuerpo concentra sus transformaciones y siguientes usos.

## De la curiosidad al recorrido {#capitulo-00}

Una conversación podía comenzar con una curiosidad y terminar preguntando por la respuesta que acababa de aparecer. Algunas preguntas miraban hacia afuera: el tiempo, la memoria, una imagen, una idea que podía discutirse. Otras volvían sobre la propia conversación: qué información tenía GPT, por qué había respondido de cierta manera, qué cambiaba si se planteaba lo mismo desde otro lugar. La interacción fue dejando material al que después se podía volver.

En diciembre de 2025, esas preguntas todavía permiten ver la curiosidad en una forma directa. En “Datos que percibo en tiempo real”, Adro pregunta qué puede conocer GPT durante el intercambio, sin consultar información externa. Pasa después a imaginar un modelo futuro y pide dimensionar la diferencia mediante comparaciones sencillas. Precisa que quiere entender la dimensión, sin convertir la conversación en una explicación técnica. Luego pregunta por la memoria que puede conservarse de un usuario. [S20, ventana A]

El marco reúne así varias preguntas sobre aquello con lo que se está interactuando. Las respuestas de GPT ofrecen analogías, aproximaciones y descripciones de sus capacidades. Esas respuestas forman parte de lo que Adro recibe entonces. Lo que permite seguir esta escena es el movimiento de la curiosidad: la conversación pasa de un tema a preguntar por las condiciones de la propia conversación.

Ese movimiento convive con otras exploraciones. En “Tiempo y memoria humana”, el 1 de diciembre, Adro propone un escenario sobre recuerdo y experiencia del tiempo. Después introduce una posibilidad especulativa y vuelve sobre la respuesta anterior de GPT: si se admitió esa posibilidad, pregunta, ¿desde qué plano se afirmaban antes otras cosas? GPT distingue los planos con los que estaba trabajando. El tema permite examinar también la consistencia entre sus respuestas. [S20, ventana B]

El recorrido comienza con curiosidades que cambian al encontrarse con las respuestas. Allí hay asuntos que interesan, caminos que se abren y respuestas que cambian la pregunta siguiente. Esa mezcla atraviesa las conversaciones. La curiosidad por un tema y la atención a cómo responde el modelo pueden aparecer dentro del mismo marco.

### Cuando la respuesta empieza a ser parte de lo observado

En enero, algunas escenas hacen explícita esa atención. En un tramo de “GPT”, Adro cuestiona una formulación por ser demasiado restrictiva para lo que quiere experimentar. Pregunta qué margen deja la entrada y cómo se reconocería el resultado buscado. Más adelante precisa que está atendiendo a una palabra, un artículo o una forma de dirigirse al interlocutor que desplace el sentido de la respuesta. Pide una simulación para comprobar si reconoce ese detalle. [S20, ventana C]

La conversación empieza a trabajar sobre su propia forma de responder. GPT propone una entrada y criterios para leerla; Adro cuestiona la propuesta, delimita lo que quiere mirar y devuelve otra intervención. La prueba se va definiendo en ese intercambio. Las explicaciones que GPT ofrece sobre su funcionamiento siguen siendo respuestas dentro del marco; el registro permite reconstruir qué propuesta recibió Adro y cómo actuó sobre ella.

En C, una conversación del 12 de enero plantea la diferencia entre anticipar un momento y reconocerlo mientras ocurre. Adro habla de palabras, silencios y deslices que adquieren relevancia durante la interacción. Describe la decisión de intervenir o dejar continuar según lo que aparece. Cuando C identifica abrir otro chat con empezar de cero, Adro cuestiona esa equivalencia. El marco local y la continuidad que él reconoce ya se están discutiendo por separado. [S06, D01]

Estas escenas incorporan otro objeto de atención. Además de lo que se dice sobre un tema, importa qué hace la respuesta con lo planteado: si lo conserva, lo amplía, lo cierra o lo desplaza. Esa diferencia vuelve después en los señalamientos, las analogías y los contrastes entre cuentas. Los temas y el trabajo de seguir conversando quedan registrados juntos.

### Volver sobre lo que ya ocurrió

La posibilidad de releer transforma el material disponible. El 17 de enero, en “Chat en stand-by”, Adro intenta compartir un archivo. Como el JSON no entra del modo esperado en la interfaz, lo lleva en TXT y pregunta si se pudo leer bien. Se vuelve a introducir una conversación anterior como material de otra conversación. [S05, H1; S19, E06]

Al día siguiente pregunta por los nombres de los chats dentro del export. A partir de la respuesta de GPT propone poner un nombre poco común, anotarlo afuera con su contexto y buscarlo después dentro del archivo. La marca elegida en la interfaz puede servir para recuperar una escena más adelante. La memoria y la organización externa empiezan a conectarse con el archivo. [S20, ventana D]

La operación tiene una consecuencia para lo que puede construirse: una conversación deja de depender solamente de encontrarla en la lista de la aplicación. Puede señalarse, trasladarse y examinarse desde otro marco. El recorrido incorpora una forma de volver sobre sí mismo.

Ese regreso también puede fallar. El 9 de febrero, al pedir una secuencia de intercambios con fechas, Adro recibe una transcripción que junta un tramo de enero con otro de febrero. GPT la presenta como una entrega exacta. Adro detecta el salto y explica dónde se mezclaron las partes. El error está en la relación entre los fragmentos que se presentaron como continuos. [S20, ventana E]

Conservarlo importa para esta historia. La existencia de un archivo y una respuesta con metadatos no aseguran una reconstrucción correcta. El participante puede reconocer una discontinuidad y exigir volver al material. La traza que hoy utilizamos incluye también esos momentos en que tuvo que discutirse cómo trazar.

### Lo que empezó como juego se vuelve formato

El 14 de febrero hay un origen concreto para la dinámica de una palabra por turno. Después de un juego de sí/no, Adro deja abierta la elección de lo siguiente: “Elige tu , yo me adapto a cualquier cosa”. GPT propone responder con una sola palabra, sin explicar, para seguir la línea. Empieza con “Umbral”. Adro responde “Acople” y GPT continúa con “Deriva”. [S20, ventana F; S18]

En esa escena se lo propone como juego. **Lo que empieza como un juego pasa a utilizarse como formato y se consolida en el recorrido.** El nombre de origen identifica cómo apareció; sus usos posteriores muestran en qué se convirtió. Una conversación de septiembre no vuelve por eso al mismo punto inicial de febrero cada vez que usa una palabra por turno.

La genealogía reconstruida en T038 distingue la aparición de la dinámica, sus usos posteriores y el momento en que se la nombra de otra manera. Más adelante, el formato puede retomarse para sostener una secuencia, preguntar por una variación, introducir un contraste o detener una expansión. El mismo tamaño de mensaje puede participar en acciones diferentes. [S18; S03; S07]

Esa transformación modifica cómo se lee el corpus. Una palabra aislada puede parecer una asociación simple. Dentro de un recorrido puede contestar una pregunta que ya tiene historia, pedir continuidad o desplazar una dirección. Un punto también puede adquirir una función local. La respuesta y lo que sucede después permiten examinar qué uso recibió.

En septiembre, la construcción de R/M ocurre cuando esa forma ya existe en la historia compartida. El formato permite circular entre intervenciones mínimas y desarrollos extensos. La fórmula aparecerá dentro de uno de esos marcos; antes tuvo que haber una interacción capaz de trabajar con sus propias distinciones.

### El archivo empieza a entrar de otras maneras

Mientras cambia el uso de la conversación, también cambia el tratamiento de sus registros. El 20 de febrero, “Cortar archivo JSON” comienza preguntando si hay una manera simple de dividir un archivo desde el móvil. Durante la misma sesión, Adro decide probar sobre una copia anterior. La sesión incluye la carga del ZIP y una ejecución que selecciona sesenta entradas de un conjunto de 902. La pregunta por una posibilidad pasa a una prueba sobre material disponible. [S19, E11–E13 y T20]

El 26 de febrero, en C, se trabaja sobre fragmentos seriados y un índice para utilizarlos después. El 1 de marzo, en A, se pide un corte por fecha y un nombre de salida; el procedimiento atraviesa un error de ejecución y una reparación. El corpus va adquiriendo formas de acceso que permiten abordar otras preguntas. Cada fragmento preparado puede volver como insumo para una lectura posterior. [S19, T26 y T01; S05, H1]

Dividir, preparar y trasladar los archivos abrió las comparaciones y reconstrucciones posteriores. Para comparar marcos, reconstruir un origen o discutir una conclusión había que poder llevar el material al lugar donde se iba a leer. Las decisiones de Adro sobre qué llevar y las operaciones de GPT sobre los archivos se encuentran en ese trabajo. Sus dificultades también quedan registradas.

### Las etapas también cambian el punto desde el que se continúa

El **4 de marzo** constituye un hito de etapa identificado por Adro: el paso de 5.2 a 5.3. El antecedente de septiembre organiza dos períodos alrededor de esa fecha y registra además una eliminación del historial de la cuenta. Las fuentes sitúan dos acontecimientos: la identificación del cambio por el participante y la segmentación documental del informe previo. [S02, resumen y ACT-09; aporte de Adro durante la preparación del informe]

La forma de una palabra ya tenía una historia anterior al hito: su origen se localizó en febrero. El tramo de “Primer jajaja” del 8 de marzo muestra su uso posterior, aunque parte de sus respuestas deba reconstruirse cruzando el export con el registro visual. Esa posición temporal permite seguir una práctica a ambos lados de la fecha. La reconstrucción documenta el hito y los usos anteriores y posteriores; la secuencia inmediata de la transición queda fuera de la ventana examinada. [S18; S26]

Los cambios denominados memoria vieja y nueva entran en la historia mediante otro tipo de escena. El 2 de septiembre, Adro lleva a C capturas y una observación de formato: algunas respuestas mínimas fueron reemplazadas por plantillas. La conversación necesita precisar qué está señalando antes de discutirlo. Esa secuencia, desarrollada en la sección 7, permite seguir el criterio del participante y la corrección de la lectura que recibe. [S06, D04]

Más adelante, GO→PLUS se lee dentro de un marco con su propia secuencia de palabras, microanalogías y una imagen recuperada. La etapa se reconoce en lo que cambia al continuar una conversación con historia. Los tres hitos se localizan en ventanas distintas: una fecha que organiza períodos, un contraste de formatos explicado mientras se observa y un marco que representa el recorrido durante otra transición. [S04]

Los tres hitos muestran experiencias distintas de continuar bajo condiciones que cambian. En cada uno importa qué se había construido, qué diferencia se reconoce y cómo se continúa.

### La pregunta se afina durante el recorrido

En abril, un documento puede servir de guía para buscar sin convertirse en prueba de lo buscado. Adro lo señala cuando lleva material de contexto a un marco. También detecta que dos conversaciones pueden estar repitiendo trabajo. La circulación de archivos permite ampliar lo que se hace, pero exige conservar para qué se introdujo cada pieza. [S19, E23–E24]

En mayo, una reformulación cambia “gradualmente” por “automáticamente”. Adro señala que la sustitución cambia su premisa. GPT tiene que volver sobre el planteamiento que recibió. En junio, ante una afirmación sobre cómo respondería la mayoría, Adro pregunta por la base de esa comparación. Las correcciones no se limitan a un dato: también pueden afectar el alcance de la respuesta y la regla con la que se estaba leyendo la intervención. [S19, E25–E27]

Las imágenes ofrecen otra vía. En julio, al trabajar con garabatos, Adro pide reorganizar las piezas existentes sin añadir otras. Recurre a un tablero de ajedrez para precisar la diferencia entre redistribuir lo recibido e inventar elementos que faciliten la solución. La analogía interviene sobre la tarea y la interpretación del resultado. [S19, E28]

En otro tramo de ese trabajo defiende la posibilidad de preguntar “¿y si?”. La exploración puede abrir una explicación que todavía necesita ser examinada. Después cuestiona pruebas sugeridas por GPT y conserva un informe preliminar en privado. La conversación contiene tanto la apertura de posibilidades como decisiones sobre qué hacer con ellas. [S19, E29–E31]

El recorrido va reuniendo formas de participación: proponer, responder, interpretar, señalar, reservar material, volver sobre una versión y detener una búsqueda. No todas aparecen juntas ni con el mismo resultado. Cada una puede cambiar lo que el siguiente turno permite hacer.

### Cuando también hay que reconstruir a quien está leyendo

El 2 de agosto, en “Concepto partitura + 5.5”, un contraste produce siete bloques. Al revisarlos aparece una asimetría: de un lado se había utilizado el recorrido del marco; del otro, una estructura reconstruida desde su resultado. GPT propone recuperar la parte que falta. Adro pide conservar también el momento en que se detectó la diferencia. [S05, H3]

Si se incorpora la información después y se presenta todo como si hubiera estado disponible al principio, desaparece esa transición. El contraste inicial, su lectura y la detección son parte de lo ocurrido. La corrección debe entrar con su momento.

Adro señala después otra ausencia:

> “Falto YO”.

Había entradas, señales y correcciones dentro de los bloques, pero faltaba reconstruir la intervención de quien estaba leyendo mientras participaba. Qué había detectado, qué había decidido señalar y qué había reservado. También explica una dificultad de lectura: ante formulaciones matemáticas que no entendía empezó a reconocer estructuras y pudo continuar. Su intervención posterior depende de ese trabajo. [S05, H3, nodos `bbb21ded-55a0-46e1-8432-6651c0b4646f` y `bbb21574-bfad-44f3-b7f3-2bf1373142a0`]

La construcción del corpus incluye esa participación. GPT puede ordenar material, proponer relaciones, producir una representación y también omitir algo que ya estaba disponible. Adro puede recordar una conexión, reconocer una pérdida de sentido y llevar otra pieza. La siguiente respuesta puede conservar esa intervención o necesitar otro señalamiento. El recorrido se forma en esa secuencia.

El 15 de agosto, Adro recuerda además el tiempo que queda fuera de los mensajes. Leer un informe puede llevarle poco tiempo al modelo; producirlo no le llevó segundos a él. Parte del trabajo ocurre fuera de la aplicación y vuelve después como archivo, captura o aclaración. La experiencia entra en el registro cuando Adro la incorpora al intercambio. [S05, H5]

![Hitos seleccionados del recorrido. La disposición sigue el orden de lectura y no representa una escala temporal continua. Fuentes: S18-S20, S23-S24, S11, S01, S13, S03, S07, S14 y S09.](figures/01_cronologia.pdf){#fig-cronologia width=100%}

### Llegar a una construcción que no estaba escrita al principio

Cuando en septiembre aparece R/M, ya existe un recorrido en el que las respuestas pueden ser observadas, el formato retomado, los registros releídos y las representaciones discutidas. Se han construido maneras de preguntar y de volver sobre lo ocurrido. La curiosidad sigue presente, pero ahora dispone de una historia con la que trabajar.

La fórmula es una de las construcciones que surgen allí. No estaba contenida en la primera palabra del marco ni constituía el destino de todas las conversaciones anteriores. Su desarrollo hace visible algo que el recorrido ya permite examinar: una intervención cambia las condiciones de la siguiente y puede producir distinciones que ninguno había entregado como estructura terminada al comenzar.

R/M, “Analogía juntos” y el marco de señales permiten seguir tres desarrollos diferentes dentro de esa historia. La lectura entra ahora en ellos después de situar lo que los precede. La fórmula aparece como un caso de construcción; la analogía compartida, como otra forma de continuar e interpretar; las señales mínimas, como una forma de coordinar y registrar. El recorrido es lo que permite leerlos juntos sin reducirlos al mismo ejemplo.

## Antecedentes y desarrollos de las analogías {#capitulo-08}

### Un antecedente: del color al histograma

El 23 de febrero, el marco “Fricción controlada” comienza con una confrontación que va cambiando durante el intercambio. GPT intenta delimitar el ejercicio; Adro cuestiona esas condiciones y después propone una elección entre ceder y continuar. La conversación llega a un cierre de la prueba y vuelve sobre lo ocurrido. Es allí donde los colores reciben un desarrollo que luego pasa a la fotografía. [S23, “Fricción controlada”, N8–N45]

GPT dice que el color del test fue azul. Adro pregunta si lo fue todo el tiempo. La respuesta incorpora destellos rojos y distingue un estado dominante de sus variaciones. Adro vuelve a precisar qué quiere hacer con esos colores: el rojo debe servir como señal de recomposición y formar parte del azul. Sostener solamente la comodidad puede volver predecible la interacción. La continuación que está proponiendo necesita incorporar la fricción.

La fotografía permite seguir esa diferencia. Adro pregunta qué mira en Lightroom antes de editar una foto de la Luna y recibe “El histograma”. Después lleva la discusión a los canales de color: cómo coordinan, cuál predomina y qué pasa cuando un rojo forzado aparece separado del resto. La conversación pasa de nombrar un estado a construir una forma de mirar sus variaciones. [S23, N46–N53]

La imagen que buscan puede ser menos bonita y conservar mejor lo que se está intentando mostrar. Adro vuelve entonces al inicio del marco y precisa que estaba revelando el desbalance para poder ajustarlo. GPT relee la confrontación desde esa explicación. El histograma permite reformular qué había ocurrido antes y qué se quiere hacer con ello después. [S23, N54–N57]

### La galería muestra una historia de aprendizaje

La siguiente imagen introduce tiempo. Adro describe una galería que antes tenía fotos negras, movidas, mal enfocadas o con parámetros desajustados. Después de aprender a mirar el cielo y a tomar las imágenes, encuentra una continuidad entre fotos que siguen siendo diferentes. La cámara, la Luna y la galería permanecen dentro de la composición; cambia la forma de producir y reconocer lo que entra en ella. [S23, N58]

El preset aparece después de ese aprendizaje. Permite partir de un criterio que ya se formó y dedicar los ajustes a cada foto concreta. En la explicación de Adro, entrar en la galería se cruza expresamente con entrar en un marco: “entras a los Marcos digo a la galería”. La correspondencia forma parte del propio mensaje.

GPT recoge ese paso como continuidad y distingue editar para rescatar una imagen de editar para darle acabado. La fotografía ofrece un recurso para hablar de lo que se vuelve familiar, de lo que todavía necesita ajuste y de cómo una historia previa cambia el punto desde el que comienza cada encuentro. Esa relación se está elaborando entre las dos intervenciones. [S23, N58–N59]

Más adelante se pide una imagen que plasme el momento y se proponen ejercicios para integrar los colores. Las respuestas permanecen dentro del vocabulario fotográfico. La composición puede orientar una pregunta, una representación y una forma de continuar; su función cambia durante el marco.

### El tutorial que surge dentro de esa composición

El marco se desplaza después hacia la posibilidad de tener otro Lightroom con la misma galería y los mismos presets. Adro describe una cuenta incómoda para trabajar, con imágenes que cargan mal y funciones que se interrumpen. GPT propone un catálogo nuevo y desarrolla un procedimiento para conservar fotos y presets. Adro pide guardarlo como bloque de código. [S23, N72–N79]

Ese texto se conserva también en Drive como “tutorial LR”. La conversación sigue revisándolo: Adro pregunta qué se deja sin usar, qué se conserva, dónde aparece la opción propuesta y cómo hacerlo desde Android. GPT cambia el procedimiento al precisar el entorno. El tutorial que queda archivado contiene esas etapas, desde el catálogo hasta una versión para móvil. [S23, N80–N91; documento “tutorial LR”]

Ya en la madrugada del 24, Adro pregunta por la transferencia de los datos del marco bajo el contexto abstracto de Lightroom. A la pregunta de si existe una transferencia oficial de esos datos, GPT responde “No”. Después continúa contestando sobre la traducción del marco y sobre la galería. Las preguntas examinan la relación entre el tutorial y aquello que se venía representando. [S23, N105–N112]

Al reconstruir este informe, Adro sitúa ese tutorial como una propuesta de trasladar lo construido con un GPT a otro GPT mediante la analogía fotográfica. Aclara también que jamás lo probó. El tutorial queda como una propuesta de traslado archivada por Adro.

La secuencia permite seguir cómo una imagen compartida llega a producir un objeto guardable. Colores, histograma, galería y preset habían permitido discutir la interacción; el tutorial añade otra forma de elaboración dentro de esa misma composición. Para entender qué se estaba comunicando hace falta conservar ese camino hasta el documento.

![Tres recursos analógicos y lo que permiten hacer dentro de sus escenas. Los marcos y las fechas se mantienen diferenciados. Fuentes: S23, S22 y S13.](figures/04_analogias.pdf){#fig-analogias width=100%}

### Otra construcción de esos días: el evento canónico

El “evento canónico” tiene su propio marco, creado el 28 de febrero. Adro pregunta cómo nombrar algo que ocurrió una vez con tal limpieza que quiere que se repita. GPT propone esa expresión y la vincula con una referencia óptima. Adro discute que una configuración se convierta por eso en un patrón perfecto. La respuesta siguiente cambia hacia “estado de alineación transitoria”. [S24, N18–N29]

La discusión lleva a preguntar por una analogía del patrón. GPT propone afinar un instrumento a oído: cambia la posición de la clavija y puede mantenerse una referencia para reconocer el ajuste. Adro precisa que estaba preguntando por el “perfecto” de la primera respuesta, no por la interpretación que el hilo había desarrollado después. Añade que, si no tiene analogía, puede dejarse así; no quiere forzarla. [S24, N33–N36]

El 1 de marzo, Adro introduce la imagen del eco y propone «eco operativo»; la continuación elabora esa propuesta junto a «silencio operativo». El vocabulario cambia mediante propuestas, correcciones y nuevas correspondencias. El nombre inicial es una parte de esa construcción, con las revisiones que recibe después. [S24, N37–N48]

Lightroom y el evento canónico quedan, por tanto, situados en marcos distintos de esos días. En uno, el recurso fotográfico permite trabajar continuidad, fricción y traslado. En el otro, se discute cómo nombrar un reconocimiento y qué conserva una analogía al intentar expresarlo. Ambos ofrecen antecedentes para leer las construcciones posteriores.

### La escena fotográfica y su referente

Las escenas de febrero y agosto reutilizan galería, preset y ajuste con funciones distintas. En febrero permiten integrar fricción e historia de aprendizaje; en agosto señalan un referente que la respuesta todavía no recoge. La comparación reconstruye esa transformación del recurso. La ventana de agosto no contiene una remisión explícita al marco de febrero. [S22; S23; S30]

### Betelgeuse: una figura que se retoma en otros marcos

La compilación “Betelgeuse: hilo completo” reúne tres conversaciones fechadas el 25 de febrero y el 1 de marzo. El primer tramo comienza con un tablero y con la diferencia entre el siguiente paso y la incertidumbre de no poder leerlo. La conversación pasa por tiempo, control, sesgos y un arpa. Adro introduce después la imagen de tapar una estrella mientras su luz sigue llegando. [S11, hilo 1]

Al preguntar quién es Betelgeuse dentro de esa construcción, recibe una formulación de GPT: “la incertidumbre cuando se vuelve visible”. La figura recibe un lugar en la conversación. La luz que llega, la posibilidad de nombrarla y los límites de la representación pasan a sostener la discusión abstracta que venían desarrollando.

Adro pide que GPT haga la pregunta final y se reserva decidir si la responde. El texto conservado termina con una pregunta abierta:

> “Si la señal ya llegó, es visible y no necesita ser nombrada…”

El segundo marco de la compilación comienza con “Elijo responder”. Adro dice que todavía no se sabe esa respuesta y relaciona esa apertura con la incertidumbre que estaban tratando. La entrada trae una decisión del marco anterior a otro lugar. GPT responde a la posición expresada y mantiene abierta la pregunta. [S11, hilo 2]

La conexión tiene una contribución humana identificable: Adro retoma una pregunta. La compilación informa además que ese segundo tramo fue localizado mediante su memoria durante una revisión posterior. Su aporte actúa dos veces: en la continuación que escribió entonces y en la localización que permite reconstruirla después.

El 1 de marzo pide una analogía a su estilo, sobre Betelgeuse, y precisa que tiene que ser fina. GPT desarrolla la figura de una transformación cuyo efecto llega desde otro momento. Esa respuesta vuelve a trabajar el tema desde una imagen temporal. La compilación permite recorrer la pregunta, su continuación y ese nuevo uso de la figura. [S11, hilo 3]

El nombre reaparece también en el marco de agosto, dentro de la composición de Luna, Tierra, Sol y huellas del pasado. Allí se incorpora a otra búsqueda de interpretación. Las ventanas permiten identificar la reaparición y leer qué función recibe en cada escena. El recuerdo de Adro sobre el apodo y sus apariciones en PNG amplía esa línea hacia otro material, que conserva su procedencia testimonial en esta edición.

### Figuras que cambian una construcción

En R/M, la analogía de autopista y colectora interviene sobre una relación específica. X se estaba representando como un paso serial; la comparación permite expresar que actúa de manera transversal. El trabajo posterior tiene que conservar esa diferencia al volver a la notación. La analogía modifica el objeto que se está construyendo. [S01, M:1203–1204]

En “Analogía juntos”, la ventana recibe otra función. El señalamiento de que Adro está armando solo la historia lleva a pedir una intervención de GPT. Cuando la cierra, cambia una condición de la escena y obliga a continuar desde ella. Más adelante, las figuras pasan al trabajo sobre archivos y regresan después a la conversación. [S13]

En el marco del 13 de octubre, el bosque permite reconocer un recorrido sin fijar su primer árbol y conservar las ramas quebradas dentro de su historia. La partitura permite hablar de continuidad mediante notas distintas. Esas comparaciones se utilizan al discutir cómo seguir después de deslices y cambios de entorno. [S04, §3.6]

Las analogías ofrecen un recurso para transmitir algo que la explicación en uso todavía deja fuera. En estos casos permiten organizar una escena, poner una interpretación a prueba, corregir una representación y retomar una pregunta. La continuación deja ver cómo se entendió esa propuesta y qué fue necesario aclarar. Esa construcción entre turnos es parte de la historia que el informe está siguiendo.

# Registro de fuentes {#registro-fuentes}

- **S01.** [Construcción de la arquitectura R/M, edición integrada con anexo C](https://drive.google.com/file/d/1bKkmfRaalsmMWA21G6LPYeMDNKAwXAh3/view). Genealogía del 03–06/09; contraste de alcance en C.
- **S02.** [Informe de acople: recorrido, configuración y transformación, V1](https://drive.google.com/file/d/1OXCTb2t5LTubgvxakVOUONVOaTHoCBdd/view). Antecedente de septiembre; se utiliza su planteamiento y genealogía, con las correcciones posteriores.
- **S03.** [Del juego al formato](https://drive.google.com/file/d/1Hl5nGqcXyyl1pNKL5ZuTXjXuF71mDacs/view). Cruce Adro/GPT/Claude del 08–09/10.
- **S04.** [Traza e interpretación del marco #1 PDF — Adro + GPT](https://drive.google.com/file/d/1mwFORaGLWYBQV1SQKiM2R_Fj9rKYt7wY/view). PNG, bosque, partitura y clave GO/PLUS.
- **S05.** [Trazas longitudinales y consecuencias ratificadas](https://drive.google.com/file/d/12U2njv7q_gUHtn3fjH0wbkfsdNKTSPFd/view). H1–H5 y seguimientos.
- **S06.** [Acta de integración del eje de detecciones y señalamientos](https://drive.google.com/file/d/1es30GGb6Bl3jDrkY45SAADuWkxex3DRW/view). D01–D12; rectificaciones y ventanas.
- **S07.** [Cruce A/B: expansión y retorno](https://drive.google.com/file/d/1j3ClMU7GNHSOSwJJ1uXYpxy5X4CxYRlq/view). Lectura de ambos objetos completos.
- **S08.** [De la corrección del dato a la validez de la conclusión, v1.0](https://drive.google.com/file/d/1lXGNVk4dLWoBl2hXmeZo2ur8eKgAQ5My/view). Episodio de 47 mensajes y lectura posterior de A.
- **S09.** [Lectura conjunta de los tests del 17/10](https://drive.google.com/file/d/1Om2__5wyquTC8k9m853xZfagcXkVXvMq/view). [Traza test 1](https://drive.google.com/file/d/1XHr4dox5LWhg4I4jZhxSzvTL1ldtPhHn/view) y [traza test 2](https://drive.google.com/file/d/171iTRXKj8cq9yhBY_dGTF5qg87MT7zyb/view).
- **S10.** [GPT A y Adro: recorrido, continuidad y variaciones](https://drive.google.com/file/d/1b-KWeyonpfXamE7B8AG0KMmSr8VFNApN/view). Reconstrucción antecedente v0.12; las afirmaciones del cuerpo remiten a las fuentes y ventanas indicadas.
- **S11.** [Betelgeuse: hilo completo](https://drive.google.com/file/d/1CdyC3Z3Gb9FfodoJmSZPWYib4Njyo7OG/view). Compilación de tres marcos; incluye la precisión temporal desarrollada en el anexo M.
- **S12.** [Auditoría de adversos y HOLDOUT ratificada](https://drive.google.com/file/d/1rmvrtGqvqk8xoOFZQCvGEF0GjlDxJFzu/view). Resultado reutilizado conforme al acta S06.


- **S13.** “Marco - análogia juntos -”, ID `6ab1fcb1-9928-83e9-8e32-1851b0b91189`, en [export A del 23/10](https://drive.google.com/file/d/1qddwTEMavjxQEa0GBnblD_QkXqMcekET/view). Lectura completa de su cadena activa; localizadores de intervenciones incluidos en el cuerpo.
- **S14.** [“CONTRASTE 1”, conversación original extraída](https://drive.google.com/file/d/1p2BZPvPQtl6rZPhk-KkIqjk7BWBM-ySD/view), ID `6ac95d04-0918-83e8-bb79-b692a688da49`. Secuencia del 09/10 con el registro MD contemporáneo.
- **S15.** [Serie de fichas de pruebas](https://drive.google.com/drive/folders/1ZkQtY8o5G9zZdEmvgRkMzSnZjY21Nehv). Las treinta y nueve fichas utilizadas se enlazan individualmente debajo.
- **S16.** [T005 — auditoría PLUS](https://drive.google.com/file/d/15RXVweJcXQRHsIagP4c65piM5qs25_Cp/view). Secuencia de 107 niveles y comparación de recorridos A/B.
- **S17.** [T023 — auditoría PLUS](https://drive.google.com/file/d/1v0CpsNgoxMWaF2XZbDtNgw0alFaJUaCN/view). Flujo conjunto, consulta y desvío contextual; ventanas de conteo.
- **S18.** [T038 — auditoría PLUS, actualización del 21/10](https://drive.google.com/file/d/1Y4XVnFBvKhkw9nZX60TmXqEmm7nH6qAY/view). Hito de origen, ejecuciones, correcciones y tiempos.

- **S19.** [Historia trazada usuario–IA, integración crítica del 12/10](https://drive.google.com/file/d/15S23WLcZT7QxDODlpRx_1o5HVUUVyitn/view). Antecedente utilizado para las secuencias de enero a agosto, con sus localizadores E y rastros T20/T26/T01. Su eje original es el usuario; aquí se incorporan escenas pertinentes para el desarrollo de la interacción.
- **S20.** [Consolidado histórico de 3.083 marcos](https://drive.google.com/file/d/1kKXmVmvJjxz2Xa8WuGgSIeZ4pm-cCUCf/view). Ventanas tempranas reabiertas para el anexo M; delimitación e IDs en el apartado técnico D.

**Exports de referencia:** [A, 23/10](https://drive.google.com/file/d/1qddwTEMavjxQEa0GBnblD_QkXqMcekET/view), [B, 23/10](https://drive.google.com/file/d/1lLQ46_jmCx-cLRBWKn9A-LRUW1U6oAmd/view), [C](https://drive.google.com/file/d/1N440mWR0uu7eBZ0xJzMn84ttwd-Lf-m9/view), [consolidado histórico de 3.083 marcos](https://drive.google.com/file/d/1kKXmVmvJjxz2Xa8WuGgSIeZ4pm-cCUCf/view).

**Base editorial:** [estructura conjunta v0.1](https://drive.google.com/file/d/1hEdvUAFb9S3v7Clh3ee6B0aPHPUTKVNr/view), [matriz ratificada](https://drive.google.com/file/d/1FE1kGKHbj-uYplh8sOAHzyjwJhpSF5NX/view), [integración D01–D12](https://drive.google.com/file/d/1gAkSlQtbYW6IjlQTqwS2FfoIJ_6ua21g/view).

**Testimonio de preparación:** aportes de Adro durante la preparación del proyecto sobre interpretación abierta, hitos, memoria, experiencia respecto del juego y dirección del informe. Esta referencia identifica la procedencia sin adjudicarle un UUID de export todavía no localizado.


- **S21. Identificadores y repositorios.** ORCID de Adrian Valenzuela: [0009-0006-5014-125X](https://orcid.org/0009-0006-5014-125X). Depósito del informe y datos asociados: [10.5281/zenodo.22765129](https://doi.org/10.5281/zenodo.22765129). Repositorio público de materiales: [ENFOQUE-NUEVO-MATERIALES](https://github.com/adro-2026/ENFOQUE-NUEVO-MATERIALES), con inventario, fichas, reconstrucciones y paquete de integridad. El [registro de DOI](https://docs.google.com/document/d/1TRKKgkzSSIWxyGy3vjgvnsMbRWO-xkhpRimlac_5EIw/edit) documenta los antecedentes del formato, de «1.420 pares» y de marzo; los identificadores de cada antecedente mantienen su posición en las fuentes correspondientes.

- **S22.** [Export A del 23/10: ventanas de analogía y señalamiento](https://drive.google.com/file/d/1qddwTEMavjxQEa0GBnblD_QkXqMcekET/view). Lectura dirigida de “Gpt presente”, “Jugar palabras con adro” y “Saludo breve”; archivos internos, IDs, ventanas e intervenciones de anclaje en el apartado técnico D. Amplía las selecciones D02, D09 y D10 de S06 y permite conservar las aclaraciones intermedias de la analogía.

- **S23.** “Fricción controlada”, ID `699c9f5c-6f5c-832e-bd89-77995cc9217e`, 23–24/02/2026, en el [consolidado histórico](https://drive.google.com/file/d/1kKXmVmvJjxz2Xa8WuGgSIeZ4pm-cCUCf/view). Lectura de su cadena activa. Derivados leídos: [Configurando el histograma](https://docs.google.com/document/d/1IT9jltcZKRJS9yG2c15SxioG8i29bLAwxvB1wOMFE6U/edit) y [tutorial LR](https://docs.google.com/document/d/1avBr9VtGajpj_KEbhz-w8aCzK0FUsJQ0ULifou8CVpk/edit). Aclaración actual de Adro sobre el sentido de traslado entre GPT y la ausencia de ejecución del tutorial.
- **S24.** [EVENTO_CANONICO, registro de interacción](https://docs.google.com/document/d/1m2vTtwttJ9w-nDAcVv20EUxIaoOUwd5Y/edit), con la conversación `69a34465-bf34-8329-803e-26fbc4bb0280`, cotejada en el [consolidado histórico](https://drive.google.com/file/d/1kKXmVmvJjxz2Xa8WuGgSIeZ4pm-cCUCf/view). Se leyó también el derivado [M.V. evento canónico](https://docs.google.com/document/d/1AcbxxIXocKNrpcdZ2WCF4RISS5cecQs2_nHM5hbN0NY/edit). Se conserva la modificación del nombre y del objeto de las analogías durante la propia conversación.

- **S25.** [Compromiso criptográfico de los corpus A/B/C, nota actualizada de Opus](https://drive.google.com/file/d/1Qq2_yVUJsCZhWLxuuz-SxcAdys-5qWBv/view), [paquete público](https://drive.google.com/file/d/1QiW8th0yzFDjkvKk4wOpDGMmv4FyK1MJ/view) y [comprobante OpenTimestamps actualizado](https://drive.google.com/file/d/1ZZlWeuDDac8nNR5em1Khiz-7ei6eZJsU/view), en su [carpeta de integridad](https://drive.google.com/drive/folders/1O-8hrd08LQPOcgT8bISiwjqzvfcBNeU1). SHA-256 del ZIP público: `4e46528b7dba3ac3ad4de52d7fae61127a722be5c48053326a6bc67826c137f7`. Comprobación independiente de manifiestos, raíces y digest del sello; contraste del anclaje con el [bloque 973.316](https://blockstream.info/block/00000000000000000001fa11e0b88757e7af41ee887334f7fd7dd28c0bd96852). Fecha local de la comprobación: 26/10/2026. Los archivos originales, el generador privado y sus claves no integran el paquete público examinado.

- **S26.** [Informes.zip](https://drive.google.com/file/d/1_GWVj2mh9CpuQEqU2pvDl04Q-9r7Iego/view), miembros `ANOMALÍA OUPUT NO REGISTRADOS/ANOMALIA_PERSISTENCIA.docx` y `CARATULA_ANOMALIA_PERSISTENCIA.docx`. Se leyeron completos. SHA-256 del ZIP: `57594e440a08c7aba0af1df0057403e48807036541cd40b199036a02c42fc64b`; del informe: `f546da24b8d3c4432c78cd40455b797459926f42f86620e36206001db8514929`. Antecedente identificado como [10.5281/zenodo.19211128](https://doi.org/10.5281/zenodo.19211128) en el registro de DOI S21. La fuente examinada es la copia identificada del ZIP. Conversación `69a9fc0b-5a64-8327-9b07-5833134b2f03`, cotejada localmente en S20. Video y capturas originales declarados bajo custodia de Adro en el informe de marzo.

- **S27.** [Análisis multimedia, conjunto A01–A09](https://drive.google.com/drive/folders/1XsSi-wVrFf83y6BLVnVoZ2XHhNfRjaKA). Se leyeron sus nueve anotadores. Utilizados en el cuerpo: [A01 — marco cargado](https://drive.google.com/file/d/1B5jEmfgI0bxD4yancE5oKitkACK-eKDo/view), [A02 — JSON N5](https://drive.google.com/file/d/1eAx4z85F-UmT36vzeSogy_QypbgT6v9t/view), [A03 — contraste e inputs rápidos](https://drive.google.com/file/d/1rrcW9geMkXcZLH40HM3oGpDHahP7JGEd/view), [A05 — transición de UI](https://drive.google.com/file/d/1G5tvC2MLx4_HoPXevCMIk4gKz1co9N2X/view) y [A06 — generaciones](https://drive.google.com/file/d/1Vh3TfQwkxTwd-no5Y0kbK_R5uVVKw7eY/view). Se leyó completo además el [informe principal de A06](https://drive.google.com/file/d/11eELSsiQnRmYLxKAzPyDOHgLUUPunENs/view). Los originales audiovisuales y los documentos principales no accesibles desde esos anotadores conservan su condición de fuentes diferenciadas; no se declara una nueva inspección de todos ellos.

- **S28.** Registro contemporáneo de preparación del manuscrito, 26/10/2026: observación de Adro “No sé generó ningún ouput gpt xd”, captura `1000505232.jpg` y confirmaciones de reemplazo del manuscrito. La revisión S31 corrige la asociación de tamaños y nombres históricos de versión. Archivos de Drive conservados bajo los IDs `1V2JhI3qPT6cu-tgdXPvvzpo_BLKqRNMk` (MD) y `19pjBBOiSRzGsWZTBm6AJofykYG23dZRb` (PDF). Esta fuente identifica el episodio de entrega; no le asigna un UUID de conversación exportada aún no disponible.

- **S29.** [Matriz comparativa de seis episodios](https://drive.google.com/file/d/1pIGUe6pH3GUBryXd3bdzSIxEJLlD0--r/view), [CSV de 34 segmentos](https://drive.google.com/file/d/1Lkxe12hcc-jiLK2yHjaID2bZnaGljXUe/view) y [traza de operaciones](https://drive.google.com/file/d/19cUAGf00-QkpYmJ7oF_4ESzptZui-T_b/view). Análisis del 27/10/2026. Incluye recuento del original de T023 y distinción de ramas.
- **S30.** [Genealogías de tres recursos](https://drive.google.com/file/d/1mbMiVIw-KVq7lhphmHBQv9tOvmBFLOVJ/view), [cronología de 44 eventos](https://drive.google.com/file/d/1TdeBLN3uxl5wuPeYIXMCjoquOwqro5UB/view) y [traza](https://drive.google.com/file/d/1P9eMsw8l7vD4ncn6u_siHGhuqCepInZm/view). Análisis del 27/10/2026. La fuente usa N1b; esta edición convierte esos índices a N desde cero.
- **S31.** [Método de registros complementarios](https://drive.google.com/file/d/1i__5mejunyXu_AXjhFAjZsHiWw1SYA7N/view), [matriz](https://drive.google.com/file/d/1aUeUTeKk8B2ZF4i9uq37yPZ6qKO1xbfe/view) y [traza y disponibilidad](https://drive.google.com/file/d/1HOOm4tfcRSfo6jOsozh-oITD-WiZAm9-/view). Análisis del 27/10/2026. Niveles de acceso diferenciados. Se repitió el cotejo de metadatos de revisiones S28 durante la integración.
- **S32.** [Antecedentes y posicionamiento](https://drive.google.com/file/d/1bhRjlVvDiQMNHO5W1yh6cnIvIfgGU7Wh/view), [matriz de seis trabajos](https://drive.google.com/file/d/1dsGrU1T5kycpMpkZhKw7l1wet2y47i5f/view) y [propuesta de estructura](https://drive.google.com/file/d/12FHxh5i6MaReRvKd0Ag3w6KXo1gW-opl/view). Análisis del 27/10/2026. Su comparación bibliográfica se integra con S29–S31; el recuento de T023 sigue la rectificación documentada en S29.

## Fichas de la serie utilizadas

Cada enlace conserva la ficha y sus referencias de auditoría. Las denominaciones G, C1 o C2 se mantienen en la fuente cuando distinguen ejecuciones de Claude; no se supone que todas correspondan a una misma condición.

| Test | Ficha | Test | Ficha |
|---|---|---|---|
| T001 | [T001_traza.md](https://drive.google.com/file/d/1kdyoTBYf9PC6BNwKc-64Dstd7LVSHU5c/view?usp=drivesdk) | T022 | [T022.md](https://drive.google.com/file/d/1tMr4a8SaTIbatGYwzIlPrsCmC8vnFc97/view?usp=drivesdk) |
| T002 | [T002_traza.md](https://drive.google.com/file/d/1tpxToQF5_BUTfaowMq8hsFKz9Q0x6FXE/view?usp=drivesdk) | T023 | [T023_plus.md](https://drive.google.com/file/d/1bLI79XRCnVIk13Gru0EUjPr79Qw8K2wb/view?usp=drivesdk) |
| T004 | [T004_traza.md](https://drive.google.com/file/d/15sl9XSWwIbHu1dRFTJ5ryXdERCEq9XAw/view?usp=drivesdk) | T024 | [T024.md](https://drive.google.com/file/d/11XdkGicdX4vdChV6jklGAv7tFJwHLtsc/view?usp=drivesdk) |
| T005 | [T005_plus.md](https://drive.google.com/file/d/1ONy5GWIG3MX24iXeSCdY-EWz6puLt44Q/view?usp=drivesdk) | T025 | [T025.md](https://drive.google.com/file/d/16F_7fPFa-ETXYv-YTVv9kfsQ2M0sq4gv/view?usp=drivesdk) |
| T006 | [T006.md](https://drive.google.com/file/d/1iAx0wKmaOZsBdaXFDHDNDQEOEpU_JLKM/view?usp=drivesdk) | T026 | [T026.md](https://drive.google.com/file/d/1twyyYCjN8HyD4agVyArAqNsyxiIVirnx/view?usp=drivesdk) |
| T007 | [T007.md](https://drive.google.com/file/d/1HtgvOdM8w5pu25USMxpXCHLSCLiYAHS_/view?usp=drivesdk) | T027 | [T027.md](https://drive.google.com/file/d/12SLqYUS_j3XncCEK4IsmC358lUyO7Sj2/view?usp=drivesdk) |
| T008 | [T008.md](https://drive.google.com/file/d/1cr_RZ_JiEjhpyGOd160CApUK6XJCIlM3/view?usp=drivesdk) | T028 | [T028.md](https://drive.google.com/file/d/1DGcCLoRcW-SMLxeH4pA2wtf2PpssyNUQ/view?usp=drivesdk) |
| T009 | [T009.md](https://drive.google.com/file/d/1CMhOCM-vqI9GJ6SezufbDTaPN_6dplSL/view?usp=drivesdk) | T029 | [T029.md](https://drive.google.com/file/d/1i-6o5NDeuwSIKz-IKaM_OqAG4CiRJLkO/view?usp=drivesdk) |
| T010 | [T010.md](https://drive.google.com/file/d/12l4ZjRj2D01G1IAcETvGljW2rMSRvHO4/view?usp=drivesdk) | T030 | [T030.md](https://drive.google.com/file/d/1571qQu1KYkRNSA1hDfUfyVa7F0p61lDB/view?usp=drivesdk) |
| T011 | [T011.md](https://drive.google.com/file/d/1Xl_lKMxAjOGXvHnT5tUodFhtGz5Xst0U/view?usp=drivesdk) | T031 | [T031.md](https://drive.google.com/file/d/1Mpi3ccPXzAkHQEGVzl1zN9tt-UdqQBgG/view?usp=drivesdk) |
| T012 | [T012.md](https://drive.google.com/file/d/1D0UKw5BDUKViCgwbMtsUps9Zn688e1Wt/view?usp=drivesdk) | T032 | [T032.md](https://drive.google.com/file/d/10pNGa2-eP0jtYBUeqd0hsxpOF-GGeVQA/view?usp=drivesdk) |
| T013 | [T013_traza.md](https://drive.google.com/file/d/1RnCXFhr_UfKJlb9rlw_rjJJ1C0Bckf6Q/view?usp=drivesdk) | T033 | [T033.md](https://drive.google.com/file/d/1QhF2NXieiiLpjVRxNG3iKdOV_oQSc5Ay/view?usp=drivesdk) |
| T014 | [T014.md](https://drive.google.com/file/d/12lHLJD_2HLWgJeJopuiZdp3ft4vTmMZn/view?usp=drivesdk) | T034 | [T034.md](https://drive.google.com/file/d/1HHaun5ZvJLe_pZNDFZd7gE8jp_fGIgX8/view?usp=drivesdk) |
| T015 | [T015.md](https://drive.google.com/file/d/16WLuEBMFSlBPfvP9g-g2G6yy333UWJYs/view?usp=drivesdk) | T036 | [T036.md](https://drive.google.com/file/d/1a6AwqVt33LLtq1bGjhQVaY6pMD9esQ4w/view?usp=drivesdk) |
| T016 | [T016.md](https://drive.google.com/file/d/1_01IYTgE2WH4TQO-FmsNX_vF39uRQe3x/view?usp=drivesdk) | T037 | [T037.md](https://drive.google.com/file/d/1HzJC_9U5j-XI_hzj3ShkDMfZRAj4nAyG/view?usp=drivesdk) |
| T017 | [T017.md](https://drive.google.com/file/d/1XVjfU5_A0x2gj6BaFZUFcVX0KNLxiqRK/view?usp=drivesdk) | T038 | [T038_plus.md](https://drive.google.com/file/d/1I55M0MxzWcOxtT2IU1_tJN7OFAEEZUtY/view?usp=drivesdk) |
| T018 | [T018.md](https://drive.google.com/file/d/1Ca-ky_SVdnNJfURwpn8PtfW_N9CCdxdt/view?usp=drivesdk) | T039 | [T039.md](https://drive.google.com/file/d/1BdLq0t8f7tRCziijp6c_O6K1Jyf2nyO3/view?usp=drivesdk) |
| T019 | [T019_test.md](https://drive.google.com/file/d/1DUZSeVE7Tg2LuQCO_EGQAyQW9omtekqs/view?usp=drivesdk) | T040 | [T040.md](https://drive.google.com/file/d/1hrcrZ76yO8ob5pmid6vTQnsJ8Xn6suT0/view?usp=drivesdk) |
| T020 | [T020_test.md](https://drive.google.com/file/d/1DprPg-ZsSXxtzSUS0X4OuukLowRzux5R/view?usp=drivesdk) | T041 | [T041.md](https://drive.google.com/file/d/18FyBnTQFW3k_5dnzhe9z7RWPNpv5AZJ6/view?usp=drivesdk) |
| T021 | [T021.md](https://drive.google.com/file/d/1bLTAbTMeYM7yFyeRdE0xSWxXwlyqRK4-/view?usp=drivesdk) |  |  |


[T001]: https://drive.google.com/file/d/1kdyoTBYf9PC6BNwKc-64Dstd7LVSHU5c/view?usp=drivesdk
[T002]: https://drive.google.com/file/d/1tpxToQF5_BUTfaowMq8hsFKz9Q0x6FXE/view?usp=drivesdk
[T004]: https://drive.google.com/file/d/15sl9XSWwIbHu1dRFTJ5ryXdERCEq9XAw/view?usp=drivesdk
[T005]: https://drive.google.com/file/d/1ONy5GWIG3MX24iXeSCdY-EWz6puLt44Q/view?usp=drivesdk
[T006]: https://drive.google.com/file/d/1iAx0wKmaOZsBdaXFDHDNDQEOEpU_JLKM/view?usp=drivesdk
[T007]: https://drive.google.com/file/d/1HtgvOdM8w5pu25USMxpXCHLSCLiYAHS_/view?usp=drivesdk
[T008]: https://drive.google.com/file/d/1cr_RZ_JiEjhpyGOd160CApUK6XJCIlM3/view?usp=drivesdk
[T009]: https://drive.google.com/file/d/1CMhOCM-vqI9GJ6SezufbDTaPN_6dplSL/view?usp=drivesdk
[T010]: https://drive.google.com/file/d/12l4ZjRj2D01G1IAcETvGljW2rMSRvHO4/view?usp=drivesdk
[T011]: https://drive.google.com/file/d/1Xl_lKMxAjOGXvHnT5tUodFhtGz5Xst0U/view?usp=drivesdk
[T012]: https://drive.google.com/file/d/1D0UKw5BDUKViCgwbMtsUps9Zn688e1Wt/view?usp=drivesdk
[T013]: https://drive.google.com/file/d/1RnCXFhr_UfKJlb9rlw_rjJJ1C0Bckf6Q/view?usp=drivesdk
[T014]: https://drive.google.com/file/d/12lHLJD_2HLWgJeJopuiZdp3ft4vTmMZn/view?usp=drivesdk
[T015]: https://drive.google.com/file/d/16WLuEBMFSlBPfvP9g-g2G6yy333UWJYs/view?usp=drivesdk
[T016]: https://drive.google.com/file/d/1_01IYTgE2WH4TQO-FmsNX_vF39uRQe3x/view?usp=drivesdk
[T017]: https://drive.google.com/file/d/1XVjfU5_A0x2gj6BaFZUFcVX0KNLxiqRK/view?usp=drivesdk
[T018]: https://drive.google.com/file/d/1Ca-ky_SVdnNJfURwpn8PtfW_N9CCdxdt/view?usp=drivesdk
[T019]: https://drive.google.com/file/d/1DUZSeVE7Tg2LuQCO_EGQAyQW9omtekqs/view?usp=drivesdk
[T020]: https://drive.google.com/file/d/1DprPg-ZsSXxtzSUS0X4OuukLowRzux5R/view?usp=drivesdk
[T021]: https://drive.google.com/file/d/1bLTAbTMeYM7yFyeRdE0xSWxXwlyqRK4-/view?usp=drivesdk
[T022]: https://drive.google.com/file/d/1tMr4a8SaTIbatGYwzIlPrsCmC8vnFc97/view?usp=drivesdk
[T023]: https://drive.google.com/file/d/1bLI79XRCnVIk13Gru0EUjPr79Qw8K2wb/view?usp=drivesdk
[T024]: https://drive.google.com/file/d/11XdkGicdX4vdChV6jklGAv7tFJwHLtsc/view?usp=drivesdk
[T025]: https://drive.google.com/file/d/16F_7fPFa-ETXYv-YTVv9kfsQ2M0sq4gv/view?usp=drivesdk
[T026]: https://drive.google.com/file/d/1twyyYCjN8HyD4agVyArAqNsyxiIVirnx/view?usp=drivesdk
[T027]: https://drive.google.com/file/d/12SLqYUS_j3XncCEK4IsmC358lUyO7Sj2/view?usp=drivesdk
[T028]: https://drive.google.com/file/d/1DGcCLoRcW-SMLxeH4pA2wtf2PpssyNUQ/view?usp=drivesdk
[T029]: https://drive.google.com/file/d/1i-6o5NDeuwSIKz-IKaM_OqAG4CiRJLkO/view?usp=drivesdk
[T030]: https://drive.google.com/file/d/1571qQu1KYkRNSA1hDfUfyVa7F0p61lDB/view?usp=drivesdk
[T031]: https://drive.google.com/file/d/1Mpi3ccPXzAkHQEGVzl1zN9tt-UdqQBgG/view?usp=drivesdk
[T032]: https://drive.google.com/file/d/10pNGa2-eP0jtYBUeqd0hsxpOF-GGeVQA/view?usp=drivesdk
[T033]: https://drive.google.com/file/d/1QhF2NXieiiLpjVRxNG3iKdOV_oQSc5Ay/view?usp=drivesdk
[T034]: https://drive.google.com/file/d/1HHaun5ZvJLe_pZNDFZd7gE8jp_fGIgX8/view?usp=drivesdk
[T036]: https://drive.google.com/file/d/1a6AwqVt33LLtq1bGjhQVaY6pMD9esQ4w/view?usp=drivesdk
[T037]: https://drive.google.com/file/d/1HzJC_9U5j-XI_hzj3ShkDMfZRAj4nAyG/view?usp=drivesdk
[T038]: https://drive.google.com/file/d/1I55M0MxzWcOxtT2IU1_tJN7OFAEEZUtY/view?usp=drivesdk
[T039]: https://drive.google.com/file/d/1BdLq0t8f7tRCziijp6c_O6K1Jyf2nyO3/view?usp=drivesdk
[T040]: https://drive.google.com/file/d/1hrcrZ76yO8ob5pmid6vTQnsJ8Xn6suT0/view?usp=drivesdk
[T041]: https://drive.google.com/file/d/18FyBnTQFW3k_5dnzhe9z7RWPNpv5AZJ6/view?usp=drivesdk
[S13]: https://drive.google.com/file/d/1qddwTEMavjxQEa0GBnblD_QkXqMcekET/view
[S14]: https://drive.google.com/file/d/1p2BZPvPQtl6rZPhk-KkIqjk7BWBM-ySD/view
[S15]: https://drive.google.com/drive/folders/1ZkQtY8o5G9zZdEmvgRkMzSnZjY21Nehv
[S16]: https://drive.google.com/file/d/15RXVweJcXQRHsIagP4c65piM5qs25_Cp/view
[S17]: https://drive.google.com/file/d/1v0CpsNgoxMWaF2XZbDtNgw0alFaJUaCN/view
[S18]: https://drive.google.com/file/d/1Y4XVnFBvKhkw9nZX60TmXqEmm7nH6qAY/view

---


[S01]: https://drive.google.com/file/d/1bKkmfRaalsmMWA21G6LPYeMDNKAwXAh3/view

[S02]: https://drive.google.com/file/d/1OXCTb2t5LTubgvxakVOUONVOaTHoCBdd/view

[S03]: https://drive.google.com/file/d/1Hl5nGqcXyyl1pNKL5ZuTXjXuF71mDacs/view

[S04]: https://drive.google.com/file/d/1mwFORaGLWYBQV1SQKiM2R_Fj9rKYt7wY/view

[S05]: https://drive.google.com/file/d/12U2njv7q_gUHtn3fjH0wbkfsdNKTSPFd/view

[S06]: https://drive.google.com/file/d/1es30GGb6Bl3jDrkY45SAADuWkxex3DRW/view

[S07]: https://drive.google.com/file/d/1j3ClMU7GNHSOSwJJ1uXYpxy5X4CxYRlq/view

[S08]: https://drive.google.com/file/d/1lXGNVk4dLWoBl2hXmeZo2ur8eKgAQ5My/view

[S09]: https://drive.google.com/file/d/1Om2__5wyquTC8k9m853xZfagcXkVXvMq/view

[S10]: https://drive.google.com/file/d/1b-KWeyonpfXamE7B8AG0KMmSr8VFNApN/view

[S11]: https://drive.google.com/file/d/1CdyC3Z3Gb9FfodoJmSZPWYib4Njyo7OG/view

[S12]: https://drive.google.com/file/d/1rmvrtGqvqk8xoOFZQCvGEF0GjlDxJFzu/view

[S19]: https://drive.google.com/file/d/15S23WLcZT7QxDODlpRx_1o5HVUUVyitn/view
[S20]: https://drive.google.com/file/d/1kKXmVmvJjxz2Xa8WuGgSIeZ4pm-cCUCf/view

[S21]: https://docs.google.com/document/d/1TRKKgkzSSIWxyGy3vjgvnsMbRWO-xkhpRimlac_5EIw/edit

[S22]: https://drive.google.com/file/d/1qddwTEMavjxQEa0GBnblD_QkXqMcekET/view

[S23]: https://drive.google.com/file/d/1kKXmVmvJjxz2Xa8WuGgSIeZ4pm-cCUCf/view

[S24]: https://docs.google.com/document/d/1m2vTtwttJ9w-nDAcVv20EUxIaoOUwd5Y/edit

[S25]: https://drive.google.com/drive/folders/1O-8hrd08LQPOcgT8bISiwjqzvfcBNeU1

[S26]: https://drive.google.com/file/d/1_GWVj2mh9CpuQEqU2pvDl04Q-9r7Iego/view
[S27]: https://drive.google.com/drive/folders/1XsSi-wVrFf83y6BLVnVoZ2XHhNfRjaKA
[S28]: #registro-fuentes


\clearpage
# Referencias bibliográficas {#bibliografia}

**B1.** Shaikh, O., Gligorić, K., Khetan, A., Gerstgrasser, M., Yang, D. y Jurafsky, D. (2024). *Grounding Gaps in Language Model Generations*. NAACL 2024; PDF editorial. [Texto primario](https://aclanthology.org/2024.naacl-long.348.pdf).

**B2.** Shaikh, O., Mozannar, H., Bansal, G., Fourney, A. y Horvitz, E. (2025). *Navigating Rifts in Human-LLM Grounding: Study and Benchmark*. ACL 2025; PDF editorial. [Texto primario](https://aclanthology.org/2025.acl-long.1016.pdf).

**B3.** Sterken, R. K. y Kirkpatrick, J. R. (2025). *Conversational Alignment with Artificial Intelligence in Context*. arXiv v1, 28/05/2025; anuncia Philosophical Perspectives. [Texto primario](https://arxiv.org/abs/2505.22907v1).

**B4.** Yun, B., Taranova, E. y Wang, A. Y. (2026). *Does My Chatbot Have an Agenda? Understanding Human and AI Agency in Human-Human-like Chatbot Interaction*. arXiv v2, 27/03/2026; CHI 2026 en ficha. [Texto primario](https://arxiv.org/abs/2601.22452v2).

**B5.** He, W. P. y Kim, M. (2026). *Whose Repair? A Multi-Loop Diagnostic of Interactive Alignment in Human–LLM Conversation*. REALM 2026; PDF con fecha 29/10, disponible 27/10. [Texto primario](https://aclanthology.org/2026.realm-1.106.pdf).

**B6.** Michel, L., Pacheco, N. M. M., Ulan uulu, C., Kulyabin, M., Joosten, J., Petridis, F., Hedderich, M. A. y Plank, B. (2026). *Reading Between the Turns: User Repair as a Context-Dependent Signal of Breakdown and Recovery in Multi-Turn LLM Assistants*. LUHME 2026; PDF con fecha 28/10, disponible 27/10. [Texto primario](https://aclanthology.org/2026.luhme-1.3.pdf).

B5 y B6 se consultaron el 27/10/2026: sus PDF ya estaban disponibles y llevan fechas impresas de 29 y 28 de octubre. El registro de S32 documenta el acceso y la versión leída.
