import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './styles.css';

const LessonDetail = () => {
    const { lessonId } = useParams();
    const [lesson, setLesson] = useState(null);

    useEffect(() => {
        axios.get(`/api/lessons/${lessonId}`)
        .then(response => setLesson(response.data))
        .catch(error => console.error('Error fetching lesson:', error));
    }, [lessonId]);

    return lesson ? (
        <div className="lesson-detail">
            <h2>{lesson.title}</h2>
            <p>{lesson.content}</p>
        </div>
    ) : <p>Loading...</p>;
};

export default LessonDetail;