
export function translateError(message: string): string {
    if (message === 'A user with that username already exists.') {
        return 'Username já registrado'
    } 

    if (message === 'This password is too short. It must contain at least 8 characters.') {
        return 'Senha deve conter ao menos 8 caracteres'
    }

    if (message === 'This password is too common.') {
        return 'Esta senha é comum demais'
    }

    if (message === 'The password is too similar to the username.') {
        return 'Senha parecida demais com o username'
    }

    if (message === 'The password is too similar to the first name.') {
        return 'Senha parecida demais com o nome'
    }

    if (message === 'The password is too similar to the last name.') {
        return 'Senha parecida demais com o sobrenome'
    }

    return message
}