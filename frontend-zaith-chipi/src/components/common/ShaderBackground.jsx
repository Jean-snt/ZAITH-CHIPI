import React, { useRef, useEffect } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Vector2 } from 'three';

const fragmentShader = `
  uniform vec2 u_resolution;
  uniform vec2 u_mouse;
  uniform float u_time;

  // Función de ruido para las estrellas
  float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898, 78.233))) * 43758.5453123);
  }

  // Función para crear un "metaball" o punto de luz
  float metaball(vec2 coord, vec2 center, float radius) {
    return radius / distance(coord, center);
  }

  void main() {
    // Normalizamos las coordenadas
    vec2 st = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / u_resolution.y;
    vec2 mouse = (u_mouse - 0.5 * u_resolution.xy) / u_resolution.y;

    float intensity = 0.0;

    // Puntos de luz que se mueven lentamente
    vec2 center1 = vec2(0.7 * cos(u_time * 0.15), 0.7 * sin(u_time * 0.2));
    vec2 center2 = vec2(0.6 * cos(u_time * 0.1), 0.6 * sin(u_time * 0.3));
    
    // El ratón actúa como un tercer punto de luz más sutil
    vec2 mouse_center = mouse * 1.2;

    // Sumamos la intensidad de los puntos de luz
    intensity += metaball(st, center1, 0.15);
    intensity += metaball(st, center2, 0.2);
    intensity += metaball(st, mouse_center, 0.08);

    // ---- Paleta de Colores "Nebulosa Cósmica" ----
    vec3 color_deep_space = vec3(0.01, 0.02, 0.06); // Azul casi negro del espacio profundo
    vec3 color_nebula_mid = vec3(0.1, 0.2, 0.7);   // Azul principal de la nebulosa
    vec3 color_nebula_highlight = vec3(0.8, 0.9, 1.0); // Blanco/Azul claro para los brillos

    // Mezclamos los colores para un efecto más suave y gaseoso
    vec3 final_color = mix(color_deep_space, color_nebula_mid, smoothstep(0.5, 0.8, intensity));
    final_color = mix(final_color, color_nebula_highlight, smoothstep(0.9, 1.1, intensity));
    
    // ---- Efecto de Estrellas ----
    // Usamos ruido de alta frecuencia para generar puntos pequeños
    float stars = smoothstep(0.995, 1.0, random(st * 150.0));
    final_color += vec3(stars * 0.5); // Añadimos las estrellas al color final

    gl_FragColor = vec4(final_color, 1.0);
  }
`;

const ShaderPlane = () => {
  const meshRef = useRef();
  const mousePosition = useRef({ x: 0, y: 0 });

  useEffect(() => {
    const handleMouseMove = (event) => {
      mousePosition.current = { x: event.clientX, y: event.clientY };
    };
    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  useFrame(({ clock, size }) => {
    if (meshRef.current) {
        meshRef.current.material.uniforms.u_time.value = clock.getElapsedTime();
        meshRef.current.material.uniforms.u_mouse.value.x = mousePosition.current.x;
        meshRef.current.material.uniforms.u_mouse.value.y = size.height - mousePosition.current.y; // Invertimos Y
        meshRef.current.material.uniforms.u_resolution.value.x = size.width;
        meshRef.current.material.uniforms.u_resolution.value.y = size.height;
    }
  });

  return (
    <mesh ref={meshRef} scale={[window.innerWidth, window.innerHeight, 1]}>
      <planeGeometry args={[1, 1]} />
      <shaderMaterial
        fragmentShader={fragmentShader}
        uniforms={{
          u_time: { value: 0 },
          u_mouse: { value: new Vector2(0, 0) },
          u_resolution: { value: new Vector2(window.innerWidth, window.innerHeight) },
        }}
      />
    </mesh>
  );
};

const ShaderBackground = () => {
  return (
    <div style={{ position: 'fixed', top: 0, left: 0, width: '100vw', height: '100vh', zIndex: -1 }}>
      <Canvas>
        <ShaderPlane />
      </Canvas>
    </div>
  );
};

export default ShaderBackground;