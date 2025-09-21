const express = require('express');
const sqlite = require('sqlite3').verbose();
const websocket = require('ws');

const app = express();
const database = new sqlite.Database('cars.db');

app.use(express.json());

const wss = new websocket.Server({ port: 3001 });

wss.on('connection', (ws) => {
  console.log('Websocket new connection!');
});

function broadcastMessage(message) {
  wss.clients.forEach((client) => {
    if (client.readyState === websocket.OPEN) {
      client.send(JSON.stringify(message));
    }
  });
}

database.run(`
  CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    kilometers INTEGER NOT NULL,
    transmission TEXT NOT NULL,
    fuelType TEXT NOT NULL
  )
`);

const PORT = 3000;

// Get all cars
app.get('/cars', (req, res) => {
  console.log(`[GET /cars] Request received`);
  database.all('SELECT * FROM cars', [], (err, rows) => {
    if (err) {
      console.error(`[GET /cars] Error: ${err.message}`);
      res.status(500).json({ error: err.message });
    } else {
      console.log(`[GET /cars] Successfully retrieved ${rows.length} cars`);
      res.json(rows);
    }
  });
});

// Add a car
app.post('/cars', (req, res) => {
  console.log(`[POST /cars] Request received with body:`, req.body);
  const { name, price, kilometers, transmission, fuelType } = req.body;

  database.run(
    'INSERT INTO cars (name, price, kilometers, transmission, fuelType) VALUES (?, ?, ?, ?, ?)',
    [name, price, kilometers, transmission, fuelType],
    function (err) {
      if (err) {
        console.error(`[POST /cars] Error: ${err.message}`);
        res.status(500).json({ error: err.message });
      } else {
        const newCar = {
          id: this.lastID,
          name,
          price,
          kilometers,
          transmission,
          fuelType,
        };
        console.log(`[POST /cars] Car added with ID: ${this.lastID}`);

        broadcastMessage({ type: 'add', payload: newCar });

        res.json(newCar);
      }
    }
  );
});

// Update a car
app.put('/cars/:id', (req, res) => {
  const { id } = req.params;
  console.log(`[PUT /cars/:id] Request received for ID: ${id} with body:`, req.body);
  const { name, price, kilometers, transmission, fuelType } = req.body;

  database.run(
    'UPDATE cars SET name = ?, price = ?, kilometers = ?, transmission = ?, fuelType = ? WHERE id = ?',
    [name, price, kilometers, transmission, fuelType, id],
    function (err) {
      if (err) {
        console.error(`[PUT /cars/:id] Error for ID ${id}: ${err.message}`);
        res.status(500).json({ error: err.message });
      } else {
        console.log(`[PUT /cars/:id] Car with ID ${id} updated. Changes: ${this.changes}`);
        const updatedCar = {
          id,
          name,
          price,
          kilometers,
          transmission,
          fuelType,
        };

        broadcastMessage({ type: 'update', payload: updatedCar });

        res.json(updatedCar);
      }
    }
  );
});

// Delete a car
app.delete('/cars/:id', (req, res) => {
  const { id } = req.params;
  console.log(`[DELETE /cars/:id] Request received for ID: ${id}`);

  database.run('DELETE FROM cars WHERE id = ?', [id], function (err) {
    if (err) {
      console.error(`[DELETE /cars/:id] Error for ID ${id}: ${err.message}`);
      res.status(500).json({ error: err.message });
    } else {
      console.log(`[DELETE /cars/:id] Car with ID ${id} deleted. Changes: ${this.changes}`);

      broadcastMessage({ type: 'delete', payload: { carId: parseInt(id) } });

      res.json({ changes: this.changes });
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
  console.log(`WebSocket server running at ws://localhost:3001`);
});
