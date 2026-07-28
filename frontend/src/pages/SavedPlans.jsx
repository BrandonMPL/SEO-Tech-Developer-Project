import {useState} from 'react'
import { Link } from 'react-router-dom'

function SavedPlans(){
    const [plans] = useState(() => {
        return JSON.parse(localStorage.getItem('savedStudyPlans') || '[]')
    })
    return(
        <>
        <main className="app plans-page">
            <header className="app-header">
                <Link className="back-link" to="/">
                    Back to Search
                </Link>

                <h1>Saved Study Plans</h1>
                <p>Review the plans you have created</p>
            </header>

            <section className='saved-plans-list'>
                {plans.length === 0? (
                    <div className='empty-plans'>
                        <h2>No saved plans yet</h2>
                        <p>Create a study plan on the home page, then save it here</p>
                    </div>
                ) :
                (
                    plans.map((plan) => (
                        <article className = "saved-plan-card"
                        key={plan.id}>
                        <p className="saved-date">Saved</p>
                        <h2> {plan.title}</h2>
                        <p>Based on: {plan.selectedTitles}</p>

                        <ol>
                            {plan.weeks.map((week) =>(
                                <li key={week}>{week}</li>
                            ))}
                        </ol>
                        </article>
                    ))
                )}
            </section>
        </main>
        </>

    )
}
export default SavedPlans;