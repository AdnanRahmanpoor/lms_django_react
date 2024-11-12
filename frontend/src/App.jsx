import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './pages/Register';
import Login from './pages/Login';


function App() {
    return (
        <Router>
            <div>
                <Routes>
                    <Route path="/register" element={<Register />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/" element={<CourseList />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;