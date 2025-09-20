import { getAllGiftStatuses, getSpecificGiftStatus, getEmptyGiftStatus, createGiftStatus, updateGiftStatus, deleteGiftStatus } from "../../service/giftStatus";
import { useNotificationsStore } from "@/stores/notifications";
import router from "@/router"


export default {
    async getAllGiftStatusesAction() {
        return await getAllGiftStatuses().then((res) => {
            this.giftStatuses = res.data.giftStatuses;
            this.tableHeads = res.data.tableHeads;
            this.attributes = res.data.attributes;
        })
    },

    async resetGiftStatusAction() {
        this.giftStatus = null;
    },

    async getEmptyGiftStatusAction() {
        return await getEmptyGiftStatus().then((res) => {
            this.giftStatus = res.data;
        })
    },

    async getSpecificGiftStatusAction(payload) {
        return await getSpecificGiftStatus(payload).then((res) => {
            console.log(res.data);
        })
    },
    async createGiftStatusAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await createGiftStatus(payload).then((res) => {
            router.push({name: "giftStatusList"})

            notificationsStore.setNotification({
            message: res?.data?.detail || "Status created successfully",
            statusCode: res?.status || 201
            })
        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    },

    async updateGiftStatusAction(payload) {
        return await updateGiftStatus(payload).then((res) => {
            console.log(res.data);
        })
    },

    async deleteGiftStatusAction(payload) {
        return await deleteGiftStatus(payload).then((res) => {
            console.log(res.data);
        })
    }
}