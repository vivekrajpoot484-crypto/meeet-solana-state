import express from "express";
import { runPrediction } from "../oracle/engine.ts";

const router = express.Router();

router.post("/predict", (req, res) => {
  const { question } = req.body;

  if (!question) {
    return res.status(400).json({ error: "question required" });
  }

  const result = runPrediction(question);

  return res.json(result);
});

export default router;