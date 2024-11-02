const initialState = {
    user: null,
    token: localStorage.getItem('token'),
    isAuthenticated: false,
    error: null,
};

export const authReducer = (state = initialState, action) => {
    switch (action.type) {
        case 'REGISTER_SUCCES':
            return { ...state, user: action.payload, isAuthenticated: true, error: null};
        case 'LOGIN_SUCCESS':
            return { ...state, user: action.payload.user, token: action.payload.token, isAuthenticated: true, error: null};
        case 'AUTH_ERROR':
            return { ...state, error: action.payload };
        case 'LOGOUT':
            return { ...state, user: null, token: null, isAuthenticated: false, error: null };
        default:
            return state;
    }
};