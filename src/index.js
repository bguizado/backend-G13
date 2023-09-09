import express from "express";
import cors from "cors";
import { equipoRouter } from "./routes/equipo.routes.js";
import { usuarioRouter } from "./routes/usuario.routes.js";
import { partidoRouter } from "./routes/partido.routes.js";

const servidor = express();
servidor.use(express.json());
servidor.use(cors());

servidor.use(equipoRouter);
servidor.use(usuarioRouter);
servidor.use(partidoRouter);

const PORT = process.env.PORT ?? 3000;

servidor.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
});