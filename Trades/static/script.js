// Function to fetch trades and show the table
function fetchTrades() {
    const assetClass = document.getElementById('assetClass').value;
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const minPrice = parseFloat(document.getElementById('minPrice').value);
    const maxPrice = parseFloat(document.getElementById('maxPrice').value);
    const tradeType = document.getElementById('tradeType').value;

    const queryParams = new URLSearchParams();
    if (assetClass) queryParams.append('assetClass', assetClass);
    if (startDate) queryParams.append('startDate', startDate);
    if (endDate) queryParams.append('endDate', endDate);
    if (!isNaN(minPrice)) queryParams.append('minPrice', minPrice);
    if (!isNaN(maxPrice)) queryParams.append('maxPrice', maxPrice);
    if (tradeType) queryParams.append('tradeType', tradeType);

    const queryString = queryParams.toString();
    const url = `/api/trades?${queryString}`;   

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            const tradesTable = document.getElementById('tradesTable');
            tradesTable.innerHTML = '';

            // Create table header
            const tableHeaderRow = document.createElement('tr');
            for (const key in data[0]) {
                const th = document.createElement('th');
                th.textContent = key;
                tableHeaderRow.appendChild(th);
            }
            tradesTable.appendChild(tableHeaderRow);

            // Create table rows
            data.forEach((trade) => {
                const tableRow = document.createElement('tr');
                for (const key in trade) {
                    const td = document.createElement('td');
                    td.textContent = trade[key];
                    tableRow.appendChild(td);
                }
                tradesTable.appendChild(tableRow);
            });

            // Hide the home page and display the trades table page
            document.getElementById('homePage').style.display = 'none';
            document.getElementById('tablePage').style.display = 'block';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

// Function to go back to the home page and hide the table page
function goBack() {
    // Show the home page and hide the table page
    document.getElementById('homePage').style.display = 'block';
    document.getElementById('tablePage').style.display = 'none';
}