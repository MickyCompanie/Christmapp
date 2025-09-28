import api from "..";


export async function getAllGifts() {
    return await api.get('gifts/')
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function getEmptyGift(){
    return await api.get('gifts/empty').then((response) => {
        return response
    }).catch((error) => {
        console.error(error)
    })
}

export async function getSpecificGift(payload) {
    return await api.get(`gifts/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function createGift(payload) {
    return await api.post('gifts/', payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function updateGift(payload) {
    return await api.patch(`gifts/${payload.uid}`, payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
export async function deleteGift(payload) {
    return await api.delete(`gifts/${payload}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}
