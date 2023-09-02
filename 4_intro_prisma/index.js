import express from "express";
import Prisma from "@prisma/client";

const conexion = new Prisma.PrismaClient();

const servidor = express();

servidor.use(express.json());

const PORT = 3000;

servidor.route("/grados").post(async (req, res) => {
    const { body: data } = req;
    try {
        const resultado = await conexion.grado.create({
            data,
            // {
            //     nombreNumerico: body.nombreNumerico,
            //     nombreTexto: body.nombreTexto,
            // }
        });
        console.log(resultado);
        res.json({
            message: "Grado creado exitosamente",
        });
    } catch (error) {
        console.error("Error al crear el grado:", error);
        res.status(500).json({
            message: "Error al crear el grado",
            error: error.message, // Proporciona el mensaje de error específico
        });
    }
}).get(async (req, res) => {
    const resultado = await conexion.grado.findMany();

    res.json({
      content: resultado,
    });
  });

servidor.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
