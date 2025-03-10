// proxy.js (Node.js backend example)
const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio'); // To parse HTML responses
const app = express();
const port = 3000;

app.use(express.static('public'));  // Serve HTML files from the 'public' folder

// Route to fetch Bing search results
app.get('/search', async (req, res) => {
    const query = req.query.q;
    const url = `https://www.bing.com/search?q=${encodeURIComponent(query)}`;

    try {
        const response = await axios.get(url);
        const $ = cheerio.load(response.data);
        let results = [];

        $('li.b_algo').each((index, element) => {
            const title = $(element).find('h2').text();
            const link = $(element).find('a').attr('href');
            if (title && link) {
                results.push({ title, link });
            }
        });

        res.json(results); // Send the results back to the frontend
    } catch (error) {
        res.status(500).send('Error fetching results from Bing');
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
