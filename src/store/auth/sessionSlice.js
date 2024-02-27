import { createSlice } from "@reduxjs/toolkit";
const token = localStorage.getItem('token');

const initialState = {
    signedIn: token ? true : false
}

const sessionSlice = createSlice({
    name: 'auth/session',
    initialState,
    reducers: {
        setSignInSuccess: (state, action) => {
            state.signedIn = true;
            localStorage.setItem('token', action.payload);
        },
        setSignOutSuccess: (state, action) => {
            state.signedIn = false;
            localStorage.removeItem('token');
        }
    }
});

export const { setSignInSuccess, setSignOutSuccess } = sessionSlice.actions;

export default sessionSlice.reducer;