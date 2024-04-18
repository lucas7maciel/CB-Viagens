
export interface UserProps {
    id: number,
    password: string,
    last_login: string | null,
    is_superuser: boolean,
    username: string,
    first_name: string | null,
    last_name: string | null,
    email: string | null,
    is_staff: boolean,
    is_active: boolean,
    date_joined: string | null,
    phone_number: string | null
}