import React, { useContext, useState, useEffect } from 'react';
import { NavContext, claseContext } from '../layouts/layoutProfesor';
import QRScanner from '../components/QRScanner'; // Asegúrate de que la ruta sea correcta

const Asistencias = () => {
  const { showNav } = useContext(NavContext);
  const { dataClase } = useContext(claseContext);
  const [matricula, setMatricula] = useState('');
  const [mensaje, setMensaje] = useState('');
  const [asistencias, setAsistencias] = useState([]);

  useEffect(() => {
    showNav();
    fetchAsistencias();
  }, [showNav, dataClase]);

  const fetchAsistencias = async () => {
    const nrc_clase = dataClase.nrc;
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/Asistencia/?materia_nrc=${nrc_clase}`);
      if (response.ok) {
        const result = await response.json();
        setAsistencias(result);
      } else {
        console.error('Error al obtener las asistencias:', response.statusText);
      }
    } catch (error) {
      console.error('Error al conectar con el servidor:', error);
    }
  };

  const handleGuardar = async () => {
    const nrc_clase = dataClase.nrc;
    const data = {
      matricula: matricula,
      materia_nrc: nrc_clase
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/api/Asistencia/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      if (response.ok) {
        const result = await response.json();
        setMensaje('Asistencia registrada correctamente.');
        console.log('Asistencia registrada:', result);
        fetchAsistencias(); // Actualiza la lista de asistencias
      } else {
        const errorData = await response.json();
        const detail = errorData.detail || '';

        if (detail.includes('Invalid pk')) {
          setMensaje('La matrícula no está registrada en el sistema.');
        } else if (detail.includes('no está inscrito en la clase')) {
          setMensaje('El alumno no está inscrito en la clase o no tiene una inscripción activa.');
        } else {
          setMensaje('Ocurrió un error al registrar la asistencia.');
        }
        console.error('Error:', errorData);
      }
    } catch (error) {
      setMensaje('Error al conectar con el servidor.');
      console.error('Error al conectar con el servidor:', error);
    }
  };

  const handleScan = (scannedMatricula) => {
    setMatricula(scannedMatricula); // Actualiza el campo de matrícula con el valor escaneado
  };

  return (
    <div className="items-center text-center mt-10">
      <h2 className="text-2xl font-bold">Sección de Asistencias</h2>

      <div className="mt-4">
        <label htmlFor="matricula" className="block text-xl font-medium text-white">
          Matrícula:
        </label>
        <input
          type="text"
          id="matricula"
          value={matricula}
          onChange={(e) => setMatricula(e.target.value)} // Permite la entrada manual
          className="mt-1 p-2 border border-gray-300 rounded text-black"
          placeholder="Ingresa la matrícula"
        />
      </div>

      <div className="mt-4">
        <button
          onClick={handleGuardar}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 mr-2"
        >
          Guardar
        </button>
      </div>

      {/* Mostrar el mensaje debajo del botón */}
      {mensaje && (
        <div className="mt-4 p-2 border border-white rounded text-red-500 w-11/12 sm:w-7/12 md:w-7/12 lg:w-7/12 xl:w-7/12 mx-auto">
          {mensaje}
        </div>
      )}

      <div className="mt-4 w-11/12 md:w-7/12 lg:w-7/12 mx-auto">
        <QRScanner onScan={handleScan} />
      </div>

      {/* Mostrar la tabla con las asistencias */}
      <div className="mt-10 w-11/12 md:w-7/12 lg:w-7/12 mx-auto">
        <h3 className="text-xl font-bold">Lista de Asistencias</h3>
        <table className="w-full mt-4 border-collapse border border-gray-300">
          <thead>
            <tr>
              <th className="border border-gray-300 p-2">Matrícula</th>
              <th className="border border-gray-300 p-2">Fecha</th>
            </tr>
          </thead>
          <tbody>
            {asistencias.map((asistencia) => (
              <tr key={asistencia.id_asistencia}>
                <td className="border border-gray-300 p-2">{asistencia.matricula}</td>
                <td className="border border-gray-300 p-2">{asistencia.fecha}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Asistencias;
