import api from "..";


export async function getAllGroceries() {
    return await api.get('groceries/')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getEmptyGrocerie() {
    return api.get('groceries/empty')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getSpecificGrocerie(payload) {
    return await api.get(`groceries/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function createGrocerie(payload) {
    return await api.post('groceries/', payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function updateGrocerie(payload) {
    return await api.patch(`groceries/${payload.uid}`, payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
export async function deleteGrocerie(payload) {
    return await api.delete(`groceries/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
