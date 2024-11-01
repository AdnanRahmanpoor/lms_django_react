import axiosInstance from '../../services/axiosInstance';

export const register = (userData) => async (dispatch) => {
    try {
        const response = await axiosInstance.post('users/register/', userData);
        dispatch({ type: 'REGISTER_SUCCESS', payload: response.data });
    } catch (error) {
        dispatch({ type: 'AUTH_ERROR', payload: error.response.data });
    }
};

export const login = (credentials) => async (dispatch) => {
    try {
        const response = await axiosInstance.post('users/login/', credentials);
        localStorage.setItem('token', response.data.token);
        dispatch({ type: 'LOGIN_SUCCESSS', payload: response.data });
    } catch (error) {
        dispatch({ type: 'AUTH_ERROR', payload: error.response.data });
    }
};

export const logout = () => {
    localStorage.removeItem('token');
    return { type: 'LOGOUT' };
};