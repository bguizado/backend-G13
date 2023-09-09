import { conexion } from "../conexion.js";

export const prueba = async (req, res) => {
    res.json({
        message: "Llego al final"
    });
};



export const finalizarPartido = async (req, res) => {
    const { id } = req.params;
    const partidoEncontrado = await conexion.partido.findUnique({
        where: { id: parseInt(id) },
    });

    if (partidoEncontrado.finalizado) {
        return res.json({
            message: "El partido ya finalizo!"
        })
    }

    if (partidoEncontrado.empezado === false) {
        return res.json({
            message: "El partido debe empezar para poder finalizarlo"
        });
    }

    await conexion.partido.update({
        data: {
            finalizado: true,
        },
        where: {
            id: partidoEncontrado.id,
        },
    });

    return res.json({
        message: "Partido finalizado exitosamente"
    });
};