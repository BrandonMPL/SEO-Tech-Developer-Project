import { useState } from 'react'

const mockBooks = [
    {id: 'book-1',
    title: 'Eloquent JavaScript',
    author: 'Marijn Haverbeke',
    },
    {
        id: 'book-2',
        title: 'JavaScript: The Good Parts',
        author: 'Douglas Crockford',
    },
    {
        id: 'book-3',
        title: 'You Don’t Know JS Yet',
        author: 'Kyle Simpson',
    },
]

function SearchBooks(){
    const [search, setSearch] = useState("");
    const [books, setBooks] = useState([]);

    const [selectedBooks, setSelectedBooks] = useState([]);

    const [studyPlan, setStudyPlan] = useState(null)
    const [savedMessage, setsavedMessage] = useState('')

    function searchBooks() {
        const searchTerm = search.trim().toLowerCase()

        const matchingBooks = mockBooks.filter((book) =>
            `${book.title} ${book.author}`.toLowerCase().includes(searchTerm)
        )
    setBooks(matchingBooks)
    }

    function toggleBook(book) {
        const isAlreadySelected = selectedBooks.some(
            (selectedBook) => selectedBook.id === book.id
        )

        if (isAlreadySelected) {
            setSelectedBooks(
            selectedBooks.filter((selectedBook) => selectedBook.id !== book.id)
            )
            } else {
            setSelectedBooks([...selectedBooks, book])
            }
        }
    
    function generateStudyPlan(){
        const selectedTitles = selectedBooks
        .map((book)=>book.title).join(', ')

        setStudyPlan({
            title: `${search || 'Custom'} Study Plan`,
            selectedTitles,
            weeks: [
                'Week 1: Read the introduction and first chapters.',
        'Week 2: Take notes on the main concepts.',
        'Week 3: Complete practice exercises or a small project.',
        'Week 4: Review your notes and test your understanding.',
            ],
        })
    }

    function saveStudyPlan(){
        const existingPlans = JSON.parse(
            localStorage.getItem('savedStudyPlans') || '[]'
        )
        const planToSave = {
            id: Date.now(),
            ...studyPlan,
            savedAT: new Date().toLocaleDateString(),
        }
        localStorage.setItem(
            'savedStudyPlans',
            JSON.stringify([...existingPlans, planToSave])
        )
        setsavedMessage('Study Plan Saved')
    }
    
    return (
        <>
        <h2>Search Topics to Study For:</h2>
        <input type="text"
            placeholder="Enter study topic"
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            className="primary-input"
        />

        <button className="primary-button" onClick={searchBooks}>
            Search
        </button>

        {books.length > 0 && (
            <div >
                <h3>Suggested Books</h3>

                {books.map((book) => {
                    const isSelected = selectedBooks.some(
                        (selectedBook) => selectedBook.id === book.id)

                return (
                    <label className={`book-result ${isSelected ? 'selected' : ''}`}
                key={book.id}>
                <input  type="checkbox"
                checked={isSelected}
                onChange={() => toggleBook(book)}/>

                <div>
                    <h4>{book.title}</h4>
                    <p>By {book.author}</p>
                </div>
            </label>
            )
        })}

            {books.length > 0 && (
                <p className="selection-count">
                {selectedBooks.length} book(s) selected
                </p>
            )}
        </div>
        )}

        <button
        className = "primary-button"
        onClick={generateStudyPlan}
        disabled={selectedBooks.length === 0}>
            Generate Study Plan
        </button>

        {studyPlan && (
            <section className='study-plan'>
                <h3>
                    {studyPlan.title}
                </h3>
                <p>
                    Based on: {studyPlan.selectedTitles}
                </p>
                <ol>
                    {studyPlan.weeks.map((week) =>
                    (
                        <li key={week}>{week}</li>
                    ))}
                </ol>

                <button className='primary-button'
                onClick={saveStudyPlan}>
                    Save study plan
                </button>
                {savedMessage && (
                    <p className='save-message'>{savedMessage}</p>
                )}
            </section>
        )}
        </>
    );
}

export default SearchBooks;


/*laber for="books">Type Here</laber>
        <input type="books"></input>
*/
