// server.js
const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());

app.get('/api/jobs', (req, res) => {
  // Retrieve jobs from the database
  const jobs = [
    { id: 1, title: 'Software Engineer', description: 'Lorem ipsum dolor sit amet.' },
    { id: 2, title: 'Web Developer', description: 'Consectetur adipiscing elit.' },
    { id: 3, title: 'Data Analyst', description: 'Praesent ac nisl eget est.' },
  ];

  res.json(jobs);
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});