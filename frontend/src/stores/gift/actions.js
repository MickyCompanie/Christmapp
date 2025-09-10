import { getAllGifts, getSpecificGift, createGift, updateGift, deleteGift } from "../../service/gift";
import router from "@/router"


export default {
    async getAllGiftsAction() {
        return await getAllGifts().then((res) => {
            console.log(res.data);
        })
    },
    async getSpecificGiftAction(payload) {
        return await getSpecificGift(payload).then((res) => {
            console.log(res.data);
        })
    },
    async createGiftAction(payload) {
        return await createGift(payload).then((res) => {
            console.log(res.data);
        })
    },

    async updateGiftAction(payload) {
        return await updateGift(payload).then((res) => {
            console.log(res.data);
        })
    },

    async deleteGiftAction(payload) {
        return await deleteGift(payload).then((res) => {
            console.log(res.data);
        })
    }
}