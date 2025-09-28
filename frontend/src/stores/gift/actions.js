import { getAllGifts, getSpecificGift, getEmptyGift, createGift, updateGift, deleteGift } from "../../service/gift";
import { useNotificationsStore } from "@/stores/notifications";
import router from "@/router"


export default {
    async getAllGiftsAction() {
        return await getAllGifts().then((res) => {
            this.tableHeads = res.data.tableHeads
            this.attributes = res.data.attributes
            this.gifts = res.data.gifts
        })
    },

    async getEmptyGiftAction() {
        return await getEmptyGift().then((response) => {
            this.gift = response.data.gift
            this.persons = response.data.persons
            this.statuses = response.data.statuses
        })
    },

    async resetGiftAction(){
        this.gift = null
    },

    async getSpecificGiftAction(payload) {
        return await getSpecificGift(payload).then((response) => {
            this.gift = response.data.gift
            this.persons = response.data.persons
            this.statuses = response.data.statuses
        })
    },
    async createGiftAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await createGift(payload).then((res) => {
            router.push({name: "giftlist"})
            this.resetGiftAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "Gift created successfully",
            statusCode: res?.status || 201
            })
        })
    },

    async updateGiftAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await updateGift(payload).then((res) => {
            router.push({name: "giftlist"})
            this.resetGiftAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "Gift updated successfully",
            statusCode: res?.status || 201
            })
        })
    },

    async deleteGiftAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await deleteGift(payload).then((res) => {
            this.getAllGiftsAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "Gift deleted successfully",
            statusCode: res?.status || 201
            })
        })
    }
}