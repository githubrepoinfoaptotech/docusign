import { combineReducers, configureStore } from "@reduxjs/toolkit";
import presistedAuthReducer from "./slicers/authSlice";
import { persistStore, FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER } from "redux-persist";



const coimbined_reducers= combineReducers({
    auth: presistedAuthReducer
})

const store = configureStore({
  reducer: coimbined_reducers,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    }),
})

// Can still subscribe to the store
store.subscribe(() => console.log(store.getState()))

const presist = persistStore(store);

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export default {store,presist};