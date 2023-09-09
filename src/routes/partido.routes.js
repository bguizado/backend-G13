import express from "express";
import { finalizarPartido, prueba } from "../controllers/partido.controller.js";
import { validarUsuario, validarUsuarioAdmin } from "../utils/validador.js";

export const partidoRouter = express.Router();

partidoRouter.post("/finalizar-partido/:id", finalizarPartido);
partidoRouter.post("/prueba", validarUsuario, validarUsuarioAdmin, prueba);