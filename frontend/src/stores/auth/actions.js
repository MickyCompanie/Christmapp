import { 
    signin,
    signup,
    revokeToken,
    getUser
} from "../../service/auth";

import router from "@/router"


export default {
    async signUp(payload) {
        const response = await signup(payload)
    },

    async login(payload) {
        const response = await signin(payload);
        this.accessToken = response.data.access_token;
        this.refreshToken = response.data.refresh_token;
        localStorage.setItem("accessToken", response.data.access_token);
        localStorage.setItem("refreshToken", response.data.refresh_token);
        this.getCurrentUser();


        router.push({name: "home"})
    },


    async getCurrentUser() {
        const response = await getUser();
        this.user = response.data;
    },

    async logout() {
        return await revokeToken().then(() => {
            this.accessToken = null;
            this.refreshToken = null;
            localStorage.removeItem("accessToken");
            localStorage.removeItem("refreshToken");

            router.push({name: "signin"})
        })
    } 
};