import api from "..";


export async function updatePerson(payload) {
    console.log(`payload: ${JSON.stringify(payload)}`)
    return await api.patch(`persons/${payload.uid}`, payload)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}