import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import axios from 'axios';
import './styles.css';

const CourseDetail = () => {
    const { courseId } = useParams();
    const [course, setCourse] = useState(null);

    useEffect(() => {
        axios.get(`/api/courses/${courseId}/`)
            .then(response => setCourse(response.data))
            .catch(error => console.error('Error fetching course details:', error));
    }, [courseId]);

    return course ? (
        <div className="course-detail">
            <h2>{course.title}</h2>
            <p>{course.description}</p>
            <h3>Lessons</h3>
            <ul>
                {course.lessons.map(lesson => (
                    <li key={lesson.id}>
                        <Link to={`/courses/${course.id}/lessons/${lesson.id}`}>{lesson.title}</Link>
                    </li>
                ))}
            </ul>
        </div>
    ) : <p>Loading...</p>;
};

export default CourseDetail;