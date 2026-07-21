import { useState } from 'react'
import './App.css'
import Header from './components/Header'
import SearchBooks from './components/Search'
function App() {

  return (
    <main className="app">
      <header className="app-header">
        <h1>Study Planner</h1>
          <p>You're best friend in creating your own personalized study plan.</p>
      </header>

      <section className="planner-card">
        <SearchBooks />

      </section>
    </main>
  )
}

export default App
