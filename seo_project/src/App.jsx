import { useState } from 'react'
import {BrowserRouter, Routes, Route} from "react-router-dom"
import './App.css'
import Home from "./pages/Home"
import SavedPlans from './pages/SavedPlans'


function App() {

  return (
    <BrowserRouter>
      <Routes>
          <Route
            path="/"
            element={<Home />}
          />

          <Route
            path="/plans"
            element={<SavedPlans />}
          />
      </Routes>
    
    </BrowserRouter>

  )
}

export default App
