import express from "express";
import cors from "cors";
import predictRoute from "./api/predict.ts";

const app = express();

app.use(cors()); // 🔥 required
app.use(express.json());

app.use("/api", predictRoute);

app.listen(3000, () => {
  console.log("MEEET Oracle API running on port 3000");
});