import axiosInstance from '../../services/axiosInstance';

export const register = (userData) => async (dispatch) => {
    try {
        const response = await axiosInstance.post('users/register/', userData);
        dispatch({ type: 'REGISTER_SUCCESS', payload: response.data });
        return response.data;
    } catch (error) {
        const errorMessage = error.response && error.response.data ? error.response.data : 'Registration Failed';
        dispatch({ type: 'AUTH_ERROR', payload: errorMessage });
        throw errorMessage;
    }
};

export const login = (credentials) => async (dispatch) => {
    try {
        const response = await axiosInstance.post('users/login/', credentials);
        if (response.data && response.data.token) {
            localStorage.setItem('token', response.data.token);
            dispatch({ type: 'LOGIN_SUCCESSS', payload: response.data });
        } else {
            throw new Error('Token not provided in the response');
        }
    } catch (error) {
        const errorMessage = error.response && error.response.data ? error.response.data : 'Login Failed';
        dispatch({ type: 'AUTH_ERROR', payload: errorMessage });
    }
};

export const logout = () => {
    localStorage.removeItem('token');
    return { type: 'LOGOUT' };
};