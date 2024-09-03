document.getElementById('search-books').addEventListener('click', searchBooks);

function searchBooks() {
    const query = document.getElementById('search-query').value;
    if (!query) {
        alert('Please enter a book title');
        return;
    }

    const xhr = new XMLHttpRequest();
    const url = `https://openlibrary.org/search.json?q=${encodeURIComponent(query)}`; // Open Library API endpoint

    xhr.open('GET', url, true);

    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            const response = JSON.parse(xhr.responseText);
            displayBooks(response.docs);
        } else {
            console.error('Error fetching data:', xhr.statusText);
        }
    };

    xhr.onerror = function () {
        console.error('Request failed');
    };

    xhr.send();
}

function displayBooks(books) {
    const bookResultsDiv = document.getElementById('book-results');
    bookResultsDiv.innerHTML = '';

    if (books.length > 0) {
        books.forEach(book => {
            const bookElement = document.createElement('div');
            bookElement.className = 'book';
            bookElement.innerHTML = `
                <h3>${book.title}</h3>
                <p><strong>Author(s):</strong> ${book.author_name ? book.author_name.join(', ') : 'Unknown'}</p>
            `;
            bookResultsDiv.appendChild(bookElement);
        });
    } else {
        bookResultsDiv.innerHTML = '<p>No books found.</p>';
    }
}