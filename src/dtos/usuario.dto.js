import { TipoUsuario } from "@prisma/client";
import Joi from "joi";

export const registroUsuarioDto = Joi.object({
    nombre: Joi.string().required(),
    email: Joi.string().email().required(),
    password: Joi.string().regex(new RegExp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%-*]).{6,}$"
    )).message({
        'string.pattern.base':'El password debe contener al menos una mayuscula, una minuscula, un numero, un caracter especial y no ser menor de 6 caracteres'
    }).required(),
    tipoUsuario: Joi.string().valid(TipoUsuario.ADMIN, TipoUsuario.CLIENTE).optional(),
});

export const loginDto = Joi.object({
    email: Joi.string().email().required(),
    password: Joi.string().required(),
})