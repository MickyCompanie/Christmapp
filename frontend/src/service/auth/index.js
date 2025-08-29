import api from "..";

export async function signup(email, password) {
    return await api.post("/auth/signup", {
        email,
        password,
    }).then((response) => {
        return response;
    }).catch((error) => {
        console.error(error);
    });
}

export async function signin(payload) {
    return await api.post("/auth/login", 
        payload
    ).then((response) => {
        return response;
    }).catch((error) => {
        console.error(error);
    });
}

export async function getUser() {
    return await api.get("/auth/me")
    .then((response) => {
        return response;
    }).catch((error) => {
        console.error(error);
    });
}

export async function revokeToken() {
    return await api.get("/auth/logout")
    .then((response) => {
        return response;
    }).catch((error) => {
        console.error(error);
    });
}
