import api from "..";


export async function getAllGroceriesStatuses() {
    return await api.get('groceries-statuses/')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getEmptyGroceriesStatus() {
    return await api.get('groceries-statuses/empty')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getSpecificGroceriesStatus(payload) {
    return await api.get(`groceries-statuses/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function createGroceriesStatus(payload) {
    return await api.post('groceries-statuses/', payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function updateGroceriesStatus(payload) {
    return await api.patch(`groceries-statuses/${payload.uid}`, payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
export async function deleteGroceriesStatus(payload) {
    return await api.delete(`groceries-statuses/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
