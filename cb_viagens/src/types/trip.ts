
export interface TripProps {
    id: number
    name: string
    price_confort: string
    price_econ: string
    city: string
    duration: string
    seat: string
    bed: string
}

export interface TripModalProps {
    active: boolean
    current: TripProps | null
}