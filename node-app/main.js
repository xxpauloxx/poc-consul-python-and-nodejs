const express = require("express");
const Consul = require("consul");
const app = express();
const port = process.env.SERVICE_PORT || 3000;

const consulClient = new Consul({host: "consul", port: "8500"});

app.get("/", async (_, res) => {
    data = await consulClient.kv.get("node-app/data");
    res.send(`Consul: ${data["Value"]}\n`);
});

app.listen(port, () => {
  console.log(`Node.js App listening at http://localhost:${port}`);
});
