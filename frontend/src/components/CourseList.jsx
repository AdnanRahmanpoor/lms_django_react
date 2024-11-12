import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import './styles.css';

const CourseList = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        axios.get('/api/courses/')
        .then(response => setCourses(response.data))
        .catch(error => console.error('Error fetching courses:', error));
    }, []);

    return(
        <div className="course-list">
            <h2>Available Courses</h2>
            {courses.map(course => (
                <div className="course-card" key={course.id}>
                    <h3>{course.title}</h3>
                    <p>{course.description}</p>
                    <Link to={`/courses/${course.id}`}>View Details</Link>
                </div>
            ))}
        </div>
    );
};

export default CourseList;