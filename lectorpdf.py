import PyPDF2

def extraer_comentarios(pdf_path):
    comentarios = []
    
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_paginas = reader.numPages
        
        for i in range(num_paginas):
            pagina = reader.getPage(i)
            comentarios_pagina = pagina.extractText()
            
            if '/Annots' in pagina:
                anotaciones = pagina['/Annots'].getObject()
                for anotacion in anotaciones:
                    tipo = anotacion.getObject()['/Subtype']
                    if tipo == '/Text':
                        comentario = anotacion.getObject()['/Contents']
                        comentarios.append(comentario)
    
    return comentarios

# Ruta al archivo PDF
pdf_path = 'ruta/al/archivo.pdf'

# Llamada a la función para extraer comentarios
comentarios_extraidos = extraer_comentarios(pdf_path)

# Imprimir los comentarios extraídos
for comentario in comentarios_extraidos:
    print(comentario)
    
# PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.

