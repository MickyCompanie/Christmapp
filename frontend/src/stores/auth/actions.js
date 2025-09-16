import { signin, signup, revokeToken, getUser } from "../../service/auth";
import { updatePerson } from "../../service/person";

import router from "@/router"


export default {
    async signUp(payload) {
        const response = await signup(payload).then((res) => {
            this.login(payload)
        })


    },

    async login(payload, fromSignUp) {
        const response = await signin(payload);
        this.accessToken = response.data.access_token;
        this.refreshToken = response.data.refresh_token;
        localStorage.setItem("accessToken", response.data.access_token);
        localStorage.setItem("refreshToken", response.data.refresh_token);
        this.getCurrentUser();

        router.push({name: fromSignUp ? "profile" : "home"})
    },


    async getCurrentUser() {
        return await getUser().then((response) => {
            this.user = response.data
        }).catch(() => {
            this.logout()
        });
    },

    async logout() {
        return await revokeToken().then(() => {
            this.accessToken = null;
            this.refreshToken = null;
            localStorage.removeItem("accessToken");
            localStorage.removeItem("refreshToken");

            router.push({name: "signin"})
        })
    },

    async proceedToUpdatePerson(payload){
        return await updatePerson(payload).then((res) => {
            this.user.person = res.data
            router.push({name: "home"})
        })
    }
};