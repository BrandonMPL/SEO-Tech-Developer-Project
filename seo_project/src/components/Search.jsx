import { useState } from 'react'


function SearchBooks(){
    const [search, setSearch] = useState("");
    const [books, setBooks] = useState([]);

    const [selectedBooks, setSelectedBooks] = useState([]);

    async function searchBooks(){
        const response = await fetch("http://localhost:8000/search",{
            method: "POST",
            headers: { 
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                    search:search,
                })
        });

        const data = await response.json();
        setBooks(data.books);
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

        <button className="primary-button">
            Search
        </button>
        </>
    );
}

export default SearchBooks;


/*laber for="books">Type Here</laber>
        <input type="books"></input>
*/
