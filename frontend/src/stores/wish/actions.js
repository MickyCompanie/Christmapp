import { getAllWishes, getSpecificWish, createWish, updateWish, deleteWish, getEmptyWish } from "../../service/wish";
import { useNotificationsStore } from "@/stores/notifications";
import router from "@/router"



export default {
    async getAllWishesAction() {
        return await getAllWishes().then((res) => {
            this.wishes = res.data.wishes;
            this.tableHeads = res.data.tableHeads;
            this.attributes = res.data.attributes;
        })
    },

    async resetWish(){
        this.wish = null;
    },

    async getSpecificWishAction(payload) {
        return await getSpecificWish(payload).then((res) => {
            this.wish = res.data;
        })
    },

    async getEmptyWishAction() {
        return await getEmptyWish().then((res) => {
            this.wish = res.data;
        })
    },

    async createWishAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await createWish(payload).then((res) => {
            router.push({name: "wisheslist"})

            notificationsStore.setNotification({
            message: res?.data?.detail || "Wish created successfully",
            statusCode: res?.status || 201
            })

        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    },

    async updateWishAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await updateWish(payload).then((res) => {
            router.push({name: "wisheslist"})

            notificationsStore.setNotification({
            message: res?.data?.detail || "Wish updated successfully",
            statusCode: res?.status || 201
            })
        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    },

    async deleteWishAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await deleteWish(payload).then((res) => {
            this.getAllWishesAction();

            notificationsStore.setNotification({
            message: res?.data?.detail || "Wish deleted successfully",
            statusCode: res?.status || 201
            })
        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    }
}