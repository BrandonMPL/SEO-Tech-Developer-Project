import { Link } from 'react-router-dom'

function SavedPlans(){
    return(
        <>
        <main className="app">
            <header className="app-header">
                <h1>Saved Study Plans</h1>
            </header>
                <p>No study plans saved yet.</p>

            <Link className="back-link" to="/">
                Back to Search
            </Link>
        </main>
        </>

    )
}
export default SavedPlans;