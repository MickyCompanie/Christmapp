import { signin, signup, revokeToken, getUser, getAllUsers, upgradeUserRole, downgradeUserRole } from "../../service/auth";
import { updatePerson } from "../../service/person";
import { useNotificationsStore } from "@/stores/notifications";
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

    async getAllUsersAction() {
        return await getAllUsers()
        .then((response) => {
            this.users = response.data
        })
        .catch((error) => {

        })
    },

    async upgradeUserRoleAction(uid){
        const notificationsStore = useNotificationsStore();

        return await upgradeUserRole(uid).then((response) => {
            this.getAllUsersAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "User Upgraded Successfully",
            statusCode: res?.status || 201
            })

        }).catch((error) => {

        })
    },

    async downgradeUserRoleAction(uid){
        const notificationsStore = useNotificationsStore();
        
        return await downgradeUserRole(uid)
        .then((response) => {
            this.getAllUsersAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "User Downgraded Successfully",
            statusCode: res?.status || 201
            })

        })
        .catch((error) => {

        })
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