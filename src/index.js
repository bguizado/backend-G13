import express from "express";
import cors from "cors";

const servidor = express();
servidor.use(express.json());
servidor.use(cors());

const PORT = procces.env.PORT ?? 3000;

servidor.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
});