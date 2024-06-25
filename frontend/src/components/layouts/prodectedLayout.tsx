import React from 'react'
import { Outlet } from 'react-router-dom';
import OpenNavbar from '../openNavbar';
import AuthProvider from '../../contexts/prodectedContext';

const ProdectedLayout: React.FC = () => {
    return (
        <AuthProvider>
            <OpenNavbar/>
            <Outlet />
        </AuthProvider>
    )
}

export default ProdectedLayout;