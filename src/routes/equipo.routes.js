import express from "express";
import { listarEquipos } from "../controllers/equipos.controller.js";

export const  equipoRouter = express.Router()

equipoRouter.get("/equipos", listarEquipos);