import React, { useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { login } from '../redux/actions/authActions';

const Login = () => {
    const [credentials, setCredentials] = useState({ username: '', password: '' });
    const dispatch = useDispatch();
    const error = useSelector((state) => state.auth.error);

    const handleChange = (e) => setCredentials({ ...credentials, [e.target.name]: e.target.value });

    const handleSubmit = (e) => {
        e.preventDefault();
        dispatch(login(credentials));
    };

    return (
        <div>
            <h2>Login</h2>
            {error && <p>{error}</p>}
            <form onSubmit={handleSubmit}>
                <input type="text" name="username" placeholder="Username" onChange={handleChange} required />
                <input type="text" name="password" placeholder="Password" onChange={handleChange} required />
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default Login;