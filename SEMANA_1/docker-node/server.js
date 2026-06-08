const express = require("express");

const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.json({ mensaje: "Hola desde Node.js dentro de Docker" });
});

app.get("/estado", (req, res) => {
  res.json({ estado: "ok", servicio: "docker-node" });
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Servidor Node.js escuchando en el puerto ${port}`);
});
