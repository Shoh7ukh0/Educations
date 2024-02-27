import { combineReducers } from "@reduxjs/toolkit";
import sessionSlice from "./auth/sessionSlice";

const rootReducer = combineReducers({
    session: sessionSlice
});

export default rootReducer;