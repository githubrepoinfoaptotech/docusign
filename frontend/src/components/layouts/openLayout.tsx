import React from 'react'
import { Outlet } from 'react-router-dom';
import OpenProvider from '../../contexts/openContext';
import OpenNavbar from '../openNavbar';

const OpenLayout: React.FC = () => {
    return (
        <OpenProvider>
            <OpenNavbar/>
            <Outlet />
        </OpenProvider>
    )
}

export default OpenLayout;