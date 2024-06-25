import React, { createContext, useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { RootState } from "../../redux/store";
import { useNavigate } from "react-router-dom";


interface IloginValues {
    loggedIn:boolean,
    setLoggedIn:React.Dispatch<React.SetStateAction<boolean>>
}

export const ProdectedContext = createContext<IloginValues|undefined>(undefined);

const AuthProvider:React.FC<React.PropsWithChildren>=({children})=>{
    const token = useSelector((state:RootState)=>state.auth.token);
    const [loggedIn,setLoggedIn]=useState<boolean>(true);
    const navigate = useNavigate();
    if(!token){
        setLoggedIn(false);
    }

    useEffect(()=>{
        console.log(token);
        if(!loggedIn){
            navigate("/login");
        }
    },[loggedIn,navigate,token]);

    return(
        <ProdectedContext.Provider value={{loggedIn,setLoggedIn}}>
            {children}
        </ProdectedContext.Provider>
    )
}



export default AuthProvider;


