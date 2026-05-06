En MX Linux puedes renombrar muchos archivos de imágenes fácilmente con varios métodos, desde herramientas de línea de comandos hasta scripts simples. [hostinger](https://www.hostinger.com/mx/tutoriales/renombrar-archivos-linux)

## Usando el comando rename

La forma más directa es usar `rename`, que permite renombrar masivamente usando expresiones regulares de Perl. Para numerar tus imágenes consecutivamente como 0001.jpg, 0002.jpg, etc., puedes usar un script sencillo. [alexhost](https://alexhost.com/es/faq/how-to-renaming-files-with-mv/)

## Script con bash y mv

Este script renombrará todas las imágenes jpg en el directorio actual con numeración secuencial: [comandoslinux.github](https://comandoslinux.github.io/comandos/rename.html)

```bash
#!/bin/bash
i=1
for FILE in *.jpg; do
  NEWNAME=$(printf '%04d.jpg' $i)
  mv "$FILE" "$NEWNAME"
  i=$((i+1))
done
```

Para incluir también archivos PNG, modifica el script para procesar ambas extensiones: [hostinger](https://www.hostinger.com/mx/tutoriales/renombrar-archivos-linux)

```bash
#!/bin/bash
i=1
for FILE in *.{jpg,png,JPG,PNG}; do
  [ -f "$FILE" ] || continue
  ext="${FILE##*.}"
  NEWNAME=$(printf '%04d.%s' $i "$ext")
  mv "$FILE" "$NEWNAME"
  i=$((i+1))
done
```

El formato `%04d` crea números con 4 dígitos rellenados con ceros (0001, 0002, etc.). Puedes cambiar el número de dígitos ajustando el valor (por ejemplo, `%03d` para 001, 002, etc.). [comandoslinux.github](https://comandoslinux.github.io/comandos/rename.html)

## Opción con rename y expresiones regulares

Si prefieres usar `rename` directamente para renombrar con patrones, primero asegúrate de tenerlo instalado: [alexhost](https://alexhost.com/es/faq/how-to-renaming-files-with-mv/)

```bash
sudo apt install rename
```

Para operaciones más complejas como agregar prefijos o reemplazar partes del nombre, `rename` funciona con expresiones regulares tipo Perl. Por ejemplo, para cambiar "DSC" por "FOTO" en todos los archivos: [reiser](https://www.reiser.cl/2021/01/09/renombrar-varios-archivos-a-la-vez-en-lote-desde-consola-linux/)

```bash
rename 's/DSC/FOTO/g' *
```

Sin embargo, para numeración secuencial simple, el script con bucle `for` es más adecuado. [comandoslinux.github](https://comandoslinux.github.io/comandos/rename.html)



Para ejecutar el script en MX Linux, sigue estos pasos: [computernewage](https://computernewage.com/2023/03/31/gnu-linux-scripting-bash-ejemplo-6/)

## Crear y guardar el script

1. Abre un editor de texto (como `nano`, `vim` o el editor gráfico que prefieras)
2. Copia el código del script
3. Guárdalo con un nombre descriptivo, por ejemplo: `renombrar.sh`

```bash
nano renombrar.sh
```

## Dar permisos de ejecución

Antes de ejecutarlo, necesitas hacerlo ejecutable con el comando `chmod`: [computernewage](https://computernewage.com/2023/03/31/gnu-linux-scripting-bash-ejemplo-6/)

```bash
chmod +x renombrar.sh
```

## Ejecutar el script

Tienes dos opciones para ejecutarlo: [computernewage](https://computernewage.com/2023/03/31/gnu-linux-scripting-bash-ejemplo-6/)

**Opción 1:** Ejecutar directamente (después de darle permisos):
```bash
./renombrar.sh
```

**Opción 2:** Ejecutar con bash explícitamente (no requiere permisos):
```bash
bash renombrar.sh
```

## Recomendación importante

Antes de ejecutar el script en tus imágenes reales, **haz una copia de seguridad** de los archivos. El renombrado es irreversible y si algo sale mal, podrías perder los nombres originales. [htcmania](https://www.htcmania.com/showthread.php?p=35141770)

También puedes probar primero el script en una carpeta de prueba con algunas imágenes de ejemplo para verificar que funciona como esperas. [computernewage](https://computernewage.com/2023/03/31/gnu-linux-scripting-bash-ejemplo-6/)
