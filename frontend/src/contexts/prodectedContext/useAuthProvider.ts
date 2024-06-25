import { useContext } from "react";
import { ProdectedContext } from ".";

export function useAuthProvider(){
    const context=useContext(ProdectedContext);
    if(!context){
        throw Error("useAuthProvider must be within the AuthProvider");
    }
    return context;
}