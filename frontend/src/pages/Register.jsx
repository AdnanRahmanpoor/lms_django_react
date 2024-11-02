import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { register } from '../redux/actions/authActions';

const Register = () => {
    const [formData, setFormData] = useState({ username: '', email: '', password: ''});
    const [message, setMessage] = useState('');
    const dispatch = useDispatch();
    const error = useSelector((state) => state.auth.error);

    const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const result = await dispatch(register(formData));
            setMessage(`Welcome, ${result.username}!`);
        } catch (error) {
            setMessage(error.toString());
        }
    };

    return (
        <div>
            <h2>Register</h2>
            {error && <p>{error}</p>}
            {message && <p>{message}</p>}
            <form onSubmit={handleSubmit}>
                <input type="text" name="username" placeholder='Username' onChange={handleChange} required/>
                <input type="email" name="email" placeholder='Email' onChange={handleChange} required/>
                <input type="password" name="password" placeholder='Password' onChange={handleChange} required/>
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Register;