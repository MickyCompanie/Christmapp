import api from "..";


export async function getAllWishes() {
    return await api.get('/wishes/')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getSpecificWish(payload) {
    return await api.get(`/wishes/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getEmptyWish() {
    return await api.get('/wishes/empty')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function createWish(payload) {
    return await api.post('/wishes/', payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function updateWish(payload) {
    return await api.patch(`/wishes/${payload.uid}`, payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
export async function deleteWish(payload) {
    return await api.delete(`/wishes/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
