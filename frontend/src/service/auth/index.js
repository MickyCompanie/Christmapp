import api from "..";
import { useNotificationsStore } from "@/stores/index.js";

export async function signup(payload) {
    const notificationsStore = useNotificationsStore();

    return await api.post("/auth/signup", payload)
    .then((response) => {
        return response;
    }).catch((error) => {
        notificationsStore.setNotification({
            message: error?.response?.data?.detail || null,
            statusCode: error?.response?.status || 500
        });
        
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

export async function getAllUsers(){
    return await api.get("users/")
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function upgradeUserRole(uid){
    return await api.post(`users/upgrade/${uid}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function downgradeUserRole(uid){
    return await api.post(`users/downgrade/${uid}`)
    .then((response) => {
        return response
    })
    .catch((error) => {
        console.error(error)
    })
}

export async function revokeToken() {
    return await api.get("/auth/logout")
    .then((response) => {
        return response;
    }).catch((error) => {
        console.error(error);
    });
}
