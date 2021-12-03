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
