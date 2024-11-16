import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './styles.css';

const EnrollmentList = () => {
    const [enrollments, setEnrollments] = useState([]);

    useEffect(() => {
        axios.get('/api/enrollment/')
        .then(response => setEnrollments(response.data))
        .catch(error => console.error('Error fetching enrollments:', error));
    }, []);

    return(
        <div className='enrollment-list'>
            <h2>My Enrollments</h2>
            <ul>
                {enrollments.map(enrollment => (
                    <li key={enrollment.id}>{enrollment.course.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default EnrollmentList;