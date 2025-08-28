import { 
    signin,
    signup,
    refreshToken,
    revokeToken,
    getUser
} from "../../service/auth";

import router from "@/router"

export default {
    async login(payload) {
        console.log('dans action login')
        const response = await signin(payload);
        console.log('apres signin')
        console.log(response.data)
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
        return await revokeToken()
    } 
};