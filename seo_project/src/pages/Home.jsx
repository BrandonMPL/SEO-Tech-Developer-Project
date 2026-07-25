import SearchBooks from '../components/Search'
import Header from '../components/Header'

function Home(){
    return(
        <main className="app">
            <Header className="app-header">
                <p>You're best friend in creating your own personalized study plan.</p>
            </Header>

            <section className="planner-card">
                <SearchBooks />

            </section>
        </main>
    )
}

export default Home;