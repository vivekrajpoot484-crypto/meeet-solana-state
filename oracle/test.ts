import { runPrediction } from "./engine.js";

const result = runPrediction("Will BTC reach $100k in 2025?");

console.log(JSON.stringify(result, null, 2));