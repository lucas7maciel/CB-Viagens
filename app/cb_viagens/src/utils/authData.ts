export function getHeaders() {
  const token: string | null = localStorage.getItem('token')
  const headers: HeadersInit | undefined = {
    Authorization: `Token ${token}`
  }

  return {headers}
}

export async function getId() {
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/auth/users/me`, getHeaders())

    if (res.status === 401) {
      throw new Error('Unauthorized request');
    }

    if (!res.ok) {
      throw new Error('Falha no servidor')
    }

    const user = await res.json()

    if (!user) {
      throw new Error('Falha ao identificar usuário')
    }

    return user.data?.id
  } catch (error) {
    console.error(error)
  }

  return undefined
}

export function logout(router: any) {
  localStorage.setItem('token', '')
  router.push('signin')
}
