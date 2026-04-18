**F112th Simulator**

- **Propósito**: Este paquete de ROS2 contiene la configuración necesaria para simular un robot diferencial (F1/12-like) en Gazebo, incluyendo descripción del robot, archivos de lanzamiento, mundos y parámetros útiles para pruebas de control y navegación.

- **Objetivo**: Proveer un entorno reproducible para desarrollar y probar controladores, teleoperación y algoritmos de planificación/seguimiento de trayectoria sobre un robot diferencial en simulación.

**Contenido Principal**
- **`description/`**: Archivos `xacro`/URDF que definen el robot y modelos auxiliares.
- **`launch/`**: Launch files de ROS2 para levantar la simulación completa (`launch_sim.launch.py`), teleoperación por joystick (`joystick.launch.py`), y demás configuraciones de lanzamiento.
- **`config/`**: Parámetros YAML para `joy`, `twist_mux`, `mapper`, y otros nodos de ejemplo.
- **`worlds/`**: Ficheros de mundos para Gazebo (varios escenarios de prueba).
- **`map/`**: Mapas y archivos de posegraph usados en pruebas de SLAM/localización.
- **`docs/`**: Documentación y notas históricas del proyecto.

**Requisitos y versiones recomendadas**
- **ROS2**: Este paquete está preparado para ROS2 (ament_cmake). Se ha probado con **ROS2 Humble**; funcionará con distros posteriores, pero verifica compatibilidad de `gazebo_ros` y otras dependencias.
- **Gazebo**: Se usa `gazebo_ros` (Gazebo clásico). Asegúrate de tener la versión compatible con tu distribución de ROS2.
- **Dependencias de sistema**: `ros-<distro>-gazebo-ros`, `ros-<distro>-joy`, `ros-<distro>-teleop-twist-joy`, `twist_mux`, y paquetes que el proyecto referencie.

**Instalación rápida**
1. Coloca este paquete dentro de tu workspace de ROS2, por ejemplo: `~/ros2_ws/src/`.
2. Desde la raíz del workspace compila con `colcon`:

```bash
cd ~/ros2_ws
colcon build --packages-select f112th_sim_2502_yankee
source install/setup.bash
```

3. Lanza la simulación (ejemplo):

```bash
ros2 launch f112th_sim_2502_yankee launch_sim.launch.py
```

Nota: Los `launch` incluidos usan internamente la variable `package_name` con el valor `f112th_sim_2502_yankee`. Si renombraste el paquete o el repositorio, reemplaza esa cadena por el nombre actual del paquete (o actualiza `package.xml`).

**Descripción de los launch files más importantes**
- **`launch_sim.launch.py`**: Incluye `rsp.launch.py` (robot_state_publisher), lanza Gazebo (`gazebo.launch.py` de `gazebo_ros`), y spawn del `robot_description` usando `spawn_entity.py`. Además lanza `joystick` y `twist_mux`.
- **`joystick.launch.py`**: Lanza `joy_node` y `teleop_node` para teleoperación con joystick.

**Configuración y personalización rápida**
- Cambiar posición de spawn: en `launch_sim.launch.py` en la sección `spawn_entity` puedes editar `-x`, `-y`, `-z`, `-Y` para ajustar dónde aparece el robot.
- Usar reloj simulado: los `launch` pasan `use_sim_time=true` a nodos que lo soportan.
- Parametrización: los ficheros en `config/` contienen parámetros listos para usar. Edita o añade archivos YAML según tu hardware/estrategia.

**Consideraciones y buenas prácticas**
- **Respaldos antes de cambios**: antes de borrar o mover archivos crea un backup o carpeta `archive/`.
- **Compatibilidad ROS2/Gazebo**: Verifica versiones; si observas mensajes de API incompatibles, ajusta tu distro de ROS2 o la versión de `gazebo_ros`.
- **Rendimiento**: Gazebo y los mundos complejos consumen recursos; cierra otras aplicaciones intensivas y reduce la calidad del mundo si es necesario.