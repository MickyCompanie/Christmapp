import { getAllGiftStatuses, getSpecificGiftStatus, createGiftStatus, updateGiftStatus, deleteGiftStatus } from "../../service/giftStatus";
import router from "@/router"


export default {
    async getAllGiftStatusesAction() {
        return await getAllGiftStatuses().then((res) => {
            console.log(res.data);
        })
    },
    async getSpecificGiftStatusAction(payload) {
        return await getSpecificGiftStatus(payload).then((res) => {
            console.log(res.data);
        })
    },
    async createGiftStatusAction(payload) {
        return await createGiftStatus(payload).then((res) => {
            console.log(res.data);
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