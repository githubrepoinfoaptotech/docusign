
import './App.css'
import OpenLayout from './components/layouts/openLayout'
import Login from './pages/login'
import PdfViewer from './pages/pdf'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Signup from './pages/signup'
import ProdectedLayout from './components/layouts/prodectedLayout'
import Dashboard from './pages/dashboard'



function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<OpenLayout />}>
            <Route path='/' element={<PdfViewer path='/input.pdf' />} />
            <Route path='login' element={<Login />} />
            <Route path='signup' element={<Signup />} />
          </Route>

          <Route path='/pages/' element={<ProdectedLayout />}>
            <Route path='dashboard' element={<Dashboard/>} />
          </Route>

        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
