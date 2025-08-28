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

export async function revokeToken(token) {
    return await api.post("/auth/signout", token)
    .then((response) => {
        return response;
    }).catch((error) => {
        console.error(error);
    });
}

export async function refreshToken(token) {
    return await api.post("/auth/refresh", token)
    .then((response) => {
        return response;
    }).catch((error) => {
        console.error(error);
    });
}