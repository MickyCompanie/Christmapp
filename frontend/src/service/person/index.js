import api from "..";

export async function getAllPerson(){
    return await api.get('persons/')
    .then((response) => {
        return response
    }).catch((error) => {
        console.error(error)
    })
}

export async function getEmptyPerson(){
    return await api.get('persons/empty')
    .then((response) => {
        return response
    }).catch((error) => {
        console.error(error)
    })
}

export async function getSpecificPerson(payload){
    return await api.get(`persons/${payload}`)
    .then((response) => {
        return response
    }).catch((error) => {
        console.error(error)
    })
}

export async function createPerson(payload){
    return await api.post('persons/', payload)
    .then((response) => {
        return response
    }).catch((error) => {
        console.error(error)
    })
}

export async function updatePerson(payload) {
    return await api.patch(`persons/${payload.uid}`, payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function deletePerson(payload){
    return await api.delete(`persons/${payload}`)
    .then((response) => {
        return response
    }).catch((error) => {
        console.error(error)
    })
}