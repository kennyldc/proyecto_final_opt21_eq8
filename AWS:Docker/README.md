# Configuración de AWS y Docker

## AWS

Para la realización de este proyecto se hizo uso de los servicios en la nube de AWS. Siguiendo la siguiente configuración:
### EC2
- AMI. Ubuntu Server 20.04 LTS (HVM), SSD Volume Type - ami-083654bd07b5da81d (64-bit x86)
- Instance Type. t2.micro
- Instance Details. Network: VPC propia,  Auto-assign Public IP: Enable
- Advance Details. User data: Se instalan docker en la instancia.
- Storage. Size (GiB): 8
- Security Group. Se creo SG propio con Source: My IP, y se habilitó el puerto 8888 para el uso de la imagen de Docker.

Más información sobre la configuración de AWS disponible en la siguente [liga](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/1.2.Instalaci%C3%B3n-de-herramientas-%C3%BAtiles-en-AWS).


## Docker

Para poder reproducir el contenido de este repositorio se recomienda el uso de la siguiente imagen usando los siguientes comandos.

```
docker run --rm -v <ruta a mi directorio>:/datos --name jupyterlab_optimizacion -p 8888:8888 -d palmoreck/jupyterlab_optimizacion:3.1.0

```

La información sobre la imagen se encuentra aquí. [palmoreck/jupyterlab_optimizacion:3.1.0](https://github.com/palmoreck/dockerfiles/blob/master/jupyterlab/optimizacion/3.1.0/Dockerfile)
