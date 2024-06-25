import { PayloadAction, createSlice } from '@reduxjs/toolkit'
import {persistReducer} from "redux-persist";
import storage from "redux-persist/lib/storage";

interface IAction{
    token:string|null,
    isLoggedin:boolean
}

const presistConfig={
    key:"auth",
    storage
}

const AuthSlice = createSlice({
  name: 'auth',
  initialState: {
    token:"",
    isLoggedin:false
  },
  reducers: {
    loggedinReducer: (state, action:PayloadAction<IAction>) => {
        if(action.payload.token){
            state.token = action.payload.token;
            state.isLoggedin = true;
        }else{
            state.token = "",
            state.isLoggedin = false
        }
    },
    loggedoutReducer: (state) => {
      state.token = "",
      state.isLoggedin = false
    }
  }
});

const presistedAuthReducer = persistReducer(presistConfig,AuthSlice.reducer);




export const { loggedinReducer, loggedoutReducer } = AuthSlice.actions;
export default presistedAuthReducer;