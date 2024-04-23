export async function getId() {
  try {
    const token: string | null = localStorage.getItem('token')
    const headers: HeadersInit | undefined = {
      Authorization: `Token ${token}`
    }
    const res = await fetch(`${import.meta.env.VITE_API_URL}/auth/users/me`, { headers })

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

  return null
}
