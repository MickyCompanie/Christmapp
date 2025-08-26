import { 
    signin,
    signup,
    refreshToken,
    revokeToken,
    getUser
} from "../../service/auth";

export default {
    async login(credentials) {
        const data = await signin(credentials);
        this.accessToken = data.accessToken;
        this.refreshToken = data.refreshToken;
        localStorage.setItem("accessToken", data.accessToken);
        localStorage.setItem("refreshToken", data.refreshToken);
        this.getCurrentUser();
    },
    async getCurrentUser() {
        const data = await getUser();
        this.user = data;
    }
};