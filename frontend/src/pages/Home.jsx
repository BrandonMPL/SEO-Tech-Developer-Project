import SearchBooks from '../components/Search'
import Header from '../components/Header'
import { Link } from 'react-router-dom'

function Home(){
    return(
        <main className="app">
            <Header className="app-header">
                <p>You're best friend in creating your own personalized study plan.</p>
            </Header>

            <section className="planner-card">
                <SearchBooks />

            </section>

            <section className="view-plans-card">
                <div className='view-class-b'>
                    <h2>Your Saved Plans</h2>
                </div>

                <Link className="secondary-button" to="/plans">
                    View Plans
                </Link>
            </section>
        </main>
    )
}

export default Home;