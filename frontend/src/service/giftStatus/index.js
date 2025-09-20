import api from "..";


export async function getAllGiftStatuses() {
    return await api.get('gift-statuses/')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getEmptyGiftStatus() {
    return await api.get('gift-statuses/empty/')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getSpecificGiftStatus(payload) {
    return await api.get(`gift-statuses/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function createGiftStatus(payload) {
    return await api.post('gift-statuses/', payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function updateGiftStatus(payload) {
    return await api.patch(`gift-statuses/${payload.uid}`, payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
export async function deleteGiftStatus(payload) {
    return await api.delete(`gift-statuses/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
