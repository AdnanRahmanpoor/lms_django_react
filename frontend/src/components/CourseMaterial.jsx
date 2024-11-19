import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './styles.css';

const CourseMaterial = () => {
    const { materialId } = useParams();
    const [material, setMaterial] = useState(null);

    useEffect(() => {
        axios.get(`/api/materials/${materialId}/`)
        .then(response => setMaterial(response.data))
        .catch(error => console.error('Error fetching material:', error));
    }, [materialId]);

    return material ? (
        <div className="course-material">
            <h2>{material.title}</h2>
            <p>Type: {material.material_type}</p>
            <a href={material.file} download>Download Material</a>
        </div>
    ) : <p>Loading...</p>;
};

export default CourseMaterial;