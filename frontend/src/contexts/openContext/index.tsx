import React, { createContext, useState } from 'react'

interface IOpenContext{
    isLoggedIn: boolean,
    setIsLoggedin: React.Dispatch<React.SetStateAction<boolean>>
}

export const OpenContext = createContext<IOpenContext|undefined>(undefined)

const OpenProvider:React.FC<React.PropsWithChildren> = ({children}) => {
    const [isLoggedIn,setIsLoggedin]=useState(false);
    const Providervalue:IOpenContext={
        isLoggedIn:isLoggedIn,
        setIsLoggedin:setIsLoggedin
    }
  return (
    <OpenContext.Provider value={Providervalue} >
        {children}
    </OpenContext.Provider>
  )
}

export default OpenProvider