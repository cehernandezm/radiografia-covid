<h1 align="center">
  <br>
  <a></a>
  <br>
 COVID-19 Chest X-Ray Analysis 
  <br>
</h1>

<h4 align="center"> Aplicacion desarrollada en ReactJS que permite subir imagenes
de radiografias, y se analiza dando como resultado, si es covid, normal o pneumonia. Es un proyecto unicamente con fines educativos, el modelo predictivo, no es preciso, y no esta altamente entrenado.</h4>


   [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)  

<p align="center">
  <a href="#instalar">Herramientas</a> •
  <a href="#arquitectura">Arquitectura</a>•
  <a href="#como-funciona">Como Funciona</a> •
  <a href="#license">Licencia</a>•
  <a href="#soporte">Soporte</a>
</p>

![7094dde6-a461-4345-9efe-03526106e383](https://user-images.githubusercontent.com/20384738/98444536-d8114500-20d7-11eb-9013-22251a6e5b8a.jpg)


## Herramientas

- Para entrenar el modelo se utilizo  [Amazon SageMaker](https://aws.amazon.com/sagemaker/) 

- El modelo entrenado se encuentra subido en un bucket de S3

- La api para cargar el modelo entrado y luego hacer predicciones fue desarrollada en python


## Arquitectura
![Publicación de aplicaciones web de AWS](https://user-images.githubusercontent.com/20384738/98444811-7356ea00-20d9-11eb-9311-051c2980ea48.png)




## Como Funciona
>Se sube una imagen desde el lado del cliente y esta hace una peticion a la API 
### Pascal
>La api hace uso del modelo entrenado, almacenando temporalmente la imagen en formato base64 en el servidor, luego intenta predecir de que tipo es, y se devuelve el porcentaje mas alto.


## License

- **[MIT license](http://opensource.org/licenses/mit-license.php)**

## Soporte


- Twitter at <a href="https://twitter.com/cehernandezz" target="_blank">`@cehernandezz`</a>

---
