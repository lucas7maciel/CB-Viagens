const animDuration: number = 1000 //ms

function playErrorAnim(ref) {
  try {
    ref.classList.add('error_input')
    setTimeout(() => {
      ref.classList.remove('error_input')
    }, animDuration)
  } catch (error) {
    console.error('Error occurred while manipulating the class:', error)
  }
}

export function checkUsername(
  value: string | null,
  ref,
  setMessage: (value: string) => void
): boolean {
  let ok: boolean = false

  if (!value) {
    setMessage('Username vazio')
  } else if (value.length < 4) {
    setMessage('Username deve ter ao menos 4 caracteres')
  } else if (value.length > 15) {
    setMessage('Username deve ter no máximo 15 caracteres')
  } else {
    ok = true
  }

  if (!ok) playErrorAnim(ref)

  return ok
}

export function checkPassword(value: string, ref, setMessage: (value: string) => void): boolean {
  let ok: boolean = false

  if (!value) {
    setMessage('Senha vazia')
  } else if (value.length < 4) {
    setMessage('Senha deve ter ao menos 4 caracteres')
  } else if (value.length > 15) {
    setMessage('Senha deve ter no máximo 15 caracteres')
  } else {
    ok = true
  }

  if (!ok) playErrorAnim(ref)

  return ok
}

export function confirmPassword(
  value: string,
  password: string,
  ref,
  setMessage: (value: string) => void
): boolean {
  let ok: boolean = false

  if (!value) {
    setMessage('Confirme a senha')
  } else if (value != password) {
    setMessage('Senhas diferentes')
  } else {
    ok = true
  }

  if (!ok) playErrorAnim(ref)
  return ok
}

export function checkFirstName(
  value: string | null,
  ref,
  setMessage: (value: string) => void
): boolean {
  let ok: boolean = false

  if (!value) {
    setMessage('Nome vazio')
  } else if (value.length < 2) {
    setMessage('Nome deve ter ao menos 2 caracteres')
  } else if (value.length > 20) {
    setMessage('Nome deve ter no máximo 20 caracteres')
  } else {
    ok = true
  }

  if (!ok) playErrorAnim(ref)

  return ok
}

export function checkLastName(
  value: string | null,
  ref,
  setMessage: (value: string) => void
): boolean {
  let ok: boolean = false

  if (!value) {
    setMessage('Sobrenome vazio')
  } else if (value.length < 2) {
    setMessage('Sobrenome deve ter ao menos 2 caracteres')
  } else if (value.length > 20) {
    setMessage('Sobrenome deve ter no máximo 20 caracteres')
  } else {
    ok = true
  }

  if (!ok) playErrorAnim(ref)

  return ok
}
