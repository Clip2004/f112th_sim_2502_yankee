CLEANUP PROPOSAL FOR f112th_sim_2502_yankee

Resumen
- Autor: GitHub Copilot (asistente)
- Propósito: listar archivos/carpetas que parecen redundantes, temporales o duplicados y proponer acciones (mover a `archive/` dentro del paquete o eliminar definitivamente) para mantener el repositorio limpio.
- Acción propuesta por defecto (reversible): mover a `archive/` dentro del paquete. No realizaré cambios sin tu aprobación.

Propuesta detallada
1) worlds/final_world
   - Tipo: fichero sin extensión en `worlds/`.
   - Motivo: parece un archivo temporal o binario incompleto; no tiene extensión reconocible (.world) y no encaja con otros nombres.
   - Acción propuesta: mover a `archive/worlds/final_world` para inspección.

2) worlds/rviz_sim_world.rvizrviz
   - Tipo: archivo con extensión duplicada.
   - Motivo: existe `rviz_sim_world.rviz`; este archivo parece una copia mal nombrada.
   - Acción propuesta: mover a `archive/worlds/` o eliminar (recomendado: mover a `archive/`).

3) worlds/room_world/  (y su subdirectorio duplicado `room_world/room_world`)
   - Tipo: modelos de Gazebo con duplicado de estructura de carpetas.
   - Motivo: hay una carpeta `room_world/room_world/` dentro de la misma ruta; probablemente copias generadas por el editor de modelos.
   - Acción propuesta: conservar una sola copia funcional en `worlds/room_world/` y mover la(s) copia(s) redundante(s) a `archive/models/room_world_copy_*/`.

4) worlds/Untitled/
   - Tipo: carpeta de modelo con nombre genérico "Untitled".
   - Motivo: suele ser un modelo de prueba o plantilla generado por Gazebo/Editor.
   - Acción propuesta: mover a `archive/models/Untitled/`.

5) worlds/walls_test/pista_cerrada/
   - Tipo: modelo dentro de `walls_test/`.
   - Motivo: revisar si se usa en escenarios activos; puede ser prueba local.
   - Acción propuesta: mover a `archive/models/walls_test/pista_cerrada/` si no es necesario.

6) .vscode/
   - Tipo: configuración del editor VS Code.
   - Motivo: ajustes del desarrollador local; en proyectos compartidos suelen omitirse o añadirse a `.gitignore`.
   - Acción propuesta: mantener fuera del repo (añadir a `.gitignore`) o dejar si el equipo necesita compartir esa configuración. No moveré ni eliminaré sin confirmar.

Notas y pasos propuestos
- Si aceptas, realizaré los siguientes pasos en un único commit:
  1. Crear `archive/` dentro de `f112th_sim_2502_yankee/` con subcarpetas `worlds/` y `models/` según corresponda.
  2. Mover los archivos/carpetas listados a las rutas dentro de `archive/` (preservando estructura original cuando sea posible).
  3. Añadir `.gitkeep` en carpetas `archive/` para que se mantengan en git si están vacías.
  4. Actualizar `README.md` (esto ya fue hecho) y añadir una nota en `CLEANUP_PROPOSAL.md` con los movimientos realizados.

- Si prefieres, puedo en vez de mover, crear un `cleanup-PR` con los cambios propuestos para que los revises antes de mezclar.

Confirmación requerida
- Responde con una de las opciones:
  - `archive`: mover los archivos propuestos a `archive/` y crear un commit (reversible).
  - `pr`: crear una rama/PR con los cambios propuestos para revisión (no mover nada en `main`).
  - `none`: no hacer cambios; solo dejar esta propuesta en el repo.

Si eliges `archive` o `pr`, indicar si quieres que incluya también `.vscode/` en `.gitignore`.

---

Acciones realizadas (por petición: `archive`)
- Se creó la carpeta `archive/` con subdirectorios `worlds/` y `models/`.
- Movimientos ejecutados:
  - `worlds/final_world` -> `archive/worlds/final_world` (si existía).
  - `worlds/rviz_sim_world.rvizrviz` -> `archive/worlds/rviz_sim_world.rvizrviz` (si existía).
  - `worlds/room_world/room_world` -> `archive/models/room_world_copy/` (si existía).
  - `worlds/Untitled/` -> `archive/models/Untitled/` (si existía).
  - `worlds/walls_test/pista_cerrada/` -> `archive/models/walls_test/pista_cerrada/` (si existía).
- Se añadieron archivos `.gitkeep` en `archive/`, `archive/worlds/` y `archive/models/`.

Estado actual: los archivos listados fueron movidos a `archive/` cuando existían en el repositorio. Si quieres revertir algún movimiento, indícalo y lo restauro.

Siguientes pasos recomendados (para completar el proceso en el control de versiones):
1. Revisa los cambios localmente y, desde la raíz del repositorio, ejecuta:

```bash
git add src/f112th_sim_2502_yankee/README.md \
    src/f112th_sim_2502_yankee/CLEANUP_PROPOSAL.md \
    src/f112th_sim_2502_yankee/archive/
git commit -m "chore: mover archivos temporales/duplicados a archive/ y actualizar README"
git push origin HEAD
```

2. Si prefieres que cree una rama y un PR con estos cambios en lugar de commitearlos directamente en `main`, puedo preparar las instrucciones o hacerlo si me indicas el remoto y me permites ejecutar `git` aquí (nota: la sesión anterior indicó un problema de repo cuando el comando se ejecutó desde otra carpeta; ahora la estructura muestra `.git` en la carpeta del paquete, por lo que los comandos anteriores deberían ejecutarse desde la raíz del repo).

Indica si quieres que además añada `.vscode/` a `.gitignore` y lo incluya en el commit.

