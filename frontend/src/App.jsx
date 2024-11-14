import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './pages/Register';
import Login from './pages/Login';
import CourseList from './components/CourseList';
import CourseDetail from './components/CourseDetail';
import LessonDetail from "./components/LessonDetail";

function App() {
    return (
        <Router>
            <div>
                <Routes>
                    <Route path="/register" element={<Register />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/" element={<CourseList />} />
                    <Route path="/courses/:courseId" element={<CourseDetail />} />
                    <Route path="/courses/:courseId/lessons/:lessonId" element={<LessonDetail />} />

                </Routes>
            </div>
        </Router>
    );
}

export default App;